'''
Template for Maya UI with PyQt

'''

import os
from PySide2 import QtWidgets, QtCore, QtGui
from maya_pyqt_template_ui import Ui_Form
import excepthook_override

# override exception hook
ex = excepthook_override.Except()
ex.run_excepthook(os.path.basename(__file__))


class MayaUiTemplate(QtWidgets.QWidget, Ui_Form):
    """
    Run the script inside maya with a pyqt ui
    """

    def __init__(self):
        """
        init function
        """
        super(MayaUiTemplate, self).__init__(None)
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        self.log_path = "PATH_TO_LOG_FILE.txt"

    def setup_ui(self):
        """
        PyQt window and function connection setup. inherits from the UI file.
        """
        form = self
        # get setupui method from generated pyqt file
        super(MayaUiTemplate, self).setupUi(form)

        form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # Window always on top

    def message_query(self, title, message):
        """
        Popup to ask user input
        Args:
            title: Title of the popup
            message: Message of the popup
        Returns: True / False for the user's answer
        """
        result = QtWidgets.QMessageBox.question(self, title, message,
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            answer = True
        else:
            answer = False
        self.write_to_log(title + " | " + message + " | " + str(answer))
        return answer

    def handle_error(self, error_message):
        """
        Handle error by sending an error message
        Args:
            error_message: the error message
        """
        QtWidgets.QMessageBox.warning(self, "Warning", error_message)
        print error_message
        self.write_to_log(error_message)

    def popup_message(self, title, message):
        """
        A popup message
        Args:
            title: Title of the popup message
            message: Body of the popup message
        """
        QtWidgets.QMessageBox.information(self, title, message)
        self.write_to_log(title + " | " + message)

    def write_to_log(self, message):
        """
        Write message to log file
        Args:
            message: message to write to log
        """
        print message
        try:
            f = open(self.log_path, "a+")
            f.write("\n" + message)
        except Exception as e:
            print str(e)
            print "Couldn't append to log " + self.log_path


uiTemplate = MayaUiTemplate()
uiTemplate.setup_ui()
uiTemplate.show()
