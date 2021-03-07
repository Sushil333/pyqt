import os
import socket
import _thread
import json
import time
import pandas as pd
import base64
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def resource_path(relative_path):
    relative_path = relative_path.replace("/", "\\")
    return os.path.join(os.path.abspath("."), relative_path)


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9001


def contact_client(cmd, callback):
    global HOST, PORT
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(cmd.encode("UTF-8"))
        data = s.recv(1024)
        retval = data.decode("UTF-8")
        w_obj = json.loads(retval)
        time.sleep(0.2)
        callback(w_obj)


config_file = os.getcwd() + "\\Cool.config"

for line in open(config_file, "r"):
    exec(line.strip())

lang = "en"


class I18N():
    '''Internationalization'''

    def __init__(self, language):
        if language == 'en':
            self.resourceLanguageEnglish()
        elif language == 'de':
            self.resourceLanguageGerman()
        elif language == "fr":
            self.resourceLanguageFrench()
        else:
            raise NotImplementedError('Unsupported language.')

    def resourceLanguageEnglish(self):
        self.supplier = "Supplier"
        self.article = "Article"
        self.driver_name = "Driver Name"
        self.scan_license_plate = "Scan License Plate"
        self.enter_license_plate = "Enter License Plate"
        self.qr_code_has_printed = "QR Code has printed"
        self.number = "Number"
        self.next = "Next"
        self.back = "Back"
        self.description = "Description"
        self.do_have_qr_code = "Do you have QR Code?"
        self.enter_code = "Enter Code"
        self.yes = "Yes"
        self.no = "No"
        self.enter = "Enter"
        self.please_enter_correct_code = "* Please Enter Correct Code"
        self.get = "Get"
        self.weight = "Weight"
        self.initial_weighing = "Initial Weighing"
        self.truck_image_has_captured = "Truck Image has captured"
        self.weighing_after_unload = "Weighing After Unload"
        self.signature_here_for_confirmation = "Signature here for confirmation"
        self.please_wait_the_QR_code_is_printing = "Please wait, the QR code is printing!"

    def resourceLanguageGerman(self):
        self.supplier = "Lieferant"
        self.article = "Artikel"
        self.driver_name = "Fahrername"
        self.scan_license_plate = "KFZ-Kennzeichenerkennung"
        self.enter_license_plate = "KFZ-Kennzeichen eingeben"
        self.qr_code_has_printed = "Der QR-Code wurde ausgegeben"
        self.number = "Nummer"
        self.next = "Weiter"
        self.back = "Zurück"
        self.description = "Beschreibung"
        self.do_have_qr_code = "Haben Sie einen QR-Code?"
        self.enter_code = "Code eingeben"
        self.yes = "Ja"
        self.no = "Nein"
        self.enter = "eingeben"
        self.please_enter_correct_code = "* Bitte geben Sie den richtigen Code ein"
        self.get = "Erkennen"
        self.weight = "Gewicht"
        self.initial_weighing = "Erstes Wiegen"
        self.truck_image_has_captured = "Truck Image wurde erfasst"
        self.weighing_after_unload = "Wiegen nach dem Entladen"
        self.signature_here_for_confirmation = "Unterschrift hier zur Bestätigung"
        self.please_wait_the_QR_code_is_printing = "Bitte warten Sie, der QR code wird gedruckt!"

class Ui_Language(object):
    def setupUi(self, Language):
        Language.setWindowFlag(Qt.FramelessWindowHint)
        Language.setObjectName("Language")
        Language.setEnabled(True)
        Language.resize(1024, 768)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        Language.setFont(font)
        Language.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Language)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 60, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.englishButton = QtWidgets.QPushButton(self.centralwidget)
        self.englishButton.setGeometry(QtCore.QRect(70, 200, 200, 120))
        self.englishButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/english.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.englishButton.setIcon(icon)
        self.englishButton.setIconSize(QtCore.QSize(250, 150))
        self.englishButton.setObjectName("englishButton")
        self.germanyButton = QtWidgets.QPushButton(self.centralwidget)
        self.germanyButton.setGeometry(QtCore.QRect(400, 200, 200, 120))
        self.germanyButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/germany.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.germanyButton.setIcon(icon1)
        self.germanyButton.setIconSize(QtCore.QSize(250, 150))
        self.germanyButton.setObjectName("germanyButton")
        self.franceButton = QtWidgets.QPushButton(self.centralwidget)
        self.franceButton.setGeometry(QtCore.QRect(750, 200, 200, 120))
        self.franceButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/france.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.franceButton.setIcon(icon2)
        self.franceButton.setIconSize(QtCore.QSize(250, 150))
        self.franceButton.setObjectName("franceButton")
        self.romaniaButton = QtWidgets.QPushButton(self.centralwidget)
        self.romaniaButton.setGeometry(QtCore.QRect(230, 390, 200, 120))
        self.romaniaButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/romania.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.romaniaButton.setIcon(icon3)
        self.romaniaButton.setIconSize(QtCore.QSize(250, 150))
        self.romaniaButton.setObjectName("romaniaButton")
        self.turkeyButton = QtWidgets.QPushButton(self.centralwidget)
        self.turkeyButton.setEnabled(True)
        self.turkeyButton.setGeometry(QtCore.QRect(580, 390, 200, 120))
        self.turkeyButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/turkey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.turkeyButton.setIcon(icon4)
        self.turkeyButton.setIconSize(QtCore.QSize(250, 150))
        self.turkeyButton.setObjectName("turkeyButton")
        self.mouseTimer = QtCore.QTimer()
        self.mouseTimer.setInterval(250)
        self.mouseTimer.setSingleShot(True)
        self.mouseTimer.timeout.connect(self.mouseTimeout)
        self.left_count = 0
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.click_count = 0
        self.label_2.mousePressEvent = self.checkAboard;
        Language.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Language)
        self.statusbar.setObjectName("statusbar")
        Language.setStatusBar(self.statusbar)

        self.retranslateUi(Language)
        QtCore.QMetaObject.connectSlotsByName(Language)

        self.englishButton.clicked.connect(lambda: self.clicked("english", Language))
        self.germanyButton.clicked.connect(lambda: self.clicked("germany", Language))
        self.franceButton.clicked.connect(lambda: self.clicked("france", Language))
        self.romaniaButton.clicked.connect(lambda: self.clicked("romania", Language))
        self.turkeyButton.clicked.connect(lambda: self.clicked("turkey", Language))

    def retranslateUi(self, Language):
        _translate = QtCore.QCoreApplication.translate
        Language.setWindowTitle(_translate("Language", "Coolback"))
        self.label.setText(_translate("Language", "Select Language"))

    def clicked(self, text, window):
        global lang
        if text == "english":
            lang = "en"
        elif text == "germany":
            lang = "de"
        elif text == "france":
            pass
        elif text == "romania":
            pass
        elif text == "turkey":
            pass
        self.checkCode = QtWidgets.QMainWindow()
        self.ui = Ui_checkCode()
        #self.logo.mousePressEvent = None
        self.ui.setupUi(self.checkCode)
        self.checkCode.show()
        window.hide()

    def checkAboard(self, event):
        self.click_count += 1
        self.mouseTimer.start()
        if self.click_count > 3:
            _thread.start_new_thread(contact_client, ("QUIT","nothing"))
            time.sleep(5)
            sys.exit(0)

    def mouseTimeout(self):
        self.click_count = 0

