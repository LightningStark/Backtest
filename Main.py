from PyQt5 import QtWidgets
from HomeWindow import Ui_MainWindow
import csv, sys
from Mycollection import Strategy
import GlobVar
import pandas as pd
from ReportWindow import Ui_MainWindow_3
from BrowsingWindow import FileDialog
from AlertWindow import Ui_MainWindow_2
from UserGuideWindow import Ui_MainWindow_4

def Buy_Selected():
    GlobVar.rd_button_selected = "BUY"
    print("selected option->", GlobVar.rd_button_selected)


def Sell_Selected():
    GlobVar.rd_button_selected = "SELL"
    print("selected option->", GlobVar.rd_button_selected)


def Change_in_Strategy_Value(self):
    GlobVar.strategy = str(ui.comboBox.currentText())


def Change_in_Entry_Value(self):
    GlobVar.EntryAt = str(ui.comboBox_2.currentText())

def BrowseDialog(self):

    fd = FileDialog()
    fd.showDialog()
    ui.label_13.setText(GlobVar.Directory)

def UserGuide(self):

    ug = Ui_MainWindow_4()
    ug.setupUi(MainWindow_4)
    MainWindow_4.show()


def GetReport():
    Days = int(ui.plainTextEdit_5.toPlainText())
    Target = float(ui.plainTextEdit.toPlainText())
    Stoploss = float(ui.plainTextEdit_2.toPlainText())
    Entry_LowerLimit = float(ui.plainTextEdit_3.toPlainText())
    Entry_UpperLimit = float(ui.plainTextEdit_4.toPlainText())
    GlobVar.strategy = str(ui.comboBox.currentText())
    GlobVar.EntryAt = str(ui.comboBox_2.currentText())

    GlobVar.stockcount = 0
    GlobVar.tradecount = 0
    GlobVar.points = 0
    GlobVar.totallose = 0
    GlobVar.totalwin = 0
    GlobVar.count = 0
    GlobVar.RESULT = []

    if (len(GlobVar.rd_button_selected) != 0) & (len(GlobVar.Directory) != 0) & (10 <= Days <= 200)\
            & (Entry_LowerLimit < Entry_UpperLimit) & (Entry_LowerLimit != Entry_UpperLimit)\
            & (Target > 0) & (Stoploss > 0):
        for k in GlobVar.stocks:
            # csv file name
            filename = k + ".csv"
            GlobVar.stockcount += 1
            GlobVar.RESULT.insert(GlobVar.count, [k.upper(), "", "", "", "", ""])
            GlobVar.count += 1

            # reading csv file
            with open(str(GlobVar.Directory) + '/' + filename, 'r') as csvfile:

                # creating a csv reader object
                csvreader = csv.reader(csvfile)
                data = list(csvreader)
                i = 0

                for i in range(Days, csvreader.line_num - 1):
                    # initialising/creating object
                    stock = Strategy(data, csvreader, i, Days, Target, Stoploss,
                                     Entry_LowerLimit, Entry_UpperLimit)

                    # access attributes
                    stock.execute()

        resultdf = pd.DataFrame(GlobVar.RESULT,
                                columns=['Stock', 'Date', 'PrevDelivery%', 'Profit Upto%', 'ClosedAt%', 'P/L'])
        rw = Ui_MainWindow_3()
        rw.setupUi(MainWindow_3, resultdf)
        MainWindow_3.show()
        # for debugging
        print("total", GlobVar.tradecount, "trades from", GlobVar.stockcount, "stocks")
        print("win ratio is ", (GlobVar.totalwin / GlobVar.tradecount) * 100)
        print("losses : ", GlobVar.totallose)
        print("points : ", GlobVar.points)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        print(resultdf)

    elif len(GlobVar.Directory) == 0:
        print("empty directory ")
        aw = Ui_MainWindow_2()
        aw.setupUi(MainWindow_2)
        MainWindow_2.resize(350,50)
        aw.label.setText("Please select Downloaded 'stocks' folder")
        MainWindow_2.show()

    elif len(GlobVar.rd_button_selected) == 0:
        print("please select buy or sell")
        aw = Ui_MainWindow_2()
        aw.setupUi(MainWindow_2)
        MainWindow_2.resize(250,50)
        aw.label.setText("Please select Buy or Sell")
        MainWindow_2.show()

    elif (Entry_LowerLimit >= Entry_UpperLimit):
        aw = Ui_MainWindow_2()
        aw.setupUi(MainWindow_2)
        MainWindow_2.resize(500,50)
        aw.label.setText("Lower Limit must be LESS than Upper Limit ")
        MainWindow_2.show()

    elif ((Days < 10) & (Days > 200)):
        aw = Ui_MainWindow_2()
        aw.setupUi(MainWindow_2)
        aw.label.setText("Select Days Betwwen 10 and 200 (just safe values, Both included)")
        MainWindow_2.show()

    elif Target <= 0:
        aw = Ui_MainWindow_2()
        aw.setupUi(MainWindow_2)
        MainWindow_2.resize(500,50)
        aw.label.setText("Target cant be Negative or 0, Because we want to make Profit ;)")
        MainWindow_2.show()

    elif Stoploss <= 0:
        aw = Ui_MainWindow_2()
        aw.setupUi(MainWindow_2)
        MainWindow_2.resize(500,50)
        aw.label.setText("Stoploss cant be Negative or 0, it's better to be safe than be :(")
        MainWindow_2.show()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow_2 = QtWidgets.QMainWindow()
MainWindow_3 = QtWidgets.QMainWindow()
MainWindow_4 = QtWidgets.QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.radioButton.toggled.connect(Buy_Selected)
ui.radioButton_2.toggled.connect(Sell_Selected)
ui.pushButton.clicked.connect(GetReport)
ui.pushButton_2.clicked.connect(UserGuide)
ui.pushButton_3.clicked.connect(BrowseDialog)
ui.comboBox.activated.connect(Change_in_Strategy_Value)
ui.comboBox_2.activated.connect(Change_in_Entry_Value)
MainWindow.show()
sys.exit(app.exec_())
