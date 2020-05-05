import sys
from PyQt5.QtWidgets import *
from PyQt5 import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        import random
        self.Menu = QLabel(' 같 은 그 림 찾 기', self)
        self.Menu.setGeometry(QtCore.QRect(50, 50, 50, 50))
        self.Menu.setFont(QtGui.QFont("궁서", 25))
        self.Menu.move(0, 20)
        self.Menu.resize(400, 100)

        self.card_number = []
        a_card = ['[!]','[!]','[@]','[@]','[#]','[#]','[$]','[$]','[%]','[%]','[&]','[&]','[*]','[*]','[~]','[~]']
        b_card = ['[?]','[?]','[?]','[?]','[?]','[?]','[?]','[?]','[?]','[?]','[?]','[?]','[?]','[?]','[?]','[?]']
        random.shuffle(a_card)

        for a in range(4):
            for b in range(1, 5):
                self.card_number.append(QPushButton(a_card[(4*a)+b-1], self))
                self.card_number[(4*a)+b-1].move(30+(90*a) , 60+(70*b))
                self.card_number[(4*a)+b-1].resize(70, 60)
                self.card_number[(4*a)+b-1].setStyleSheet('background: orange')


        self.name_number = []
        name = ['Player1[   ]', 'Player2[   ]']
        for i in range(2):
            self.name_number.append(QLabel(name[i], self))
            self.name_number[i].move(20 + (190 * i), 430)
            self.name_number[i].resize(170, 50)
            self.name_number[i].setFont(QtGui.QFont("궁서", 13))

        self.name_number = []
        name = ['0', '0']
        for i in range(2):
            self.name_number.append(QLabel(name[i], self))
            self.name_number[i].move(148 + (190 * i), 445)
            self.name_number[i].resize(20, 20)
            self.name_number[i].setFont(QtGui.QFont("궁서", 13))



        self.setWindowTitle('같은그림 찾기 게임')
        self.move(300, 300)
        self.resize(400, 500)
        self.setStyleSheet('background: white')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
