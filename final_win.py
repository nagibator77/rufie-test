from instr import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.unitUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def unitUI(self):
        self.index=QLabel(txt_index)
        self.working=QLabel(txt_workheart)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.working, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

app=QApplication([])
mw=FinalWin()
mw.set_appear()
mw.unitUI()
mw.show()

app.exec_()
