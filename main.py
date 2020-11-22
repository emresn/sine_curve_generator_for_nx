import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sqlite3
from ui import Ui_Form


class Main(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)





app = QtWidgets.QApplication(sys.argv)

main = Main()
main.show()
app.exec()