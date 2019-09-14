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

    def setup_ui(self):
        """
        PyQt window and function connection setup. inherits from the UI file.
        """
        form = self
        # get setupui method from generated pyqt file
        super(MayaUiTemplate, self).setupUi(form)

        form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # Window always on top


uiTemplate = MayaUiTemplate()
uiTemplate.setup_ui()
uiTemplate.show()
