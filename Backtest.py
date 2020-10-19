# importing csv module
import csv
from Mycollection import Strategy
import GlobVar
import pandas as pd
import tkinter
from Report import Report
from tkinter import *

OPTIONS = ["Pinbar",
           "BearEngulf", "Hanging",
           "BullEngulf"]


def sel():
    GlobVar.Rd_Button_Selected = str(var.get())
    print("selected option->", GlobVar.Rd_Button_Selected)


def test():
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

    if (len(GlobVar.Rd_Button_Selected) != 0):
        for k in stocks:
            # csv file name
            filename = k + ".csv"
            path = 'cipla.csv'
            filename_upper = filename.upper()
            GlobVar.stockcount += 1
            GlobVar.RESULT.insert(GlobVar.count, [k.upper(), "", "", "", "", ""])
            GlobVar.count += 1

            # reading csv file
            with open('C:/Users/umang/source/repos/PythonApplication1/stocks/' + filename, 'r') as csvfile:
                # creating a csv reader object
                csvreader = csv.reader(csvfile)
                data = list(csvreader)
                i = 0
                for i in range(12, csvreader.line_num - 1):

                    # initialising/creating object
                    stock = Strategy(data, csvreader, i, str(variable.get()), GlobVar.Rd_Button_Selected)

                    # access attributes
                    stock.execute()
                    del stock
    else:
        print("please select buy or sell")
        message = StringVar()
        label = Label(mainwindow, textvariable=message, relief=SUNKEN)
        message.set("please select buy or sell")
        label.pack()
        return

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    resultdf = pd.DataFrame(GlobVar.RESULT,
                            columns=['Stock', 'Date', 'PrevDelivery%', 'Profit Upto%', 'ClosedAt%', 'P/L'])
    print("\n", resultdf)

    print("total", GlobVar.tradecount, "trades from", GlobVar.stockcount, "stocks")
    print("win ratio is ", (GlobVar.totalwin / GlobVar.tradecount) * 100)
    print("losses : ", GlobVar.totallose)
    print("points : ", GlobVar.points)

    newWindow = Toplevel(mainwindow)
    newWindow.wm_title("Report")
    #an object for reporting output of backtesting stocks
    report = Report(resultdf, newWindow)
    newWindow.mainloop()


mainwindow = tkinter.Tk()
mainwindow.geometry("500x200")

# radiobutton
var = tkinter.StringVar()
R1 = tkinter.Radiobutton(mainwindow, text="Buy", variable=var, value="BUY", command=sel)
R1.pack(anchor='center')
R2 = tkinter.Radiobutton(mainwindow, text="Sell", variable=var, value="SELL", command=sel)
R2.pack(anchor='center')

# option menu
variable = tkinter.StringVar()
variable.set(OPTIONS[0])  # default value
w = tkinter.OptionMenu(mainwindow, variable, *OPTIONS)
w.pack()

# button
B = tkinter.Button(mainwindow, text="Test", command=test)
B.place(x=450, y=50)

# title
mainwindow.wm_title("Backtest for Intraday Trading")
mainwindow.mainloop()
