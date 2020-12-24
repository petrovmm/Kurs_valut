from bs4 import BeautifulSoup
import requests
import sys

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
import PySide2

from form import Ui_Dialog

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


def get_currency():
    print('hey guys <3')


ui.pushButton.clicked.connect(get_currency)




sys.exit(app.exec_())