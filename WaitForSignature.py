# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WaitForSignature.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WaitForSignature(object):
    def setupUi(self, WaitForSignature):
        WaitForSignature.setObjectName("WaitForSignature")
        WaitForSignature.resize(1024, 768)
        WaitForSignature.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(WaitForSignature)
        self.label.setGeometry(QtCore.QRect(400, 150, 161, 131))
        self.label.setStyleSheet("align: center;\n"
"border: 2px solid darkblue;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/trackpad.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.msg_label = QtWidgets.QLabel(WaitForSignature)
        self.msg_label.setGeometry(QtCore.QRect(10, 360, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.msg_label.setFont(font)
        self.msg_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg_label.setAutoFillBackground(False)
        self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label.setObjectName("msg_label")
        self.backButton = QtWidgets.QPushButton(WaitForSignature)
        self.backButton.setGeometry(QtCore.QRect(24, 530, 151, 111))
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.logo = QtWidgets.QLabel(WaitForSignature)
        self.logo.setGeometry(QtCore.QRect(720, 20, 281, 81))
        self.logo.setAutoFillBackground(False)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.nextButton = QtWidgets.QPushButton(WaitForSignature)
        self.nextButton.setGeometry(QtCore.QRect(830, 530, 151, 111))
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nextButton.setIcon(icon1)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")

        self.retranslateUi(WaitForSignature)
        QtCore.QMetaObject.connectSlotsByName(WaitForSignature)

    def retranslateUi(self, WaitForSignature):
        _translate = QtCore.QCoreApplication.translate
        WaitForSignature.setWindowTitle(_translate("WaitForSignature", "Trimble"))
        self.msg_label.setText(_translate("WaitForSignature", "Line_1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WaitForSignature = QtWidgets.QWidget()
    ui = Ui_WaitForSignature()
    ui.setupUi(WaitForSignature)
    WaitForSignature.show()
    sys.exit(app.exec_())
