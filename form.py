# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(516, 391)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 90, 161, 31))
        font = QFont()
        font.setFamily(u"Levenim MT")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color:#ff3881 ;\n"
"background-color:#5cff92 ;")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 160, 471, 211))
        font1 = QFont()
        font1.setFamily(u"Levenim MT")
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:#0d0924 ;\n"
"background-color: #a1ffd8;\n"
"")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 20, 411, 51))
        font2 = QFont()
        font2.setFamily(u"Levenim MT")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.lineEdit.setFont(font2)
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setStyleSheet(u"color:#9ef9ff ;\n"
"background-color: #ff3881;\n"
"")
        self.lineEdit.setFrame(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Predict", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

