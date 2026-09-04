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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

from zoomable_label import ZoomableLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(987, 903)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 941, 801))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Ubuntu Sans Mono"])
        font.setPointSize(38)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.label)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sourceDir = QLineEdit(self.layoutWidget)
        self.sourceDir.setObjectName(u"sourceDir")

        self.gridLayout.addWidget(self.sourceDir, 3, 1, 1, 1)

        self.sigmaSlider = QSlider(self.layoutWidget)
        self.sigmaSlider.setObjectName(u"sigmaSlider")
        self.sigmaSlider.setMinimum(1)
        self.sigmaSlider.setMaximum(10)
        self.sigmaSlider.setValue(2)
        self.sigmaSlider.setOrientation(Qt.Orientation.Horizontal)
        self.sigmaSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.sigmaSlider.setTickInterval(1)

        self.gridLayout.addWidget(self.sigmaSlider, 0, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.amountDisplay = QLineEdit(self.layoutWidget)
        self.amountDisplay.setObjectName(u"amountDisplay")
        self.amountDisplay.setAutoFillBackground(False)
        self.amountDisplay.setStyleSheet(u"")

        self.gridLayout.addWidget(self.amountDisplay, 1, 2, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.sourceFileBrowse = QPushButton(self.layoutWidget)
        self.sourceFileBrowse.setObjectName(u"sourceFileBrowse")

        self.gridLayout.addWidget(self.sourceFileBrowse, 3, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.targetFileBrowse = QPushButton(self.layoutWidget)
        self.targetFileBrowse.setObjectName(u"targetFileBrowse")

        self.gridLayout.addWidget(self.targetFileBrowse, 4, 2, 1, 1)

        self.targetDir = QLineEdit(self.layoutWidget)
        self.targetDir.setObjectName(u"targetDir")

        self.gridLayout.addWidget(self.targetDir, 4, 1, 1, 1)

        self.sigmaDisplay = QLineEdit(self.layoutWidget)
        self.sigmaDisplay.setObjectName(u"sigmaDisplay")
        self.sigmaDisplay.setAutoFillBackground(False)
        self.sigmaDisplay.setStyleSheet(u"")

        self.gridLayout.addWidget(self.sigmaDisplay, 0, 2, 1, 1)

        self.amountSlider = QSlider(self.layoutWidget)
        self.amountSlider.setObjectName(u"amountSlider")
        self.amountSlider.setMinimum(1)
        self.amountSlider.setMaximum(30)
        self.amountSlider.setValue(17)
        self.amountSlider.setOrientation(Qt.Orientation.Horizontal)
        self.amountSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.amountSlider.setTickInterval(1)

        self.gridLayout.addWidget(self.amountSlider, 1, 1, 1, 1)

        self.colorMap = QComboBox(self.layoutWidget)
        self.colorMap.setObjectName(u"colorMap")

        self.gridLayout.addWidget(self.colorMap, 2, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.originalImage = ZoomableLabel(self.layoutWidget)
        self.originalImage.setObjectName(u"originalImage")
        self.originalImage.setFrameShape(QFrame.Shape.NoFrame)
        self.originalImage.setFrameShadow(QFrame.Shadow.Sunken)
        self.originalImage.setLineWidth(2)
        self.originalImage.setMidLineWidth(2)

        self.gridLayout_2.addWidget(self.originalImage, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.newImage = ZoomableLabel(self.layoutWidget)
        self.newImage.setObjectName(u"newImage")
        self.newImage.setFrameShape(QFrame.Shape.NoFrame)
        self.newImage.setFrameShadow(QFrame.Shadow.Sunken)
        self.newImage.setLineWidth(2)
        self.newImage.setMidLineWidth(2)

        self.gridLayout_2.addWidget(self.newImage, 1, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 8)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        font1 = QFont()
        font1.setBold(True)
        self.label_11.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_11)

        self.status = QLabel(self.layoutWidget)
        self.status.setObjectName(u"status")
        font2 = QFont()
        font2.setItalic(False)
        self.status.setFont(font2)
        self.status.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.status)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 12)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.progressBar = QProgressBar(self.layoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.proceedButton = QPushButton(self.layoutWidget)
        self.proceedButton.setObjectName(u"proceedButton")
        self.proceedButton.setStyleSheet(u"background: rgb(246, 245, 244)")

        self.horizontalLayout.addWidget(self.proceedButton)

        self.cancelButton = QPushButton(self.layoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setStyleSheet(u"background: rgb(246, 245, 244)")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 987, 23))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sharper Image", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"(A tool for sharpening images)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Target directory:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Amount:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Source directory:", None))
        self.sourceFileBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sigma:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color filter:", None))
        self.targetFileBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.originalImage.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.newImage.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Before:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"After:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Progress:", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"Not started", None))
        self.proceedButton.setText(QCoreApplication.translate("MainWindow", u"Process Files Now!", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Main Menu", None))
    # retranslateUi

