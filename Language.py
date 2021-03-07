# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Language.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_language(object):
    def setupUi(self, language):
        language.setObjectName("language")
        language.resize(1024, 768)
        language.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(language)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(720, 20, 281, 81))
        self.logo.setAutoFillBackground(True)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.englishButton = QtWidgets.QPushButton(self.centralwidget)
        self.englishButton.setGeometry(QtCore.QRect(80, 280, 361, 191))
        self.englishButton.setAutoFillBackground(False)
        self.englishButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/english.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.englishButton.setIcon(icon)
        self.englishButton.setIconSize(QtCore.QSize(393, 233))
        self.englishButton.setCheckable(False)
        self.englishButton.setAutoRepeat(False)
        self.englishButton.setAutoExclusive(False)
        self.englishButton.setDefault(False)
        self.englishButton.setObjectName("englishButton")
        self.germanButton = QtWidgets.QPushButton(self.centralwidget)
        self.germanButton.setGeometry(QtCore.QRect(570, 280, 361, 191))
        self.germanButton.setAutoFillBackground(False)
        self.germanButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/german.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.germanButton.setIcon(icon1)
        self.germanButton.setIconSize(QtCore.QSize(370, 231))
        self.germanButton.setCheckable(False)
        self.germanButton.setAutoRepeat(False)
        self.germanButton.setAutoExclusive(False)
        self.germanButton.setDefault(False)
        self.germanButton.setObjectName("germanButton")
        language.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(language)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 20))
        self.menubar.setObjectName("menubar")
        language.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(language)
        self.statusbar.setObjectName("statusbar")
        language.setStatusBar(self.statusbar)

        self.retranslateUi(language)
        QtCore.QMetaObject.connectSlotsByName(language)
        
        self.englishButton.clicked.connect(lambda: self.clicked("English"))
        self.germanButton.clicked.connect(lambda: self.clicked("German"))

    def retranslateUi(self, language):
        _translate = QtCore.QCoreApplication.translate
        language.setWindowTitle(_translate("language", "MainWindow"))
        self.englishButton.setToolTip(_translate("language", "<html><head/><body><p>English</p></body></html>"))
        self.germanButton.setToolTip(_translate("language", "<html><head/><body><p>German</p></body></html>"))
    
    def clicked(self, text):
        if text == "English":
            pass
        elif text == "German":
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    language = QtWidgets.QMainWindow()
    ui = Ui_language()
    ui.setupUi(language)
    language.show()
    sys.exit(app.exec_())
