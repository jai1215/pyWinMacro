# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyWinMacro.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 240)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(169, 10, 141, 81))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 20, 150, 59))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.InfoLabel0 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel0.setFont(font)
        self.InfoLabel0.setObjectName("InfoLabel0")
        self.verticalLayout.addWidget(self.InfoLabel0)
        self.InfoLabel1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel1.setFont(font)
        self.InfoLabel1.setObjectName("InfoLabel1")
        self.verticalLayout.addWidget(self.InfoLabel1)
        self.InfoLabel2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel2.setFont(font)
        self.InfoLabel2.setObjectName("InfoLabel2")
        self.verticalLayout.addWidget(self.InfoLabel2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Information"))
        self.InfoLabel0.setText(_translate("Form", "Mouse Pos(  0,  0)"))
        self.InfoLabel1.setText(_translate("Form", "Test Label1"))
        self.InfoLabel2.setText(_translate("Form", "Test Label2"))
        self.pushButton.setText(_translate("Form", "TestButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

