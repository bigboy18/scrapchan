import sys
import urllib.request
from bs4 import BeautifulSoup
import shutil
import requests
import re
import os
from PyQt5 import QtCore, QtWidgets
import bs4
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import random
import string
import time


def nav():
    url = 'https://boards.4chan.org/i/'
    lista = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    b = soup.find_all('a', {"class": "replylink"})
    odnosniki = soup.find("div", {"id": "boardNavDesktop"})
    for i in odnosniki.span:
        if isinstance(i, (bs4.element.Tag)):
            temp = (i.attrs["title"], i.text)
            temp = " ".join(temp)
            lista.append(temp)
    return lista


def waliduj(nazwa):
    zakazane = r'#%&*:<>?\/'
    dobranazwa = ''
    for i in nazwa:
        if i in zakazane:
            pass
        else:
            dobranazwa += i
    return dobranazwa


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


class Ui_MainWindow(object):

    def browsefolder(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\',
                                                         QtWidgets.QFileDialog.ShowDirsOnly)
        print('klinkniey')
        return dir

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 304)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 10, 161, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.fromspin = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.fromspin.setObjectName("fromspin")
        self.fromspin.setProperty("value", 1)
        self.fromspin.setMinimum(1)

        self.horizontalLayout.addWidget(self.fromspin)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.tospin = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.tospin.setMaximum(20)
        self.tospin.setProperty("value", 15)
        self.tospin.setObjectName("tospin")

        self.horizontalLayout.addWidget(self.tospin)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(450, 4, 311, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 431, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(r'C:\4chan')

        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushYes = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushYes.setObjectName("pushYes")
        self.horizontalLayout_4.addWidget(self.pushYes)

        self.pushNo = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushNo.setObjectName("pushNo")
        self.horizontalLayout_4.addWidget(self.pushNo)

        self.pushEnd = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushEnd.setObjectName("pushEnd")
        self.horizontalLayout_4.addWidget(self.pushEnd)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(nav())

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 20))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.browseoutput)
        self.pushButton_2.clicked.connect(self.scrape)
        self.judge = False
        self.pushEnd.clicked.connect(self.isend)
        self.pushYes.clicked.connect(self.isok)
        self.pushNo.clicked.connect(self.isnok)

    def isok(self):
        self.judge = "yes"

    def isnok(self):
        self.judge = "no"

    def isend(self):
        self.judge = "end"

    def scrape(self):
        topic = str(self.comboBox.currentText())

        topic = topic.split()[-1]
        numeracja = []

        podstrona = topic + '/'
        for k in range(self.fromspin.value(), self.tospin.value()):
            print(k)
            if k == 1:
                numer = ""
            else:
                numer = k
            urlek = 'https://boards.4chan.org/' + podstrona + str(numer)
            numeracja.append(urlek)
        print(numeracja)

        for url in numeracja:

            listatematow = []

            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            b = soup.find_all('a', {"class": "replylink"})
            for i in b:
                print(b)
                if i.text == 'Reply':
                    '''

                    print('https://boards.4chan.org/' + podstrona + i['href'])
                    self.textBrowser.setText('https://boards.4chan.org/' + podstrona + i['href'])
                    self.textBrowser.repaint()

                    while not self.judge:
                        print('odpowiedz')
                        time.sleep(1)

                    if self.judge == "yes":
                        listatematow.append('https://boards.4chan.org/' + podstrona + i['href'])
                    elif self.judge == "end":
                        break
                    else:
                        pass
                    '''
                    listatematow.append('https://boards.4chan.org/' + podstrona + i['href'])

            print(listatematow)
            for link in listatematow:
                response = requests.get(link)

                soup = BeautifulSoup(response.text, 'html.parser')

                tytuł = soup.find('span', {"class": "subject"}).text
                print(tytuł)
                if not tytuł:
                    tytuł = randomString()
                tytuł = waliduj(tytuł)
                filename = self.lineEdit.text() + '/' + podstrona + tytuł
                os.makedirs(filename, exist_ok=True)
                obrazki = soup.findAll('a', {"class": "fileThumb"})

                for obrazek in obrazki:
                    link = 'https:' + obrazek['href']
                    nazwa = obrazek['href'].split('/')[-1].split('.')[0]
                    rozszerzenie = obrazek['href'].split('/')[-1].split('.')[1]
                    print(nazwa)

                    try:
                        fota = urllib.request.urlopen(link)
                    except:
                        pass
                    response = requests.get(link, stream=True)
                    with open(filename + '/{}.{}'.format(nazwa, rozszerzenie), 'wb') as out_file:
                        shutil.copyfileobj(response.raw, out_file)
                        print(out_file)

    def browseoutput(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\',
                                                         QtWidgets.QFileDialog.ShowDirsOnly)
        self.lineEdit.setText(dir)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "From"))
        self.label.setText(_translate("MainWindow", "To"))
        self.pushButton_2.setText(_translate("MainWindow", "Scrape"))
        self.label_3.setText(_translate("MainWindow", "Save To:"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushYes.setText(_translate("MainWindow", "YES"))
        self.pushNo.setText(_translate("MainWindow", "NO"))
        self.pushEnd.setText(_translate("MainWindow", "END"))


class MyForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()

    sys.exit(app.exec_())