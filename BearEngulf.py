import GlobVar


# SELLING STOCKS
def BearEngulf(self):

    if ((self.close < self.prevclose) & (self.close < self.prevopen)
            & (self.open > self.prevclose) & (self.open > self.prevopen)
            & (self.close * 0.99 < self.nextopen < self.close * 1.01)):
        highest = self.prevhigh
        n = 0

        for j in range(self.i - 11, self.i - 1):
            dailyhigh = float(self.data[j][5])
            if ((highest > dailyhigh) & (self.high > dailyhigh)):
                n += 1
                if (n == 10):
                  
                    closediff = ((self.nextclose - self.close) * 100) / self.close

                    if (self.tgtper >= 0.5):

                        GlobVar.RESULT.insert(GlobVar.count, ["",self.date, self.PevDlypercent, self.tgtper, closediff,"Profit"])
                        GlobVar.totalwin += 1
                        GlobVar.count +=1
                        GlobVar.tradecount += 1
                        GlobVar.points = GlobVar.points + (self.nextopen * 0.5 / 100)

                    else:

                        GlobVar.RESULT.insert(GlobVar.count, ["",self.date, self.PevDlypercent, self.tgtper, closediff,"Loss"])
                        GlobVar.totallose += 1
                        GlobVar.count +=1
                        GlobVar.tradecount += 1
                        GlobVar.points = GlobVar.points - (self.nextopen - self.nextclose)
            else:
                break

