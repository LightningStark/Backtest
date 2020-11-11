import UniversalVar

# Selling STOCKS
def Pinbar(self):
    if ((self.open < (((self.high - self.low) * 0.5) + self.low))
            & (self.close < (((self.high - self.low) * 0.5) + self.low))
            & (self.open > self.close) 
            & (self.close * (self.Entry_LowerLimit) < self.nextopen < self.close * self.Entry_UpperLimit)):

        maxhigh = self.high
        n = 0
        self.offset = (self.Days - 2)

        for j in range((self.i - self.offset), self.i):

            dailyhigh = float(self.data[j][5])

            if maxhigh > dailyhigh:
                n += 1
                if n == self.offset:

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

        del n , dailyhigh