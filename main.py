from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from zkToolsGui import Ui_ZKTools
import os
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))


class MyWindow(QMainWindow, Ui_ZKTools):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())