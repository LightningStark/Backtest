import pandas as pd

def statement(WINS,LOSSES):					

	windf = pd.DataFrame(WINS,columns = ['date','days','W/L','PerDly'])
	losedf = pd.DataFrame(LOSSES,columns = ['date','days','W/L','PerDly'])
	if not windf.empty:
		print("\n",windf)
		#print ("\n", (win/tradecount)*100, "%")
	else:
		print ("--")
		#print("%.2f" %x)
	if not losedf.empty:
		print("\n",losedf)
		#print ("\n", (win/tradecount)*100, "%")
	else:
		print ("--")

	#print ("\n total trades =", tradecount)