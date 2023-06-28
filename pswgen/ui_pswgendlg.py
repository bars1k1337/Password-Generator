# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pswgendlg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PswGenDialog(object):
    def setupUi(self, PswGenDialog):
        if not PswGenDialog.objectName():
            PswGenDialog.setObjectName(u"PswGenDialog")
        PswGenDialog.resize(416, 166)
        self.verticalLayout = QVBoxLayout(PswGenDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(PswGenDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pswLenSlider = QSlider(PswGenDialog)
        self.pswLenSlider.setObjectName(u"pswLenSlider")
        self.pswLenSlider.setPageStep(1)
        self.pswLenSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.pswLenSlider)

        self.pswLenSpin = QSpinBox(PswGenDialog)
        self.pswLenSpin.setObjectName(u"pswLenSpin")

        self.horizontalLayout.addWidget(self.pswLenSpin)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.useDigitsCheck = QCheckBox(PswGenDialog)
        self.useDigitsCheck.setObjectName(u"useDigitsCheck")

        self.verticalLayout.addWidget(self.useDigitsCheck)

        self.useSpecsCheck = QCheckBox(PswGenDialog)
        self.useSpecsCheck.setObjectName(u"useSpecsCheck")

        self.verticalLayout.addWidget(self.useSpecsCheck)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(PswGenDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pswEdit = QLineEdit(PswGenDialog)
        self.pswEdit.setObjectName(u"pswEdit")
        self.pswEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.pswEdit)

        self.generateButton = QPushButton(PswGenDialog)
        self.generateButton.setObjectName(u"generateButton")

        self.horizontalLayout_2.addWidget(self.generateButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(PswGenDialog)

        QMetaObject.connectSlotsByName(PswGenDialog)
    # setupUi

    def retranslateUi(self, PswGenDialog):
        PswGenDialog.setWindowTitle(QCoreApplication.translate("PswGenDialog", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u043f\u0430\u0440\u043e\u043b\u0456\u0432", None))
        self.label.setText(QCoreApplication.translate("PswGenDialog", u"\u0414\u043e\u0432\u0436\u0438\u043d\u0430 \u043f\u0430\u0440\u043e\u043b\u044e:", None))
        self.useDigitsCheck.setText(QCoreApplication.translate("PswGenDialog", u"\u0412\u0438\u043a\u043e\u0440\u0438\u0441\u0442\u043e\u0432\u0443\u0432\u0430\u0442\u0438 \u0446\u0438\u0444\u0440\u0438", None))
        self.useSpecsCheck.setText(QCoreApplication.translate("PswGenDialog", u"\u0412\u0438\u043a\u043e\u0440\u0438\u0441\u0442\u043e\u0432\u0443\u0432\u0430\u0442\u0438 \u0441\u043f\u0435\u0446\u0456\u0430\u043b\u044c\u043d\u0456 \u0441\u0438\u043c\u0432\u043e\u043b\u0438", None))
        self.label_2.setText(QCoreApplication.translate("PswGenDialog", u"\u0412\u0430\u0448 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.generateButton.setText(QCoreApplication.translate("PswGenDialog", u"\u0417\u0433\u0435\u043d\u0435\u0440\u0443\u0432\u0430\u0442\u0438!", None))
    # retranslateUi

