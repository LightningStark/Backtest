import GlobVar


# SELLING STOCKS
def BearEngulf(self):
    if ((self.close < self.prevclose) & (self.close < self.prevopen)
            & (self.open > self.prevclose) & (self.open > self.prevopen)
            & (self.close * self.Entry_LowerLimit < self.nextopen < self.close * self.Entry_UpperLimit)):

        highest = self.prevhigh
        n = 0
        self.offset = (self.Days - 1)

        for j in range(self.i - self.offset, self.i):
            dailyhigh = float(self.data[j][5])

            if (highest > dailyhigh) & (self.high > dailyhigh):
                n += 1
                if n == self.offset - 1:

                    closediff = ((self.nextclose - self.close) * 100) / self.close

                    if self.TargetUpto >= self.Target:

                        GlobVar.RESULT.insert(GlobVar.count,
                                              ["", self.date, self.PevDlypercent, self.TargetUpto, closediff, "Profit"])
                        GlobVar.totalwin += 1
                        GlobVar.count += 1
                        GlobVar.tradecount += 1
                        GlobVar.points = GlobVar.points + (self.nextopen * 0.5 / 100)

                    else:

                        GlobVar.RESULT.insert(GlobVar.count,
                                              ["", self.date, self.PevDlypercent, self.TargetUpto, closediff, "Loss"])
                        GlobVar.totallose += 1
                        GlobVar.count += 1
                        GlobVar.tradecount += 1
                        GlobVar.points = GlobVar.points - (self.nextopen - self.nextclose)
            else:
                break
