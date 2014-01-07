

from PySide import QtGui
from fieldworkmeshfittingstep.ui_configuredialog import Ui_ConfigureDialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''

class ConfigureDialog(QtGui.QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self, parent)
        
        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._makeConnections()

    def _makeConnections(self):
        self._ui.lineEdit0.textChanged.connect(self.validate)

    def accept(self):
        '''
        Override the accept method so that we can confirm saving an
        invalid configuration.
        '''
        result = QtGui.QMessageBox.Yes
        if not self.validate():
            result = QtGui.QMessageBox.warning(self, 'Invalid Configuration',
                'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if result == QtGui.QMessageBox.Yes:
            QtGui.QDialog.accept(self)

    def validate(self):
        '''
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the 
        overall validity of the configuration.
        '''
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEdit0.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEdit0.text())
        if valid:
            self._ui.lineEdit0.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEdit0.setStyleSheet(INVALID_STYLE_SHEET)

        return valid

    def getConfig(self):
        '''
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = self._ui.lineEdit0.text()
        config = {}
        config['identifier'] = self._ui.lineEdit0.text()
        config['GD'] = self._ui.lineEdit1.text()
        config['sobelovD'] = self._ui.lineEdit2.text()
        config['sobelovW'] = self._ui.lineEdit3.text()
        config['normalD'] = self._ui.lineEdit4.text()
        config['normalW'] = self._ui.lineEdit5.text()
        config['itMaxPerIt'] = self._ui.lineEdit6.text()
        config['xtol'] = self._ui.lineEdit7.text()
        config['itMax'] = self._ui.lineEdit8.text()
        config['mode'] = self._ui.lineEdit9.text()
        config['nClosestPoints'] = self._ui.lineEdit10.text()
        config['treeArgs'] = self._ui.lineEdit11.text()
        config['fitVerbose'] = self._ui.lineEdit12.text()
        config['fixedNodes'] = self._ui.lineEdit13.text()
        return config

    def setConfig(self, config):
        '''
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = config['identifier']
        self._ui.lineEdit0.setText(config['identifier'])
        self._ui.lineEdit1.setText(config['GD'])
        self._ui.lineEdit2.setText(config['sobelovD'])
        self._ui.lineEdit3.setText(config['sobelovW'])
        self._ui.lineEdit4.setText(config['normalD'])
        self._ui.lineEdit5.setText(config['normalW'])
        self._ui.lineEdit6.setText(config['itMaxPerIt'])
        self._ui.lineEdit7.setText(config['xtol'])
        self._ui.lineEdit8.setText(config['itMax'])
        self._ui.lineEdit9.setText(config['mode'])
        self._ui.lineEdit10.setText(config['nClosestPoints'])
        self._ui.lineEdit11.setText(config['treeArgs'])
        self._ui.lineEdit12.setText(config['fitVerbose'])
        self._ui.lineEdit13.setText(config['fixedNodes'])

