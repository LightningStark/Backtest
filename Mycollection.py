from Pinbar import Pinbar
from Hanging import Hanging
from BearEngulf import BearEngulf
from BullEngulf import BullEngulf

class Strategy:
    'Common base class for all strategies'


    def __init__(self, data, csvreader,i,strat,Rd_Button_Selected):
        self.data = data
        self.csvreader = csvreader
        self.strat = strat
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
        
        if(Rd_Button_Selected == "BUY"):
            self.tgtper = ((self.nexthigh - self.nextopen) / self.nextopen) * 100
        if(Rd_Button_Selected == "SELL"):
            self.tgtper = ((self.nextopen - self.nextlow) / self.nextopen) * 100

 ### trading strategies
    def execute(self):
        if(self.strat == "Pinbar"):    
            Pinbar(self)
        if(self.strat == "BearEngulf"):    
            BearEngulf(self)
        if(self.strat == "BullEngulf"):    
            BullEngulf(self)
        if(self.strat == "Hanging"):    
            Hanging(self)
        



