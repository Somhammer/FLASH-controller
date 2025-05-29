import os, sys
import platform

#import serial.tools.list_ports
#import serial

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtSvgWidgets import QSvgWidget

from ui_mainwindow import Ui_MainWindow
from qled import QLed

DISCONNECTED = 10001
CONNECTED = 10002
OFFBEAM = 20001
ONBEAM = 20002

class MainThread(QThread):
    finished = Signal()
    return_board_status = Signal(int)
    return_beam_status = Signal(int)
    return_port_list = Signal(list)

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.board_status = DISCONNECTED
        self.beam_status = OFFBEAM
        self.beam_time = 0
        self.has_error = False
        self.set_actions()
        
    def set_actions(self):
        self.return_board_status.connect(self.window.receive_board_status)
        self.return_beam_status.connect(self.window.receive_beam_status)
        self.finished.connect(self.window.on_beam_finished)

    def run(self):
        while not self.isInterruptionRequested():
            if self.beam_status == OFFBEAM: break
            try:
                self.turn_on_and_off_voltage()
            except:
                self.has_error = True

        self.return_beam_status.emit(self.beam_status)
        self.finished.emit(self.has_error)

    def start(self):
        if not self.isRunning():
            super().start()

    @Slot(bool)
    def receive_connect(self, on_connection):
        try:
            if on_connection:
                self.board_status = CONNECTED
            else:
                self.board_status = DISCONNECTED
        except:
            self.board_status = DISCONNECTED
        finally:
            self.return_board_status.emit(self.board_status)

    @Slot(bool)
    def receive_tune(self, on_tunning):
        if self.board_status == CONNECTED:
            if on_tunning: self.beam_status = ONBEAM
            else: self.beam_status = OFFBEAM
        else:
            self.beam_status = OFFBEAM

        self.return_beam_status.emit(self.beam_status)
        self.start()

    @Slot(bool, float)
    def receive_start(self, on_beam, beam_time):
        if self.board_status == CONNECTED:
            if on_beam: self.beam_status = ONBEAM
            else: self.beam_status = OFFBEAM
        else:
            self.beam_status = OFFBEAM
        self.beam_time = beam_time
        self.return_beam_status.emit(self.beam_status)
        self.start()

    def turn_on_and_off_voltage(self):
        pass

