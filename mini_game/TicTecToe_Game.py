import sys
from PyQt5.QtWidgets import *
from PyQt5 import *



class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.count = 1
        self.a = 0

        self.Menu = QLabel('  틱 택 톡 게 임', self)
        self.Menu.setGeometry(QtCore.QRect(50, 50, 50, 50))
        self.Menu.setFont(QtGui.QFont("궁서", 25))
        self.Menu.move(0, 20)
        self.Menu.resize(400, 100)


        self.game_number = []
        self.game_number2 = []

        for a in range(3):
            for b in range(1, 4):
                self.game_number.append(QPushButton(self))
                self.game_number[(a*3)+(b-1)].move((115 * b) - 85, 130 + (95 * a))
                self.game_number[(a*3)+(b-1)].resize(100, 80)
                self.game_number[(a*3)+(b-1)].clicked.connect( \
                    lambda state, btn=self.game_number[(a*3)+(b-1)]: self.gameStart(state, btn))

        self.menu_number = []
        name = ['다시 시작', '다시 누르기', '확인']
        for i in range(3):
            self.menu_number.append(QPushButton(name[i],self))
            self.menu_number[i].move(20+(130*i), 430)
            self.menu_number[i].resize(100, 50)
            self.menu_number[i].setStyleSheet("Color: red")

            self.menu_number[0].clicked.connect( \
                lambda state, btn=self.menu_number[0]: self.reset(state, btn))
            # self.menu_number[1].addAction(self.undo)



        self.setWindowTitle('틱택톡 게임')
        self.move(300, 300)
        self.resize(400, 500)
        self.setStyleSheet('background: white')
        self.show()

    def gameStart(self, state, btn):
        if self.count % 2 == 1:
            btn.setText('O')
            # self.game_number2[(a*3)+(b-1)].append(x)
            self.count += 1

        elif self.count % 2 == 0:
            btn.setText('X')
            # self.game_number2[(a*3)+(b-1)].append(x)
            self.count += 1

    def gameCheck (self):
        for i in range(3):
            if (game_number[i * 3] == 'O' and game_number[(i * 3) + 1] == 'O' and game_number[(i * 3) + 2] == 'O'):
                self.menu_number[2].setText('O win')
                a = 1
            elif (game_number[i] == 'O' and game_number[3 + i] == 'O' and game_number[6 + i] == 'O'):
                self.menu_number[2].setText('O win')
                a = 1
        #
        # if a == 1:
        #     break
        # if (bingo[0] == 'O' and bingo[4] == 'O' and bingo[8] == 'O'):
        #     self.menu_number[2].setText('O win')
        # elif (bingo[2] == 'O' and bingo[4] == 'O' and bingo[6] == 'O'):
        #     self.menu_number[2].setText('O win')

        # for j in range(3):
        #     if (bingo[j * 3] == 'X' and bingo[(j * 3) + 1] == 'X' and bingo[(j * 3) + 2] == 'X'):
        #         self.menu_number[2].setText('X win')
        #         a = 1
        #     elif (bingo[j] == 'X' and bingo[3 + j] == 'X' and bingo[6 + j] == 'X'):
        #         self.menu_number[2].setText('X win')
        #         a = 1
        # if a == 1:
        # if (bingo[0] == 'X' and bingo[4] == 'O' and bingo[8] == 'X'):
        #     self.menu_number[2].setText('X win')
        # elif (bingo[2] == 'X' and bingo[4] == 'X' and bingo[6] == 'X'):
        #     self.menu_number[2].setText('X win')
        #
    def reset(self, state, btn):
        self.game_number.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())