import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class ventanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ventanaPrincipal()
    gui.show()
    sys.exit(app.exec())