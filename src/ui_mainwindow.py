# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.fameTuning = QFrame(self.centralwidget)
        self.fameTuning.setObjectName(u"fameTuning")
        self.fameTuning.setStyleSheet(u"border: 0px;\n"
"border-radius: 15px;\n"
"background-color: rgb(42, 42, 42);")
        self.fameTuning.setFrameShape(QFrame.Shape.NoFrame)
        self.fameTuning.setFrameShadow(QFrame.Shadow.Plain)
        self.fameTuning.setLineWidth(0)
        self.gridLayout = QGridLayout(self.fameTuning)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label1 = QLabel(self.fameTuning)
        self.label1.setObjectName(u"label1")
        self.label1.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Noto Sans KR"])
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setStyleSheet(u"color: rgb(153, 153, 153)")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label1, 1, 0, 1, 1)

        self.label3 = QLabel(self.fameTuning)
        self.label3.setObjectName(u"label3")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans KR"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label3.setFont(font1)
        self.label3.setStyleSheet(u"color: rgb(153, 153, 153)")

        self.gridLayout.addWidget(self.label3, 0, 0, 1, 2)

        self.label2 = QLabel(self.fameTuning)
        self.label2.setObjectName(u"label2")
        self.label2.setMaximumSize(QSize(16777215, 16777215))
        self.label2.setFont(font)
        self.label2.setStyleSheet(u"color: rgb(153, 153, 153)")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label2, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.fameTuning, 2, 1, 1, 1)

        self.frameGraph = QFrame(self.centralwidget)
        self.frameGraph.setObjectName(u"frameGraph")
        self.frameGraph.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(42, 42, 42);")
        self.frameGraph.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGraph.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGraph.setLineWidth(0)
        self.gridLayout_4 = QGridLayout(self.frameGraph)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.iconBeamStatusLight = QLabel(self.frameGraph)
        self.iconBeamStatusLight.setObjectName(u"iconBeamStatusLight")
        self.iconBeamStatusLight.setMinimumSize(QSize(280, 280))
        self.iconBeamStatusLight.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_4.addWidget(self.iconBeamStatusLight, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameGraph, 1, 0, 3, 1)

        self.pushTune = QPushButton(self.centralwidget)
        self.pushTune.setObjectName(u"pushTune")
        sizePolicy.setHeightForWidth(self.pushTune.sizePolicy().hasHeightForWidth())
        self.pushTune.setSizePolicy(sizePolicy)
        self.pushTune.setMinimumSize(QSize(90, 90))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans KR ExtraBold"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.pushTune.setFont(font2)
        self.pushTune.setStyleSheet(u"QPushButton {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(141, 255, 116);\n"
"  color: rgb(141, 255, 116);\n"
"}")

        self.gridLayout_3.addWidget(self.pushTune, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.frameKeypad = QFrame(self.centralwidget)
        self.frameKeypad.setObjectName(u"frameKeypad")
        self.frameKeypad.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(42, 42, 42);")
        self.frameKeypad.setFrameShape(QFrame.Shape.NoFrame)
        self.frameKeypad.setFrameShadow(QFrame.Shadow.Plain)
        self.frameKeypad.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.frameKeypad)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.pushNum0 = QPushButton(self.frameKeypad)
        self.pushNum0.setObjectName(u"pushNum0")
        sizePolicy.setHeightForWidth(self.pushNum0.sizePolicy().hasHeightForWidth())
        self.pushNum0.setSizePolicy(sizePolicy)
        self.pushNum0.setMinimumSize(QSize(60, 60))
        self.pushNum0.setMaximumSize(QSize(60, 70))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans KR"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.pushNum0.setFont(font3)
        self.pushNum0.setStyleSheet(u"QPushButton {\n"
"  border: 0px solid;\n"
"  border-radius: 6px;\n"
"  background-color: rgb(51, 51, 51);\n"
"  color: rgb(153, 153, 153);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}")

        self.gridLayout_2.addWidget(self.pushNum0, 3, 0, 1, 1)

        self.pushNum2 = QPushButton(self.frameKeypad)
        self.pushNum2.setObjectName(u"pushNum2")
        sizePolicy.setHeightForWidth(self.pushNum2.sizePolicy().hasHeightForWidth())
        self.pushNum2.setSizePolicy(sizePolicy)
        self.pushNum2.setMinimumSize(QSize(60, 60))
        self.pushNum2.setMaximumSize(QSize(60, 60))
        self.pushNum2.setFont(font3)
        self.pushNum2.setStyleSheet(u"QPushButton {\n"
"  border: 0px solid;\n"
"  border-radius: 6px;\n"
"  background-color: rgb(51, 51, 51);\n"
"  color: rgb(153, 153, 153);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}")

        self.gridLayout_2.addWidget(self.pushNum2, 2, 1, 1, 1)

        self.pushNum8 = QPushButton(self.frameKeypad)
        self.pushNum8.setObjectName(u"pushNum8")
        sizePolicy.setHeightForWidth(self.pushNum8.sizePolicy().hasHeightForWidth())
        self.pushNum8.setSizePolicy(sizePolicy)
        self.pushNum8.setMinimumSize(QSize(60, 60))
        self.pushNum8.setMaximumSize(QSize(60, 60))
        self.pushNum8.setFont(font3)
        self.pushNum8.setStyleSheet(u"QPushButton {\n"
"  border: 0px solid;\n"
"  border-radius: 6px;\n"
"  background-color: rgb(51, 51, 51);\n"
"  color: rgb(153, 153, 153);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}")

        self.gridLayout_2.addWidget(self.pushNum8, 0, 1, 1, 1)

        self.pushNum9 = QPushButton(self.frameKeypad)
        self.pushNum9.setObjectName(u"pushNum9")
        sizePolicy.setHeightForWidth(self.pushNum9.sizePolicy().hasHeightForWidth())
        self.pushNum9.setSizePolicy(sizePolicy)
        self.pushNum9.setMinimumSize(QSize(60, 60))
        self.pushNum9.setMaximumSize(QSize(60, 60))
        self.pushNum9.setFont(font3)
        self.pushNum9.setStyleSheet(u"QPushButton {\n"
"  border: 0px;\n"
"  border-radius: 15px;\n"
"  background-color: rgb(210, 210, 210);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: rgb(175, 175, 175);\n"
"}QPushButton {\n"
"  border: 0px solid;\n"
"  border-radius: 6px;\n"
"  background-color: rgb(51, 51, 51);\n"
"  color: rgb(153, 153, 153);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}")

        self.gridLayout_2.addWidget(self.pushNum9, 0, 2, 1, 1)

        self.pushNum1 = QPushButton(self.frameKeypad)
        self.pushNum1.setObjectName(u"pushNum1")
        sizePolicy.setHeightForWidth(self.pushNum1.sizePolicy().hasHeightForWidth())
        self.pushNum1.setSizePolicy(sizePolicy)
        self.pushNum1.setMinimumSize(QSize(60, 60))
        self.pushNum1.setMaximumSize(QSize(60, 60))
        self.pushNum1.setFont(font3)
        self.pushNum1.setStyleSheet(u"QPushButton {\n"
"  border: 0px solid;\n"
"  border-radius: 6px;\n"
"  background-color: rgb(51, 51, 51);\n"
"  color: rgb(153, 153, 153);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}")

        self.gridLayout_2.addWidget(self.pushNum1, 2, 0, 1, 1)

        self.pushNum4 = QPushButton(self.frameKeypad)
        self.pushNum4.setObjectName(u"pushNum4")
        sizePolicy.setHeightForWidth(self.pushNum4.sizePolicy().hasHeightForWidth())
        self.pushNum4.setSizePolicy(sizePolicy)
        self.pushNum4.setMinimumSize(QSize(60, 60))
        self.pushNum4.setMaximumSize(QSize(60, 60))
        self.pushNum4.setFont(font3)
        self.pushNum4.setStyleSheet(u"QPushButton {\n"
"  border: 0px solid;\n"
"  border-radius: 6px;\n"
"  background-color: rgb(51, 51, 51);\n"
"  color: rgb(153, 153, 153);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}")

        self.gridLayout_2.addWidget(self.pushNum4, 1, 0, 1, 1)

        self.pushDot = QPushButton(self.frameKeypad)
        self.pushDot.setObjectName(u"pushDot")
        self.pushDot.setMinimumSize(QSize(60, 60))
        self.pushDot.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamilies([u"Noto Sans KR ExtraBold"])
        font4.setPointSize(18)
        font4.setBold(True)
        self.pushDot.setFont(font4)
        self.pushDot.setStyleSheet(u"QPushButton {\n"
"  border: 0px solid;\n"
"  border-radius: 6px;\n"
"  background-color: rgb(51, 51, 51);\n"
"  color: rgb(153, 153, 153);\n"
"  padding-bottom: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}")

        self.gridLayout_2.addWidget(self.pushDot, 3, 1, 1, 1)

        self.pushDelete = QPushButton(self.frameKeypad)
        self.pushDelete.setObjectName(u"pushDelete")
        sizePolicy.setHeightForWidth(self.pushDelete.sizePolicy().hasHeightForWidth())
        self.pushDelete.setSizePolicy(sizePolicy)
        self.pushDelete.setMinimumSize(QSize(60, 60))
        self.pushDelete.setMaximumSize(QSize(60, 60))
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(True)
        self.pushDelete.setFont(font5)
        self.pushDelete.setStyleSheet(u"QPushButton {\n"
"  border: 0px solid;\n"
"  border-radius: 10px;\n"
"  background-color: rgb(51, 51, 51);\n"
"  color: rgb(153, 153, 153);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"  icon: url(':/icons/backspace_blue.png');\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/backspace_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushDelete.setIcon(icon)
        self.pushDelete.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.pushDelete, 3, 2, 1, 1)

        self.pushNum7 = QPushButton(self.frameKeypad)
        self.pushNum7.setObjectName(u"pushNum7")
        sizePolicy.setHeightForWidth(self.pushNum7.sizePolicy().hasHeightForWidth())
        self.pushNum7.setSizePolicy(sizePolicy)
        self.pushNum7.setMinimumSize(QSize(60, 60))
        self.pushNum7.setMaximumSize(QSize(60, 60))
        self.pushNum7.setFont(font3)
        self.pushNum7.setStyleSheet(u"QPushButton {\n"
"  border: 0px solid;\n"
"  border-radius: 6px;\n"
"  background-color: rgb(51, 51, 51);\n"
"  color: rgb(153, 153, 153);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}")

        self.gridLayout_2.addWidget(self.pushNum7, 0, 0, 1, 1)

        self.pushNum6 = QPushButton(self.frameKeypad)
        self.pushNum6.setObjectName(u"pushNum6")
        sizePolicy.setHeightForWidth(self.pushNum6.sizePolicy().hasHeightForWidth())
        self.pushNum6.setSizePolicy(sizePolicy)
        self.pushNum6.setMinimumSize(QSize(60, 60))
        self.pushNum6.setMaximumSize(QSize(60, 60))
        self.pushNum6.setFont(font3)
        self.pushNum6.setStyleSheet(u"QPushButton {\n"
"  border: 0px solid;\n"
"  border-radius: 6px;\n"
"  background-color: rgb(51, 51, 51);\n"
"  color: rgb(153, 153, 153);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}")

        self.gridLayout_2.addWidget(self.pushNum6, 1, 2, 1, 1)

        self.pushNum5 = QPushButton(self.frameKeypad)
        self.pushNum5.setObjectName(u"pushNum5")
        sizePolicy.setHeightForWidth(self.pushNum5.sizePolicy().hasHeightForWidth())
        self.pushNum5.setSizePolicy(sizePolicy)
        self.pushNum5.setMinimumSize(QSize(60, 60))
        self.pushNum5.setMaximumSize(QSize(60, 60))
        self.pushNum5.setFont(font3)
        self.pushNum5.setStyleSheet(u"QPushButton {\n"
"  border: 0px solid;\n"
"  border-radius: 6px;\n"
"  background-color: rgb(51, 51, 51);\n"
"  color: rgb(153, 153, 153);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}")

        self.gridLayout_2.addWidget(self.pushNum5, 1, 1, 1, 1)

        self.pushNum3 = QPushButton(self.frameKeypad)
        self.pushNum3.setObjectName(u"pushNum3")
        sizePolicy.setHeightForWidth(self.pushNum3.sizePolicy().hasHeightForWidth())
        self.pushNum3.setSizePolicy(sizePolicy)
        self.pushNum3.setMinimumSize(QSize(60, 60))
        self.pushNum3.setMaximumSize(QSize(60, 60))
        self.pushNum3.setFont(font3)
        self.pushNum3.setStyleSheet(u"QPushButton {\n"
"  border: 0px solid;\n"
"  border-radius: 6px;\n"
"  background-color: rgb(51, 51, 51);\n"
"  color: rgb(153, 153, 153);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}")

        self.gridLayout_2.addWidget(self.pushNum3, 2, 2, 1, 1)


        self.gridLayout_3.addWidget(self.frameKeypad, 1, 3, 3, 2)

        self.fameConnection = QFrame(self.centralwidget)
        self.fameConnection.setObjectName(u"fameConnection")
        self.fameConnection.setStyleSheet(u"border: 0px;\n"
"border-radius: 15px;\n"
"background-color: rgb(42, 42, 42);")
        self.fameConnection.setFrameShape(QFrame.Shape.NoFrame)
        self.fameConnection.setFrameShadow(QFrame.Shadow.Plain)
        self.fameConnection.setLineWidth(0)
        self.gridLayout_6 = QGridLayout(self.fameConnection)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.labelConnection = QLabel(self.fameConnection)
        self.labelConnection.setObjectName(u"labelConnection")
        self.labelConnection.setMaximumSize(QSize(16777215, 16777215))
        self.labelConnection.setFont(font)
        self.labelConnection.setStyleSheet(u"color: rgb(153, 153, 153)")
        self.labelConnection.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.labelConnection, 1, 1, 1, 1)

        self.iconConnectionLight = QLabel(self.fameConnection)
        self.iconConnectionLight.setObjectName(u"iconConnectionLight")
        font6 = QFont()
        font6.setFamilies([u"\ub098\ub214\uace0\ub515OTF ExtraBold"])
        font6.setPointSize(9)
        font6.setBold(True)
        self.iconConnectionLight.setFont(font6)
        self.iconConnectionLight.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.iconConnectionLight, 1, 0, 1, 1)

        self.labelPosition = QLabel(self.fameConnection)
        self.labelPosition.setObjectName(u"labelPosition")
        self.labelPosition.setFont(font1)
        self.labelPosition.setStyleSheet(u"color: rgb(153, 153, 153)")

        self.gridLayout_6.addWidget(self.labelPosition, 0, 0, 1, 2)


        self.gridLayout_3.addWidget(self.fameConnection, 1, 1, 1, 1)

        self.pushQuit = QPushButton(self.centralwidget)
        self.pushQuit.setObjectName(u"pushQuit")
        self.pushQuit.setMaximumSize(QSize(70, 70))
        self.pushQuit.setMouseTracking(True)
        self.pushQuit.setStyleSheet(u"QPushButton {\n"
"  border: 0px solid;\n"
"  background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  icon: url(':/icons/power_green.png');\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/power_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/power_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushQuit.setIcon(icon1)
        self.pushQuit.setIconSize(QSize(48, 48))
        self.pushQuit.setCheckable(True)
        self.pushQuit.setChecked(False)

        self.gridLayout_3.addWidget(self.pushQuit, 4, 4, 1, 1)

        self.pushStart = QPushButton(self.centralwidget)
        self.pushStart.setObjectName(u"pushStart")
        sizePolicy.setHeightForWidth(self.pushStart.sizePolicy().hasHeightForWidth())
        self.pushStart.setSizePolicy(sizePolicy)
        self.pushStart.setMinimumSize(QSize(90, 90))
        self.pushStart.setFont(font2)
        self.pushStart.setStyleSheet(u"QPushButton {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(141, 255, 116);\n"
"  color: rgb(141, 255, 116);\n"
"}")

        self.gridLayout_3.addWidget(self.pushStart, 3, 2, 1, 1)

        self.labelBeamStatus = QLabel(self.centralwidget)
        self.labelBeamStatus.setObjectName(u"labelBeamStatus")
        font7 = QFont()
        font7.setFamilies([u"Noto Sans KR ExtraBold"])
        font7.setPointSize(34)
        font7.setBold(True)
        self.labelBeamStatus.setFont(font7)
        self.labelBeamStatus.setStyleSheet(u"color: rgb(71, 111, 243)")
        self.labelBeamStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.labelBeamStatus, 0, 0, 1, 1)

        self.fameTime = QFrame(self.centralwidget)
        self.fameTime.setObjectName(u"fameTime")
        self.fameTime.setStyleSheet(u"border: 0px;\n"
"border-radius: 15px;\n"
"background-color: rgb(42, 42, 42);")
        self.fameTime.setFrameShape(QFrame.Shape.NoFrame)
        self.fameTime.setFrameShadow(QFrame.Shadow.Plain)
        self.fameTime.setLineWidth(0)
        self.gridLayout_7 = QGridLayout(self.fameTime)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.labelUnit = QLabel(self.fameTime)
        self.labelUnit.setObjectName(u"labelUnit")
        font8 = QFont()
        font8.setFamilies([u"Noto Sans KR"])
        font8.setPointSize(16)
        font8.setBold(True)
        self.labelUnit.setFont(font8)
        self.labelUnit.setStyleSheet(u"color: rgb(85, 85, 85)")

        self.gridLayout_7.addWidget(self.labelUnit, 1, 1, 1, 1)

        self.lineTime = QLineEdit(self.fameTime)
        self.lineTime.setObjectName(u"lineTime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineTime.sizePolicy().hasHeightForWidth())
        self.lineTime.setSizePolicy(sizePolicy1)
        font9 = QFont()
        font9.setFamilies([u"\ub098\ub214\uc2a4\ud018\uc5b4 ExtraBold"])
        font9.setPointSize(16)
        font9.setBold(True)
        self.lineTime.setFont(font9)
        self.lineTime.setStyleSheet(u"QLineEdit {\n"
"border: 0px;\n"
"border-radius: 10px;\n"
"background-color: rgb(42, 42, 42);\n"
"color: rgb(221, 221, 221);\n"
"}\n"
"QLineEdit:hover {\n"
"color:rgb(71, 111, 243);\n"
"}")

        self.gridLayout_7.addWidget(self.lineTime, 1, 0, 1, 1)

        self.labelTime = QLabel(self.fameTime)
        self.labelTime.setObjectName(u"labelTime")
        self.labelTime.setFont(font1)
        self.labelTime.setStyleSheet(u"color: rgb(153, 153, 153)")

        self.gridLayout_7.addWidget(self.labelTime, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.fameTime, 3, 1, 1, 1)

        self.pushConnect = QPushButton(self.centralwidget)
        self.pushConnect.setObjectName(u"pushConnect")
        sizePolicy.setHeightForWidth(self.pushConnect.sizePolicy().hasHeightForWidth())
        self.pushConnect.setSizePolicy(sizePolicy)
        self.pushConnect.setMinimumSize(QSize(90, 90))
        self.pushConnect.setFont(font2)
        self.pushConnect.setStyleSheet(u"QPushButton {\n"
"  border: 2px solid rgb(71, 111, 243);\n"
"  border-radius: 10px;\n"
"  background-color: rgb(33, 36, 44);\n"
"  color: rgb(71, 111, 243);\n"
"}\n"
"QPushButton:hover {\n"
"  border: 2px solid rgb(141, 255, 116);\n"
"  color: rgb(141, 255, 116);\n"
"}")

        self.gridLayout_3.addWidget(self.pushConnect, 1, 2, 1, 1)

        self.labelLogo = QLabel(self.centralwidget)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setPixmap(QPixmap(u":/icons/ncc.png"))
        self.labelLogo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.labelLogo, 0, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"Press \"Tune\" button", None))
        self.label3.setText(QCoreApplication.translate("MainWindow", u"Beam tuning", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"before beam on.", None))
        self.iconBeamStatusLight.setText("")
        self.pushTune.setText(QCoreApplication.translate("MainWindow", u"Tune", None))
        self.pushNum0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushNum2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushNum8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushNum9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushNum1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushNum4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushDot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushDelete.setText("")
        self.pushNum7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushNum6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushNum5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushNum3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.labelConnection.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.iconConnectionLight.setText("")
        self.labelPosition.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.pushQuit.setText("")
        self.pushStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.labelBeamStatus.setText(QCoreApplication.translate("MainWindow", u"BEAM OFF", None))
        self.labelUnit.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.lineTime.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelTime.setText(QCoreApplication.translate("MainWindow", u"Beam time", None))
        self.pushConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.labelLogo.setText("")
    # retranslateUi

