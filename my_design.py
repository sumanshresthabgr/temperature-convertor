# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tempconv.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QSizePolicy,
    QWidget)
import resources_qc

class Ui_TemperatureConversion(object):
    def setupUi(self, TemperatureConversion):
        if not TemperatureConversion.objectName():
            TemperatureConversion.setObjectName(u"TemperatureConversion")
        TemperatureConversion.resize(400, 400)
        TemperatureConversion.setMinimumSize(QSize(400, 400))
        TemperatureConversion.setMaximumSize(QSize(400, 400))
        TemperatureConversion.setStyleSheet(u"background-color:rgb(0, 170, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.label = QLabel(TemperatureConversion)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 290, 51))
        font = QFont()
        font.setFamilies([u"Cooper Black"])
        font.setPointSize(18)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(TemperatureConversion)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 70, 81, 41))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift SemiBold"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.celsius_lineEdit = QLineEdit(TemperatureConversion)
        self.celsius_lineEdit.setObjectName(u"celsius_lineEdit")
        self.celsius_lineEdit.setGeometry(QRect(40, 110, 101, 41))
        font2 = QFont()
        font2.setPointSize(16)
        self.celsius_lineEdit.setFont(font2)
        self.celsius_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.celsius_lineEdit.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(TemperatureConversion)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 100, 51, 71))
        self.label_3.setPixmap(QPixmap(u":/newPrefix/two-side-arrows-white-color-icon-vector--removebg-preview.png"))
        self.label_3.setScaledContents(True)
        self.fahrenheit_lineEdit = QLineEdit(TemperatureConversion)
        self.fahrenheit_lineEdit.setObjectName(u"fahrenheit_lineEdit")
        self.fahrenheit_lineEdit.setGeometry(QRect(220, 110, 101, 41))
        self.fahrenheit_lineEdit.setFont(font2)
        self.fahrenheit_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.fahrenheit_lineEdit.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(TemperatureConversion)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 80, 150, 30))
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift SemiBold"])
        font3.setPointSize(17)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.celsius_lineEdit2 = QLineEdit(TemperatureConversion)
        self.celsius_lineEdit2.setObjectName(u"celsius_lineEdit2")
        self.celsius_lineEdit2.setGeometry(QRect(30, 200, 101, 41))
        self.celsius_lineEdit2.setFont(font2)
        self.celsius_lineEdit2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.celsius_lineEdit2.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(TemperatureConversion)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 160, 81, 41))
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift SemiBold"])
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.kelvin_lineEdit = QLineEdit(TemperatureConversion)
        self.kelvin_lineEdit.setObjectName(u"kelvin_lineEdit")
        self.kelvin_lineEdit.setGeometry(QRect(220, 200, 101, 41))
        self.kelvin_lineEdit.setFont(font2)
        self.kelvin_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.kelvin_lineEdit.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(TemperatureConversion)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 190, 51, 71))
        self.label_6.setPixmap(QPixmap(u":/newPrefix/two-side-arrows-white-color-icon-vector--removebg-preview.png"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(TemperatureConversion)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 170, 81, 20))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.fahrenheit_lineEdit2 = QLineEdit(TemperatureConversion)
        self.fahrenheit_lineEdit2.setObjectName(u"fahrenheit_lineEdit2")
        self.fahrenheit_lineEdit2.setGeometry(QRect(30, 280, 101, 41))
        self.fahrenheit_lineEdit2.setFont(font2)
        self.fahrenheit_lineEdit2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.fahrenheit_lineEdit2.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(TemperatureConversion)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 240, 101, 41))
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.kelvin_lineEdit2 = QLineEdit(TemperatureConversion)
        self.kelvin_lineEdit2.setObjectName(u"kelvin_lineEdit2")
        self.kelvin_lineEdit2.setGeometry(QRect(220, 280, 101, 41))
        self.kelvin_lineEdit2.setFont(font2)
        self.kelvin_lineEdit2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.kelvin_lineEdit2.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(TemperatureConversion)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 250, 150, 30))
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift SemiBold"])
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setItalic(False)
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_9 = QLabel(TemperatureConversion)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(150, 270, 50, 71))
        self.label_9.setPixmap(QPixmap(u":/newPrefix/two-side-arrows-white-color-icon-vector--removebg-preview.png"))
        self.label_9.setScaledContents(True)

        self.retranslateUi(TemperatureConversion)

        QMetaObject.connectSlotsByName(TemperatureConversion)
    # setupUi

    def retranslateUi(self, TemperatureConversion):
        TemperatureConversion.setWindowTitle(QCoreApplication.translate("TemperatureConversion", u"Form", None))
        self.label.setText(QCoreApplication.translate("TemperatureConversion", u"Temperature Converter", None))
        self.label_2.setText(QCoreApplication.translate("TemperatureConversion", u"Celsius", None))
        self.celsius_lineEdit.setPlaceholderText(QCoreApplication.translate("TemperatureConversion", u"0", None))
        self.label_3.setText("")
        self.fahrenheit_lineEdit.setPlaceholderText(QCoreApplication.translate("TemperatureConversion", u"32", None))
        self.label_4.setText(QCoreApplication.translate("TemperatureConversion", u"Fahrenheit", None))
        self.celsius_lineEdit2.setPlaceholderText(QCoreApplication.translate("TemperatureConversion", u"0", None))
        self.label_5.setText(QCoreApplication.translate("TemperatureConversion", u"Kelvin", None))
        self.kelvin_lineEdit.setPlaceholderText(QCoreApplication.translate("TemperatureConversion", u"32", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("TemperatureConversion", u"Celsius", None))
        self.fahrenheit_lineEdit2.setPlaceholderText(QCoreApplication.translate("TemperatureConversion", u"0", None))
        self.label_8.setText(QCoreApplication.translate("TemperatureConversion", u"Kelvin", None))
        self.kelvin_lineEdit2.setPlaceholderText(QCoreApplication.translate("TemperatureConversion", u"32", None))
        self.label_10.setText(QCoreApplication.translate("TemperatureConversion", u"Fahrenheit", None))
        self.label_9.setText("")
    # retranslateUi

