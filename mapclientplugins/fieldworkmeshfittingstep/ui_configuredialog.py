# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
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
        Dialog.resize(418, 508)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.configGroupBox = QGroupBox(Dialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label14 = QLabel(self.configGroupBox)
        self.label14.setObjectName(u"label14")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label14)

        self.lineEdit14 = QLineEdit(self.configGroupBox)
        self.lineEdit14.setObjectName(u"lineEdit14")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit14)

        self.label9 = QLabel(self.configGroupBox)
        self.label9.setObjectName(u"label9")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label9)

        self.lineEdit9 = QLineEdit(self.configGroupBox)
        self.lineEdit9.setObjectName(u"lineEdit9")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit9)

        self.label1 = QLabel(self.configGroupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label1)

        self.lineEdit1 = QLineEdit(self.configGroupBox)
        self.lineEdit1.setObjectName(u"lineEdit1")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit1)

        self.label2 = QLabel(self.configGroupBox)
        self.label2.setObjectName(u"label2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label2)

        self.lineEdit2 = QLineEdit(self.configGroupBox)
        self.lineEdit2.setObjectName(u"lineEdit2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit2)

        self.label3 = QLabel(self.configGroupBox)
        self.label3.setObjectName(u"label3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label3)

        self.lineEdit3 = QLineEdit(self.configGroupBox)
        self.lineEdit3.setObjectName(u"lineEdit3")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit3)

        self.label4 = QLabel(self.configGroupBox)
        self.label4.setObjectName(u"label4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label4)

        self.lineEdit4 = QLineEdit(self.configGroupBox)
        self.lineEdit4.setObjectName(u"lineEdit4")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit4)

        self.label5 = QLabel(self.configGroupBox)
        self.label5.setObjectName(u"label5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label5)

        self.lineEdit5 = QLineEdit(self.configGroupBox)
        self.lineEdit5.setObjectName(u"lineEdit5")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit5)

        self.label8 = QLabel(self.configGroupBox)
        self.label8.setObjectName(u"label8")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label8)

        self.lineEdit8 = QLineEdit(self.configGroupBox)
        self.lineEdit8.setObjectName(u"lineEdit8")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit8)

        self.label6 = QLabel(self.configGroupBox)
        self.label6.setObjectName(u"label6")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label6)

        self.lineEdit6 = QLineEdit(self.configGroupBox)
        self.lineEdit6.setObjectName(u"lineEdit6")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit6)

        self.label7 = QLabel(self.configGroupBox)
        self.label7.setObjectName(u"label7")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label7)

        self.lineEdit7 = QLineEdit(self.configGroupBox)
        self.lineEdit7.setObjectName(u"lineEdit7")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.lineEdit7)

        self.label11 = QLabel(self.configGroupBox)
        self.label11.setObjectName(u"label11")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label11)

        self.lineEdit11 = QLineEdit(self.configGroupBox)
        self.lineEdit11.setObjectName(u"lineEdit11")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.lineEdit11)

        self.label10 = QLabel(self.configGroupBox)
        self.label10.setObjectName(u"label10")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label10)

        self.lineEdit10 = QLineEdit(self.configGroupBox)
        self.lineEdit10.setObjectName(u"lineEdit10")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.lineEdit10)

        self.label12 = QLabel(self.configGroupBox)
        self.label12.setObjectName(u"label12")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label12)

        self.lineEdit12 = QLineEdit(self.configGroupBox)
        self.lineEdit12.setObjectName(u"lineEdit12")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.lineEdit12)

        self.label13 = QLabel(self.configGroupBox)
        self.label13.setObjectName(u"label13")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label13)

        self.lineEdit13 = QLineEdit(self.configGroupBox)
        self.lineEdit13.setObjectName(u"lineEdit13")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.lineEdit13)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ConfigureDialog", None))
        self.configGroupBox.setTitle("")
        self.label14.setText(QCoreApplication.translate("Dialog", u"GUI:", None))
        self.label9.setText(QCoreApplication.translate("Dialog", u"fit mode:  ", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"mesh discretisation:  ", None))
        self.label2.setText(QCoreApplication.translate("Dialog", u"sobelov discretisaton:", None))
        self.label3.setText(QCoreApplication.translate("Dialog", u"sobelov weight:  ", None))
        self.label4.setText(QCoreApplication.translate("Dialog", u"normal discretisation:  ", None))
        self.label5.setText(QCoreApplication.translate("Dialog", u"normal weight:  ", None))
        self.label8.setText(QCoreApplication.translate("Dialog", u"max iterations:  ", None))
        self.label6.setText(QCoreApplication.translate("Dialog", u"max sub-iterations:  ", None))
        self.label7.setText(QCoreApplication.translate("Dialog", u"xtol:  ", None))
        self.label11.setText(QCoreApplication.translate("Dialog", u"kdtree args:  ", None))
        self.label10.setText(QCoreApplication.translate("Dialog", u"n closest points:  ", None))
        self.label12.setText(QCoreApplication.translate("Dialog", u"verbose:  ", None))
        self.label13.setText(QCoreApplication.translate("Dialog", u"fixed nodes:  ", None))
    # retranslateUi

