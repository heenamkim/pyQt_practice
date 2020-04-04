import sys
from PyQt5.QtWidgets import *



class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.image = QLabel('image',self)
        self.image.move(0, 0)
        self.image.resize(400, 200)
        self.image.setStyleSheet('background:orange')


        self.priceBtn = []
        price = [1200,900,800,1500]
        for i in range(4):
            self.priceBtn.append(QPushButton('%d'%price[i], self))
            self.priceBtn[i].move(25+(90*i), 200)
            self.priceBtn[i].resize(80, 30)
            self.priceBtn[i].setStyleSheet('background:white')
            self.priceBtn[i].clicked.connect( \
                lambda state, btn=self.priceBtn[i]: self.writeNumber(state, btn))

        self.balance = QLabel('0',self)
        self.balance.move(255, 255)
        self.balance.resize(120, 50)
        self.balance.setStyleSheet('background: white')

        self.coinBtn = []
        coins = [0,100,500]
        for i in range(3):
            self.coinBtn.append(QPushButton('%d'%coins[i],self))
            self.coinBtn[i].move(25+(50*i), 300)
            self.coinBtn[i].resize(50, 50)
            self.coinBtn[i].setStyleSheet('background: white')
            self.coinBtn[i].clicked.connect( \
                lambda state, coin=self.coinBtn[i]: self.result(state, coin))

        self.changes = QLabel("0", self)
        self.changes.move(305, 320)
        self.changes.resize(70, 50)
        self.changes.setStyleSheet('background: white')

        self.message = QLabel("0", self)
        self.message.move(25, 395)
        self.message.resize(350, 80)
        self.message.setStyleSheet('background: white')


        self.setWindowTitle('Vending Machine')
        self.move(300, 300)
        self.resize(400, 500)
        self.show()

    def writeNumber(self, state, btn):
        num = btn.text()

        self.balance.setText(num)

    def result(self, state, coin):
        num = self.balance.text()
        if coin == self.coinBtn[0]:
            num = 0
            self.balance.setText('0')
            self.changes.setText('0')
            self.message.setText('cancel')
        elif coin == self.coinBtn[1]:
            num = int(num) - 100
            self.balance.setText(str(num))
            if int(num) <= 0:
                num = -int(num)
                self.balance.setText('0')
                self.changes.setText(str(num))
                self.message.setText('Here your drink!!')
        elif coin == self.coinBtn[2]:
            num = int(num) - 500
            self.balance.setText(str(num))
            if int(num) < 0:
                num = -int(num)
                self.balance.setText('0')
                self.changes.setText(str(num))
                self.message.setText('Here your drink!!')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())