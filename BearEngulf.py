import UniversalVar


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

                    closediff = "{:.2f}".format(((self.nextclose - self.close) * 100) / self.close)

                    if self.TargetUpto >= self.Target:

                        UniversalVar.RESULT.insert(UniversalVar.count,
                                                   ["", self.date, self.PevDlypercent, self.TargetUpto, closediff, "Profit"])
                        UniversalVar.totalwin += 1
                        UniversalVar.count += 1
                        UniversalVar.tradecount += 1
                        UniversalVar.points = UniversalVar.points + (self.nextopen * 0.5 / 100)

                    else:

                        UniversalVar.RESULT.insert(UniversalVar.count,
                                                   ["", self.date, self.PevDlypercent, self.TargetUpto, closediff, "Loss"])
                        UniversalVar.totallose += 1
                        UniversalVar.count += 1
                        UniversalVar.tradecount += 1
                        UniversalVar.points = UniversalVar.points - (self.nextopen - self.nextclose)
            else:
                break

        del n, dailyhigh