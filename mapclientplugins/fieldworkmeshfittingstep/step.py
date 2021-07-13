'''
MAP Client Plugin Step
'''
import json

from PySide2 import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.fieldworkmeshfittingstep.configuredialog import ConfigureDialog
from mapclientplugins.fieldworkmeshfittingstep.mayavifittingviewerwidget import MayaviFittingViewerWidget

import copy
from gias2.fieldwork.field.tools import fitting_tools
import numpy as np


class FieldworkMeshFittingStep(WorkflowStepMountPoint):
    '''
    Step for fitting fieldwork models to data clouds by optimising nodal 
    parameters subject to Sobelov and normal smoothing penalties.
    '''

    # maps config keys to fitting function argument names
    _fitConfigDict = {}
    _fitConfigDict['mesh discretisation'] = 'GD'
    _fitConfigDict['sobelov discretisation'] = 'sobD'
    _fitConfigDict['sobelov weight'] = 'sobW'
    _fitConfigDict['normal discretisation'] = 'normalD'
    _fitConfigDict['normal weight'] = 'normalW'
    _fitConfigDict['max sub-iterations'] = 'itMaxPerIt'
    _fitConfigDict['xtol'] = 'xtol'
    _fitConfigDict['max iterations'] = 'itMax'
    _fitConfigDict['fit mode'] = 'gObjType'
    _fitConfigDict['n closest points'] = 'nClosestPoints'
    _fitConfigDict['kdtree args'] = 'treeArgs'
    _fitConfigDict['verbose'] = 'fitVerbose'
    _fitConfigDict['fixed nodes'] = 'fixedNodes'

    _configDefaults = {}
    _configDefaults['identifier'] = ''
    _configDefaults['mesh discretisation'] = '5.0'
    _configDefaults['sobelov discretisation'] = '[8,8]'
    _configDefaults['sobelov weight'] = '[1e-6, 1e-6, 1e-6, 1e-6, 2e-6]'
    _configDefaults['normal discretisation'] = '8'
    _configDefaults['normal weight'] = '50.0'
    _configDefaults['max sub-iterations'] = '3'
    _configDefaults['xtol'] = '1e-6'
    _configDefaults['max iterations'] = '5'
    _configDefaults['fit mode'] = 'DPEP'
    _configDefaults['n closest points'] = '1'
    _configDefaults['kdtree args'] = '{}'
    _configDefaults['verbose'] = 'True'
    _configDefaults['fixed nodes'] = 'None'
    _configDefaults['GUI'] = 'True'

    def __init__(self, location):
        super(FieldworkMeshFittingStep, self).__init__('Fieldwork Mesh Fitting', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Fitting'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/fieldworkmeshfittingstep/images/fieldworkmeshfittingicon.png')
        # Ports:
        # data cloud (2d numpy array)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#pointcloud'))

        # GF to fit (geometric_field)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#fieldworkmodel'))

        # data weights (1d numpy array, optional)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'numpy#array1d'))

        # fitted GF (geometric_field)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#fieldworkmodel'))

        # fitted GF parameters (3d numpy array)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#fieldworkmodelparameters'))

        # RMS error (float)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'python#float'))

        # error for each data point (1d numpy array)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'numpy#array1d'))

        self._config = {}
        for k, v in list(self._configDefaults.items()):
            self._config[k] = v

        self.data = None
        self.dataWeights = None
        self.GFUnfitted = None
        self.GF = None
        self.GFFitted = None
        self.RMSEFitted = None
        self.GFParamsFitted = None
        self.fitErrors = None

        self._widget = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        if self._config['GUI'] == 'True':
            self._widget = MayaviFittingViewerWidget(self.data, self.GFUnfitted, self._config, self._fit, self._reset)
            # self._widget._ui.registerButton.clicked.connect(self._register)
            self._widget._ui.acceptButton.clicked.connect(self._doneExecution)
            self._widget._ui.abortButton.clicked.connect(self._abort)
            self._widget._ui.resetButton.clicked.connect(self._reset)
            self._setCurrentWidget(self._widget)

        elif self._config['GUI'] == 'False':
            self._fit()
            self.GFFitted = copy.deepcopy(self.GF)
            self._doneExecution()

    def _mapFitConfigs(self):

        fitkwargs = {}
        fitkwargs['GF'] = self.GF
        fitkwargs['data'] = self.data
        fitkwargs['dataWeights'] = self.dataWeights
        fitkwargs['fullErrors'] = True
        for k, v in list(self._fitConfigDict.items()):
            if k == 'fit mode':
                fitkwargs[v] = self._config[k]
            elif k == 'fixed nodes':
                inputStr = self._config[k]
                fixedNodes = []
                if (inputStr == 'none') or (inputStr == 'None') or (len(inputStr) == 0):
                    pass
                else:
                    words = inputStr.split(',')
                    for w in words:
                        if '-' in w:
                            x0, x1 = w.split('-')
                            fixedNodes += range(int(x0), int(x1) + 1)
                        else:
                            fixedNodes.append(int(w))

                fitkwargs[v] = fixedNodes

                # inputStr = self._config[k]
                # if inputStr=='None':
                #     fitkwargs[v]=None
                # else:
                #     fixedNodes = []
                #     words = inputStr.split(',')
                #     for w in words:
                #         if '-' in w:
                #             x0,x1 = w.split('-')
                #             fixedNodes += range(int(x0), int(x1)+1)
                #         else:
                #             fixedNodes.append(int(w))
                #     fitkwargs[v] = fixedNodes
            else:
                fitkwargs[v] = eval(self._config[k])

        return fitkwargs

    def _fit(self, callbackSignal=None):

        # parse configurations
        fitkwargs = self._mapFitConfigs()

        if callbackSignal is not None:
            def callback(output):
                callbackSignal.emit(output)
        else:
            callback = None

        fitkwargs['fitOutputCallback'] = callback

        # call fitting functions
        (GFFitted, paramsFitted, RMSEFitted, errorsFitted) = fitting_tools.fitSurfacePerItSearch(**fitkwargs)

        self.GFFitted = copy.deepcopy(GFFitted)
        self.GFParamsFitted = paramsFitted
        self.RMSEFitted = RMSEFitted
        self.fitErrors = np.sqrt(errorsFitted)

        return self.GFFitted, self.GFParamsFitted, self.RMSEFitted, self.fitErrors

    def _abort(self):
        # self._doneExecution()
        raise RuntimeError('mesh fitting aborted')

    def _reset(self):
        self.GFFitted = None
        self.GFParamsFitted = None
        self.RMSEFitted = None
        self.FitErrors = None
        self.GF = copy.deepcopy(self.GFUnfitted)

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 0:
            self.data = np.array(dataIn, dtype=float)  # ju#pointcoordinates
        elif index == 1:
            self.GF = dataIn  # ju#fieldworkmodel
            self.GFUnfitted = copy.deepcopy(self.GF)
        else:
            self.dataWeights = np.array(dataIn, dtype=float)  # numpyarray1d - dataWeights

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        if index == 3:
            return self.GFFitted  # ju#fieldworkmodel
        elif index == 4:
            return self.GFParamsFitted  # ju#fieldworkmodelparameters
        elif index == 5:
            return self.RMSEFitted  # float
        else:
            return self.fitErrors  # numpyarray1d

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self):
        '''
        Add code to serialize this step to disk. Returns a json string for
        mapclient to serialise.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        '''
        Add code to deserialize this step from disk. Parses a json string
        given by mapclient
        '''
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()
