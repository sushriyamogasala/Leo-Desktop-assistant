from gui import Ui_MainWindow
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import Lucy

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        
    def run(self):
        Lucy.security()

startfunctions = MainThread()


class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lucy_ui = Ui_MainWindow()
        self.lucy_ui.setupUi(self)

    def startfun(self):
        self.lucy_ui.movies_2 = QtGui.QMovie("src/__1.gif")
        self.lucy_ui.sm.setMovie(self.lucy_ui.movies_2)
        self.lucy_ui.movies_2.start()

        self.lucy_ui.movies_3 = QtGui.QMovie("src/Jarvis_Gui (1).gif")
        self.lucy_ui.middle.setMovie(self.lucy_ui.movies_3)
        self.lucy_ui.movies_3.start()

        self.lucy_ui.movies_4 = QtGui.QMovie("src/Earth.gif")
        self.lucy_ui.earth.setMovie(self.lucy_ui.movies_4)
        self.lucy_ui.movies_4.start()

        self.lucy_ui.movies_5 = QtGui.QMovie("src/dribbble.gif")
        self.lucy_ui.percent.setMovie(self.lucy_ui.movies_5)
        self.lucy_ui.movies_5.start()

        self.lucy_ui.movies_6 = QtGui.QMovie("src/200.gif")
        self.lucy_ui.code.setMovie(self.lucy_ui.movies_6)
        self.lucy_ui.movies_6.start()

        self.lucy_ui.movies_7 = QtGui.QMovie("src/0baf79ba59be86610edc1f810a79f2b7.gif")
        self.lucy_ui.loadpic.setMovie(self.lucy_ui.movies_7)
        self.lucy_ui.movies_7.start()

        self.lucy_ui.movies_8 = QtGui.QMovie("src/initial.gif")
        self.lucy_ui.initialize.setMovie(self.lucy_ui.movies_8)
        self.lucy_ui.movies_8.start()

        startfunctions.start()

    def cls(self):
        self.close()


gui_app = QApplication(sys.argv)
gui_lucy = Gui_start()
gui_lucy.startfun()
gui_lucy.show()
exit(gui_app.exec_()) 