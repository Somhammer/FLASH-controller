import os, sys
import datetime

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

sys.path.append(BASE_PATH)

from mainwindow import MainWindow

if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)

    ex = MainWindow()
    sys.exit(app.exec())