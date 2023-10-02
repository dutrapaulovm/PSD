# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormCadastroTeatro.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_FormCadastroTeatro(object):
    def setupUi(self, FormCadastroTeatro):
        if not FormCadastroTeatro.objectName():
            FormCadastroTeatro.setObjectName(u"FormCadastroTeatro")
        FormCadastroTeatro.resize(465, 322)
        self.horizontalLayoutWidget = QWidget(FormCadastroTeatro)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 160, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnSalvar = QPushButton(self.horizontalLayoutWidget)
        self.btnSalvar.setObjectName(u"btnSalvar")

        self.horizontalLayout.addWidget(self.btnSalvar)

        self.btnCancelar = QPushButton(self.horizontalLayoutWidget)
        self.btnCancelar.setObjectName(u"btnCancelar")

        self.horizontalLayout.addWidget(self.btnCancelar)

        self.formLayoutWidget = QWidget(FormCadastroTeatro)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 40, 461, 191))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.edtNome = QLineEdit(self.formLayoutWidget)
        self.edtNome.setObjectName(u"edtNome")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edtNome)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.spnCapAssentos = QSpinBox(self.formLayoutWidget)
        self.spnCapAssentos.setObjectName(u"spnCapAssentos")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spnCapAssentos)


        self.retranslateUi(FormCadastroTeatro)

        QMetaObject.connectSlotsByName(FormCadastroTeatro)
    # setupUi

    def retranslateUi(self, FormCadastroTeatro):
        FormCadastroTeatro.setWindowTitle(QCoreApplication.translate("FormCadastroTeatro", u"Dialog", None))
        self.btnSalvar.setText(QCoreApplication.translate("FormCadastroTeatro", u"Salvar", None))
        self.btnCancelar.setText(QCoreApplication.translate("FormCadastroTeatro", u"Cancelar", None))
        self.label.setText(QCoreApplication.translate("FormCadastroTeatro", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("FormCadastroTeatro", u"Cap. Assentos:", None))
    # retranslateUi

