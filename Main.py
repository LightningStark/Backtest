from PyQt5 import QtWidgets
from HomeWindow import Ui_HomeWindow
import csv, sys
from Mycollection import Strategy
import GlobVar
import pandas as pd
from ReportWindow import Ui_MainWindow_3
from BrowsingWindow import FileDialog
from Alert import Ui_AlertWindow

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

    if (len(GlobVar.rd_button_selected) != 0) & (len(GlobVar.Directory) != 0):
        for k in stocks:
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

        # for debugging
        print("total", GlobVar.tradecount, "trades from", GlobVar.stockcount, "stocks")
        print("win ratio is ", (GlobVar.totalwin / GlobVar.tradecount) * 100)
        print("losses : ", GlobVar.totallose)
        print("points : ", GlobVar.points)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)

        resultdf = pd.DataFrame(GlobVar.RESULT,
                                columns=['Stock', 'Date', 'PrevDelivery%', 'Profit Upto%', 'ClosedAt%', 'P/L'])
        rw = Ui_MainWindow_3()
        rw.setupUi(MainWindow_3, resultdf)
        MainWindow_3.show()

    elif len(GlobVar.Directory) == 0:
        print("empty directory ")
        aw = Ui_AlertWindow()
        aw.setupUi(MainWindow_2)
        aw.AlertBrowse(MainWindow_2)
        MainWindow_2.show()

    elif len(GlobVar.rd_button_selected) == 0:
        print("please select buy or sell")
        aw = Ui_AlertWindow()
        aw.setupUi(MainWindow_2)
        aw.AlertBuySell(MainWindow_2)
        MainWindow_2.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow_2 = QtWidgets.QMainWindow()
    MainWindow_3 = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(MainWindow)
    ui.radioButton.toggled.connect(Buy_Selected)
    ui.radioButton_2.toggled.connect(Sell_Selected)
    ui.pushButton.clicked.connect(btnClicked)
    ui.pushButton_2.clicked.connect(BrowseDialog)
    ui.comboBox.activated.connect(Change_in_Strategy_Value)
    ui.comboBox_2.activated.connect(Change_in_Entry_Value)
    MainWindow.show()
    sys.exit(app.exec_())
