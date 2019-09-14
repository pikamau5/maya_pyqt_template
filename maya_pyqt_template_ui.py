# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lkoekoek\Documents\maya\2019\scripts\rsExportUi.ui',
# licensing of 'C:\Users\lkoekoek\Documents\maya\2019\scripts\rsExportUi.ui' applies.
#
# Created: Mon Sep  2 23:03:26 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 50)
        self.a_button = QtWidgets.QPushButton(Form)
        self.a_button.setGeometry(QtCore.QRect(10, 10, 280, 28))
        self.a_button.setObjectName("button")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Template", None, -1))
        self.a_button.setText(QtWidgets.QApplication.translate("Form", "A Button", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
