from PyQt5 import QtCore, QtGui, QtWidgets
import os
import zeep
import socket
import _thread
import json
import time


def resource_path(relative_path):
    relative_path = relative_path.replace("/","\\")
    return os.path.join(os.path.abspath("."), relative_path)


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9001

def contact_client(callback):
    global HOST, PORT
    cmd = "GET WEIGHT"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(cmd.encode("UTF-8"))
        data = s.recv(1024)
        retval = data.decode("UTF-8")
        w_obj = json.loads(retval)
        time.sleep(1)
        callback(w_obj)


wsdl = 'http://www.trimbleforestry.de:21099/PelletsLoadingServices?singleWsdl'
client = zeep.Client(wsdl=wsdl)

os.environ["LANG"] = "en"

class I18N():
    '''Internationalization'''
    def __init__(self, language):      
        if   language == 'en': self.resourceLanguageEnglish()
        elif language == 'de': self.resourceLanguageGerman()
        elif language == "fr": self.resourceLanguageFrench()
        else: raise NotImplementedError('Unsupported language.')
        
    def resourceLanguageEnglish(self):
        self.enter_license_plate = "License Plate"
        self.license_not_reco = "License Plate can't recognize, please enter keypad entry"
        self.next = "Next"
        self.back = "Back"
        self.home = "Home"
        self.vehicle_in_yard = "Vehicle in yard list ?"
        self.yes = "Yes"
        self.no = "No"
        self.load_potato = "You are here to load Potato"
        self.confirm = "Confirm"
        self.instructions = 'I agree to confirm read all instructions'
        self.barcode = "Please Present QR Code"
        self.enter_order_no = "Enter Order No."
        self.below_max_load = "Below Maximum Load ?"
        self.display_to_operator = "Reference the display to operator scale"
        self.tare_allowed = "Tare Allowed ?"
        self.tare_valid = "Tare Valid ?"
        self.tare_weight_not_valid = "Not a valid tare weight! Drive to the operator scale after unloading"
        self.weigh_error_free = "Weighing Error Free ?"
        self.scale_error = "There is a scale error"
        self.drive_to_unloading = "Drive to unloading point !"
        self.add_vehicle = "Adding Vehicle in yard list"
        self.self_weighing = "Self Weighing Allowed ?"
        self.enter_name = "Please Enter Name"
        self.please_sign_at_terminal = "Please confirm the weighing data with your signature!"
        self.sign_at_terminal = 'sign the weighing data at the terminal'
        self.sending_and_collecting = "Sending Signature, Collecting Weighing Slip and"
        self.remove_vehicle = "Remove Vehicle In Yard List"
        self.ok = "OK"
        self.license_plate = "License Plate"
        self.order_number = "Order Number"
        self.name = "Name"
        self.good_ride = "Good Ride"
        self.error = "Error"
        self.scan_pickup_number = "Scan Pickup Number"
        self.enter_pickup_number = "Enter Pickup Number"
        self.code_not_recognize = "Code Not Recognize, Please Enter Pickup Number Manually"
        self.invalid_pickup_number = "Invalid Pickup Number"
        self.pickup_valid = "Pickup Valid ?"
        self.truck_driver_drive_from_yard = "Thanks, Have a good ride"
        self.truck_driver_clarifies = "Truck driver clarifies with pellet sales whether collection is possible"
        self.weekly_contiengent_is_increased = "Weekly Contiengent Is Increased ?"
        self.enter_driver_name = "Driver"
        self.enter_contractor = "Trucking Company"
        self.enter_remark = "Remark"
        self.pdf_is_printed = "PDF is Printed"
        self.enter_details = "Please enter your details"
        self.empty_weigh_start = "Please wait the empty weight is triggerd"
        self.operates_the_filling = "Start the filling mechanism"
        self.start_loading = "Start Loading Truck"
        self.stop_loading1 = "Loading may start now."
        self.stop_loading2 = "If ready press 'Loading finished'"
        self.weighing_completed = "Please wait for trigger full weight"
        self.please_wait_data_is_sending = "Please wait the delivery note will be printed"
        self.cancel = "Cancel"
        self.lf = "Loading finished"
        self.total_load = "Total Load"
        self.please_fill = "Please fill this field"
        

    def resourceLanguageGerman(self):      
        self.enter_license_plate = "Kennzeichen eingeben"
        self.license_not_reco = "Das Nummernschild kann nicht erkannt werden. Bitte geben Sie die Tastatur ein"
        self.next = "weiter"
        self.back = "Zurück"
        self.home = "Zuhause"
        self.vehicle_in_yard = "Fahrzeug in Hofliste ?"
        self.yes = "Ja"
        self.no = "Nein"
        self.load_potato = "Sie sind hier, um Kartoffel zu laden"
        self.confirm = "Bestätigen"
        self.instructions = 'Ich bin damit einverstanden, alle Anweisungen zu lesen'
        self.barcode = "Bitte legen Sie den QR-Code vor"
        self.enter_order_no = "Bestellnummer eingeben."
        self.below_max_load = "Unterhalb der maximalen Last?"
        self.display_to_operator = "Verweisen Sie die Anzeige auf die Bedienerskala"
        self.tare_allowed = "Tara erlaubt ?"
        self.tare_valid = "Tara gültig ?"
        self.tare_weight_not_valid = "Kein gültiges Taragewicht! Fahren Sie nach dem Entladen zur Bedienerwaage"
        self.weigh_error_free = "Fehlerfrei wiegen ?"
        self.scale_error = "Es liegt ein Skalierungsfehler vor"
        self.drive_to_unloading = "Zum Entladepunkt fahren !"
        self.add_vehicle = "Fahrzeug zur Yard-Liste hinzufügen"
        self.self_weighing = "Selbstwägen erlaubt ?"
        self.enter_name = "Bitte geben Sie den Namen ein"
        self.please_sign_at_terminal = "Bitte unterschreiben Sie die Wiegedaten am Terminal"
        self.sign_at_terminal = 'Bitte bestätigen Sie durch Ihre Unterschrift die ermittelten Wiegedaten!'
        self.sending_and_collecting = "Unterschrift senden, Wiegezettel sammeln und"
        self.remove_vehicle = "Fahrzeug in der Yard-Liste entfernen"
        self.ok = "OK"
        self.license_plate = "Nummernschild"
        self.order_number = "Order Number"
        self.name = "Name"
        self.good_ride = "Gute Fahrt"
        self.error = "Error"
        self.scan_pickup_number = "Scan-Abholnummer"
        self.enter_pickup_number = "Geben Sie die Abholnummer ein"
        self.code_not_recognize = "Code nicht erkannt, bitte geben Sie die Abholnummer manuell ein"
        self.invalid_pickup_number = "Ungültige Abholnummer"
        self.pickup_valid = "Abholung gültig?"
        self.truck_driver_drive_from_yard = "Danke, gute Fahrt"
        self.truck_driver_clarifies = "LKW-Fahrer klärt mit Pelletverkäufen, ob eine Abholung möglich ist"
        self.weekly_contiengent_is_increased = "Wöchentlicher Kontinent wird erhöht?"
        self.enter_driver_name = "Fahrer"
        self.enter_contractor = "Fuhrunternehmer"
        self.enter_remark = "Bemerkung"
        self.pdf_is_printed = "PDF wird gedruckt"
        self.enter_details = "Bitte geben Sie Ihre Daten ein"
        self.empty_weigh_start = "Bitte warten Sie, es erfolgt die Leerwiegung des LKW"
        self.operates_the_filling = "Starten Sie den Füllmechanismus"
        self.start_loading = "Starten Sie das Laden des LKW"
        self.stop_loading1 = "Die Verladung kann jetzt gestartet werden"
        self.stop_loading2 = "Wenn Sie die Verladung abgeschlossen haben, drücken Sie bitte auf 'Verladung abschlossen'"
        self.weighing_completed = "Bitte warten Sie, es erfolgt die Vollwiegung des LKW!"
        self.please_wait_data_is_sending = "Bitte warten, der Lieferschein wird gedruckt!"
        self.cancel = "Abbrechen"
        self.lf = "Verladung abschlossen"
        self.total_load = "Ladevolumen" 
        self.please_fill = "Bitte füllen Sie dieses Feld aus"  

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
        
        self.englishButton.clicked.connect(lambda: self.clicked("English", language))
        self.germanButton.clicked.connect(lambda: self.clicked("German", language))

    def retranslateUi(self, language):
        _translate = QtCore.QCoreApplication.translate
        language.setWindowTitle(_translate("language", "Trimble"))
        self.englishButton.setToolTip(_translate("language", "<html><head/><body><p>English</p></body></html>"))
        self.germanButton.setToolTip(_translate("language", "<html><head/><body><p>German</p></body></html>"))
    
    def clicked(self, text, window):
        if text == "English":
            os.environ["LANG"] = "en"
            self.ScanPickupNumber = QtWidgets.QWidget()
            self.ui = Ui_ScanPickupNumber()
            self.ui.setupUi(self.ScanPickupNumber)
            self.ScanPickupNumber.show()
            window.hide()
        elif text == "German":
            os.environ["LANG"] = "de"
            self.ScanPickupNumber = QtWidgets.QWidget()
            self.ui = Ui_ScanPickupNumber()
            self.ui.setupUi(self.ScanPickupNumber)
            self.ScanPickupNumber.show()
            window.hide()
        
        
