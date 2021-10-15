from PySide2 import QtWidgets
from mapclientplugins.fieldworkmeshfittingstep.ui_configuredialog import Ui_Dialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        self._makeConnections()

    def _makeConnections(self):
        pass

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                                                   'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # It's not currently possible for the configuration to be invalid, we may want to update this.
        return True

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.
        """
        config = {}
        config['mesh discretisation'] = self._ui.lineEdit1.text()
        config['sobelov discretisation'] = self._ui.lineEdit2.text()
        config['sobelov weight'] = self._ui.lineEdit3.text()
        config['normal discretisation'] = self._ui.lineEdit4.text()
        config['normal weight'] = self._ui.lineEdit5.text()
        config['max sub-iterations'] = self._ui.lineEdit6.text()
        config['xtol'] = self._ui.lineEdit7.text()
        config['max iterations'] = self._ui.lineEdit8.text()
        config['fit mode'] = self._ui.lineEdit9.text()
        config['n closest points'] = self._ui.lineEdit10.text()
        config['kdtree args'] = self._ui.lineEdit11.text()
        config['verbose'] = self._ui.lineEdit12.text()
        config['fixed nodes'] = self._ui.lineEdit13.text()
        config['GUI'] = self._ui.lineEdit14.text()
        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.
        """
        self._ui.lineEdit1.setText(config['mesh discretisation'])
        self._ui.lineEdit2.setText(config['sobelov discretisation'])
        self._ui.lineEdit3.setText(config['sobelov weight'])
        self._ui.lineEdit4.setText(config['normal discretisation'])
        self._ui.lineEdit5.setText(config['normal weight'])
        self._ui.lineEdit6.setText(config['max sub-iterations'])
        self._ui.lineEdit7.setText(config['xtol'])
        self._ui.lineEdit8.setText(config['max iterations'])
        self._ui.lineEdit9.setText(config['fit mode'])
        self._ui.lineEdit10.setText(config['n closest points'])
        self._ui.lineEdit11.setText(config['kdtree args'])
        self._ui.lineEdit12.setText(config['verbose'])
        self._ui.lineEdit13.setText(config['fixed nodes'])
        self._ui.lineEdit14.setText(config['GUI'])
