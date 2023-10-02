# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormCadastroAtor.ui'
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
    QWidget)

class Ui_FormCadastroAtor(object):
    def setupUi(self, FormCadastroAtor):
        if not FormCadastroAtor.objectName():
            FormCadastroAtor.setObjectName(u"FormCadastroAtor")
        FormCadastroAtor.resize(465, 322)
        self.horizontalLayoutWidget = QWidget(FormCadastroAtor)
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

        self.formLayoutWidget = QWidget(FormCadastroAtor)
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


        self.retranslateUi(FormCadastroAtor)

        QMetaObject.connectSlotsByName(FormCadastroAtor)
    # setupUi

    def retranslateUi(self, FormCadastroAtor):
        FormCadastroAtor.setWindowTitle(QCoreApplication.translate("FormCadastroAtor", u"Dialog", None))
        self.btnSalvar.setText(QCoreApplication.translate("FormCadastroAtor", u"Salvar", None))
        self.btnCancelar.setText(QCoreApplication.translate("FormCadastroAtor", u"Cancelar", None))
        self.label.setText(QCoreApplication.translate("FormCadastroAtor", u"Nome:", None))
    # retranslateUi

