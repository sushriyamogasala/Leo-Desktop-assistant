from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer,QTime,Qt,QDate
import leo
import psutil

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        MainWindow.setWindowIcon(QtGui.QIcon('src/logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1551, 921))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("src/Black_Template.jpg"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")

        self.sm = QtWidgets.QLabel(self.centralwidget)
        self.sm.setGeometry(QtCore.QRect(-100, 450, 641, 481))
        self.sm.setText("")
        self.sm.setPixmap(QtGui.QPixmap("src/__1.gif"))
        self.sm.setScaledContents(True)
        self.sm.setObjectName("sm")

        self.middle = QtWidgets.QLabel(self.centralwidget)
        self.middle.setGeometry(QtCore.QRect(420, 170, 781, 441))
        self.middle.setText("")
        self.middle.setPixmap(QtGui.QPixmap("src/Jarvis_Gui (1).gif"))
        self.middle.setScaledContents(True)
        self.middle.setObjectName("middle")

        self.earth = QtWidgets.QLabel(self.centralwidget)
        self.earth.setGeometry(QtCore.QRect(1090, -10, 401, 301))
        self.earth.setText("")
        self.earth.setPixmap(QtGui.QPixmap("src/Earth.gif"))
        self.earth.setScaledContents(True)
        self.earth.setObjectName("earth")

        self.percent = QtWidgets.QLabel(self.centralwidget)
        self.percent.setGeometry(QtCore.QRect(1070, 560, 441, 401))
        self.percent.setText("")
        self.percent.setPixmap(QtGui.QPixmap("src/dribbble.gif"))
        self.percent.setScaledContents(True)
        self.percent.setObjectName("percent")

        self.code = QtWidgets.QLabel(self.centralwidget)
        self.code.setGeometry(QtCore.QRect(40, 50, 321, 241))
        self.code.setText("")
        self.code.setPixmap(QtGui.QPixmap("src/200.gif"))
        self.code.setScaledContents(True)
        self.code.setObjectName("code")

        self.loadpic = QtWidgets.QLabel(self.centralwidget)
        self.loadpic.setGeometry(QtCore.QRect(410, 620, 701, 231))
        self.loadpic.setText("")
        self.loadpic.setPixmap(QtGui.QPixmap("src/0baf79ba59be86610edc1f810a79f2b7.gif"))
        self.loadpic.setScaledContents(True)
        self.loadpic.setObjectName("loadpic")

        self.loadbox = QtWidgets.QLabel(self.centralwidget)
        self.loadbox.setGeometry(QtCore.QRect(650, 790, 211, 61))
        self.loadbox.setText("")
        self.loadbox.setPixmap(QtGui.QPixmap("src/wd.jpg"))
        self.loadbox.setScaledContents(True)
        self.loadbox.setObjectName("loadbox")

        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(690, 800, 131, 31))
        self.loading.setStyleSheet("background-color:Transparent;\n"
                                   "color:aqua;\n"
                                   "font: 13pt \"Berlin Sans FB\";")
        self.loading.setObjectName("loading")

        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(1110, 310, 351, 71))
        self.date.setText("")
        self.date.setPixmap(QtGui.QPixmap("src/gggf.jpg"))
        self.date.setScaledContents(True)
        self.date.setObjectName("date")

        self.datee = QtWidgets.QLabel(self.centralwidget)
        self.datee.setGeometry(QtCore.QRect(1200, 310, 381, 71))
        self.datee.setStyleSheet("background-color:Transparent;\n"
                                 "color:aqua;\n"
                                 "font: 15pt \"Berlin Sans FB\";")
        self.datee.setObjectName("datee")

        self.day = QtWidgets.QLabel(self.centralwidget)
        self.day.setGeometry(QtCore.QRect(1110, 420, 351, 71))
        self.day.setText("")
        self.day.setPixmap(QtGui.QPixmap("src/gggf.jpg"))
        self.day.setScaledContents(True)
        self.day.setObjectName("day")

        self.dayee = QtWidgets.QLabel(self.centralwidget)
        self.dayee.setGeometry(QtCore.QRect(1230, 420, 381, 71))
        self.dayee.setStyleSheet("background-color:Transparent;\n"
                                 "color:aqua;\n"
                                 "font: 15pt \"Berlin Sans FB\";")
        self.dayee.setObjectName("dayee")

        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(1110, 520, 351, 71))
        self.time.setText("")
        self.time.setPixmap(QtGui.QPixmap("src/gggf.jpg"))
        self.time.setScaledContents(True)
        self.time.setObjectName("time")

        self.timee = QtWidgets.QLabel(self.centralwidget)
        self.timee.setGeometry(QtCore.QRect(1240, 520, 381, 71))
        self.timee.setStyleSheet("background-color:Transparent;\n"
                                 "color:aqua;\n"
                                 "font: 18pt \"Berlin Sans FB\";")
        self.timee.setObjectName("timee")

        self.initialize = QtWidgets.QLabel(self.centralwidget)
        self.initialize.setGeometry(QtCore.QRect(540, -30, 451, 211))
        self.initialize.setText("")
        self.initialize.setPixmap(QtGui.QPixmap("src/initial.gif"))
        self.initialize.setScaledContents(True)
        self.initialize.setObjectName("initialize")

        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(30, 330, 351, 71))
        self.temp.setText("")
        self.temp.setPixmap(QtGui.QPixmap("src/gggf.jpg"))
        self.temp.setScaledContents(True)
        self.temp.setObjectName("temp")

        self.tempe = QtWidgets.QLabel(self.centralwidget)
        self.tempe.setGeometry(QtCore.QRect(70, 330, 381, 71))
        self.tempe.setStyleSheet("background-color:Transparent;\n"
                                 "color:aqua;\n"
                                 "font: 12pt \"Berlin Sans FB\";")
        self.tempe.setObjectName("tempe")

        self.region = QtWidgets.QLabel(self.centralwidget)
        self.region.setGeometry(QtCore.QRect(30, 440, 351, 71))
        self.region.setText("")
        self.region.setPixmap(QtGui.QPixmap("src/gggf.jpg"))
        self.region.setScaledContents(True)
        self.region.setObjectName("region")

        self.reg = QtWidgets.QLabel(self.centralwidget)
        self.reg.setGeometry(QtCore.QRect(150, 440, 381, 71))
        self.reg.setStyleSheet("background-color:Transparent;\n"
                                 "color:aqua;\n"
                                 "font: 18pt \"Berlin Sans FB\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "leo"))
        self.loading.setText(_translate("MainWindow", "Loading . . ."))

        dt = QDate.currentDate()
        dt1 = dt.toString("dd  MMMM  yyyy")
        self.datee.setText(_translate("MainWindow", dt1))
        dd = dt.toString("dddd")
        self.dayee.setText(_translate("MainWindow", dd))
        dt = psutil.sensors_battery()
        z = str(dt.percent)
        self.timee.setText(_translate("MainWindow",z+' %'))
        t = leo.ert()
        self.reg.setText(_translate("MainWindow", t))
        r = leo.wolfram("Temperature of visakhapatnam")
        self.tempe.setText(_translate("MainWindow", r))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
