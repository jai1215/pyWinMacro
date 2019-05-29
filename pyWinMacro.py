# import numpy as np
# from PIL import ImageGrab
# import cv2
from PyQt5.QtWidgets import *
import pyWinStatus
import threading
import sys

class pyWinMacro():
    def __init__(self):
        self.app = self.initGui()
        self.initThread()

    def initGui(self):
        app = QApplication(sys.argv)
        winStatus = pyWinStatus.pyWinStatus()
        winStatus.show()
        winStatus.label_update(0, "test_main")
        return app
    
    def initThread(self):
        tGui = threading.Thread(target=self.runGui)
        tMonitor = threading.Thread(target=self.runMonitor)
        tGui.start()
        tMonitor.start()

    def runGui(self):
        print("@I : Gui Start")
        self.app.exec_()

    def runMonitor(self):
        print("@I : Monitor Start")

if __name__ == "__main__":
    macro = pyWinMacro()
    print("run")

    