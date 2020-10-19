from pandastable import Table, TableModel
from tkinter import *

class Report(Frame):
        """Basic frame for the Report"""
        def __init__(self,resultdf,newWindow):
            Frame.__init__(self)
            newWindow.geometry('1000x400')
            f = Frame(newWindow)
            f.pack(fill=BOTH,expand=1)
            self.table = pt = Table(f, dataframe=resultdf,
                                    showtoolbar=True, showstatusbar=False)
            pt.show()
            return

