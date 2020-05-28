# importing csv module 
import csv 
from pinbar import pinbarengulf
from hanging import hangingengulf
from ThreeWS import ThreeWS
from ThreeBC import ThreeBC
import GlobVar

stocks = ["bergepaint", "bpcl", "cipla", "infy", "mindtree","reliance", "tatasteel", "cholafin","exideind", "tatachem", "maruti",
		  "bajfinance","bandhanbnk", "chollafin", "siemens", "pel", "vedl","heromotoco", "ramcocem", "bel","bhel", "adanient", "srtransfin",
		  "suntv","auropharma"]
x=0

#for loop
for k in stocks:
	# csv file name 
	filename =  k + ".csv";filename_upper = filename.upper()
	print(filename_upper, end = '')
	x += 1

	# reading csv file 
	with open(filename, 'r') as csvfile: 

		# creating a csv reader object 
		csvreader = csv.reader(csvfile)
		data=list(csvreader)
		#trading strategies
		pinbarengulf(data,csvreader)
		hangingengulf(data,csvreader)
		#ThreeWS(data,csvreader)
		#ThreeBC(data,csvreader)
	
	if (x == len(stocks)):
		print("total", GlobVar.tradecount,"trades from",x,"stocks" )
		print("win ratio is ",(GlobVar.totalwin/GlobVar.tradecount)*100)
	#end for loop