class Ui_ScanPickupNumber(object):
    def setupUi(self, ScanPickupNumber):
        ScanPickupNumber.setObjectName("ScanPickupNumber")
        ScanPickupNumber.resize(1024, 768)
        font = QtGui.QFont()
        font.setPointSize(12)
        ScanPickupNumber.setFont(font)
        ScanPickupNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logo = QtWidgets.QLabel(ScanPickupNumber)
        self.logo.setGeometry(QtCore.QRect(720, 30, 281, 81))
        self.logo.setAutoFillBackground(False)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(ScanPickupNumber)
        self.label.setGeometry(QtCore.QRect(220, 230, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.pickupLineEdit = QtWidgets.QLineEdit(ScanPickupNumber)
        self.pickupLineEdit.setGeometry(QtCore.QRect(420, 230, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pickupLineEdit.setFont(font)
        self.pickupLineEdit.setTabletTracking(True)
        self.pickupLineEdit.setAutoFillBackground(False)
        self.pickupLineEdit.setStyleSheet("border: 1px solid black;")
        self.pickupLineEdit.setFrame(True)
        self.pickupLineEdit.setDragEnabled(False)
        self.pickupLineEdit.setReadOnly(False)
        self.pickupLineEdit.setObjectName("pickupLineEdit")
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'[0-9]+'))
        self.pickupLineEdit.setValidator(validator)
        self.nextButton = QtWidgets.QPushButton(ScanPickupNumber)
        self.nextButton.setGeometry(QtCore.QRect(840, 550, 151, 111))
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nextButton.setIcon(icon)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.backButton = QtWidgets.QPushButton(ScanPickupNumber)
        self.backButton.setGeometry(QtCore.QRect(30, 550, 151, 111))
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(icon1)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.Button_1 = QtWidgets.QPushButton(ScanPickupNumber)
        self.Button_1.setGeometry(QtCore.QRect(420, 330, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_1.setFont(font)
        self.Button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_1.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_1.setAutoDefault(False)
        self.Button_1.setObjectName("Button_1")
        self.Button_2 = QtWidgets.QPushButton(ScanPickupNumber)
        self.Button_2.setGeometry(QtCore.QRect(500, 330, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_2.setFont(font)
        self.Button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_2.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_2.setAutoDefault(False)
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(ScanPickupNumber)
        self.Button_3.setGeometry(QtCore.QRect(580, 330, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_3.setFont(font)
        self.Button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_3.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_3.setAutoDefault(False)
        self.Button_3.setObjectName("Button_3")
        self.Button_4 = QtWidgets.QPushButton(ScanPickupNumber)
        self.Button_4.setGeometry(QtCore.QRect(420, 410, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_4.setFont(font)
        self.Button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_4.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_4.setAutoDefault(False)
        self.Button_4.setObjectName("Button_4")
        self.Button_7 = QtWidgets.QPushButton(ScanPickupNumber)
        self.Button_7.setGeometry(QtCore.QRect(420, 490, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_7.setFont(font)
        self.Button_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_7.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_7.setAutoDefault(False)
        self.Button_7.setObjectName("Button_7")
        self.Button_6 = QtWidgets.QPushButton(ScanPickupNumber)
        self.Button_6.setGeometry(QtCore.QRect(580, 410, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_6.setFont(font)
        self.Button_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_6.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_6.setAutoDefault(False)
        self.Button_6.setObjectName("Button_6")
        self.Button_5 = QtWidgets.QPushButton(ScanPickupNumber)
        self.Button_5.setGeometry(QtCore.QRect(500, 410, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_5.setFont(font)
        self.Button_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_5.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_5.setAutoDefault(False)
        self.Button_5.setObjectName("Button_5")
        self.Button_8 = QtWidgets.QPushButton(ScanPickupNumber)
        self.Button_8.setGeometry(QtCore.QRect(500, 490, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_8.setFont(font)
        self.Button_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_8.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_8.setAutoDefault(False)
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(ScanPickupNumber)
        self.Button_9.setGeometry(QtCore.QRect(580, 490, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_9.setFont(font)
        self.Button_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_9.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_9.setAutoDefault(False)
        self.Button_9.setObjectName("Button_9")
        self.Button_0 = QtWidgets.QPushButton(ScanPickupNumber)
        self.Button_0.setGeometry(QtCore.QRect(500, 570, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_0.setFont(font)
        self.Button_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_0.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_0.setAutoDefault(False)
        self.Button_0.setObjectName("Button_0")
        self.Button_back = QtWidgets.QPushButton(ScanPickupNumber)
        self.Button_back.setGeometry(QtCore.QRect(580, 570, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_back.setFont(font)
        self.Button_back.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_back.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_back.setAutoDefault(False)
        self.Button_back.setObjectName("Button_back")
        self.Button_dot = QtWidgets.QPushButton(ScanPickupNumber)
        self.Button_dot.setGeometry(QtCore.QRect(420, 570, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_dot.setFont(font)
        self.Button_dot.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_dot.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_dot.setAutoDefault(False)
        self.Button_dot.setObjectName("Button_dot")


        self.retranslateUi(ScanPickupNumber)
        QtCore.QMetaObject.connectSlotsByName(ScanPickupNumber)
        
        self.backButton.clicked.connect(lambda: self.clicked("back", ScanPickupNumber))
        self.nextButton.clicked.connect(lambda: self.clicked("next", ScanPickupNumber))
        
        self.pickupLineEdit.setFocus()

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

        

    def retranslateUi(self, ScanPickupNumber):
        _translate = QtCore.QCoreApplication.translate
        ScanPickupNumber.setWindowTitle(_translate("ScanPickupNumber", "Trimble"))
        self.i18n = I18N(os.environ["LANG"])
        self.label.setText(_translate("ScanPickupNumber", self.i18n.scan_pickup_number))
        self.Button_1.setText(_translate("ScanPickupNumber", "1"))
        self.Button_2.setText(_translate("ScanPickupNumber", "2"))
        self.Button_3.setText(_translate("ScanPickupNumber", "3"))
        self.Button_4.setText(_translate("ScanPickupNumber", "4"))
        self.Button_7.setText(_translate("ScanPickupNumber", "7"))
        self.Button_6.setText(_translate("ScanPickupNumber", "6"))
        self.Button_5.setText(_translate("ScanPickupNumber", "5"))
        self.Button_8.setText(_translate("ScanPickupNumber", "8"))
        self.Button_9.setText(_translate("ScanPickupNumber", "9"))
        self.Button_0.setText(_translate("ScanPickupNumber", "0"))
        self.Button_back.setText(_translate("ScanPickupNumber", "<-"))
        self.Button_dot.setText(_translate("ScanPickupNumber", "."))
        
    def clicked(self, text, window):
        if text == "back":
            self.language = QtWidgets.QMainWindow()
            self.ui_lang = Ui_language()
            self.ui_lang.setupUi(self.language)
            self.language.show()
            window.hide()
        elif text == "next":
            if len(self.pickupLineEdit.text()) == 0:
                _translate = QtCore.QCoreApplication.translate
                self.label.setText(_translate("ScanPickupNumber", self.i18n.scan_pickup_number+" *"))
            else:
                number = int(self.pickupLineEdit.text())
                os.environ["PK_NO"] = str(number)
                ret_val = client.service.CheckLoadingOK(number)
                if ret_val["OK"] == True:
                    os.environ["MSG"] = ret_val["Message"]
                    self.EnterData = QtWidgets.QWidget()
                    self.ui_ed = Ui_EnterData()
                    self.ui_ed.setupUi(self.EnterData)
                    self.EnterData.show()
                    window.hide()   
                else:
                    os.environ["MSG"] = ret_val["Message"]
                    self.InvalidPickupNumber = QtWidgets.QWidget()
                    self.ui = Ui_InvalidPickupNumber()
                    self.ui.setupUi(self.InvalidPickupNumber)
                    self.InvalidPickupNumber.show()
                    window.hide()

    def key_press(self, text):    
        if text == "<-":
            txt = self.pickupLineEdit.text()
            self.pickupLineEdit.setText(txt[:-1])
        else:    
            txt = self.pickupLineEdit.text()
            txt += text
            self.pickupLineEdit.setText(txt)

            
            
class Ui_InvalidPickupNumber(object):
    def setupUi(self, InvalidPickupNumber):
        InvalidPickupNumber.setObjectName("InvalidPickupNumber")
        InvalidPickupNumber.resize(1024, 768)
        InvalidPickupNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logo = QtWidgets.QLabel(InvalidPickupNumber)
        self.logo.setGeometry(QtCore.QRect(710, 30, 281, 81))
        self.logo.setAutoFillBackground(False)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(InvalidPickupNumber)
        self.label.setGeometry(QtCore.QRect(440, 180, 191, 151))
        self.label.setStyleSheet("align: center;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/information.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.msg_label = QtWidgets.QLabel(InvalidPickupNumber)
        self.msg_label.setGeometry(QtCore.QRect(46, 393, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.msg_label.setFont(font)
        self.msg_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg_label.setAutoFillBackground(True)
        self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label.setObjectName("msg_label")
        self.nextButton = QtWidgets.QPushButton(InvalidPickupNumber)
        self.nextButton.setGeometry(QtCore.QRect(840, 550, 151, 111))
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/Home.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nextButton.setIcon(icon)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.backButton = QtWidgets.QPushButton(InvalidPickupNumber)
        self.backButton.setGeometry(QtCore.QRect(60, 550, 151, 111))
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(icon1)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")

        self.retranslateUi(InvalidPickupNumber)
        QtCore.QMetaObject.connectSlotsByName(InvalidPickupNumber)
        
        self.backButton.clicked.connect(lambda: self.clicked("back", InvalidPickupNumber))
        self.nextButton.clicked.connect(lambda: self.clicked("next", InvalidPickupNumber))

    def retranslateUi(self, InvalidPickupNumber):
        _translate = QtCore.QCoreApplication.translate
        InvalidPickupNumber.setWindowTitle(_translate("InvalidPickupNumber", "Trimble"))
        self.msg_label.setText(_translate("InvalidPickupNumber", os.environ["MSG"]))
        
    def clicked(self, text, window):
        if text == "back":
            self.ScanPickupNumber = QtWidgets.QWidget()
            self.ui = Ui_ScanPickupNumber()
            self.ui.setupUi(self.ScanPickupNumber)
            self.ScanPickupNumber.show()
            window.hide()
        elif text == "next":
            self.language = QtWidgets.QMainWindow()
            self.ui = Ui_language()
            self.ui.setupUi(self.language)
            self.language.show()
            window.hide()

class Ui_EnterData(object):
    def setupUi(self, EnterData):
        uppervalidator = QtGui.QRegExpValidator(QtCore.QRegExp("[A-Z]{1,20}"))
        EnterData.setObjectName("EnterData")
        EnterData.resize(1024, 769)
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
        self.licenseLineEdit.setValidator(uppervalidator)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.licenseLineEdit.setFont(font)
        self.licenseLineEdit.setTabletTracking(True)
        self.licenseLineEdit.setAutoFillBackground(False)
        self.licenseLineEdit.setStyleSheet("border: 1px solid black;")
        self.licenseLineEdit.setFrame(True)
        self.licenseLineEdit.setDragEnabled(False)
        self.licenseLineEdit.setReadOnly(False)
        self.licenseLineEdit.setObjectName("licenseLineEdit")
        self.licenseLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
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
        self.label.setGeometry(QtCore.QRect(180, 10, 500, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(EnterData)
        self.label_2.setGeometry(QtCore.QRect(190, 170, 551, 51))
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
        self.driverLineEdit.setValidator(uppervalidator)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.driverLineEdit.setFont(font)
        self.driverLineEdit.setTabletTracking(True)
        self.driverLineEdit.setAutoFillBackground(False)
        self.driverLineEdit.setStyleSheet("border: 1px solid black;")
        self.driverLineEdit.setFrame(True)
        self.driverLineEdit.setDragEnabled(False)
        self.driverLineEdit.setReadOnly(False)
        self.driverLineEdit.setObjectName("driverLineEdit")
        self.driverLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.companyLineEdit = QtWidgets.QLineEdit(EnterData)
        self.companyLineEdit.setGeometry(QtCore.QRect(410, 340, 301, 31))
        self.companyLineEdit.setValidator(uppervalidator)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.companyLineEdit.setFont(font)
        self.companyLineEdit.setTabletTracking(True)
        self.companyLineEdit.setAutoFillBackground(False)
        self.companyLineEdit.setStyleSheet("border: 1px solid black;")
        self.companyLineEdit.setFrame(True)
        self.companyLineEdit.setDragEnabled(False)
        self.companyLineEdit.setReadOnly(False)
        self.companyLineEdit.setObjectName("companyLineEdit")
        self.companyLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.remarkLineEdit = QtWidgets.QLineEdit(EnterData)
        self.remarkLineEdit.setGeometry(QtCore.QRect(410, 390, 301, 31))
        self.remarkLineEdit.setValidator(uppervalidator)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.remarkLineEdit.setFont(font)
        self.remarkLineEdit.setTabletTracking(True)
        self.remarkLineEdit.setAutoFillBackground(False)
        self.remarkLineEdit.setStyleSheet("border: 1px solid black;")
        self.remarkLineEdit.setFrame(True)
        self.remarkLineEdit.setDragEnabled(False)
        self.remarkLineEdit.setReadOnly(False)
        self.remarkLineEdit.setObjectName("remarkLineEdit")
        self.remarkLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.remarkLineEdit.setValidator(uppervalidator)
        self.abol_numLineEdit = QtWidgets.QLineEdit(EnterData)
        self.abol_numLineEdit.setGeometry(QtCore.QRect(410, 110, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.abol_numLineEdit.setFont(font)
        self.abol_numLineEdit.setTabletTracking(True)
        self.abol_numLineEdit.setAutoFillBackground(False)
        self.abol_numLineEdit.setStyleSheet("border: 1px solid black;")
        self.abol_numLineEdit.setFrame(True)
        self.abol_numLineEdit.setDragEnabled(False)
        self.abol_numLineEdit.setReadOnly(False)
        self.abol_numLineEdit.setObjectName("abol_numLineEdit")
        self.abol_numLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.abol_numLineEdit.setDisabled(True)
        self.ladevolumenLineEdit = QtWidgets.QLineEdit(EnterData)
        self.ladevolumenLineEdit.setGeometry(QtCore.QRect(410, 440, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ladevolumenLineEdit.setFont(font)
        self.ladevolumenLineEdit.setTabletTracking(True)
        self.ladevolumenLineEdit.setAutoFillBackground(False)
        self.ladevolumenLineEdit.setStyleSheet("border: 1px solid black;")
        self.ladevolumenLineEdit.setFrame(True)
        self.ladevolumenLineEdit.setDragEnabled(False)
        self.ladevolumenLineEdit.setReadOnly(False)
        self.ladevolumenLineEdit.setObjectName("ladevolumenLineEdit")
        self.ladevolumenLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'[0-9]+'))
        self.ladevolumenLineEdit.setValidator(validator)
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
        self.label_6.setGeometry(QtCore.QRect(180, 110, 171, 31))
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
        self.Button_1.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
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
        self.Button_3.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.Button_3.setObjectName("Button_3")
        self.Button_2 = QtWidgets.QPushButton(EnterData)
        self.Button_2.setGeometry(QtCore.QRect(290, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_2.setFont(font)
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
        self.ButtonSpace.setGeometry(QtCore.QRect(640, 660, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonSpace.setFont(font)
        self.ButtonSpace.setStyleSheet("border: 1px solid black;\n"
"color: white;\n"
"background-color: rgb(45, 45, 45);")
        self.ButtonSpace.setObjectName("ButtonSpace")

        self.retranslateUi(EnterData)
        QtCore.QMetaObject.connectSlotsByName(EnterData)

        self.backButton.clicked.connect(lambda: self.clicked("back", EnterData))
        self.nextButton.clicked.connect(lambda: self.clicked("next", EnterData))
        
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
        
        self.abol_numLineEdit.setText(os.environ["PK_NO"])

        self.getButton.hide()
        
        
    def retranslateUi(self, EnterData):
        self.i18n = I18N(os.environ["LANG"])
        _translate = QtCore.QCoreApplication.translate
        EnterData.setWindowTitle(_translate("EnterData", "Trimble"))
        self.label.setText(_translate("EnterData", os.environ["MSG"]))
        self.label_2.setText(_translate("EnterData", self.i18n.enter_details))
        self.label_3.setText(_translate("EnterData", self.i18n.enter_license_plate))
        self.getButton.setText(_translate("EnterData", "Get"))
        self.label_4.setText(_translate("EnterData", self.i18n.enter_driver_name))
        self.label_5.setText(_translate("EnterData", self.i18n.enter_contractor))
        self.label_6.setText(_translate("EnterData", "Abhol-Nummer"))
        self.label_7.setText(_translate("EnterData", self.i18n.enter_remark))
        self.label_8.setText(_translate("EnterData", self.i18n.total_load + " (kg)"))
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
        self.ButtonGerA.setText(_translate("EnterData", "Ä"))
        self.LButton.setText(_translate("EnterData", "L"))
        self.KButton.setText(_translate("EnterData", "K"))
        self.JButton.setText(_translate("EnterData", "J"))
        self.ButtonGerO.setText(_translate("EnterData", "Ö"))
        self.ZButton.setText(_translate("EnterData", "Z"))
        self.XButton.setText(_translate("EnterData", "X"))
        self.CButton.setText(_translate("EnterData", "C"))
        self.BButton.setText(_translate("EnterData", "B"))
        self.VButton.setText(_translate("EnterData", "V"))
        self.NButton.setText(_translate("EnterData", "N"))
        self.MButton.setText(_translate("EnterData", "M"))
        self.ButtonGerU.setText(_translate("EnterData", "Ü    "))
        self.ButtonSpace.setText(_translate("EnterData", "SPACE"))
        
        
        
    def clicked(self, text, window):
        _translate = QtCore.QCoreApplication.translate
        self.i18n = I18N(os.environ["LANG"])
        if text == "next":
            if len(self.licenseLineEdit.text()) == 0:
                self.licenseLineEdit.setStyleSheet("border: 1px solid red")
                QtWidgets.QToolTip.showText(self.licenseLineEdit.pos(), self.i18n.please_fill)
            
            elif len(self.driverLineEdit.text()) == 0:
                self.driverLineEdit.setStyleSheet("border: 1px solid red")
                QtWidgets.QToolTip.showText(self.driverLineEdit.pos(), self.i18n.please_fill)
            
            elif len(self.companyLineEdit.text()) == 0:
                self.companyLineEdit.setStyleSheet("border: 1px solid red")
                QtWidgets.QToolTip.showText(self.companyLineEdit.pos(), self.i18n.please_fill)
            
            elif len(self.ladevolumenLineEdit.text()) == 0:
                self.ladevolumenLineEdit.setStyleSheet("border: 1px solid red")
                QtWidgets.QToolTip.showText(self.ladevolumenLineEdit.pos(), self.i18n.please_fill)
            else:   
                os.environ["license_no"] = self.licenseLineEdit.text()
                os.environ["driver_name"] = self.driverLineEdit.text()
                os.environ["contractor"] = self.companyLineEdit.text()
                os.environ["remark"] = self.remarkLineEdit.text()
                self.EmptyWeighing = QtWidgets.QWidget()
                self.ui = Ui_EmptyWeighing()
                self.ui.setupUi(self.EmptyWeighing)
                self.EmptyWeighing.show()
                window.hide()
        else:
            self.ScanPickupNumber = QtWidgets.QWidget()
            self.ui = Ui_ScanPickupNumber()
            self.ui.setupUi(self.ScanPickupNumber)
            self.ScanPickupNumber.show()
            window.hide()
    
    def key_press(self, text):
            
        if self.licenseLineEdit.hasFocus():
            if text == "<-":
                txt = self.licenseLineEdit.text()
                self.licenseLineEdit.setText(txt[:-1])
            else:    
                txt = self.licenseLineEdit.text()
                txt += text
                self.licenseLineEdit.setText(txt)

        elif self.driverLineEdit.hasFocus():
            if text == "<-":
                txt = self.driverLineEdit.text()
                self.driverLineEdit.setText(txt[:-1])
            else:    
                txt = self.driverLineEdit.text()
                txt += text
                self.driverLineEdit.setText(txt)
                
        elif self.companyLineEdit.hasFocus():
            if text == "<-":
                txt = self.companyLineEdit.text()
                self.companyLineEdit.setText(txt[:-1])
            else:    
                txt = self.companyLineEdit.text()
                txt += text
                self.companyLineEdit.setText(txt)
            
        elif self.remarkLineEdit.hasFocus():
            if text == "<-":
                txt = self.remarkLineEdit.text()
                self.remarkLineEdit.setText(txt[:-1])
            else:    
                txt = self.remarkLineEdit.text()
                txt += text
                self.remarkLineEdit.setText(txt)
            
        elif self.ladevolumenLineEdit.hasFocus():
            if text == "<-":
                txt = self.ladevolumenLineEdit.text()
                self.ladevolumenLineEdit.setText(txt[:-1])
            elif text in "0123456789.":    
                txt = self.ladevolumenLineEdit.text()
                txt += text
                self.ladevolumenLineEdit.setText(txt)
        
    
    def get(self):
        global HOST, PORT
        cmd = "GET PLATE"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(cmd.encode("UTF-8"))
            data = s.recv(1024)
            retval = data.decode("UTF-8")
            w_obj = json.loads(retval)
            self.licenseLineEdit.setText(w_obj["license_plate"])


class Ui_EmptyWeighing(object):
    def setupUi(self, EmptyWeighing):
        EmptyWeighing.setObjectName("EmptyWeighing")
        EmptyWeighing.resize(1024, 768)
        EmptyWeighing.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backButton = QtWidgets.QPushButton(EmptyWeighing)
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.backButton.setGeometry(QtCore.QRect(24, 520, 151, 111))
        self.nextButton = QtWidgets.QPushButton(EmptyWeighing)
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nextButton.setIcon(icon1)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.setGeometry(QtCore.QRect(850, 510, 151, 111))
        self.msg_label = QtWidgets.QLabel(EmptyWeighing)
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
        self.label = QtWidgets.QLabel(EmptyWeighing)
        self.label.setGeometry(QtCore.QRect(400, 140, 171, 131))
        self.label.setStyleSheet("align: center;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/information.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(EmptyWeighing)
        self.logo.setGeometry(QtCore.QRect(720, 10, 281, 81))
        self.logo.setAutoFillBackground(False)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.msg_label_2 = QtWidgets.QLabel(EmptyWeighing)
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

        self.retranslateUi(EmptyWeighing)
        QtCore.QMetaObject.connectSlotsByName(EmptyWeighing)
        
        self.backButton.clicked.connect(lambda: self.clicked("back", EmptyWeighing))
        self.nextButton.clicked.connect(lambda: self.clicked("next", EmptyWeighing))
        
        self.nextButton.hide()
        self.backButton.hide()
        
        _thread.start_new_thread(contact_client, (self.enable_all,))

    def retranslateUi(self, EmptyWeighing):
        _translate = QtCore.QCoreApplication.translate
        EmptyWeighing.setWindowTitle(_translate("EmptyWeighing", "Trimble"))
        self.i18n = I18N(os.environ["LANG"])
        self.msg_label.setText(_translate("EmptyWeighing", self.i18n.empty_weigh_start))
        self.msg_label_2.setText(_translate("EmptyWeighing", ""))
        
    def clicked(self, text, window):
        if text == "next":
            self.StartLoading = QtWidgets.QWidget()
            self.ui = Ui_StartLoading()
            self.ui.setupUi(self.StartLoading)
            self.StartLoading.show()
            window.hide()
        else:
            self.EnterData = QtWidgets.QWidget()
            self.ui_ed = Ui_EnterData()
            self.ui_ed.setupUi(self.EnterData)
            self.EnterData.show()
            window.hide()   
            
    def enable_all(self, w_obj):
        os.environ["st_weight"] = w_obj['weight']
        st_datetime = w_obj['date'] + " " + w_obj["time"]
        os.environ["st_datetime"] = st_datetime
        os.environ["st_alibi_nr"] = w_obj['alibi_nr']
        _translate = QtCore.QCoreApplication.translate
        self.msg_label_2.setText(_translate("EmptyWeighing", "Gewicht: " + w_obj["weight"] + " kg"))
        self.nextButton.show()
        self.backButton.show()
        
        
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
        
        self.backButton.clicked.connect(lambda: self.clicked("back", StartLoading))
        self.nextButton.clicked.connect(lambda: self.clicked("next", StartLoading))

    def retranslateUi(self, StartLoading):
        _translate = QtCore.QCoreApplication.translate
        StartLoading.setWindowTitle(_translate("StartLoading", "Trimble"))
        self.i18n = I18N(os.environ["LANG"])
        self.nextButton.setText(_translate("StartLoading", self.i18n.lf))
        self.msg_label.setText(_translate("StartLoading", self.i18n.stop_loading1))
        self.msg_label_2.setText(_translate("StartLoading", self.i18n.stop_loading2))
        
    def clicked(self, text, window):
        if text == "next":
            self.FullWeighing = QtWidgets.QWidget()
            self.ui = Ui_FullWeighing()
            self.ui.setupUi(self.FullWeighing)
            self.FullWeighing.show()
            window.hide() 
        else:
            self.EmptyWeighing = QtWidgets.QWidget()
            self.ui = Ui_EmptyWeighing()
            self.ui.setupUi(self.EmptyWeighing)
            self.EmptyWeighing.show()
            window.hide() 
            

class Ui_FullWeighing(object):
    def setupUi(self, FullWeighing):
        FullWeighing.setObjectName("FullWeighing")
        FullWeighing.resize(1024, 768)
        FullWeighing.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backButton = QtWidgets.QPushButton(FullWeighing)
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")
        self.backButton.setGeometry(QtCore.QRect(24, 520, 151, 111))
        self.nextButton = QtWidgets.QPushButton(FullWeighing)
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nextButton.setIcon(icon1)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.setGeometry(QtCore.QRect(850, 510, 151, 111))
        self.msg_label = QtWidgets.QLabel(FullWeighing)
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
        self.label = QtWidgets.QLabel(FullWeighing)
        self.label.setGeometry(QtCore.QRect(400, 140, 171, 131))
        self.label.setStyleSheet("align: center;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/information.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(FullWeighing)
        self.logo.setGeometry(QtCore.QRect(720, 10, 281, 81))
        self.logo.setAutoFillBackground(False)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.msg_label_2 = QtWidgets.QLabel(FullWeighing)
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

        self.retranslateUi(FullWeighing)
        QtCore.QMetaObject.connectSlotsByName(FullWeighing)
        
        self.backButton.clicked.connect(lambda: self.clicked("back", FullWeighing))
        self.nextButton.clicked.connect(lambda: self.clicked("next", FullWeighing))
        
        self.nextButton.hide()
        self.backButton.hide()
        
        _thread.start_new_thread(contact_client, (self.enable_all,))

    def retranslateUi(self, FullWeighing):
        _translate = QtCore.QCoreApplication.translate
        FullWeighing.setWindowTitle(_translate("FullWeighing", "Trimble"))
        self.i18n = I18N(os.environ["LANG"])
        self.msg_label.setText(_translate("FullWeighing", self.i18n.weighing_completed))
        self.msg_label_2.setText(_translate("FullWeighing", ""))
        
    def clicked(self, text, window):
        if text == "next":
            ui = Ui_Signature()
            ui.show()
            window.hide()
        else:
            self.StartLoading = QtWidgets.QWidget()
            self.ui = Ui_StartLoading()
            self.ui.setupUi(self.StartLoading)
            self.StartLoading.show()
            window.hide()  
            
    def enable_all(self, w_obj):
        os.environ["end_weight"] = w_obj['weight']
        st_datetime = w_obj['date'] + " " + w_obj["time"]
        os.environ["end_datetime"] = st_datetime
        os.environ["end_alibi_nr"] = w_obj['alibi_nr']
        _translate = QtCore.QCoreApplication.translate
        self.msg_label_2.setText(_translate("FullWeighing", "Gewicht: " + w_obj["weight"] + " kg"))
        self.nextButton.show()
        self.backButton.show()
        
        
# class Ui_WaitForSignature(object):
#     def setupUi(self, WaitForSignature):
#         WaitForSignature.setObjectName("WaitForSignature")
#         WaitForSignature.resize(1024, 768)
#         WaitForSignature.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.label = QtWidgets.QLabel(WaitForSignature)
#         self.label.setGeometry(QtCore.QRect(400, 150, 161, 131))
#         self.label.setStyleSheet("align: center;\n"
# "border: 2px solid darkblue;")
#         self.label.setText("")
#         self.label.setPixmap(QtGui.QPixmap("img/trackpad.png"))
#         self.label.setScaledContents(True)
#         self.label.setAlignment(QtCore.Qt.AlignCenter)
#         self.label.setObjectName("label")
#         self.msg_label = QtWidgets.QLabel(WaitForSignature)
#         self.msg_label.setGeometry(QtCore.QRect(10, 360, 951, 41))
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.msg_label.setFont(font)
#         self.msg_label.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.msg_label.setAutoFillBackground(False)
#         self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.msg_label.setObjectName("msg_label")
#         self.backButton = QtWidgets.QPushButton(WaitForSignature)
#         self.backButton.setGeometry(QtCore.QRect(24, 530, 151, 111))
#         self.backButton.setStyleSheet("border: 1px solid white;")
#         self.backButton.setText("")
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
#         self.backButton.setIcon(icon)
#         self.backButton.setIconSize(QtCore.QSize(103, 105))
#         self.backButton.setObjectName("backButton")
#         self.logo = QtWidgets.QLabel(WaitForSignature)
#         self.logo.setGeometry(QtCore.QRect(720, 20, 281, 81))
#         self.logo.setAutoFillBackground(False)
#         self.logo.setText("")
#         self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
#         self.logo.setScaledContents(True)
#         self.logo.setObjectName("logo")
#         self.nextButton = QtWidgets.QPushButton(WaitForSignature)
#         self.nextButton.setGeometry(QtCore.QRect(830, 530, 151, 111))
#         self.nextButton.setStyleSheet("border: 1px solid white;")
#         self.nextButton.setText("")
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
#         self.nextButton.setIcon(icon1)
#         self.nextButton.setIconSize(QtCore.QSize(103, 105))
#         self.nextButton.setObjectName("nextButton")

#         self.retranslateUi(WaitForSignature)
#         QtCore.QMetaObject.connectSlotsByName(WaitForSignature)
        
#         self.backButton.clicked.connect(lambda: self.clicked("back", WaitForSignature))
#         self.nextButton.clicked.connect(lambda: self.clicked("next", WaitForSignature))

#     def retranslateUi(self, WaitForSignature):
#         _translate = QtCore.QCoreApplication.translate
#         WaitForSignature.setWindowTitle(_translate("WaitForSignature", "Trimble"))
#         self.i18n = I18N(os.environ["LANG"])
#         self.msg_label.setText(_translate("WaitForSignature", self.i18n.please_sign_at_terminal))
        
#     def clicked(self, text, window):
#         if text == "next":
#             ui = Ui_Signature()
#             ui.show()
#             window.hide()
#         else:
#             self.FullWeighing = QtWidgets.QWidget()
#             self.ui = Ui_FullWeighing()
#             self.ui.setupUi(self.FullWeighing)
#             self.FullWeighing.show()
#             window.hide()
           
           
            
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

class Ui_Signature(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
        self.setObjectName("Signature")
        self.resize(1024, 768)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logo = QtWidgets.QLabel(self)
        self.logo.setGeometry(QtCore.QRect(730, 20, 281, 81))
        self.logo.setAutoFillBackground(False)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
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

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(130, 180, 771, 20))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(120, 190, 21, 321))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_2.setFont(font)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(890, 190, 20, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setWeight(50)
        self.line_3.setFont(font)
        self.line_3.setStyleSheet("")
        self.line_3.setLineWidth(2)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self)
        self.line_4.setWindowModality(QtCore.Qt.NonModal)
        self.line_4.setEnabled(True)
        self.line_4.setGeometry(QtCore.QRect(130, 500, 771, 20))
        self.line_4.setStyleSheet("")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(110, 110, 811, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.i18n = I18N(os.environ["LANG"])
        self.label.setText(self.i18n.please_sign_at_terminal)

    def retranslateUi(self, Signature):
        _translate = QtCore.QCoreApplication.translate
        Signature.setWindowTitle(_translate("Signature", "Trimble"))
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
  
    def save(self, window): 
        ##### Joerg 4 ####
        data = QByteArray()
        buf = QBuffer(data)
        self.image.save(buf, 'JPEG')
        #self.image.save("pickup_no_{}.png".format(os.environ["PK_NO"]))
        ##### Joerg 4 ####
        
        pk_no = int(os.environ["PK_NO"])
        license_no = str(os.environ["license_no"])
        driver_name = os.environ["driver_name"]
        contractor = os.environ["contractor"]
        remark = os.environ["remark"]
        
        import datetime
        st_weight = float(os.environ["st_weight"])
        st_datetime_obj = datetime.datetime.strptime(os.environ["st_datetime"], '%d.%m.%y %H:%M')
        st_alibi_nr = int(os.environ["st_alibi_nr"])
        
        end_weight = os.environ["end_weight"]
        end_datetime_obj = datetime.datetime.strptime(os.environ["end_datetime"], '%d.%m.%y %H:%M')
        end_alibi_nr = os.environ["end_alibi_nr"]
        
        
        import base64
        #with open("pickup_no_{}.png".format(str(pk_no)), "rb") as img_file:
        #    b64_string = base64.b64encode(img_file.read())
        b64_string = data.toBase64()

        ##### Joerg 4 Only for testing comment this ###
        # f_test_image = open("image_test.html", "wb")
        # f_test_image.write("<html><body><h1>Testimage</h1>\n".encode("UTF-8"))
        # f_test_image.write('<p><img src="data:image/jpeg;base64, '.encode("UTF-8"))
        # f_test_image.write(b64_string)
        # f_test_image.write('" />'.encode("UTF-8"))
        # f_test_image.write("</p>\n".encode("UTF-8"))
        # f_test_image.write("</body></html>\n".encode("UTF-8"))
        # f_test_image.close()
        ##### Joerg 4 end of Only for testing comment this ###
        
        ret_val2 = client.service.SaveDeliveryAndGetPDF(pk_no, 
                                                        license_no, 
                                                        driver_name, 
                                                        contractor, 
                                                        remark, 
                                                        b64_string, 
                                                        st_weight,
                                                        st_datetime_obj,
                                                        st_alibi_nr, 
                                                        end_weight, 
                                                        end_datetime_obj,
                                                        end_alibi_nr)
        f = open(resource_path("data_{}.pdf".format(str(pk_no))), "wb")
        f.write(ret_val2["PDF"])
        f.close()
        import webbrowser
        webbrowser.open_new(resource_path("data_{}.pdf".format(str(pk_no))))
        
        self.Print = QtWidgets.QWidget()
        self.ui = Ui_Print()
        self.ui.setupUi(self.Print)
        self.Print.show()
        window.hide()
        
    def clear(self): 
        self.image.fill(Qt.white) 
        self.update() 
        
        
class Ui_Print(object):
    def setupUi(self, Print):
        Print.setObjectName("Print")
        Print.resize(1024, 768)
        Print.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logo = QtWidgets.QLabel(Print)
        self.logo.setGeometry(QtCore.QRect(710, 30, 281, 81))
        self.logo.setAutoFillBackground(False)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(Print)
        self.label.setGeometry(QtCore.QRect(440, 180, 191, 151))
        self.label.setStyleSheet("align: center;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/information.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.msg_label = QtWidgets.QLabel(Print)
        self.msg_label.setGeometry(QtCore.QRect(46, 393, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.msg_label.setFont(font)
        self.msg_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg_label.setAutoFillBackground(True)
        self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label.setObjectName("msg_label")
        self.nextButton = QtWidgets.QPushButton(Print)
        self.nextButton.setGeometry(QtCore.QRect(840, 550, 151, 111))
        self.nextButton.setStyleSheet("border: 1px solid white;")
        self.nextButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/NextArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nextButton.setIcon(icon)
        self.nextButton.setIconSize(QtCore.QSize(103, 105))
        self.nextButton.setObjectName("nextButton")
        self.backButton = QtWidgets.QPushButton(Print)
        self.backButton.setGeometry(QtCore.QRect(60, 550, 151, 111))
        self.backButton.setStyleSheet("border: 1px solid white;")
        self.backButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backButton.setIcon(icon1)
        self.backButton.setIconSize(QtCore.QSize(103, 105))
        self.backButton.setObjectName("backButton")

        self.retranslateUi(Print)
        QtCore.QMetaObject.connectSlotsByName(Print)
        
        self.backButton.clicked.connect(lambda: self.clicked("back", Print))
        self.nextButton.clicked.connect(lambda: self.clicked("next", Print))

    def retranslateUi(self, Print):
        _translate = QtCore.QCoreApplication.translate
        Print.setWindowTitle(_translate("Print", "Trimble"))
        self.i18n = I18N(os.environ["LANG"])
        self.msg_label.setText(_translate("Print", self.i18n.please_wait_data_is_sending))
        
    def clicked(self, text, window):
        if text == "back":
            ui = Ui_Signature()
            ui.show()
            window.hide()
        elif text == "next":
            self.language = QtWidgets.QMainWindow()
            self.ui_lang = Ui_language()
            self.ui_lang.setupUi(self.language)
            self.language.show()
            window.hide()
    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    language = QtWidgets.QMainWindow()
    ui = Ui_language()
    ui.setupUi(language)
    language.show()
    sys.exit(app.exec_())
