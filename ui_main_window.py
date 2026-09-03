# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(793, 825)
        font = QFont()
        font.setBold(False)
        Dialog.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 10, 561, 62))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Ubuntu Sans Mono"])
        font1.setPointSize(38)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 80, 203, 18))
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 120, 731, 661))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.sourceFileBrowse = QPushButton(self.widget)
        self.sourceFileBrowse.setObjectName(u"sourceFileBrowse")

        self.gridLayout.addWidget(self.sourceFileBrowse, 2, 2, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.targetFileBrowse = QPushButton(self.widget)
        self.targetFileBrowse.setObjectName(u"targetFileBrowse")

        self.gridLayout.addWidget(self.targetFileBrowse, 3, 2, 1, 1)

        self.sigmaSlider = QSlider(self.widget)
        self.sigmaSlider.setObjectName(u"sigmaSlider")
        self.sigmaSlider.setMinimum(1)
        self.sigmaSlider.setMaximum(5)
        self.sigmaSlider.setValue(2)
        self.sigmaSlider.setOrientation(Qt.Orientation.Horizontal)
        self.sigmaSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.sigmaSlider.setTickInterval(1)

        self.gridLayout.addWidget(self.sigmaSlider, 0, 1, 1, 1)

        self.amontSlider = QSlider(self.widget)
        self.amontSlider.setObjectName(u"amontSlider")
        self.amontSlider.setMinimum(1)
        self.amontSlider.setMaximum(30)
        self.amontSlider.setValue(17)
        self.amontSlider.setOrientation(Qt.Orientation.Horizontal)
        self.amontSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.amontSlider.setTickInterval(1)

        self.gridLayout.addWidget(self.amontSlider, 1, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.sourceDir = QLineEdit(self.widget)
        self.sourceDir.setObjectName(u"sourceDir")

        self.gridLayout.addWidget(self.sourceDir, 2, 1, 1, 1)

        self.targetDir = QLineEdit(self.widget)
        self.targetDir.setObjectName(u"targetDir")

        self.gridLayout.addWidget(self.targetDir, 3, 1, 1, 1)

        self.sigmaDisplay = QLineEdit(self.widget)
        self.sigmaDisplay.setObjectName(u"sigmaDisplay")
        self.sigmaDisplay.setAutoFillBackground(False)
        self.sigmaDisplay.setStyleSheet(u" background: rgb(246, 245, 244); \n"
"")

        self.gridLayout.addWidget(self.sigmaDisplay, 0, 2, 1, 1)

        self.amountDisplay = QLineEdit(self.widget)
        self.amountDisplay.setObjectName(u"amountDisplay")
        self.amountDisplay.setAutoFillBackground(False)
        self.amountDisplay.setStyleSheet(u" background: rgb(246, 245, 244); \n"
"")

        self.gridLayout.addWidget(self.amountDisplay, 1, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)

        self.originalImage = QLabel(self.widget)
        self.originalImage.setObjectName(u"originalImage")
        self.originalImage.setFrameShape(QFrame.Shape.Box)
        self.originalImage.setMidLineWidth(1)

        self.gridLayout_2.addWidget(self.originalImage, 1, 0, 1, 1)

        self.newImage = QLabel(self.widget)
        self.newImage.setObjectName(u"newImage")
        self.newImage.setFrameShape(QFrame.Shape.Box)
        self.newImage.setMidLineWidth(1)

        self.gridLayout_2.addWidget(self.newImage, 1, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 6)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"The Sharper Image", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"(A tool for sharpening images)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Amount:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Target directory:", None))
        self.sourceFileBrowse.setText(QCoreApplication.translate("Dialog", u"Browse...", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Sigma:", None))
        self.targetFileBrowse.setText(QCoreApplication.translate("Dialog", u"Browse...", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Source directory:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Before:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"After:", None))
        self.originalImage.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.newImage.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Progress:", None))
    # retranslateUi

