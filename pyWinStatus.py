import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./Qt5ui/pyWinMacro.ui")[0]

class statusWindow(QMainWindow, form_class):
    """
        pyQt basic Class
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle('pyWinMacro')
        self.setupUi(self)

    def label_update(self, labelNum, msg):
        if labelNum == 0:
            self.InfoLabel0.setText(msg)
        else:
            raise NameError('Cannot Find labelNum')

class pyWinStatus(statusWindow):
    """
        Status Control Main Class
    """
    def __init__(self):
        super().__init__()

    def setMousePos(self, pos):
        msg = "Mouse Pos (%3d, %3d)" % pos
        self.label_update(0, msg)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    winStatus = pyWinStatus()
    winStatus.show()
    winStatus.label_update(0, "test")
    app.exec_()