class MainWindow(QMainWindow, Ui_MainWindow):
    request_connect = Signal(bool)
    request_tune = Signal(bool)
    request_start = Signal(bool, float)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        if platform.system() == "Windows":
            self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        else:
            self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

        self.mthread = MainThread(self)
        self.connection_status = DISCONNECTED
        self.beam_status = OFFBEAM

        self.on_connection = False
        self.on_tunning = False
        self.on_beam = False

        self.setFixedSize(800, 480)
        self.set_icons()
        self.set_actions()
        self.show()

    def set_icons(self):
        icon_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'icons')
        iconNCC = QIcon(os.path.join(icon_dir, 'ncc.png'))

        #self.led = QLed(self)#, onColour=QLed.Grey, shape=QLed.shapes.Rounds)
        self.ledBeamStatus = QLed(self.iconBeamStatusLight, onColour=QLed.Red, shape=QLed.Circle)
        self.ledBeamStatus.value = True     
        self.iconBeamStatusLight.setFixedSize(216,216)
        self.ledBeamStatus.setFixedSize(self.iconBeamStatusLight.sizeHint())
        self.ledConnectionStatus = QLed(self.iconConnectionLight, onColour=QLed.Red, shape=QLed.Circle)
        self.ledConnectionStatus.value = True     
        self.iconConnectionLight.setFixedSize(30,30)
        self.ledConnectionStatus.setFixedSize(self.iconConnectionLight.sizeHint())

    def set_actions(self):
        self.request_connect.connect(self.mthread.receive_connect)
        self.request_tune.connect(self.mthread.receive_tune)
        self.request_start.connect(self.mthread.receive_start)

        self.pushConnect.clicked.connect(self.connect_to_board)
        self.pushTune.clicked.connect(self.tune_on_and_off_beam)
        self.pushStart.clicked.connect(self.turn_on_and_off_beam)
        self.pushQuit.clicked.connect(self.close)

        # Keypad
        self.pushNum0.clicked.connect(lambda: self.modify_beam_time(self.pushNum0))
        self.pushNum1.clicked.connect(lambda: self.modify_beam_time(self.pushNum1))
        self.pushNum2.clicked.connect(lambda: self.modify_beam_time(self.pushNum2))
        self.pushNum3.clicked.connect(lambda: self.modify_beam_time(self.pushNum3))
        self.pushNum4.clicked.connect(lambda: self.modify_beam_time(self.pushNum4))
        self.pushNum5.clicked.connect(lambda: self.modify_beam_time(self.pushNum5))
        self.pushNum6.clicked.connect(lambda: self.modify_beam_time(self.pushNum6))
        self.pushNum7.clicked.connect(lambda: self.modify_beam_time(self.pushNum7))
        self.pushNum8.clicked.connect(lambda: self.modify_beam_time(self.pushNum8))
        self.pushNum9.clicked.connect(lambda: self.modify_beam_time(self.pushNum9))
        self.pushDelete.clicked.connect(lambda: self.modify_beam_time(self.pushDelete))
        self.pushDot.clicked.connect(lambda: self.modify_beam_time(self.pushDot))

    def update(self):
        if self.connection_status == CONNECTED:
            self.ledConnectionStatus.m_onColour = QLed.Green
            self.ledConnectionStatus.value = True
            self.labelConnection.setText("Connected")
            self.pushConnect.setText("Disconnect")
        else:  
            self.ledConnectionStatus.m_onColour = QLed.Red
            self.ledConnectionStatus.value = True
            self.labelConnection.setText("Disconnected")
            self.pushConnect.setText("Connect")

        if self.beam_status == ONBEAM:
            self.ledBeamStatus.m_onColour = QLed.Green
            self.ledBeamStatus.value = True
            self.labelBeamStatus.setText("BEAM ON")
            if self.on_tunning:
                self.pushTune.setText("Terminate")
            if self.on_beam:
                self.pushStart.setText("Stop")
        else:
            self.ledBeamStatus.m_onColour = QLed.Red
            self.ledBeamStatus.value = True
            self.labelBeamStatus.setText("BEAM OFF")
            self.pushTune.setText("Tune")
            self.pushStart.setText("Start")

    def connect_to_board(self):
        self.on_connection = not self.on_connection
        self.request_connect.emit(self.on_connection)
        self.update()

    def tune_on_and_off_beam(self):
        self.on_tunning = not self.on_tunning
        self.request_tune.emit(self.on_tunning)
        self.update()

    def turn_on_and_off_beam(self):
        if self.lineTime.text() == "" or float(self.lineTime.text()) <= 0.0 : return
        if self.on_tunning: return
        self.on_beam = not self.on_beam
        self.request_start.emit(self.on_beam, float(self.lineTime.text()))
        self.update()

    def modify_beam_time(self, button :QPushButton):
        full_text = self.lineTime.text()
        text = button.text()
        if button == self.pushDelete:
            if full_text == "": return
            self.lineTime.setText(self.lineTime.text()[:-1])
        elif button == self.pushDot:
            if len(full_text.split(".")) > 1: return
            self.lineTime.setText(self.lineTime.text()+text)
        else:
            self.lineTime.setText(self.lineTime.text()+text)

    def on_beam_finished(self):
        if self.mthread.has_error:
            QMessageBox.critical(self, "Error", "An error occurred during beam on.")

    @Slot(int)
    def receive_board_status(self, status):
        self.connection_status = status
        if self.connection_status != CONNECTED:
            self.on_connection = False
        self.update()

    @Slot(int)
    def receive_beam_status(self, status):
        self.beam_status = status
        if self.beam_status != ONBEAM:
            self.on_tunning = False
            self.on_beam = False
        self.update()

    @Slot()
    def receive_thread_is_terminated(self):
        pass
        #self.close()