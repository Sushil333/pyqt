# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartLoading.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartLoading(object):
    def setupUi(self, StartLoading):
        StartLoading.setObjectName("StartLoading")
        StartLoading.resize(1024, 768)
        StartLoading.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backButton = QtWidgets.QPushButton(StartLoading)
        self.backButton.setGeometry(QtCore.QRect(24, 530, 151, 111))
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.logo = QtWidgets.QLabel(StartLoading)
        self.logo.setGeometry(QtCore.QRect(720, 20, 281, 81))
        self.logo.setAutoFillBackground(False)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.nextButton = QtWidgets.QPushButton(StartLoading)
        self.nextButton.setGeometry(QtCore.QRect(800, 550, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet("border: 4px solid darkblue;\n"
"color: darkblue;\n"
"border-radius: 25px;")
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.label = QtWidgets.QLabel(StartLoading)
        self.label.setGeometry(QtCore.QRect(400, 150, 161, 131))
        self.label.setStyleSheet("align: center;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/information.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.msg_label = QtWidgets.QLabel(StartLoading)
        self.msg_label.setGeometry(QtCore.QRect(10, 320, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.msg_label.setFont(font)
        self.msg_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg_label.setAutoFillBackground(False)
        self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label.setObjectName("msg_label")
        self.msg_label_2 = QtWidgets.QLabel(StartLoading)
        self.msg_label_2.setGeometry(QtCore.QRect(20, 370, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.msg_label_2.setFont(font)
        self.msg_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg_label_2.setAutoFillBackground(False)
        self.msg_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label_2.setObjectName("msg_label_2")

        self.retranslateUi(StartLoading)
        QtCore.QMetaObject.connectSlotsByName(StartLoading)

    def retranslateUi(self, StartLoading):
        _translate = QtCore.QCoreApplication.translate
        StartLoading.setWindowTitle(_translate("StartLoading", "Trimble"))
        self.nextButton.setText(_translate("StartLoading", "Verladung abschlossen"))
        self.msg_label.setText(_translate("StartLoading", "Line_1"))
        self.msg_label_2.setText(_translate("StartLoading", "Line_2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartLoading = QtWidgets.QWidget()
    ui = Ui_StartLoading()
    ui.setupUi(StartLoading)
    StartLoading.show()
    sys.exit(app.exec_())