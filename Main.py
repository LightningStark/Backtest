import logging
import csv, sys
import pandas as pd
import UniversalVar

from PyQt5 import QtWidgets
from BrowsingWindow import FileDialog
from Mycollection import Strategy
from HomeWindow import Ui_MainWindow
from ReportWindow import Ui_MainWindow_3
from AlertWindow import Ui_MainWindow_2
from UserGuideWindow import Ui_MainWindow_4

# Get the top-level logger object
log = logging.getLogger()

# make it print to the console.
console = logging.StreamHandler()
log.addHandler(console)


def Buy_Selected():
    UniversalVar.rd_button_selected = sys.intern('Buy')


def Sell_Selected():
    UniversalVar.rd_button_selected = sys.intern('Sell')


UniversalVar.strategy = lambda: sys.intern(str(hw.comboBox.currentText()))

UniversalVar.EntryAt = lambda: sys.intern(str(hw.comboBox_2.currentText()))


def BrowseDialog():
    FileDialog()
    hw.label_13.setText(UniversalVar.Directory)


def UserGuide():
    ug = Ui_MainWindow_4()
    ug.setupUi(MainWindow_4)
    MainWindow_4.show()


def GetReport():
    Days = int(hw.plainTextEdit_5.toPlainText())
    Target = float(hw.plainTextEdit.toPlainText())
    Stoploss = float(hw.plainTextEdit_2.toPlainText())
    Entry_LowerLimit = float(hw.plainTextEdit_3.toPlainText())
    Entry_UpperLimit = float(hw.plainTextEdit_4.toPlainText())
    UniversalVar.strategy = str(hw.comboBox.currentText())
    UniversalVar.EntryAt = str(hw.comboBox_2.currentText())

    UniversalVar.stockcount = 0
    UniversalVar.tradecount = 0
    UniversalVar.points = 0
    UniversalVar.totallose = 0
    UniversalVar.totalwin = 0
    UniversalVar.count = 0
    UniversalVar.RESULT = []

    if (len(UniversalVar.rd_button_selected) != 0) & (len(UniversalVar.Directory) != 0) & (10 <= Days <= 200) \
            & (Entry_LowerLimit < Entry_UpperLimit) & (Entry_LowerLimit != Entry_UpperLimit) \
            & (Target > 0) & (Stoploss > 0):
        for k in UniversalVar.stocks:

            filename = k + ".csv"
            UniversalVar.stockcount += 1
            UniversalVar.RESULT.insert(UniversalVar.count, [k.upper(), "", "", "", "", ""])
            UniversalVar.count += 1

            with open(UniversalVar.Directory + '/' + filename, 'r') as csvfile:

                csvreader = csv.reader(csvfile)
                data = list(csvreader)

                for i in range(Days, csvreader.line_num - 1):


                    stock = Strategy(data, csvreader, i, Days, Target, Stoploss,
                                     Entry_LowerLimit, Entry_UpperLimit)

                    stock.execute()

        resultdf = pd.DataFrame(UniversalVar.RESULT,
                                        columns=['Stock', 'Date', 'PrevDelivery%', 'Profit Upto%', 'ClosedAt%',
                                                 'P/L'])
        if UniversalVar.tradecount != 0:
            rw = Ui_MainWindow_3()
            rw.setupUi(MainWindow_3, resultdf)
            MainWindow_3.show()
            log.warning(resultdf)

        else:
            aw = Ui_MainWindow_2()
            aw.setupUi(MainWindow_2)
            MainWindow_2.resize(200, 50)
            aw.label.setText(sys.intern("No Trades Found"))
            MainWindow_2.show()

        del Entry_UpperLimit, Entry_LowerLimit
        del Days, Target, Stoploss, i, k, resultdf

    elif len(UniversalVar.Directory) == 0:
        aw = Ui_MainWindow_2()
        aw.setupUi(MainWindow_2)
        MainWindow_2.resize(350, 50)
        aw.label.setText(sys.intern("Please select Downloaded \"stocks\" folder"))
        MainWindow_2.show()

    elif len(UniversalVar.rd_button_selected) == 0:
        aw = Ui_MainWindow_2()
        aw.setupUi(MainWindow_2)
        MainWindow_2.resize(250, 50)
        aw.label.setText(sys.intern('Please select Buy or Sell'))
        MainWindow_2.show()

    elif Entry_LowerLimit >= Entry_UpperLimit:
        aw = Ui_MainWindow_2()
        aw.setupUi(MainWindow_2)
        MainWindow_2.resize(500, 50)
        aw.label.setText(sys.intern('Lower Limit must be LESS than Upper Limit'))
        MainWindow_2.show()

    elif (Days < 10) | (Days > 200):
        aw = Ui_MainWindow_2()
        aw.setupUi(MainWindow_2)
        MainWindow_2.resize(500, 50)
        aw.label.setText(sys.intern('Select Days between 10 and 200 (just safe values, Both included)'))
        MainWindow_2.show()

    elif Target <= 0:
        aw = Ui_MainWindow_2()
        aw.setupUi(MainWindow_2)
        MainWindow_2.resize(500, 50)
        aw.label.setText(sys.intern('Target cant be Negative or 0, Because we want to make Profit ;)'))
        MainWindow_2.show()

    elif Stoploss <= 0:
        aw = Ui_MainWindow_2()
        aw.setupUi(MainWindow_2)
        MainWindow_2.resize(500, 50)
        aw.label.setText(sys.intern('Stoploss cant be Negative or 0, its better to be safe than be :('))
        MainWindow_2.show()


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
MainWindow_2 = QtWidgets.QMainWindow()
MainWindow_3 = QtWidgets.QMainWindow()
MainWindow_4 = QtWidgets.QMainWindow()

hw = Ui_MainWindow()
hw.setupUi(MainWindow)
hw.radioButton.toggled.connect(Buy_Selected)
hw.radioButton_2.toggled.connect(Sell_Selected)
hw.pushButton.clicked.connect(GetReport)
hw.pushButton_2.clicked.connect(UserGuide)
hw.pushButton_3.clicked.connect(BrowseDialog)
hw.comboBox.activated.connect(UniversalVar.strategy)
hw.comboBox_2.activated.connect(UniversalVar.EntryAt)

MainWindow.show()
sys.exit(app.exec_())
