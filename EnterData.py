# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EnterData.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EnterData(object):
    def setupUi(self, EnterData):
        EnterData.setObjectName("EnterData")
        EnterData.resize(1024, 769)
        EnterData.setFocusPolicy(QtCore.Qt.NoFocus)
        EnterData.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logo = QtWidgets.QLabel(EnterData)
        self.logo.setGeometry(QtCore.QRect(690, 20, 281, 81))
        self.logo.setAutoFillBackground(False)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.licenseLineEdit = QtWidgets.QLineEdit(EnterData)
        self.licenseLineEdit.setGeometry(QtCore.QRect(410, 240, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.licenseLineEdit.setFont(font)
        self.licenseLineEdit.setTabletTracking(True)
        self.licenseLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.licenseLineEdit.setAutoFillBackground(False)
        self.licenseLineEdit.setStyleSheet("border: 1px solid black;")
        self.licenseLineEdit.setFrame(True)
        self.licenseLineEdit.setDragEnabled(False)
        self.licenseLineEdit.setReadOnly(False)
        self.licenseLineEdit.setObjectName("licenseLineEdit")
        self.nextButton = QtWidgets.QPushButton(EnterData)
        self.nextButton.setGeometry(QtCore.QRect(870, 540, 151, 111))
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nextButton.setIcon(icon)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.backButton = QtWidgets.QPushButton(EnterData)
        self.backButton.setGeometry(QtCore.QRect(10, 540, 141, 111))
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(icon1)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.label = QtWidgets.QLabel(EnterData)
        self.label.setGeometry(QtCore.QRect(130, 10, 541, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(EnterData)
        self.label_2.setGeometry(QtCore.QRect(190, 90, 551, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(EnterData)
        self.label_3.setGeometry(QtCore.QRect(180, 240, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.driverLineEdit = QtWidgets.QLineEdit(EnterData)
        self.driverLineEdit.setGeometry(QtCore.QRect(410, 290, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.driverLineEdit.setFont(font)
        self.driverLineEdit.setTabletTracking(True)
        self.driverLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.driverLineEdit.setAutoFillBackground(False)
        self.driverLineEdit.setStyleSheet("border: 1px solid black;")
        self.driverLineEdit.setFrame(True)
        self.driverLineEdit.setDragEnabled(False)
        self.driverLineEdit.setReadOnly(False)
        self.driverLineEdit.setObjectName("driverLineEdit")
        self.companyLineEdit = QtWidgets.QLineEdit(EnterData)
        self.companyLineEdit.setGeometry(QtCore.QRect(410, 340, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.companyLineEdit.setFont(font)
        self.companyLineEdit.setTabletTracking(True)
        self.companyLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.companyLineEdit.setAutoFillBackground(False)
        self.companyLineEdit.setStyleSheet("border: 1px solid black;")
        self.companyLineEdit.setFrame(True)
        self.companyLineEdit.setDragEnabled(False)
        self.companyLineEdit.setReadOnly(False)
        self.companyLineEdit.setObjectName("companyLineEdit")
        self.remarkLineEdit = QtWidgets.QLineEdit(EnterData)
        self.remarkLineEdit.setGeometry(QtCore.QRect(410, 390, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.remarkLineEdit.setFont(font)
        self.remarkLineEdit.setTabletTracking(True)
        self.remarkLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.remarkLineEdit.setAutoFillBackground(False)
        self.remarkLineEdit.setStyleSheet("border: 1px solid black;")
        self.remarkLineEdit.setFrame(True)
        self.remarkLineEdit.setDragEnabled(False)
        self.remarkLineEdit.setReadOnly(False)
        self.remarkLineEdit.setObjectName("remarkLineEdit")
        self.abol_numLineEdit = QtWidgets.QLineEdit(EnterData)
        self.abol_numLineEdit.setGeometry(QtCore.QRect(410, 150, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.abol_numLineEdit.setFont(font)
        self.abol_numLineEdit.setTabletTracking(True)
        self.abol_numLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.abol_numLineEdit.setAutoFillBackground(False)
        self.abol_numLineEdit.setStyleSheet("border: 1px solid black;")
        self.abol_numLineEdit.setFrame(True)
        self.abol_numLineEdit.setDragEnabled(False)
        self.abol_numLineEdit.setReadOnly(False)
        self.abol_numLineEdit.setObjectName("abol_numLineEdit")
        self.ladevolumenLineEdit = QtWidgets.QLineEdit(EnterData)
        self.ladevolumenLineEdit.setGeometry(QtCore.QRect(410, 440, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ladevolumenLineEdit.setFont(font)
        self.ladevolumenLineEdit.setTabletTracking(True)
        self.ladevolumenLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ladevolumenLineEdit.setAutoFillBackground(False)
        self.ladevolumenLineEdit.setStyleSheet("border: 1px solid black;")
        self.ladevolumenLineEdit.setFrame(True)
        self.ladevolumenLineEdit.setDragEnabled(False)
        self.ladevolumenLineEdit.setReadOnly(False)
        self.ladevolumenLineEdit.setObjectName("ladevolumenLineEdit")
        self.getButton = QtWidgets.QPushButton(EnterData)
        self.getButton.setGeometry(QtCore.QRect(730, 240, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.getButton.setFont(font)
        self.getButton.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(172, 172, 172);\n"
"")
        self.getButton.setObjectName("getButton")
        self.label_4 = QtWidgets.QLabel(EnterData)
        self.label_4.setGeometry(QtCore.QRect(180, 290, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(EnterData)
        self.label_5.setGeometry(QtCore.QRect(180, 340, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(EnterData)
        self.label_6.setGeometry(QtCore.QRect(180, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(EnterData)
        self.label_7.setGeometry(QtCore.QRect(180, 390, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(EnterData)
        self.label_8.setGeometry(QtCore.QRect(180, 440, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.QButton = QtWidgets.QPushButton(EnterData)
        self.QButton.setGeometry(QtCore.QRect(240, 560, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QButton.setFont(font)
        self.QButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.QButton.setObjectName("QButton")
        self.YButton = QtWidgets.QPushButton(EnterData)
        self.YButton.setGeometry(QtCore.QRect(490, 560, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YButton.setFont(font)
        self.YButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.YButton.setObjectName("YButton")
        self.TButton = QtWidgets.QPushButton(EnterData)
        self.TButton.setGeometry(QtCore.QRect(440, 560, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TButton.setFont(font)
        self.TButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.TButton.setObjectName("TButton")
        self.EButton = QtWidgets.QPushButton(EnterData)
        self.EButton.setGeometry(QtCore.QRect(340, 560, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EButton.setFont(font)
        self.EButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.EButton.setObjectName("EButton")
        self.RButton = QtWidgets.QPushButton(EnterData)
        self.RButton.setGeometry(QtCore.QRect(390, 560, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RButton.setFont(font)
        self.RButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.RButton.setObjectName("RButton")
        self.Button_1 = QtWidgets.QPushButton(EnterData)
        self.Button_1.setGeometry(QtCore.QRect(240, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_1.setFont(font)
        self.Button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_1.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_1.setAutoDefault(False)
        self.Button_1.setObjectName("Button_1")
        self.backButton_2 = QtWidgets.QPushButton(EnterData)
        self.backButton_2.setGeometry(QtCore.QRect(740, 560, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backButton_2.setFont(font)
        self.backButton_2.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.backButton_2.setObjectName("backButton_2")
        self.PButton = QtWidgets.QPushButton(EnterData)
        self.PButton.setGeometry(QtCore.QRect(690, 560, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PButton.setFont(font)
        self.PButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.PButton.setObjectName("PButton")
        self.OButton = QtWidgets.QPushButton(EnterData)
        self.OButton.setGeometry(QtCore.QRect(640, 560, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OButton.setFont(font)
        self.OButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.OButton.setObjectName("OButton")
        self.IButton = QtWidgets.QPushButton(EnterData)
        self.IButton.setGeometry(QtCore.QRect(590, 560, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IButton.setFont(font)
        self.IButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.IButton.setObjectName("IButton")
        self.UButton = QtWidgets.QPushButton(EnterData)
        self.UButton.setGeometry(QtCore.QRect(540, 560, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UButton.setFont(font)
        self.UButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.UButton.setObjectName("UButton")
        self.WButton = QtWidgets.QPushButton(EnterData)
        self.WButton.setGeometry(QtCore.QRect(290, 560, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WButton.setFont(font)
        self.WButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.WButton.setObjectName("WButton")
        self.Button_6 = QtWidgets.QPushButton(EnterData)
        self.Button_6.setGeometry(QtCore.QRect(490, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_6.setFont(font)
        self.Button_6.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_6.setObjectName("Button_6")
        self.Button_8 = QtWidgets.QPushButton(EnterData)
        self.Button_8.setGeometry(QtCore.QRect(590, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_8.setFont(font)
        self.Button_8.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_8.setObjectName("Button_8")
        self.Button_7 = QtWidgets.QPushButton(EnterData)
        self.Button_7.setGeometry(QtCore.QRect(540, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_7.setFont(font)
        self.Button_7.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_7.setObjectName("Button_7")
        self.Button_5 = QtWidgets.QPushButton(EnterData)
        self.Button_5.setGeometry(QtCore.QRect(440, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_5.setFont(font)
        self.Button_5.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_5.setObjectName("Button_5")
        self.Button_4 = QtWidgets.QPushButton(EnterData)
        self.Button_4.setGeometry(QtCore.QRect(390, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_4.setFont(font)
        self.Button_4.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_4.setObjectName("Button_4")
        self.Button_3 = QtWidgets.QPushButton(EnterData)
        self.Button_3.setGeometry(QtCore.QRect(340, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_3.setFont(font)
        self.Button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_3.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_3.setObjectName("Button_3")
        self.Button_2 = QtWidgets.QPushButton(EnterData)
        self.Button_2.setGeometry(QtCore.QRect(290, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_2.setFont(font)
        self.Button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_2.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_2.setObjectName("Button_2")
        self.Button_9 = QtWidgets.QPushButton(EnterData)
        self.Button_9.setGeometry(QtCore.QRect(640, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_9.setFont(font)
        self.Button_9.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_9.setObjectName("Button_9")
        self.Button_0 = QtWidgets.QPushButton(EnterData)
        self.Button_0.setGeometry(QtCore.QRect(690, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_0.setFont(font)
        self.Button_0.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_0.setObjectName("Button_0")
        self.minusButton = QtWidgets.QPushButton(EnterData)
        self.minusButton.setGeometry(QtCore.QRect(740, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.minusButton.setFont(font)
        self.minusButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.minusButton.setObjectName("minusButton")
        self.AButton = QtWidgets.QPushButton(EnterData)
        self.AButton.setGeometry(QtCore.QRect(240, 610, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AButton.setFont(font)
        self.AButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.AButton.setObjectName("AButton")
        self.SButton = QtWidgets.QPushButton(EnterData)
        self.SButton.setGeometry(QtCore.QRect(290, 610, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SButton.setFont(font)
        self.SButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.SButton.setObjectName("SButton")
        self.DButton = QtWidgets.QPushButton(EnterData)
        self.DButton.setGeometry(QtCore.QRect(340, 610, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DButton.setFont(font)
        self.DButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.DButton.setObjectName("DButton")
        self.GButton = QtWidgets.QPushButton(EnterData)
        self.GButton.setGeometry(QtCore.QRect(440, 610, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GButton.setFont(font)
        self.GButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.GButton.setObjectName("GButton")
        self.FButton = QtWidgets.QPushButton(EnterData)
        self.FButton.setGeometry(QtCore.QRect(390, 610, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FButton.setFont(font)
        self.FButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.FButton.setObjectName("FButton")
        self.HButton = QtWidgets.QPushButton(EnterData)
        self.HButton.setGeometry(QtCore.QRect(490, 610, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HButton.setFont(font)
        self.HButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.HButton.setObjectName("HButton")
        self.ButtonGerA = QtWidgets.QPushButton(EnterData)
        self.ButtonGerA.setGeometry(QtCore.QRect(690, 610, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonGerA.setFont(font)
        self.ButtonGerA.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.ButtonGerA.setObjectName("ButtonGerA")
        self.LButton = QtWidgets.QPushButton(EnterData)
        self.LButton.setGeometry(QtCore.QRect(640, 610, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LButton.setFont(font)
        self.LButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.LButton.setObjectName("LButton")
        self.KButton = QtWidgets.QPushButton(EnterData)
        self.KButton.setGeometry(QtCore.QRect(590, 610, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.KButton.setFont(font)
        self.KButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.KButton.setObjectName("KButton")
        self.JButton = QtWidgets.QPushButton(EnterData)
        self.JButton.setGeometry(QtCore.QRect(540, 610, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.JButton.setFont(font)
        self.JButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.JButton.setObjectName("JButton")
        self.ButtonGerO = QtWidgets.QPushButton(EnterData)
        self.ButtonGerO.setGeometry(QtCore.QRect(740, 610, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonGerO.setFont(font)
        self.ButtonGerO.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.ButtonGerO.setObjectName("ButtonGerO")
        self.ZButton = QtWidgets.QPushButton(EnterData)
        self.ZButton.setGeometry(QtCore.QRect(240, 660, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ZButton.setFont(font)
        self.ZButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.ZButton.setObjectName("ZButton")
        self.XButton = QtWidgets.QPushButton(EnterData)
        self.XButton.setGeometry(QtCore.QRect(290, 660, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.XButton.setFont(font)
        self.XButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.XButton.setObjectName("XButton")
        self.CButton = QtWidgets.QPushButton(EnterData)
        self.CButton.setGeometry(QtCore.QRect(340, 660, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CButton.setFont(font)
        self.CButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.CButton.setObjectName("CButton")
        self.BButton = QtWidgets.QPushButton(EnterData)
        self.BButton.setGeometry(QtCore.QRect(440, 660, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BButton.setFont(font)
        self.BButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.BButton.setObjectName("BButton")
        self.VButton = QtWidgets.QPushButton(EnterData)
        self.VButton.setGeometry(QtCore.QRect(390, 660, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VButton.setFont(font)
        self.VButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.VButton.setObjectName("VButton")
        self.NButton = QtWidgets.QPushButton(EnterData)
        self.NButton.setGeometry(QtCore.QRect(490, 660, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NButton.setFont(font)
        self.NButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.NButton.setObjectName("NButton")
        self.MButton = QtWidgets.QPushButton(EnterData)
        self.MButton.setGeometry(QtCore.QRect(540, 660, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MButton.setFont(font)
        self.MButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.MButton.setObjectName("MButton")
        self.ButtonGerU = QtWidgets.QPushButton(EnterData)
        self.ButtonGerU.setGeometry(QtCore.QRect(590, 660, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonGerU.setFont(font)
        self.ButtonGerU.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.ButtonGerU.setObjectName("ButtonGerU")
        self.ButtonSpace = QtWidgets.QPushButton(EnterData)
        self.ButtonSpace.setGeometry(QtCore.QRect(690, 660, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonSpace.setFont(font)
        self.ButtonSpace.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.ButtonSpace.setObjectName("ButtonSpace")
        self.ButtonGerU_2 = QtWidgets.QPushButton(EnterData)
        self.ButtonGerU_2.setGeometry(QtCore.QRect(640, 660, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonGerU_2.setFont(font)
        self.ButtonGerU_2.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.ButtonGerU_2.setObjectName("ButtonGerU_2")

        self.retranslateUi(EnterData)
        QtCore.QMetaObject.connectSlotsByName(EnterData)

    def retranslateUi(self, EnterData):
        _translate = QtCore.QCoreApplication.translate
        EnterData.setWindowTitle(_translate("EnterData", "Trimble"))
        self.label.setText(_translate("EnterData", "MSG"))
        self.label_2.setText(_translate("EnterData", "Please Enter Your Details"))
        self.label_3.setText(_translate("EnterData", "label_3"))
        self.getButton.setText(_translate("EnterData", "Get"))
        self.label_4.setText(_translate("EnterData", "label_4"))
        self.label_5.setText(_translate("EnterData", "label_5"))
        self.label_6.setText(_translate("EnterData", "label_6"))
        self.label_7.setText(_translate("EnterData", "label_7"))
        self.label_8.setText(_translate("EnterData", "label_8"))
        self.QButton.setText(_translate("EnterData", "Q"))
        self.YButton.setText(_translate("EnterData", "Y"))
        self.TButton.setText(_translate("EnterData", "T"))
        self.EButton.setText(_translate("EnterData", "E"))
        self.RButton.setText(_translate("EnterData", "R"))
        self.Button_1.setText(_translate("EnterData", "1"))
        self.backButton_2.setText(_translate("EnterData", "<-"))
        self.PButton.setText(_translate("EnterData", "P"))
        self.OButton.setText(_translate("EnterData", "O"))
        self.IButton.setText(_translate("EnterData", "I"))
        self.UButton.setText(_translate("EnterData", "U"))
        self.WButton.setText(_translate("EnterData", "W"))
        self.Button_6.setText(_translate("EnterData", "6"))
        self.Button_8.setText(_translate("EnterData", "8"))
        self.Button_7.setText(_translate("EnterData", "7"))
        self.Button_5.setText(_translate("EnterData", "5"))
        self.Button_4.setText(_translate("EnterData", "4"))
        self.Button_3.setText(_translate("EnterData", "3"))
        self.Button_2.setText(_translate("EnterData", "2"))
        self.Button_9.setText(_translate("EnterData", "9"))
        self.Button_0.setText(_translate("EnterData", "0"))
        self.minusButton.setText(_translate("EnterData", "-"))
        self.AButton.setText(_translate("EnterData", "A"))
        self.SButton.setText(_translate("EnterData", "S"))
        self.DButton.setText(_translate("EnterData", "D"))
        self.GButton.setText(_translate("EnterData", "G"))
        self.FButton.setText(_translate("EnterData", "F"))
        self.HButton.setText(_translate("EnterData", "H"))
        self.ButtonGerA.setText(_translate("EnterData", "??"))
        self.LButton.setText(_translate("EnterData", "L"))
        self.KButton.setText(_translate("EnterData", "K"))
        self.JButton.setText(_translate("EnterData", "J"))
        self.ButtonGerO.setText(_translate("EnterData", "??"))
        self.ZButton.setText(_translate("EnterData", "Z"))
        self.XButton.setText(_translate("EnterData", "X"))
        self.CButton.setText(_translate("EnterData", "C"))
        self.BButton.setText(_translate("EnterData", "B"))
        self.VButton.setText(_translate("EnterData", "V"))
        self.NButton.setText(_translate("EnterData", "N"))
        self.MButton.setText(_translate("EnterData", "M"))
        self.ButtonGerU.setText(_translate("EnterData", "??    "))
        self.ButtonSpace.setText(_translate("EnterData", "SPACE"))
        self.ButtonGerU_2.setText(_translate("EnterData", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EnterData = QtWidgets.QWidget()
    ui = Ui_EnterData()
    ui.setupUi(EnterData)
    EnterData.show()
    sys.exit(app.exec_())
