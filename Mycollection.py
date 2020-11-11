from Pinbar import Pinbar
from HangingMan import HangingMan
from BearEngulf import BearEngulf
from BullEngulf import BullEngulf
import UniversalVar


def RdButtonSelected(self):
    if UniversalVar.rd_button_selected == "Buy":
        self.TargetUpto = float("{:.2f}".format(((self.nexthigh - self.EntryPrice) / self.EntryPrice) * 100))
    if UniversalVar.rd_button_selected == "Sell":
        self.TargetUpto = float("{:.2f}".format(((self.EntryPrice - self.nextlow) / self.EntryPrice) * 100))


class Strategy:
    """Common base class for all strategies"""

    def __init__(self, data, csvreader, i, Days, Target, Stoploss, Entry_LowerLimit, Entry_UpperLimit):
        self.data = data
        self.csvreader = csvreader
        self.i = i
        self.PevDlypercent = float(data[i][14])
        self.volume = float(data[i][10])
        self.date = data[i + 1][2]
        self.nextvolume = float(data[i + 1][10])
        self.prevopen = float(data[i - 1][4])
        self.prevhigh = float(data[i - 1][5])
        self.prevlow = float(data[i - 1][6])
        self.prevclose = float(data[i - 1][8])
        self.open = float(data[i][4])
        self.high = float(data[i][5])
        self.low = float(data[i][6])
        self.close = float(data[i][8])
        self.nextopen = float(data[i + 1][4])
        self.nexthigh = float(data[i + 1][5])
        self.nextlow = float(data[i + 1][6])
        self.nextclose = float(data[i + 1][8])
        self.Target = Target
        self.Days = Days
        self.Stoploss = Stoploss
        self.Entry_LowerLimit = 1 + (0.01 * Entry_LowerLimit)
        self.Entry_UpperLimit = 1 + (0.01 * Entry_UpperLimit)
        if UniversalVar.EntryAt == "Next Open":
            self.EntryPrice = self.nextopen
            RdButtonSelected(self)

        if UniversalVar.EntryAt == "Close":
            self.EntryPrice = self.close
            RdButtonSelected(self)

    # trading strategies
    def execute(self):

        if (UniversalVar.strategy == "Pinbar"):
            Pinbar(self)
        if (UniversalVar.strategy == "BearEngulf"):
            BearEngulf(self)
        if (UniversalVar.strategy == "BullEngulf"):
            BullEngulf(self)
        if (UniversalVar.strategy == "HangingMan"):
            HangingMan(self)
