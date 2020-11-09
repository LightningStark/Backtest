from Pinbar import Pinbar
from Hanging import Hanging
from BearEngulf import BearEngulf
from BullEngulf import BullEngulf
import GlobVar


def RdButtonSelected(self):
    if GlobVar.rd_button_selected == "BUY":
        self.TargetUpto = ((self.nexthigh - self.EntryPrice) / self.EntryPrice) * 100
    if GlobVar.rd_button_selected == "SELL":
        self.TargetUpto = ((self.EntryPrice - self.nextlow) / self.EntryPrice) * 100


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
        if GlobVar.EntryAt == "Next Open":
            self.EntryPrice = self.nextopen
            RdButtonSelected(self)

        if GlobVar.EntryAt == "Close":
            self.EntryPrice = self.close
            RdButtonSelected(self)

    # trading strategies
    def execute(self):

        if (GlobVar.strategy == "Pinbar"):
            Pinbar(self)
        if (GlobVar.strategy == "BearEngulf"):
            BearEngulf(self)
        if (GlobVar.strategy == "BullEngulf"):
            BullEngulf(self)
        if (GlobVar.strategy == "HangingMan"):
            Hanging(self)
