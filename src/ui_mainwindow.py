# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(846, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushStart = QPushButton(self.centralwidget)
        self.pushStart.setObjectName(u"pushStart")
        sizePolicy.setHeightForWidth(self.pushStart.sizePolicy().hasHeightForWidth())
        self.pushStart.setSizePolicy(sizePolicy)
        self.pushStart.setMinimumSize(QSize(90, 90))
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uace0\ub515"])
        font.setPointSize(12)
        self.pushStart.setFont(font)

        self.gridLayout_4.addWidget(self.pushStart, 4, 4, 1, 1)

        self.pushTune = QPushButton(self.centralwidget)
        self.pushTune.setObjectName(u"pushTune")
        sizePolicy.setHeightForWidth(self.pushTune.sizePolicy().hasHeightForWidth())
        self.pushTune.setSizePolicy(sizePolicy)
        self.pushTune.setMinimumSize(QSize(90, 90))
        self.pushTune.setFont(font)

        self.gridLayout_4.addWidget(self.pushTune, 3, 4, 1, 1)

        self.groupTunning = QGroupBox(self.centralwidget)
        self.groupTunning.setObjectName(u"groupTunning")
        self.groupTunning.setMinimumSize(QSize(0, 90))
        self.groupTunning.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupTunning)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelTuneWarning = QLabel(self.groupTunning)
        self.labelTuneWarning.setObjectName(u"labelTuneWarning")
        font1 = QFont()
        font1.setFamilies([u"\ub098\ub214\uace0\ub515"])
        font1.setPointSize(11)
        self.labelTuneWarning.setFont(font1)
        self.labelTuneWarning.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelTuneWarning, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupTunning)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupTunning, 3, 3, 1, 1)

        self.groupKeypad = QGroupBox(self.centralwidget)
        self.groupKeypad.setObjectName(u"groupKeypad")
        self.groupKeypad.setFont(font)
        self.gridLayout_3 = QGridLayout(self.groupKeypad)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushNum1 = QPushButton(self.groupKeypad)
        self.pushNum1.setObjectName(u"pushNum1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushNum1.sizePolicy().hasHeightForWidth())
        self.pushNum1.setSizePolicy(sizePolicy1)
        self.pushNum1.setFont(font)

        self.gridLayout_3.addWidget(self.pushNum1, 2, 0, 1, 1)

        self.pushNum9 = QPushButton(self.groupKeypad)
        self.pushNum9.setObjectName(u"pushNum9")
        sizePolicy1.setHeightForWidth(self.pushNum9.sizePolicy().hasHeightForWidth())
        self.pushNum9.setSizePolicy(sizePolicy1)
        self.pushNum9.setFont(font)

        self.gridLayout_3.addWidget(self.pushNum9, 0, 2, 1, 1)

        self.pushNum7 = QPushButton(self.groupKeypad)
        self.pushNum7.setObjectName(u"pushNum7")
        sizePolicy1.setHeightForWidth(self.pushNum7.sizePolicy().hasHeightForWidth())
        self.pushNum7.setSizePolicy(sizePolicy1)
        self.pushNum7.setFont(font)

        self.gridLayout_3.addWidget(self.pushNum7, 0, 0, 1, 1)

        self.pushNum6 = QPushButton(self.groupKeypad)
        self.pushNum6.setObjectName(u"pushNum6")
        sizePolicy1.setHeightForWidth(self.pushNum6.sizePolicy().hasHeightForWidth())
        self.pushNum6.setSizePolicy(sizePolicy1)
        self.pushNum6.setFont(font)

        self.gridLayout_3.addWidget(self.pushNum6, 1, 2, 1, 1)

        self.pushNum0 = QPushButton(self.groupKeypad)
        self.pushNum0.setObjectName(u"pushNum0")
        sizePolicy1.setHeightForWidth(self.pushNum0.sizePolicy().hasHeightForWidth())
        self.pushNum0.setSizePolicy(sizePolicy1)
        self.pushNum0.setFont(font)

        self.gridLayout_3.addWidget(self.pushNum0, 3, 0, 1, 1)

        self.pushNum8 = QPushButton(self.groupKeypad)
        self.pushNum8.setObjectName(u"pushNum8")
        sizePolicy1.setHeightForWidth(self.pushNum8.sizePolicy().hasHeightForWidth())
        self.pushNum8.setSizePolicy(sizePolicy1)
        self.pushNum8.setFont(font)

        self.gridLayout_3.addWidget(self.pushNum8, 0, 1, 1, 1)

        self.pushNum3 = QPushButton(self.groupKeypad)
        self.pushNum3.setObjectName(u"pushNum3")
        sizePolicy1.setHeightForWidth(self.pushNum3.sizePolicy().hasHeightForWidth())
        self.pushNum3.setSizePolicy(sizePolicy1)
        self.pushNum3.setFont(font)

        self.gridLayout_3.addWidget(self.pushNum3, 2, 2, 1, 1)

        self.pushNum2 = QPushButton(self.groupKeypad)
        self.pushNum2.setObjectName(u"pushNum2")
        sizePolicy1.setHeightForWidth(self.pushNum2.sizePolicy().hasHeightForWidth())
        self.pushNum2.setSizePolicy(sizePolicy1)
        self.pushNum2.setFont(font)

        self.gridLayout_3.addWidget(self.pushNum2, 2, 1, 1, 1)

        self.pushNum4 = QPushButton(self.groupKeypad)
        self.pushNum4.setObjectName(u"pushNum4")
        sizePolicy1.setHeightForWidth(self.pushNum4.sizePolicy().hasHeightForWidth())
        self.pushNum4.setSizePolicy(sizePolicy1)
        self.pushNum4.setFont(font)

        self.gridLayout_3.addWidget(self.pushNum4, 1, 0, 1, 1)

        self.pushNum5 = QPushButton(self.groupKeypad)
        self.pushNum5.setObjectName(u"pushNum5")
        sizePolicy1.setHeightForWidth(self.pushNum5.sizePolicy().hasHeightForWidth())
        self.pushNum5.setSizePolicy(sizePolicy1)
        self.pushNum5.setFont(font)

        self.gridLayout_3.addWidget(self.pushNum5, 1, 1, 1, 1)

        self.pushDelete = QPushButton(self.groupKeypad)
        self.pushDelete.setObjectName(u"pushDelete")
        sizePolicy1.setHeightForWidth(self.pushDelete.sizePolicy().hasHeightForWidth())
        self.pushDelete.setSizePolicy(sizePolicy1)
        self.pushDelete.setFont(font)

        self.gridLayout_3.addWidget(self.pushDelete, 3, 2, 1, 1)

        self.pushDot = QPushButton(self.groupKeypad)
        self.pushDot.setObjectName(u"pushDot")
        sizePolicy1.setHeightForWidth(self.pushDot.sizePolicy().hasHeightForWidth())
        self.pushDot.setSizePolicy(sizePolicy1)
        self.pushDot.setFont(font)

        self.gridLayout_3.addWidget(self.pushDot, 3, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupKeypad, 1, 5, 4, 3)

        self.groupTime = QGroupBox(self.centralwidget)
        self.groupTime.setObjectName(u"groupTime")
        self.groupTime.setMinimumSize(QSize(0, 90))
        self.groupTime.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupTime)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineTime = QLineEdit(self.groupTime)
        self.lineTime.setObjectName(u"lineTime")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineTime.sizePolicy().hasHeightForWidth())
        self.lineTime.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"\ub098\ub214\uace0\ub515"])
        font2.setPointSize(16)
        self.lineTime.setFont(font2)

        self.gridLayout_5.addWidget(self.lineTime, 0, 0, 1, 1)

        self.labelUnit = QLabel(self.groupTime)
        self.labelUnit.setObjectName(u"labelUnit")
        self.labelUnit.setMaximumSize(QSize(50, 16777215))
        self.labelUnit.setFont(font)

        self.gridLayout_5.addWidget(self.labelUnit, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupTime, 4, 3, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 6, 6, 1, 1)

        self.iconBeamStatusLight = QLabel(self.centralwidget)
        self.iconBeamStatusLight.setObjectName(u"iconBeamStatusLight")
        self.iconBeamStatusLight.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_4.addWidget(self.iconBeamStatusLight, 2, 0, 3, 3)

        self.pushQuit = QPushButton(self.centralwidget)
        self.pushQuit.setObjectName(u"pushQuit")
        sizePolicy1.setHeightForWidth(self.pushQuit.sizePolicy().hasHeightForWidth())
        self.pushQuit.setSizePolicy(sizePolicy1)
        self.pushQuit.setFont(font)

        self.gridLayout_4.addWidget(self.pushQuit, 6, 7, 1, 1)

        self.labelBeamStatus = QLabel(self.centralwidget)
        self.labelBeamStatus.setObjectName(u"labelBeamStatus")
        font3 = QFont()
        font3.setFamilies([u"\ub358\ud30c \ube44\ud2b8\ube44\ud2b8\uccb4 TTF"])
        font3.setPointSize(34)
        self.labelBeamStatus.setFont(font3)
        self.labelBeamStatus.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.labelBeamStatus, 1, 0, 1, 3)

        self.groupConnection = QGroupBox(self.centralwidget)
        self.groupConnection.setObjectName(u"groupConnection")
        self.groupConnection.setMinimumSize(QSize(0, 90))
        self.groupConnection.setFont(font)
        self.gridLayout = QGridLayout(self.groupConnection)
        self.gridLayout.setObjectName(u"gridLayout")
        self.iconConnectionLight = QLabel(self.groupConnection)
        self.iconConnectionLight.setObjectName(u"iconConnectionLight")
        self.iconConnectionLight.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.iconConnectionLight, 0, 0, 1, 1)

        self.labelConnection = QLabel(self.groupConnection)
        self.labelConnection.setObjectName(u"labelConnection")
        self.labelConnection.setMaximumSize(QSize(16777215, 16777215))
        self.labelConnection.setFont(font)

        self.gridLayout.addWidget(self.labelConnection, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupConnection, 2, 3, 1, 1)

        self.pushConnect = QPushButton(self.centralwidget)
        self.pushConnect.setObjectName(u"pushConnect")
        sizePolicy.setHeightForWidth(self.pushConnect.sizePolicy().hasHeightForWidth())
        self.pushConnect.setSizePolicy(sizePolicy)
        self.pushConnect.setMinimumSize(QSize(90, 90))
        self.pushConnect.setFont(font)

        self.gridLayout_4.addWidget(self.pushConnect, 2, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushTune.setText(QCoreApplication.translate("MainWindow", u"Tune", None))
        self.groupTunning.setTitle(QCoreApplication.translate("MainWindow", u"Beam Tuning", None))
        self.labelTuneWarning.setText(QCoreApplication.translate("MainWindow", u"Press \"Tune\" button", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"before beam tunning.", None))
        self.groupKeypad.setTitle(QCoreApplication.translate("MainWindow", u"Keypad", None))
        self.pushNum1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushNum9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushNum7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushNum6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushNum0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushNum8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushNum3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushNum2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushNum4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushNum5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushDot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.groupTime.setTitle(QCoreApplication.translate("MainWindow", u"Beam time", None))
        self.labelUnit.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.label.setText("")
        self.iconBeamStatusLight.setText("")
        self.pushQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.labelBeamStatus.setText(QCoreApplication.translate("MainWindow", u"BEAM OFF", None))
        self.groupConnection.setTitle(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.iconConnectionLight.setText("")
        self.labelConnection.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.pushConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
    # retranslateUi