code = ""
class Ui_checkCode(object):
    def setupUi(self, checkCode):
        checkCode.setWindowFlag(Qt.FramelessWindowHint)
        checkCode.setObjectName("checkCode")
        checkCode.resize(1024, 768)
        checkCode.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(checkCode)
        self.centralwidget.setObjectName("centralwidget")
        self.codeLabel = QtWidgets.QLabel(self.centralwidget)
        self.codeLabel.setGeometry(QtCore.QRect(330, 200, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.codeLabel.setFont(font)
        self.codeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.codeLabel.setObjectName("codeLabel")
        self.yesButton = QtWidgets.QPushButton(self.centralwidget)
        self.yesButton.setGeometry(QtCore.QRect(650, 340, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yesButton.setFont(font)
        self.yesButton.setStyleSheet("background-color: rgb(13, 13, 13);\n"
"color: rgb(255, 255, 255);")
        self.yesButton.setObjectName("yesButton")
        self.noButton = QtWidgets.QPushButton(self.centralwidget)
        self.noButton.setGeometry(QtCore.QRect(260, 350, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.noButton.setFont(font)
        self.noButton.setStyleSheet("background-color: rgb(13, 13, 13);\n"
"color: rgb(255, 255, 255);")
        self.noButton.setObjectName("noButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(400, 160, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(400, 140, 321, 16))
        self.errorLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.errorLabel.setObjectName("errorLabel")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(560, 300, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_3.setFont(font)
        self.Button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_3.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_3.setAutoDefault(False)
        self.Button_3.setObjectName("Button_3")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(560, 460, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_9.setFont(font)
        self.Button_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_9.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_9.setAutoDefault(False)
        self.Button_9.setObjectName("Button_9")
        self.Button_dot = QtWidgets.QPushButton(self.centralwidget)
        self.Button_dot.setGeometry(QtCore.QRect(400, 540, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_dot.setFont(font)
        self.Button_dot.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_dot.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_dot.setAutoDefault(False)
        self.Button_dot.setObjectName("Button_dot")
        self.Button_back = QtWidgets.QPushButton(self.centralwidget)
        self.Button_back.setGeometry(QtCore.QRect(560, 540, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_back.setFont(font)
        self.Button_back.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_back.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_back.setAutoDefault(False)
        self.Button_back.setObjectName("Button_back")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(400, 300, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_1.setFont(font)
        self.Button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_1.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_1.setAutoDefault(False)
        self.Button_1.setObjectName("Button_1")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(400, 460, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_7.setFont(font)
        self.Button_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_7.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_7.setAutoDefault(False)
        self.Button_7.setObjectName("Button_7")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(480, 540, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_0.setFont(font)
        self.Button_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_0.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_0.setAutoDefault(False)
        self.Button_0.setObjectName("Button_0")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(480, 460, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_8.setFont(font)
        self.Button_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_8.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_8.setAutoDefault(False)
        self.Button_8.setObjectName("Button_8")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(560, 380, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_6.setFont(font)
        self.Button_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_6.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_6.setAutoDefault(False)
        self.Button_6.setObjectName("Button_6")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(480, 380, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_5.setFont(font)
        self.Button_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_5.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_5.setAutoDefault(False)
        self.Button_5.setObjectName("Button_5")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(480, 300, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_2.setFont(font)
        self.Button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_2.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_2.setAutoDefault(False)
        self.Button_2.setObjectName("Button_2")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(400, 380, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_4.setFont(font)
        self.Button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_4.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_4.setAutoDefault(False)
        self.Button_4.setObjectName("Button_4")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(50, 550, 151, 111))
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(820, 550, 151, 111))
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon1)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        checkCode.setCentralWidget(self.centralwidget)

        self.retranslateUi(checkCode)
        QtCore.QMetaObject.connectSlotsByName(checkCode)

        self.label.hide()
        self.lineEdit.hide()
        self.nextButton.hide()
        self.backButton.hide()
        self.errorLabel.hide()
        self.Button_0.hide()
        self.Button_1.hide()
        self.Button_2.hide()
        self.Button_3.hide()
        self.Button_4.hide()
        self.Button_5.hide()
        self.Button_6.hide()
        self.Button_7.hide()
        self.Button_8.hide()
        self.Button_9.hide()
        self.Button_back.hide()
        self.Button_dot.hide()

        self.nextButton.clicked.connect(lambda: self.clicked("next", checkCode))
        self.noButton.clicked.connect(lambda: self.clicked("no", checkCode))
        self.yesButton.clicked.connect(lambda: self.clicked("yes", checkCode))
        self.backButton.clicked.connect(lambda: self.clicked("back", checkCode))

        self.Button_1.clicked.connect(lambda: self.key_press("1"))
        self.Button_2.clicked.connect(lambda: self.key_press("2"))
        self.Button_3.clicked.connect(lambda: self.key_press("3"))
        self.Button_4.clicked.connect(lambda: self.key_press("4"))
        self.Button_5.clicked.connect(lambda: self.key_press("5"))
        self.Button_6.clicked.connect(lambda: self.key_press("6"))
        self.Button_7.clicked.connect(lambda: self.key_press("7"))
        self.Button_8.clicked.connect(lambda: self.key_press("8"))
        self.Button_9.clicked.connect(lambda: self.key_press("9"))
        self.Button_0.clicked.connect(lambda: self.key_press("0"))
        self.Button_dot.clicked.connect(lambda: self.key_press("."))
        self.Button_back.clicked.connect(lambda: self.key_press("<-"))

    def retranslateUi(self, checkCode):
        _translate = QtCore.QCoreApplication.translate
        checkCode.setWindowTitle(_translate("checkCode", "Coolback"))
        self.i18n = I18N(lang)
        self.codeLabel.setText(_translate("checkCode", self.i18n.do_have_qr_code))
        self.yesButton.setText(_translate("checkCode", self.i18n.yes))
        self.noButton.setText(_translate("checkCode", self.i18n.no))
        self.label.setText(_translate("checkCode", self.i18n.enter_code))
        self.errorLabel.setText(_translate("checkCode", self.i18n.please_enter_correct_code))
        self.Button_3.setText(_translate("checkCode", "3"))
        self.Button_9.setText(_translate("checkCode", "9"))
        self.Button_dot.setText(_translate("checkCode", "."))
        self.Button_back.setText(_translate("checkCode", "<-"))
        self.Button_1.setText(_translate("checkCode", "1"))
        self.Button_7.setText(_translate("checkCode", "7"))
        self.Button_0.setText(_translate("checkCode", "0"))
        self.Button_8.setText(_translate("checkCode", "8"))
        self.Button_6.setText(_translate("checkCode", "6"))
        self.Button_5.setText(_translate("checkCode", "5"))
        self.Button_2.setText(_translate("checkCode", "2"))
        self.Button_4.setText(_translate("checkCode", "4"))


    def clicked(self, text, window):
        if text == "next":
            global license_plate, driver_name, weight_1, date_1, time_1, alibi_nr_1, supplier_no, supplier_des, article_no, article_des
            global imgstring0
            global imgstring1
            with open("yard_list.json", "r") as jsonFile:
                yard_list = json.load(jsonFile)

            entered_code = self.lineEdit.text()

            remove_item = None

            for i in range(len(yard_list)):
                if str(entered_code) == yard_list[i]["code"]:
                    license_plate = yard_list[i]["license_plate"]
                    driver_name = yard_list[i]["driver_name"]
                    weight_1 = yard_list[i]["weight_1"]
                    date_1 = yard_list[i]["date_1"]
                    time_1 = yard_list[i]["time_1"]
                    alibi_nr_1 = yard_list[i]["alibi_nr_1"]
                    supplier_no = yard_list[i]["supplier_no"]
                    supplier_des = yard_list[i]["supplier_des"]
                    article_no = yard_list[i]["article_no"]
                    article_des = yard_list[i]["article_des"]
                    imgstring0 = yard_list[i]["imgstring0"]
                    imgstring1 = yard_list[i]["imgstring1"]
                    remove_item = i


            if remove_item == None:
                self.errorLabel.show()
            else:
                yard_list.pop(remove_item)
                with open("yard_list.json", "w") as jsonFile:
                    json.dump(yard_list, jsonFile)

                self.WeightAfterUnload = QtWidgets.QMainWindow()
                self.ui = Ui_WeightAfterUnload()
                self.ui.setupUi(self.WeightAfterUnload)
                self.WeightAfterUnload.show()
                window.close()

        elif text == "no":
            self.SupplierAndArticle = QtWidgets.QMainWindow()
            self.ui = Ui_SupplierAndArticle()
            self.ui.setupUi(self.SupplierAndArticle)
            self.SupplierAndArticle.show()
            window.close()
        elif text == "back":
            self.yesButton.show()
            self.noButton.show()
            self.codeLabel.show()
            self.label.hide()
            self.lineEdit.hide()
            self.nextButton.hide()
            self.backButton.hide()
            self.errorLabel.hide()
            self.Button_0.hide()
            self.Button_1.hide()
            self.Button_2.hide()
            self.Button_3.hide()
            self.Button_4.hide()
            self.Button_5.hide()
            self.Button_6.hide()
            self.Button_7.hide()
            self.Button_8.hide()
            self.Button_9.hide()
            self.Button_back.hide()
            self.Button_dot.hide()
        else:
            self.yesButton.hide()
            self.noButton.hide()
            self.codeLabel.hide()
            self.label.show()
            self.lineEdit.show()
            self.nextButton.show()
            self.backButton.show()
            self.lineEdit.setFocus(True)
            self.Button_0.show()
            self.Button_1.show()
            self.Button_2.show()
            self.Button_3.show()
            self.Button_4.show()
            self.Button_5.show()
            self.Button_6.show()
            self.Button_7.show()
            self.Button_8.show()
            self.Button_9.show()
            self.Button_back.show()
            self.Button_dot.show()

    def key_press(self, text):
        if text == "<-":
            txt = self.lineEdit.text()
            self.lineEdit.setText(txt[:-1])
        else:
            txt = self.lineEdit.text()
            txt += text
            self.lineEdit.setText(txt)


class Ui_SupplierAndArticle(object):
    def setupUi(self, SupplierAndArticle):
        SupplierAndArticle.setWindowFlag(Qt.FramelessWindowHint)
        SupplierAndArticle.setObjectName("SupplierAndArticle")
        SupplierAndArticle.resize(1024, 768)
        SupplierAndArticle.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(SupplierAndArticle)
        self.centralwidget.setObjectName("centralwidget")
        self.supplierButton = QtWidgets.QPushButton(self.centralwidget)
        self.supplierButton.setGeometry(QtCore.QRect(140, 270, 251, 161))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.supplierButton.setFont(font)
        self.supplierButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.supplierButton.setObjectName("supplierButton")
        self.articleButton = QtWidgets.QPushButton(self.centralwidget)
        self.articleButton.setGeometry(QtCore.QRect(610, 270, 251, 161))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.articleButton.setFont(font)
        self.articleButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.articleButton.setObjectName("articleButton")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        SupplierAndArticle.setCentralWidget(self.centralwidget)

        self.retranslateUi(SupplierAndArticle)
        QtCore.QMetaObject.connectSlotsByName(SupplierAndArticle)

        self.supplierButton.clicked.connect(lambda: self.clicked("supplier", SupplierAndArticle))
        self.articleButton.setDisabled(True)


    def retranslateUi(self, SupplierAndArticle):
        _translate = QtCore.QCoreApplication.translate
        SupplierAndArticle.setWindowTitle(_translate("SupplierAndArticle", "Coolback"))
        self.i18n = I18N(lang)
        self.supplierButton.setText(_translate("SupplierAndArticle", self.i18n.supplier))
        self.articleButton.setText(_translate("SupplierAndArticle", self.i18n.article))

    def clicked(self, text, window):
        self.SupplierList = QtWidgets.QMainWindow()
        self.ui = Ui_SupplierList()
        self.ui.setupUi(self.SupplierList)
        self.ui.listWidget.setCurrentRow(0)
        self.SupplierList.show()
        window.close()



supplier_no = ""
supplier_des = ""
class Ui_SupplierList(object):
    def setupUi(self, SupplierList):
        SupplierList.setWindowFlag(Qt.FramelessWindowHint)
        SupplierList.setObjectName("SupplierList")
        SupplierList.resize(1024, 768)
        SupplierList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(SupplierList)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(90, 150, 841, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.numberLabel = QtWidgets.QLabel(self.centralwidget)
        self.numberLabel.setGeometry(QtCore.QRect(90, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.numberLabel.setFont(font)
        self.numberLabel.setObjectName("numberLabel")
        self.descriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.descriptionLabel.setGeometry(QtCore.QRect(280, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(810, 550, 151, 111))
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(50, 550, 151, 111))
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        SupplierList.setCentralWidget(self.centralwidget)

        self.retranslateUi(SupplierList)
        QtCore.QMetaObject.connectSlotsByName(SupplierList)

        self.df = pd.read_csv("data/Lieferanten.csv", sep=';', encoding='unicode_escape')

        for i in range(len(self.df)):
            self.listWidget.insertItem(i,"{}       \t\t     {}".format(str(self.df.iloc[i, 0]), str(self.df.iloc[i, 1])))

        self.nextButton.clicked.connect(lambda: self.clicked("next", SupplierList))
        self.backButton.clicked.connect(lambda: self.clicked("back", SupplierList))

    def retranslateUi(self, SupplierList):
        _translate = QtCore.QCoreApplication.translate
        SupplierList.setWindowTitle(_translate("SupplierList", "Coolback"))
        self.i18n = I18N(lang)
        self.numberLabel.setText(_translate("SupplierList", self.i18n.number))
        self.descriptionLabel.setText(_translate("SupplierList", self.i18n.description))

    def clicked(self, text, window):
        if text == "next":
            row = self.listWidget.currentRow()
            global supplier_no, supplier_des
            supplier_no = self.df.iloc[row, 0]
            supplier_des = self.df.iloc[row, 1]
            self.SupplierAndArticle = QtWidgets.QMainWindow()
            self.ui = Ui_SupplierAndArticle_1()
            self.ui.setupUi(self.SupplierAndArticle)
            self.SupplierAndArticle.show()
            window.close()
        elif text == "back":
            self.SupplierAndArticle = QtWidgets.QMainWindow()
            self.ui = Ui_SupplierAndArticle()
            self.ui.setupUi(self.SupplierAndArticle)
            self.SupplierAndArticle.show()
            window.close()


class Ui_SupplierAndArticle_1(object):
    def setupUi(self, SupplierAndArticle):
        SupplierAndArticle.setWindowFlag(Qt.FramelessWindowHint)
        SupplierAndArticle.setObjectName("SupplierAndArticle")
        SupplierAndArticle.resize(1024, 768)
        SupplierAndArticle.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(SupplierAndArticle)
        self.centralwidget.setObjectName("centralwidget")
        self.supplierButton = QtWidgets.QPushButton(self.centralwidget)
        self.supplierButton.setGeometry(QtCore.QRect(140, 270, 251, 161))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.supplierButton.setFont(font)
        self.supplierButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 10px;")
        self.supplierButton.setObjectName("supplierButton")
        self.articleButton = QtWidgets.QPushButton(self.centralwidget)
        self.articleButton.setGeometry(QtCore.QRect(610, 270, 251, 161))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.articleButton.setFont(font)
        self.articleButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius: 10px;")
        self.articleButton.setObjectName("articleButton")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        SupplierAndArticle.setCentralWidget(self.centralwidget)

        self.retranslateUi(SupplierAndArticle)
        QtCore.QMetaObject.connectSlotsByName(SupplierAndArticle)

        self.articleButton.clicked.connect(lambda: self.clicked("article", SupplierAndArticle))
        self.supplierButton.setDisabled(True)

    def retranslateUi(self, SupplierAndArticle):
        _translate = QtCore.QCoreApplication.translate
        SupplierAndArticle.setWindowTitle(_translate("SupplierAndArticle", "Coolback"))

        self.i18n = I18N(lang)
        self.supplierButton.setText(_translate("SupplierAndArticle", self.i18n.supplier))
        self.articleButton.setText(_translate("SupplierAndArticle", self.i18n.article))

    def clicked(self, text, window):
        self.ArticleList = QtWidgets.QMainWindow()
        self.ui = Ui_ArticleList()
        self.ui.setupUi(self.ArticleList)
        self.ui.listWidget.setCurrentRow(0)
        self.ArticleList.show()
        window.close()



article_no = ""
article_des = ""
class Ui_ArticleList(object):
    def setupUi(self, ArticleList):
        ArticleList.setWindowFlag(Qt.FramelessWindowHint)
        ArticleList.setObjectName("ArticleList")
        ArticleList.resize(1024, 768)
        ArticleList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ArticleList)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(90, 150, 841, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.numberLabel = QtWidgets.QLabel(self.centralwidget)
        self.numberLabel.setGeometry(QtCore.QRect(90, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.numberLabel.setFont(font)
        self.numberLabel.setObjectName("numberLabel")
        self.descriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.descriptionLabel.setGeometry(QtCore.QRect(280, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(810, 550, 151, 111))
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(50, 550, 151, 111))
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        ArticleList.setCentralWidget(self.centralwidget)

        self.retranslateUi(ArticleList)
        QtCore.QMetaObject.connectSlotsByName(ArticleList)

        self.df = pd.read_csv("data/Artikel.csv", sep=';', encoding='unicode_escape')

        for i in range(len(self.df)):
            self.listWidget.insertItem(i,"{}       \t\t     {}".format(str(self.df.iloc[i, 0]), str(self.df.iloc[i, 1])))

        self.nextButton.clicked.connect(lambda: self.clicked("next", ArticleList))
        self.backButton.clicked.connect(lambda: self.clicked("back", ArticleList))

    def retranslateUi(self, ArticleList):
        _translate = QtCore.QCoreApplication.translate
        ArticleList.setWindowTitle(_translate("ArticleList", "Coolback"))

        self.i18n = I18N(lang)
        self.numberLabel.setText(_translate("ArticleList", self.i18n.number))
        self.descriptionLabel.setText(_translate("ArticleList", self.i18n.description))


    def clicked(self, text, window):
        if text == "next":
            row = self.listWidget.currentRow()
            global article_no, article_des
            article_no = self.df.iloc[row, 0]
            article_des = self.df.iloc[row, 1]
            self.EnterName = QtWidgets.QMainWindow()
            self.ui = Ui_EnterName()
            self.ui.setupUi(self.EnterName)
            self.EnterName.show()
            window.close()
        elif text == "back":
            self.SupplierAndArticle = QtWidgets.QMainWindow()
            self.ui = Ui_SupplierAndArticle_1()
            self.ui.setupUi(self.SupplierAndArticle)
            self.SupplierAndArticle.show()
            window.close()



driver_name = ""
class Ui_EnterName(object):
    def setupUi(self, EnterName):
        EnterName.setWindowFlag(Qt.FramelessWindowHint)
        EnterName.setObjectName("EnterName")
        EnterName.resize(1024, 768)
        EnterName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(EnterName)
        self.centralwidget.setObjectName("centralwidget")
        self.driver_nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.driver_nameLabel.setGeometry(QtCore.QRect(200, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.driver_nameLabel.setFont(font)
        self.driver_nameLabel.setObjectName("driver_nameLabel")
        self.driver_nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.driver_nameLineEdit.setGeometry(QtCore.QRect(380, 210, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.driver_nameLineEdit.setFont(font)
        self.driver_nameLineEdit.setObjectName("driver_nameLineEdit")
        self.AButton = QtWidgets.QPushButton(self.centralwidget)
        self.AButton.setGeometry(QtCore.QRect(220, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AButton.setFont(font)
        self.AButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.AButton.setObjectName("AButton")
        self.ZButton = QtWidgets.QPushButton(self.centralwidget)
        self.ZButton.setGeometry(QtCore.QRect(220, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ZButton.setFont(font)
        self.ZButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.ZButton.setObjectName("ZButton")
        self.WButton = QtWidgets.QPushButton(self.centralwidget)
        self.WButton.setGeometry(QtCore.QRect(270, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WButton.setFont(font)
        self.WButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.WButton.setObjectName("WButton")
        self.SButton = QtWidgets.QPushButton(self.centralwidget)
        self.SButton.setGeometry(QtCore.QRect(270, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SButton.setFont(font)
        self.SButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.SButton.setObjectName("SButton")
        self.EButton = QtWidgets.QPushButton(self.centralwidget)
        self.EButton.setGeometry(QtCore.QRect(320, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EButton.setFont(font)
        self.EButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.EButton.setObjectName("EButton")
        self.Button_dot = QtWidgets.QPushButton(self.centralwidget)
        self.Button_dot.setGeometry(QtCore.QRect(620, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_dot.setFont(font)
        self.Button_dot.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_dot.setObjectName("Button_dot")
        self.FButton = QtWidgets.QPushButton(self.centralwidget)
        self.FButton.setGeometry(QtCore.QRect(370, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FButton.setFont(font)
        self.FButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.FButton.setObjectName("FButton")
        self.JButton = QtWidgets.QPushButton(self.centralwidget)
        self.JButton.setGeometry(QtCore.QRect(520, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.JButton.setFont(font)
        self.JButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.JButton.setObjectName("JButton")
        self.NButton = QtWidgets.QPushButton(self.centralwidget)
        self.NButton.setGeometry(QtCore.QRect(470, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NButton.setFont(font)
        self.NButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.NButton.setObjectName("NButton")
        self.VButton = QtWidgets.QPushButton(self.centralwidget)
        self.VButton.setGeometry(QtCore.QRect(370, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VButton.setFont(font)
        self.VButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.VButton.setObjectName("VButton")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(420, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_5.setFont(font)
        self.Button_5.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_5.setObjectName("Button_5")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(620, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_9.setFont(font)
        self.Button_9.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_9.setObjectName("Button_9")
        self.IButton = QtWidgets.QPushButton(self.centralwidget)
        self.IButton.setGeometry(QtCore.QRect(570, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IButton.setFont(font)
        self.IButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.IButton.setObjectName("IButton")
        self.GButton = QtWidgets.QPushButton(self.centralwidget)
        self.GButton.setGeometry(QtCore.QRect(420, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GButton.setFont(font)
        self.GButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.GButton.setObjectName("GButton")
        self.OButton = QtWidgets.QPushButton(self.centralwidget)
        self.OButton.setGeometry(QtCore.QRect(620, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OButton.setFont(font)
        self.OButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.OButton.setObjectName("OButton")
        self.MButton = QtWidgets.QPushButton(self.centralwidget)
        self.MButton.setGeometry(QtCore.QRect(520, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MButton.setFont(font)
        self.MButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.MButton.setObjectName("MButton")
        self.LButton = QtWidgets.QPushButton(self.centralwidget)
        self.LButton.setGeometry(QtCore.QRect(620, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LButton.setFont(font)
        self.LButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.LButton.setObjectName("LButton")
        self.KButton = QtWidgets.QPushButton(self.centralwidget)
        self.KButton.setGeometry(QtCore.QRect(570, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.KButton.setFont(font)
        self.KButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.KButton.setObjectName("KButton")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(270, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_2.setFont(font)
        self.Button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_2.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_2.setObjectName("Button_2")
        self.RButton = QtWidgets.QPushButton(self.centralwidget)
        self.RButton.setGeometry(QtCore.QRect(370, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RButton.setFont(font)
        self.RButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.RButton.setObjectName("RButton")
        self.PButton = QtWidgets.QPushButton(self.centralwidget)
        self.PButton.setGeometry(QtCore.QRect(670, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PButton.setFont(font)
        self.PButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.PButton.setObjectName("PButton")
        self.ButtonSpace = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSpace.setGeometry(QtCore.QRect(670, 470, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonSpace.setFont(font)
        self.ButtonSpace.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.ButtonSpace.setObjectName("ButtonSpace")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget)
        self.minusButton.setGeometry(QtCore.QRect(720, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.minusButton.setFont(font)
        self.minusButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.minusButton.setObjectName("minusButton")
        self.backButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.backButton_2.setGeometry(QtCore.QRect(720, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backButton_2.setFont(font)
        self.backButton_2.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.backButton_2.setObjectName("backButton_2")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(370, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_4.setFont(font)
        self.Button_4.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_4.setObjectName("Button_4")
        self.CButton = QtWidgets.QPushButton(self.centralwidget)
        self.CButton.setGeometry(QtCore.QRect(320, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CButton.setFont(font)
        self.CButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.CButton.setObjectName("CButton")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(470, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_6.setFont(font)
        self.Button_6.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_6.setObjectName("Button_6")
        self.HButton = QtWidgets.QPushButton(self.centralwidget)
        self.HButton.setGeometry(QtCore.QRect(470, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HButton.setFont(font)
        self.HButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.HButton.setObjectName("HButton")
        self.YButton = QtWidgets.QPushButton(self.centralwidget)
        self.YButton.setGeometry(QtCore.QRect(470, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YButton.setFont(font)
        self.YButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.YButton.setObjectName("YButton")
        self.XButton = QtWidgets.QPushButton(self.centralwidget)
        self.XButton.setGeometry(QtCore.QRect(270, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.XButton.setFont(font)
        self.XButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.XButton.setObjectName("XButton")
        self.ButtonGerU = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonGerU.setGeometry(QtCore.QRect(570, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonGerU.setFont(font)
        self.ButtonGerU.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.ButtonGerU.setObjectName("ButtonGerU")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(670, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_0.setFont(font)
        self.Button_0.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_0.setObjectName("Button_0")
        self.TButton = QtWidgets.QPushButton(self.centralwidget)
        self.TButton.setGeometry(QtCore.QRect(420, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TButton.setFont(font)
        self.TButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.TButton.setObjectName("TButton")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(570, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_8.setFont(font)
        self.Button_8.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_8.setObjectName("Button_8")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(320, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_3.setFont(font)
        self.Button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_3.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_3.setObjectName("Button_3")
        self.DButton = QtWidgets.QPushButton(self.centralwidget)
        self.DButton.setGeometry(QtCore.QRect(320, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DButton.setFont(font)
        self.DButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.DButton.setObjectName("DButton")
        self.ButtonGerO = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonGerO.setGeometry(QtCore.QRect(720, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonGerO.setFont(font)
        self.ButtonGerO.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.ButtonGerO.setObjectName("ButtonGerO")
        self.BButton = QtWidgets.QPushButton(self.centralwidget)
        self.BButton.setGeometry(QtCore.QRect(420, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BButton.setFont(font)
        self.BButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.BButton.setObjectName("BButton")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(520, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_7.setFont(font)
        self.Button_7.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_7.setObjectName("Button_7")
        self.UButton = QtWidgets.QPushButton(self.centralwidget)
        self.UButton.setGeometry(QtCore.QRect(520, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UButton.setFont(font)
        self.UButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.UButton.setObjectName("UButton")
        self.QButton = QtWidgets.QPushButton(self.centralwidget)
        self.QButton.setGeometry(QtCore.QRect(220, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QButton.setFont(font)
        self.QButton.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.QButton.setObjectName("QButton")
        self.ButtonGerA = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonGerA.setGeometry(QtCore.QRect(670, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonGerA.setFont(font)
        self.ButtonGerA.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.ButtonGerA.setObjectName("ButtonGerA")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(220, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_1.setFont(font)
        self.Button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_1.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_1.setAutoDefault(False)
        self.Button_1.setObjectName("Button_1")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(50, 570, 151, 111))
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(790, 570, 151, 111))
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon1)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        EnterName.setCentralWidget(self.centralwidget)

        self.retranslateUi(EnterName)
        QtCore.QMetaObject.connectSlotsByName(EnterName)

        self.QButton.clicked.connect(lambda: self.key_press("Q"))
        self.WButton.clicked.connect(lambda: self.key_press("W"))
        self.EButton.clicked.connect(lambda: self.key_press("E"))
        self.RButton.clicked.connect(lambda: self.key_press("R"))
        self.TButton.clicked.connect(lambda: self.key_press("T"))
        self.YButton.clicked.connect(lambda: self.key_press("Y"))
        self.UButton.clicked.connect(lambda: self.key_press("U"))
        self.IButton.clicked.connect(lambda: self.key_press("I"))
        self.OButton.clicked.connect(lambda: self.key_press("O"))
        self.PButton.clicked.connect(lambda: self.key_press("P"))
        self.AButton.clicked.connect(lambda: self.key_press("A"))
        self.SButton.clicked.connect(lambda: self.key_press("S"))
        self.DButton.clicked.connect(lambda: self.key_press("D"))
        self.FButton.clicked.connect(lambda: self.key_press("F"))
        self.GButton.clicked.connect(lambda: self.key_press("G"))
        self.HButton.clicked.connect(lambda: self.key_press("H"))
        self.JButton.clicked.connect(lambda: self.key_press("J"))
        self.KButton.clicked.connect(lambda: self.key_press("K"))
        self.LButton.clicked.connect(lambda: self.key_press("L"))
        self.ZButton.clicked.connect(lambda: self.key_press("Z"))
        self.XButton.clicked.connect(lambda: self.key_press("X"))
        self.CButton.clicked.connect(lambda: self.key_press("C"))
        self.VButton.clicked.connect(lambda: self.key_press("V"))
        self.BButton.clicked.connect(lambda: self.key_press("B"))
        self.NButton.clicked.connect(lambda: self.key_press("N"))
        self.MButton.clicked.connect(lambda: self.key_press("M"))
        self.ButtonGerA.clicked.connect(lambda: self.key_press("Ä"))
        self.ButtonGerO.clicked.connect(lambda: self.key_press("Ö"))
        self.ButtonGerU.clicked.connect(lambda: self.key_press("Ü"))
        self.Button_1.clicked.connect(lambda: self.key_press("1"))
        self.Button_2.clicked.connect(lambda: self.key_press("2"))
        self.Button_3.clicked.connect(lambda: self.key_press("3"))
        self.Button_4.clicked.connect(lambda: self.key_press("4"))
        self.Button_5.clicked.connect(lambda: self.key_press("5"))
        self.Button_6.clicked.connect(lambda: self.key_press("6"))
        self.Button_7.clicked.connect(lambda: self.key_press("7"))
        self.Button_8.clicked.connect(lambda: self.key_press("8"))
        self.Button_9.clicked.connect(lambda: self.key_press("9"))
        self.Button_0.clicked.connect(lambda: self.key_press("0"))
        self.minusButton.clicked.connect(lambda: self.key_press("-"))
        self.backButton_2.clicked.connect(lambda: self.key_press("<-"))
        self.ButtonSpace.clicked.connect(lambda: self.key_press(" "))
        self.Button_dot.clicked.connect(lambda: self.key_press(","))

        self.Button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.minusButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ButtonSpace.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ButtonGerA.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ButtonGerO.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ButtonGerU.setFocusPolicy(QtCore.Qt.NoFocus)
        self.QButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.WButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.EButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.RButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.TButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.YButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.UButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.IButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.OButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.PButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.FButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.GButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.HButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.JButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.KButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ZButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.XButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.CButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.VButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.BButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.NButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.MButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_dot.setFocusPolicy(QtCore.Qt.NoFocus)

        self.nextButton.clicked.connect(lambda: self.clicked("next", EnterName))
        self.backButton.clicked.connect(lambda: self.clicked("back", EnterName))

    def retranslateUi(self, EnterName):
        _translate = QtCore.QCoreApplication.translate
        EnterName.setWindowTitle(_translate("EnterName", "Coolpad"))

        self.i18n = I18N(lang)
        self.driver_nameLabel.setText(_translate("EnterName", self.i18n.driver_name))
        self.AButton.setText(_translate("EnterName", "A"))
        self.ZButton.setText(_translate("EnterName", "Z"))
        self.WButton.setText(_translate("EnterName", "W"))
        self.SButton.setText(_translate("EnterName", "S"))
        self.EButton.setText(_translate("EnterName", "E"))
        self.Button_dot.setText(_translate("EnterName", "."))
        self.FButton.setText(_translate("EnterName", "F"))
        self.JButton.setText(_translate("EnterName", "J"))
        self.NButton.setText(_translate("EnterName", "N"))
        self.VButton.setText(_translate("EnterName", "V"))
        self.Button_5.setText(_translate("EnterName", "5"))
        self.Button_9.setText(_translate("EnterName", "9"))
        self.IButton.setText(_translate("EnterName", "I"))
        self.GButton.setText(_translate("EnterName", "G"))
        self.OButton.setText(_translate("EnterName", "O"))
        self.MButton.setText(_translate("EnterName", "M"))
        self.LButton.setText(_translate("EnterName", "L"))
        self.KButton.setText(_translate("EnterName", "K"))
        self.Button_2.setText(_translate("EnterName", "2"))
        self.RButton.setText(_translate("EnterName", "R"))
        self.PButton.setText(_translate("EnterName", "P"))
        self.ButtonSpace.setText(_translate("EnterName", "SPACE"))
        self.minusButton.setText(_translate("EnterName", "-"))
        self.backButton_2.setText(_translate("EnterName", "<-"))
        self.Button_4.setText(_translate("EnterName", "4"))
        self.CButton.setText(_translate("EnterName", "C"))
        self.Button_6.setText(_translate("EnterName", "6"))
        self.HButton.setText(_translate("EnterName", "H"))
        self.YButton.setText(_translate("EnterName", "Y"))
        self.XButton.setText(_translate("EnterName", "X"))
        self.ButtonGerU.setText(_translate("EnterName", "Ü"))
        self.Button_0.setText(_translate("EnterName", "0"))
        self.TButton.setText(_translate("EnterName", "T"))
        self.Button_8.setText(_translate("EnterName", "8"))
        self.Button_3.setText(_translate("EnterName", "3"))
        self.DButton.setText(_translate("EnterName", "D"))
        self.ButtonGerO.setText(_translate("EnterName", "Ö"))
        self.BButton.setText(_translate("EnterName", "B"))
        self.Button_7.setText(_translate("EnterName", "7"))
        self.UButton.setText(_translate("EnterName", "U"))
        self.QButton.setText(_translate("EnterName", "Q"))
        self.ButtonGerA.setText(_translate("EnterName", "Ä"))
        self.Button_1.setText(_translate("EnterName", "1"))

    def clicked(self, text, window):
        if text == "next":
            if len(self.driver_nameLineEdit.text()) == 0:
                pass
            else:
                global driver_name
                driver_name = self.driver_nameLineEdit.text()
                self.ScanLicensePlate = QtWidgets.QMainWindow()
                self.ui = Ui_ScanLicensePlate()
                self.ui.setupUi(self.ScanLicensePlate)
                self.ScanLicensePlate.show()
                window.close()
        elif text == "back":
            self.ArticleList = QtWidgets.QMainWindow()
            self.ui = Ui_ArticleList()
            self.ui.setupUi(self.ArticleList)
            self.ArticleList.show()
            window.close()

    def key_press(self, text):

        if text == "<-":
            txt = self.driver_nameLineEdit.text()
            self.driver_nameLineEdit.setText(txt[:-1])
        else:
            txt = self.driver_nameLineEdit.text()
            txt += text
            self.driver_nameLineEdit.setText(txt)



license_plate = ""
class Ui_ScanLicensePlate(object):
    def setupUi(self, ScanLicensePlate):
        ScanLicensePlate.setWindowFlag(Qt.FramelessWindowHint)
        ScanLicensePlate.setObjectName("ScanLicensePlate")
        ScanLicensePlate.resize(1024, 768)
        ScanLicensePlate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ScanLicensePlate)
        self.centralwidget.setObjectName("centralwidget")
        self.scan_plateLabel = QtWidgets.QLabel(self.centralwidget)
        self.scan_plateLabel.setGeometry(QtCore.QRect(160, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scan_plateLabel.setFont(font)
        self.scan_plateLabel.setObjectName("scan_plateLabel")
        self.scan_plateLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.scan_plateLineEdit.setGeometry(QtCore.QRect(370, 250, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scan_plateLineEdit.setFont(font)
        self.scan_plateLineEdit.setObjectName("scan_plateLineEdit")
        self.getButton = QtWidgets.QPushButton(self.centralwidget)
        self.getButton.setGeometry(QtCore.QRect(770, 250, 111, 31))
        self.getButton.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);")
        self.getButton.setObjectName("getButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(820, 530, 151, 111))
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(50, 530, 151, 111))
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.AButton = QtWidgets.QPushButton(self.centralwidget)
        self.AButton.setGeometry(QtCore.QRect(220, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AButton.setFont(font)
        self.AButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.AButton.setObjectName("AButton")
        self.ZButton = QtWidgets.QPushButton(self.centralwidget)
        self.ZButton.setGeometry(QtCore.QRect(220, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ZButton.setFont(font)
        self.ZButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.ZButton.setObjectName("ZButton")
        self.WButton = QtWidgets.QPushButton(self.centralwidget)
        self.WButton.setGeometry(QtCore.QRect(270, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WButton.setFont(font)
        self.WButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.WButton.setObjectName("WButton")
        self.SButton = QtWidgets.QPushButton(self.centralwidget)
        self.SButton.setGeometry(QtCore.QRect(270, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SButton.setFont(font)
        self.SButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.SButton.setObjectName("SButton")
        self.EButton = QtWidgets.QPushButton(self.centralwidget)
        self.EButton.setGeometry(QtCore.QRect(320, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EButton.setFont(font)
        self.EButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.EButton.setObjectName("EButton")
        self.Button_dot = QtWidgets.QPushButton(self.centralwidget)
        self.Button_dot.setGeometry(QtCore.QRect(620, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_dot.setFont(font)
        self.Button_dot.setStyleSheet("border: 1px solid black;\n"
                                      "color: white;\n"
                                      "background-color: rgb(45, 45, 45);")
        self.Button_dot.setObjectName("Button_dot")
        self.FButton = QtWidgets.QPushButton(self.centralwidget)
        self.FButton.setGeometry(QtCore.QRect(370, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FButton.setFont(font)
        self.FButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.FButton.setObjectName("FButton")
        self.JButton = QtWidgets.QPushButton(self.centralwidget)
        self.JButton.setGeometry(QtCore.QRect(520, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.JButton.setFont(font)
        self.JButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.JButton.setObjectName("JButton")
        self.NButton = QtWidgets.QPushButton(self.centralwidget)
        self.NButton.setGeometry(QtCore.QRect(470, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NButton.setFont(font)
        self.NButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.NButton.setObjectName("NButton")
        self.VButton = QtWidgets.QPushButton(self.centralwidget)
        self.VButton.setGeometry(QtCore.QRect(370, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VButton.setFont(font)
        self.VButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.VButton.setObjectName("VButton")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(420, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_5.setFont(font)
        self.Button_5.setStyleSheet("border: 1px solid black;\n"
                                    "color: white;\n"
                                    "background-color: rgb(45, 45, 45);")
        self.Button_5.setObjectName("Button_5")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(620, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_9.setFont(font)
        self.Button_9.setStyleSheet("border: 1px solid black;\n"
                                    "color: white;\n"
                                    "background-color: rgb(45, 45, 45);")
        self.Button_9.setObjectName("Button_9")
        self.IButton = QtWidgets.QPushButton(self.centralwidget)
        self.IButton.setGeometry(QtCore.QRect(570, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IButton.setFont(font)
        self.IButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.IButton.setObjectName("IButton")
        self.GButton = QtWidgets.QPushButton(self.centralwidget)
        self.GButton.setGeometry(QtCore.QRect(420, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GButton.setFont(font)
        self.GButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.GButton.setObjectName("GButton")
        self.OButton = QtWidgets.QPushButton(self.centralwidget)
        self.OButton.setGeometry(QtCore.QRect(620, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OButton.setFont(font)
        self.OButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.OButton.setObjectName("OButton")
        self.MButton = QtWidgets.QPushButton(self.centralwidget)
        self.MButton.setGeometry(QtCore.QRect(520, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MButton.setFont(font)
        self.MButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.MButton.setObjectName("MButton")
        self.LButton = QtWidgets.QPushButton(self.centralwidget)
        self.LButton.setGeometry(QtCore.QRect(620, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LButton.setFont(font)
        self.LButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.LButton.setObjectName("LButton")
        self.KButton = QtWidgets.QPushButton(self.centralwidget)
        self.KButton.setGeometry(QtCore.QRect(570, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.KButton.setFont(font)
        self.KButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.KButton.setObjectName("KButton")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(270, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_2.setFont(font)
        self.Button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_2.setStyleSheet("border: 1px solid black;\n"
                                    "color: white;\n"
                                    "background-color: rgb(45, 45, 45);")
        self.Button_2.setObjectName("Button_2")
        self.RButton = QtWidgets.QPushButton(self.centralwidget)
        self.RButton.setGeometry(QtCore.QRect(370, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RButton.setFont(font)
        self.RButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.RButton.setObjectName("RButton")
        self.PButton = QtWidgets.QPushButton(self.centralwidget)
        self.PButton.setGeometry(QtCore.QRect(670, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PButton.setFont(font)
        self.PButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.PButton.setObjectName("PButton")
        self.ButtonSpace = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSpace.setGeometry(QtCore.QRect(670, 470, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonSpace.setFont(font)
        self.ButtonSpace.setStyleSheet("border: 1px solid black;\n"
                                       "color: white;\n"
                                       "background-color: rgb(45, 45, 45);")
        self.ButtonSpace.setObjectName("ButtonSpace")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget)
        self.minusButton.setGeometry(QtCore.QRect(720, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.minusButton.setFont(font)
        self.minusButton.setStyleSheet("border: 1px solid black;\n"
                                       "color: white;\n"
                                       "background-color: rgb(45, 45, 45);")
        self.minusButton.setObjectName("minusButton")
        self.backButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.backButton_2.setGeometry(QtCore.QRect(720, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backButton_2.setFont(font)
        self.backButton_2.setStyleSheet("border: 1px solid black;\n"
                                        "color: white;\n"
                                        "background-color: rgb(45, 45, 45);")
        self.backButton_2.setObjectName("backButton_2")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(370, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_4.setFont(font)
        self.Button_4.setStyleSheet("border: 1px solid black;\n"
                                    "color: white;\n"
                                    "background-color: rgb(45, 45, 45);")
        self.Button_4.setObjectName("Button_4")
        self.CButton = QtWidgets.QPushButton(self.centralwidget)
        self.CButton.setGeometry(QtCore.QRect(320, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CButton.setFont(font)
        self.CButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.CButton.setObjectName("CButton")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(470, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_6.setFont(font)
        self.Button_6.setStyleSheet("border: 1px solid black;\n"
                                    "color: white;\n"
                                    "background-color: rgb(45, 45, 45);")
        self.Button_6.setObjectName("Button_6")
        self.HButton = QtWidgets.QPushButton(self.centralwidget)
        self.HButton.setGeometry(QtCore.QRect(470, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HButton.setFont(font)
        self.HButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.HButton.setObjectName("HButton")
        self.YButton = QtWidgets.QPushButton(self.centralwidget)
        self.YButton.setGeometry(QtCore.QRect(470, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YButton.setFont(font)
        self.YButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.YButton.setObjectName("YButton")
        self.XButton = QtWidgets.QPushButton(self.centralwidget)
        self.XButton.setGeometry(QtCore.QRect(270, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.XButton.setFont(font)
        self.XButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.XButton.setObjectName("XButton")
        self.ButtonGerU = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonGerU.setGeometry(QtCore.QRect(570, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonGerU.setFont(font)
        self.ButtonGerU.setStyleSheet("border: 1px solid black;\n"
                                      "color: white;\n"
                                      "background-color: rgb(45, 45, 45);")
        self.ButtonGerU.setObjectName("ButtonGerU")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(670, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_0.setFont(font)
        self.Button_0.setStyleSheet("border: 1px solid black;\n"
                                    "color: white;\n"
                                    "background-color: rgb(45, 45, 45);")
        self.Button_0.setObjectName("Button_0")
        self.TButton = QtWidgets.QPushButton(self.centralwidget)
        self.TButton.setGeometry(QtCore.QRect(420, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TButton.setFont(font)
        self.TButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.TButton.setObjectName("TButton")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(570, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_8.setFont(font)
        self.Button_8.setStyleSheet("border: 1px solid black;\n"
                                    "color: white;\n"
                                    "background-color: rgb(45, 45, 45);")
        self.Button_8.setObjectName("Button_8")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(320, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_3.setFont(font)
        self.Button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_3.setStyleSheet("border: 1px solid black;\n"
                                    "color: white;\n"
                                    "background-color: rgb(45, 45, 45);")
        self.Button_3.setObjectName("Button_3")
        self.DButton = QtWidgets.QPushButton(self.centralwidget)
        self.DButton.setGeometry(QtCore.QRect(320, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DButton.setFont(font)
        self.DButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.DButton.setObjectName("DButton")
        self.ButtonGerO = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonGerO.setGeometry(QtCore.QRect(720, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonGerO.setFont(font)
        self.ButtonGerO.setStyleSheet("border: 1px solid black;\n"
                                      "color: white;\n"
                                      "background-color: rgb(45, 45, 45);")
        self.ButtonGerO.setObjectName("ButtonGerO")
        self.BButton = QtWidgets.QPushButton(self.centralwidget)
        self.BButton.setGeometry(QtCore.QRect(420, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BButton.setFont(font)
        self.BButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.BButton.setObjectName("BButton")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(520, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_7.setFont(font)
        self.Button_7.setStyleSheet("border: 1px solid black;\n"
                                    "color: white;\n"
                                    "background-color: rgb(45, 45, 45);")
        self.Button_7.setObjectName("Button_7")
        self.UButton = QtWidgets.QPushButton(self.centralwidget)
        self.UButton.setGeometry(QtCore.QRect(520, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UButton.setFont(font)
        self.UButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.UButton.setObjectName("UButton")
        self.QButton = QtWidgets.QPushButton(self.centralwidget)
        self.QButton.setGeometry(QtCore.QRect(220, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QButton.setFont(font)
        self.QButton.setStyleSheet("border: 1px solid black;\n"
                                   "color: white;\n"
                                   "background-color: rgb(45, 45, 45);")
        self.QButton.setObjectName("QButton")
        self.ButtonGerA = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonGerA.setGeometry(QtCore.QRect(670, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonGerA.setFont(font)
        self.ButtonGerA.setStyleSheet("border: 1px solid black;\n"
                                      "color: white;\n"
                                      "background-color: rgb(45, 45, 45);")
        self.ButtonGerA.setObjectName("ButtonGerA")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(220, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_1.setFont(font)
        self.Button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_1.setStyleSheet("border: 1px solid black;\n"
                                    "color: white;\n"
                                    "background-color: rgb(45, 45, 45);")
        self.Button_1.setAutoDefault(False)
        self.Button_1.setObjectName("Button_1")
        ScanLicensePlate.setCentralWidget(self.centralwidget)

        self.retranslateUi(ScanLicensePlate)
        QtCore.QMetaObject.connectSlotsByName(ScanLicensePlate)

        self.nextButton.clicked.connect(lambda: self.clicked("next", ScanLicensePlate))
        self.backButton.clicked.connect(lambda: self.clicked("back", ScanLicensePlate))
        self.getButton.clicked.connect(lambda: self.get())

        self.QButton.clicked.connect(lambda: self.key_press("Q"))
        self.WButton.clicked.connect(lambda: self.key_press("W"))
        self.EButton.clicked.connect(lambda: self.key_press("E"))
        self.RButton.clicked.connect(lambda: self.key_press("R"))
        self.TButton.clicked.connect(lambda: self.key_press("T"))
        self.YButton.clicked.connect(lambda: self.key_press("Y"))
        self.UButton.clicked.connect(lambda: self.key_press("U"))
        self.IButton.clicked.connect(lambda: self.key_press("I"))
        self.OButton.clicked.connect(lambda: self.key_press("O"))
        self.PButton.clicked.connect(lambda: self.key_press("P"))
        self.AButton.clicked.connect(lambda: self.key_press("A"))
        self.SButton.clicked.connect(lambda: self.key_press("S"))
        self.DButton.clicked.connect(lambda: self.key_press("D"))
        self.FButton.clicked.connect(lambda: self.key_press("F"))
        self.GButton.clicked.connect(lambda: self.key_press("G"))
        self.HButton.clicked.connect(lambda: self.key_press("H"))
        self.JButton.clicked.connect(lambda: self.key_press("J"))
        self.KButton.clicked.connect(lambda: self.key_press("K"))
        self.LButton.clicked.connect(lambda: self.key_press("L"))
        self.ZButton.clicked.connect(lambda: self.key_press("Z"))
        self.XButton.clicked.connect(lambda: self.key_press("X"))
        self.CButton.clicked.connect(lambda: self.key_press("C"))
        self.VButton.clicked.connect(lambda: self.key_press("V"))
        self.BButton.clicked.connect(lambda: self.key_press("B"))
        self.NButton.clicked.connect(lambda: self.key_press("N"))
        self.MButton.clicked.connect(lambda: self.key_press("M"))
        self.ButtonGerA.clicked.connect(lambda: self.key_press("Ä"))
        self.ButtonGerO.clicked.connect(lambda: self.key_press("Ö"))
        self.ButtonGerU.clicked.connect(lambda: self.key_press("Ü"))
        self.Button_1.clicked.connect(lambda: self.key_press("1"))
        self.Button_2.clicked.connect(lambda: self.key_press("2"))
        self.Button_3.clicked.connect(lambda: self.key_press("3"))
        self.Button_4.clicked.connect(lambda: self.key_press("4"))
        self.Button_5.clicked.connect(lambda: self.key_press("5"))
        self.Button_6.clicked.connect(lambda: self.key_press("6"))
        self.Button_7.clicked.connect(lambda: self.key_press("7"))
        self.Button_8.clicked.connect(lambda: self.key_press("8"))
        self.Button_9.clicked.connect(lambda: self.key_press("9"))
        self.Button_0.clicked.connect(lambda: self.key_press("0"))
        self.minusButton.clicked.connect(lambda: self.key_press("-"))
        self.backButton_2.clicked.connect(lambda: self.key_press("<-"))
        self.ButtonSpace.clicked.connect(lambda: self.key_press(" "))
        self.Button_dot.clicked.connect(lambda: self.key_press(","))

        self.Button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.minusButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ButtonSpace.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ButtonGerA.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ButtonGerO.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ButtonGerU.setFocusPolicy(QtCore.Qt.NoFocus)
        self.QButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.WButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.EButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.RButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.TButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.YButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.UButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.IButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.OButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.PButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.FButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.GButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.HButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.JButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.KButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ZButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.XButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.CButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.VButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.BButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.NButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.MButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_dot.setFocusPolicy(QtCore.Qt.NoFocus)

    def retranslateUi(self, ScanLicensePlate):
        _translate = QtCore.QCoreApplication.translate
        ScanLicensePlate.setWindowTitle(_translate("ScanLicensePlate", "Coolback"))

        self.i18n = I18N(lang)
        self.scan_plateLabel.setText(_translate("ScanLicensePlate", self.i18n.scan_license_plate))
        self.getButton.setText(_translate("ScanLicensePlate", self.i18n.get))
        self.AButton.setText(_translate("EnterName", "A"))
        self.ZButton.setText(_translate("EnterName", "Z"))
        self.WButton.setText(_translate("EnterName", "W"))
        self.SButton.setText(_translate("EnterName", "S"))
        self.EButton.setText(_translate("EnterName", "E"))
        self.Button_dot.setText(_translate("EnterName", "."))
        self.FButton.setText(_translate("EnterName", "F"))
        self.JButton.setText(_translate("EnterName", "J"))
        self.NButton.setText(_translate("EnterName", "N"))
        self.VButton.setText(_translate("EnterName", "V"))
        self.Button_5.setText(_translate("EnterName", "5"))
        self.Button_9.setText(_translate("EnterName", "9"))
        self.IButton.setText(_translate("EnterName", "I"))
        self.GButton.setText(_translate("EnterName", "G"))
        self.OButton.setText(_translate("EnterName", "O"))
        self.MButton.setText(_translate("EnterName", "M"))
        self.LButton.setText(_translate("EnterName", "L"))
        self.KButton.setText(_translate("EnterName", "K"))
        self.Button_2.setText(_translate("EnterName", "2"))
        self.RButton.setText(_translate("EnterName", "R"))
        self.PButton.setText(_translate("EnterName", "P"))
        self.ButtonSpace.setText(_translate("EnterName", "SPACE"))
        self.minusButton.setText(_translate("EnterName", "-"))
        self.backButton_2.setText(_translate("EnterName", "<-"))
        self.Button_4.setText(_translate("EnterName", "4"))
        self.CButton.setText(_translate("EnterName", "C"))
        self.Button_6.setText(_translate("EnterName", "6"))
        self.HButton.setText(_translate("EnterName", "H"))
        self.YButton.setText(_translate("EnterName", "Y"))
        self.XButton.setText(_translate("EnterName", "X"))
        self.ButtonGerU.setText(_translate("EnterName", "Ü"))
        self.Button_0.setText(_translate("EnterName", "0"))
        self.TButton.setText(_translate("EnterName", "T"))
        self.Button_8.setText(_translate("EnterName", "8"))
        self.Button_3.setText(_translate("EnterName", "3"))
        self.DButton.setText(_translate("EnterName", "D"))
        self.ButtonGerO.setText(_translate("EnterName", "Ö"))
        self.BButton.setText(_translate("EnterName", "B"))
        self.Button_7.setText(_translate("EnterName", "7"))
        self.UButton.setText(_translate("EnterName", "U"))
        self.QButton.setText(_translate("EnterName", "Q"))
        self.ButtonGerA.setText(_translate("EnterName", "Ä"))
        self.Button_1.setText(_translate("EnterName", "1"))

    def clicked(self, text, window):
        if text == "next":
            if len(self.scan_plateLineEdit.text()) == 0:
                pass
                '''self.EnterLicensePlate = QtWidgets.QMainWindow()
                self.ui = Ui_EnterLicensePlate()
                self.ui.setupUi(self.EnterLicensePlate)
                self.EnterLicensePlate.show()
                window.close()'''
            else:
                global license_plate
                license_plate = self.scan_plateLineEdit.text()
                self.EmptyWeighing = QtWidgets.QWidget()
                self.ui = Ui_EmptyWeighing()
                self.ui.setupUi(self.EmptyWeighing)
                self.EmptyWeighing.show()
                window.close()
        elif text == "back":
            self.EnterName = QtWidgets.QMainWindow()
            self.ui = Ui_EnterName()
            self.ui.setupUi(self.EnterName)
            self.EnterName.show()
            window.close()

    def get(self):
        global HOST, PORT
        cmd = "GET PLATE0"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(cmd.encode("UTF-8"))
            data = s.recv(1024)
            retval = data.decode("UTF-8")
            w_obj = json.loads(retval)
            self.scan_plateLineEdit.setText(w_obj["license_plate"])

    def key_press(self, text):

        if text == "<-":
            txt = self.driver_nameLineEdit.text()
            self.scan_plateLineEdit.setText(txt[:-1])
        else:
            txt = self.scan_plateLineEdit.text()
            txt += text
            self.scan_plateLineEdit.setText(txt)



weight_1 = ""
date_1 = ""
time_1 = ""
alibi_nr_1 = ""
class Ui_EmptyWeighing(object):
    def setupUi(self, Weight):
        Weight.setWindowFlag(Qt.FramelessWindowHint)
        Weight.setObjectName("Weight")
        Weight.resize(1024, 768)
        Weight.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backButton = QtWidgets.QPushButton(Weight)
        self.backButton.setStyleSheet("border: 1px solid white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.backButton.setGeometry(QtCore.QRect(24, 520, 151, 111))
        self.nextButton = QtWidgets.QPushButton(Weight)
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nextButton.setIcon(icon1)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.setGeometry(QtCore.QRect(850, 510, 151, 111))
        self.msg_label = QtWidgets.QLabel(Weight)
        self.msg_label.setGeometry(QtCore.QRect(10, 310, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.msg_label.setFont(font)
        self.msg_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg_label.setAutoFillBackground(False)
        self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label.setObjectName("msg_label")
        self.label = QtWidgets.QLabel(Weight)
        self.label.setGeometry(QtCore.QRect(400, 140, 171, 131))
        self.label.setPixmap(QtGui.QPixmap("img/information.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(Weight)
        self.logo.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.msg_label_2 = QtWidgets.QLabel(Weight)
        self.msg_label_2.setGeometry(QtCore.QRect(10, 400, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.msg_label_2.setFont(font)
        self.msg_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg_label_2.setAutoFillBackground(False)
        self.msg_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label_2.setObjectName("msg_label_2")

        self.retranslateUi(Weight)
        QtCore.QMetaObject.connectSlotsByName(Weight)

        self.backButton.clicked.connect(lambda: self.clicked("back", Weight))
        self.nextButton.clicked.connect(lambda: self.clicked("next", Weight))

        self.nextButton.hide()
        self.backButton.hide()

        _thread.start_new_thread(contact_client, ("GET WEIGHTNM", self.enable_all))

    def retranslateUi(self, Weight):
        _translate = QtCore.QCoreApplication.translate
        Weight.setWindowTitle(_translate("Weight", "Coolback"))
        self.i18n = I18N(lang)
        self.msg_label.setText(_translate("Weight", self.i18n.initial_weighing))

    def clicked(self, text, window):
        if text == "next":
            self.ImageCaptured = QtWidgets.QMainWindow()
            self.ui = Ui_ImageCaptured()
            self.ui.setupUi(self.ImageCaptured)
            self.ImageCaptured.show()
            window.close()
        else:
            self.EnterLicensePlate = QtWidgets.QMainWindow()
            self.ui = Ui_EnterLicensePlate()
            self.ui.setupUi(self.EnterLicensePlate)
            self.EnterLicensePlate.show()
            window.close()

    def enable_all(self, w_obj):
        global weight_1, date_1, time_1, alibi_nr_1
        weight_1 = w_obj['weight']
        date_1 = w_obj['date']
        time_1 = w_obj["time"]
        alibi_nr_1 = w_obj['alibi_nr']
        _translate = QtCore.QCoreApplication.translate
        self.i18n = I18N(lang)
        self.msg_label_2.setText(_translate("Weight", self.i18n.weight+": " + w_obj["weight"] + " kg"))
        self.nextButton.show()
        self.backButton.show()



imgstring0 = ""
imgstring1 = ""
class Ui_ImageCaptured(object):
    def setupUi(self, ImageCaptured):
        ImageCaptured.setWindowFlag(Qt.FramelessWindowHint)
        ImageCaptured.setObjectName("ImageCaptured")
        ImageCaptured.resize(1024, 768)
        ImageCaptured.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ImageCaptured)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 991, 91))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 400, 91, 31))
        self.pushButton.setStyleSheet("background-color: rgb(21, 21, 21);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        ImageCaptured.setCentralWidget(self.centralwidget)

        self.retranslateUi(ImageCaptured)
        QtCore.QMetaObject.connectSlotsByName(ImageCaptured)

        self.pushButton.clicked.connect(lambda: self.clicked("next", ImageCaptured))

    def retranslateUi(self, ImageCaptured):
        _translate = QtCore.QCoreApplication.translate
        ImageCaptured.setWindowTitle(_translate("ImageCaptured", "Coolback"))
        self.i18n = I18N(lang)
        self.label.setText(_translate("ImageCaptured", self.i18n.truck_image_has_captured))
        self.pushButton.setText(_translate("ImageCaptured", "OK"))

    def clicked(self, text, window):
        if text == "next":
            global imgstring0
            global imgstring1
            imgstring0 = self.get(0)
            imgstring1 = self.get(1)

            self.QRCode = QtWidgets.QMainWindow()
            self.ui = Ui_QRCode()
            self.ui.setupUi(self.QRCode)
            self.QRCode.show()
            window.close()

    def get(self, nr):
        global HOST, PORT
        ok = False
        cmd = "GET IMAGE%d" % (nr)
        while not ok:
            ok = True
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(cmd.encode("UTF-8"))
                data = ""
                d = s.recv(1000000)
                while d:
                    data += d.decode("UTF-8")
                    d = s.recv(1000000)
            retval = data.encode("UTF-8")
            try:
                jobj = json.loads(retval)
            except:
                print("JSON error")
                ok = False
                time.sleep(2)
        b64_string = jobj["image_data"]
        return b64_string


class Ui_QRCode(object):
    def setupUi(self, QRCode):
        QRCode.setWindowFlag(Qt.FramelessWindowHint)
        QRCode.setObjectName("QRCode")
        QRCode.resize(1024, 768)
        QRCode.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(QRCode)
        self.centralwidget.setObjectName("centralwidget")
        self.codeImage = QtWidgets.QLabel(self.centralwidget)
        self.codeImage.setGeometry(QtCore.QRect(380, 190, 241, 201))
        import qrcode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        from random import randint
        n = 6
        self.code = ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])
        try:
            with open("yard_list.json", "r") as jsonFile:
                yard_list = json.load(jsonFile)
            for data in yard_list:
                if data["code"] == str(self.code):
                    self.code = ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])
        except:
            pass

        qr.add_data(self.code)
        qr.make(fit=True)

        self.img = qr.make_image(fill_color="black", back_color="white")

        from PIL.ImageQt import ImageQt
        qimage = ImageQt(self.img)

        self.codeImage.setPixmap(QtGui.QPixmap.fromImage(qimage))
        self.codeImage.setScaledContents(True)
        self.codeImage.setObjectName("codeImage")
        self.codelabel = QtWidgets.QLabel(self.centralwidget)
        self.codelabel.setGeometry(QtCore.QRect(380, 430, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.codelabel.setFont(font)
        self.codelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.codelabel.setObjectName("codelabel")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(810, 550, 151, 111))
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(50, 550, 151, 111))
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.heading_label = QtWidgets.QLabel(self.centralwidget)
        self.heading_label.setGeometry(QtCore.QRect(156, 93, 691, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.heading_label.setFont(font)
        self.heading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.heading_label.setObjectName("heading_label")
        QRCode.setCentralWidget(self.centralwidget)

        self.retranslateUi(QRCode)
        QtCore.QMetaObject.connectSlotsByName(QRCode)

        self.nextButton.clicked.connect(lambda: self.clicked("next", QRCode))
        # self.backButton.clicked.connect(lambda: self.clicked("back", QRCode))

        self.nextButton.hide()
        self.backButton.hide()
        _thread.start_new_thread(self.print_document, (QRCode,))

    def retranslateUi(self, QRCode):
        _translate = QtCore.QCoreApplication.translate
        QRCode.setWindowTitle(_translate("QRCode", "Coolback"))
        self.codelabel.setText(_translate("QRCode", self.code))
        self.i18n = I18N(lang)
        self.heading_label.setText(_translate("QRCode", self.i18n.please_wait_the_QR_code_is_printing))

    def clicked(self, text, window):
        # if text == "next":
        self.Language = QtWidgets.QMainWindow()
        self.ui = Ui_Language()
        self.ui.setupUi(self.Language)
        self.Language.show()
        window.close()

        # else:
        #     self.ImageCaptured = QtWidgets.QMainWindow()
        #     self.ui = Ui_ImageCaptured()
        #     self.ui.setupUi(self.ImageCaptured)
        #     self.ImageCaptured.show()
        #     window.close()

    def print_document(self, window):
        global license_plate
        global driver_name
        global weight_1
        global date_1
        global time_1
        global alibi_nr_1
        global supplier_no
        global supplier_des
        global article_no
        global article_des
        global imgstring0
        global imgstring1

        yard_list = ""
        try:
            with open("yard_list.json", "r") as jsonFile:
                yard_list = json.load(jsonFile)
        except:
            yard_list = []

        data = {}
        data["code"] = str(self.code)
        data["license_plate"] = str(license_plate)
        data["driver_name"] = str(driver_name)
        data["supplier_no"] = str(supplier_no)
        data["supplier_des"] = str(supplier_des)
        data["article_no"] = str(article_no)
        data["article_des"] = str(article_des)
        data["weight_1"] = str(weight_1)
        data["date_1"] = str(date_1)
        data["time_1"] = str(time_1)
        data["alibi_nr_1"] = str(alibi_nr_1)
        data["imgstring0"] = imgstring0
        data["imgstring1"] = imgstring1

        yard_list.append(data)

        with open("yard_list.json", "w") as jsonFile:
            json.dump(yard_list, jsonFile)

        from reportlab.pdfgen import canvas
        self.img.save("temp.png")

        COOL_PDF_FILE = ("{}.pdf".format(self.code))
        COOL_PDF_PRINT_CMD = "PDFtoPrinter.exe"

        pdf = canvas.Canvas(COOL_PDF_FILE)
        pdf.setTitle("QR Code")
        pdf.drawString(275, 525, self.code)
        pdf.drawImage("temp.png", 150, 550)
        os.remove("temp.png")
        pdf.save()

        cmd = '%s %s "%s"' % (COOL_PDF_PRINT_CMD, COOL_PDF_FILE, COOL_PDF_PRINTER)
        # print("cmd = " + cmd)
        os.system(cmd)
        cmd = 'del "%s"' % (COOL_PDF_FILE)
        # print("cmd = " + cmd)
        os.system(cmd)
        time.sleep(4)
        self.nextButton.click()





weight_2 = ""
date_2 = ""
time_2 = ""
alibi_nr_2 = ""
class Ui_WeightAfterUnload(object):
    def setupUi(self, Weight):
        Weight.setWindowFlag(Qt.FramelessWindowHint)
        Weight.setObjectName("EmptyWeighing")
        Weight.resize(1024, 768)
        Weight.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backButton = QtWidgets.QPushButton(Weight)
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.backButton.setGeometry(QtCore.QRect(24, 520, 151, 111))
        self.nextButton = QtWidgets.QPushButton(Weight)
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nextButton.setIcon(icon1)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.setGeometry(QtCore.QRect(850, 510, 151, 111))
        self.msg_label = QtWidgets.QLabel(Weight)
        self.msg_label.setGeometry(QtCore.QRect(10, 310, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.msg_label.setFont(font)
        self.msg_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg_label.setAutoFillBackground(False)
        self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label.setObjectName("msg_label")
        self.label = QtWidgets.QLabel(Weight)
        self.label.setGeometry(QtCore.QRect(400, 140, 171, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/information.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(Weight)
        self.logo.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.msg_label_2 = QtWidgets.QLabel(Weight)
        self.msg_label_2.setGeometry(QtCore.QRect(10, 400, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.msg_label_2.setFont(font)
        self.msg_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg_label_2.setAutoFillBackground(False)
        self.msg_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label_2.setObjectName("msg_label_2")

        self.retranslateUi(Weight)
        QtCore.QMetaObject.connectSlotsByName(Weight)

        self.backButton.clicked.connect(lambda: self.clicked("back", Weight))
        self.nextButton.clicked.connect(lambda: self.clicked("next", Weight))

        self.nextButton.hide()
        self.backButton.hide()

        _thread.start_new_thread(contact_client, ("GET WEIGHTNM", self.enable_all))

    def retranslateUi(self, Weight):
        _translate = QtCore.QCoreApplication.translate
        Weight.setWindowTitle(_translate("Weight", "Coolback"))
        self.i18n = I18N(lang)
        self.msg_label.setText(_translate("Weight", self.i18n.weighing_after_unload))

    def clicked(self, text, window):
        if text == "next":
            ui = Ui_Signature_2()
            ui.show()
            window.close()
        elif text == "back":
            self.QRCode = QtWidgets.QMainWindow()
            self.ui = Ui_QRCode()
            self.ui.setupUi(self.QRCode)
            self.QRCode.show()
            window.close()

    def enable_all(self, w_obj):
        global weight_2, date_2, time_2, alibi_nr_2
        weight_2 = w_obj['weight']
        date_2 = w_obj['date']
        time_2 = w_obj["time"]
        alibi_nr_2 = w_obj['alibi_nr']
        _translate = QtCore.QCoreApplication.translate
        self.i18n = I18N(lang)
        self.msg_label_2.setText(_translate("EmptyWeighing", self.i18n.weight+": " + w_obj["weight"] + " kg"))
        self.nextButton.show()
        self.backButton.show()


from datetime import datetime


class Ui_Signature_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setObjectName("Signature")
        self.resize(1024, 768)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nextButton_2 = QtWidgets.QPushButton(self)
        self.nextButton_2.setGeometry(QtCore.QRect(90, 550, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nextButton_2.setFont(font)
        self.nextButton_2.setStyleSheet("border: 4px solid darkblue;\n"
                                        "color: darkblue;\n"
                                        "border-radius: 25px;")
        self.nextButton_2.setIconSize(QtCore.QSize(103, 105))
        self.nextButton_2.setObjectName("nextButton_2")
        self.nextButton_3 = QtWidgets.QPushButton(self)
        self.nextButton_3.setGeometry(QtCore.QRect(860, 550, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nextButton_3.setFont(font)
        self.nextButton_3.setStyleSheet("border: 4px solid darkblue;\n"
                                        "color: darkblue;\n"
                                        "border-radius: 25px;")
        self.nextButton_3.setIconSize(QtCore.QSize(103, 105))
        self.nextButton_3.setObjectName("nextButton_3")

        self.image = QImage(self.size(), QImage.Format_RGB32)

        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 4
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        self.nextButton_2.clicked.connect(lambda: self.clear())
        self.nextButton_3.clicked.connect(lambda: self.save(self))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.logo = QtWidgets.QLabel(self)
        self.logo.setGeometry(QtCore.QRect(790, 10, 221, 101))
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(110, 110, 811, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.i18n = I18N(lang)
        self.label.setText(self.i18n.signature_here_for_confirmation)

    def retranslateUi(self, Signature):
        _translate = QtCore.QCoreApplication.translate
        Signature.setWindowTitle(_translate("Signature", "Coolback"))
        self.nextButton_2.setText(_translate("Signature", "RESET"))
        self.nextButton_3.setText(_translate("Signature", "OK"))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):

        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)

            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            painter.drawLine(self.lastPoint, event.pos())

            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)

        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
        canvasPainter.drawRect(130, 180, 770, 320)

    def save(self, window):

        parent_dir = os.getcwd()

        current_datetime = datetime.now()
        current_datetime = str(current_datetime)[:-10].replace(" ", "-").replace(":", "-")

        running_number = 000000

        results_directory = "results"
        results_path = os.path.join(parent_dir, results_directory)
        nr_file = os.path.join(parent_dir, "data\\lfd.txt")
        try:
            os.mkdir(results_path)
        except:
            pass
        try:
            nrf = open(nr_file, "r")
            count_i = int(nrf.read(1000))
            count_i += 1
            nrf.close()
        except:
            count_i = 1
        nrf = open(nr_file, "w")
        nrf.write("%d" % (count_i))
        nrf.close()

        count_s0 = str(count_i)
        count_s = str(count_i).zfill(6)

        sub_directory = "res-" + current_datetime + "-" + count_s
        sub_path = os.path.join(results_path, sub_directory)
        os.mkdir(sub_path)

        signature_path = sub_path + "/signature-" + current_datetime + "-" + count_s + ".jpeg"
        self.image.save(signature_path, 'JPEG')

        global imgstring0
        imgdata0 = base64.b64decode(imgstring0)

        img1 = sub_path + "/img1-" + current_datetime + "-" + count_s + ".jpg"
        with open(img1, 'wb') as f:
            f.write(imgdata0)

        global imgstring1
        imgdata1 = base64.b64decode(imgstring1)

        img2 = sub_path + "/img2-" + current_datetime + "-" + count_s + ".jpg"
        with open(img2, 'wb') as f:
            f.write(imgdata1)

        global driver_name
        global license_plate
        global supplier_no, supplier_des
        global article_no, article_des
        global weight_1, date_1, time_1, alibi_nr_1
        global weight_2, date_2, time_2, alibi_nr_2

        data = [[count_s0,
                 license_plate,
                 driver_name,
                 supplier_no,
                 supplier_des,
                 article_no,
                 article_des,
                 weight_1,
                 date_1,
                 time_1,
                 alibi_nr_1,
                 weight_2,
                 date_2,
                 time_2,
                 alibi_nr_2,
                 abs(int(weight_2) - int(weight_1))]]

        columns_name = ['Nr.',
                        'KFZ-Kennzeichen',
                        'Fahrername',
                        'Lieferant Nr',
                        'Lieferantenbeschreibung',
                        'Artikel Nr',
                        'Artikelbeschreibung',
                        'Wiegung1',
                        'Datum1',
                        'Uhrzeit1',
                        'AlibiNr1',
                        'Wiegung2',
                        'Datum2',
                        'Uhrzeit2',
                        'AlibiNr2',
                        'Netto']

        df = pd.DataFrame(data, columns=columns_name)
        values_path = sub_path + "/vals-" + current_datetime + "-" + count_s + ".csv"
        df.to_csv(values_path, index=False, sep=';')

        self.Language = QtWidgets.QMainWindow()
        self.ui = Ui_Language()
        self.ui.setupUi(self.Language)
        self.Language.show()
        window.close()

    def clear(self):
        self.image.fill(Qt.white)
        self.update()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Language = QtWidgets.QMainWindow()
    ui = Ui_Language()
    ui.setupUi(Language)
    Language.show()
    sys.exit(app.exec_())
