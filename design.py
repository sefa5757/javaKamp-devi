# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(629, 491)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_city_name = QLineEdit(Form)
        self.txt_city_name.setObjectName(u"txt_city_name")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_city_name.sizePolicy().hasHeightForWidth())
        self.txt_city_name.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(23)
        self.txt_city_name.setFont(font)
        self.txt_city_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.txt_city_name)

        self.btn_add_city = QPushButton(Form)
        self.btn_add_city.setObjectName(u"btn_add_city")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_add_city.sizePolicy().hasHeightForWidth())
        self.btn_add_city.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(17)
        self.btn_add_city.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_add_city)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.city_list_combo_box = QComboBox(Form)
        self.city_list_combo_box.setObjectName(u"city_list_combo_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.city_list_combo_box.sizePolicy().hasHeightForWidth())
        self.city_list_combo_box.setSizePolicy(sizePolicy2)
        self.city_list_combo_box.setFont(font1)

        self.verticalLayout.addWidget(self.city_list_combo_box)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_get_weather = QPushButton(Form)
        self.btn_get_weather.setObjectName(u"btn_get_weather")
        sizePolicy1.setHeightForWidth(self.btn_get_weather.sizePolicy().hasHeightForWidth())
        self.btn_get_weather.setSizePolicy(sizePolicy1)
        self.btn_get_weather.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btn_get_weather)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lbl_weather_info = QLabel(Form)
        self.lbl_weather_info.setObjectName(u"lbl_coin_weather")
        self.lbl_weather_info.setFont(font)
        self.lbl_weather_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_weather_info)

        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 10)
        self.verticalLayout.setStretch(3, 70)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.txt_city_name.setPlaceholderText(QCoreApplication.translate("Form", u"İl bilgisini giriniz...", None))
        self.btn_add_city.setText(QCoreApplication.translate("Form", u"Ekle", None))
        self.btn_get_weather.setText(QCoreApplication.translate("Form", u"Hava Durumu", None))
        self.lbl_weather_info.setText(QCoreApplication.translate("Form", u"Weather", None))
    # retranslateUi

