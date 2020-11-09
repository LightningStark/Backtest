import sys
from PyQt5 import QtWidgets
from HomeWindow import Ui_MainWindow
import csv
from Mycollection import Strategy
import GlobVar
import pandas as pd
from Report import Ui_ReportWindow


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


def btnClicked():
    Days = int(ui.plainTextEdit_5.toPlainText())
    Target = float(ui.plainTextEdit.toPlainText())
    Stoploss = float(ui.plainTextEdit_2.toPlainText())
    Entry_LowerLimit = float(ui.plainTextEdit_3.toPlainText())
    Entry_UpperLimit = float(ui.plainTextEdit_4.toPlainText())
    GlobVar.strategy = str(ui.comboBox.currentText())
    GlobVar.EntryAt = str(ui.comboBox_2.currentText())


    stocks = ["bergepaint", "bpcl", "cipla", "infy", "mindtree", "reliance", "tatasteel", "cholafin", "exideind",
              "tatachem", "maruti",
              "bajfinance", "bandhanbnk", "chollafin", "siemens", "pel", "vedl", "heromotoco", "ramcocem", "bel",
              "bhel",
              "adanient", "srtransfin",
              "suntv", "auropharma", "mfsl", "ujjivan", "jublfood"]

    GlobVar.stockcount = 0
    GlobVar.tradecount = 0
    GlobVar.points = 0
    GlobVar.totallose = 0
    GlobVar.totalwin = 0
    GlobVar.count = 0
    GlobVar.RESULT = []

    if len(GlobVar.rd_button_selected) != 0:
        for k in stocks:
            # csv file name
            filename = k + ".csv"
            GlobVar.stockcount += 1
            GlobVar.RESULT.insert(GlobVar.count, [k.upper(), "", "", "", "", ""])
            GlobVar.count += 1

            # reading csv file
            with open('/home/umang/Desktop/repos/Backtest/stocks/' + filename, 'r') as csvfile:

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
    else:
        print("please select buy or sell")

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    resultdf = pd.DataFrame(GlobVar.RESULT,
                            columns=['Stock', 'Date', 'PrevDelivery%', 'Profit Upto%', 'ClosedAt%', 'P/L'])
    print("\n", resultdf)

    # an object for reporting results on Report Window
    ui.rw = Ui_ReportWindow(resultdf)
    ui.rw.show()

    #for debugging
    print("total", GlobVar.tradecount, "trades from", GlobVar.stockcount, "stocks")
    print("win ratio is ", (GlobVar.totalwin / GlobVar.tradecount) * 100)
    print("losses : ", GlobVar.totallose)
    print("points : ", GlobVar.points)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.radioButton.toggled.connect(Buy_Selected)
    ui.radioButton_2.toggled.connect(Sell_Selected)
    ui.pushButton.clicked.connect(btnClicked)
    ui.comboBox.activated.connect(Change_in_Strategy_Value)
    ui.comboBox_2.activated.connect(Change_in_Entry_Value)
    MainWindow.show()
    sys.exit(app.exec_())
