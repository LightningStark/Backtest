from result import statement
import GlobVar

global WINS;global LOSSES

# SELLING STOCKS

def pinbarengulf(data,csvreader):
	print("\n PinbarEngulf || Short")
	WINS = [];LOSSES = [];win = 0; lose = 0
	for i in range(2,csvreader.line_num-1):
		PerDly  = float (data[i][14]);volume = float (data[i][10]); date = data [i+1][2]; nextvolume = float (data[i+1][10])
		prevopen = float(data[i-1][4]); prevhigh = float(data[i-1][5]); prevlow = float (data[i-1][6]);prevclose = float (data[i-1][8])
		open = float(data[i][4]); high = float(data[i][5]); low = float (data[i][6]);close = float (data[i][8])
		nextopen = float(data[i+1][4]); nexthigh = float(data[i+1][5]); nextlow = float (data[i+1][6]);nextclose = float (data[i+1][8])
		

		if ((prevopen < (((prevhigh-prevlow)/2)+prevlow)) & (prevclose < (((prevhigh-prevlow)/2)+prevlow))& (close < prevclose) 
			& (close < prevopen) & (open > prevclose) & (open > prevopen)): 
	
			entryprice = nextopen ; stoploss = high*1.01 ; target = nextopen*0.99; days = 1; GlobVar.tradecount += 1
			
			for j in range(i+1,csvreader.line_num):
				newhigh= float(data[j][5]);newlow = float (data[j][6])
				
				if (newlow <= target):
					
					WINS.insert(win,[date,days,'T',PerDly]);win += 1;GlobVar.totalwin += 1
					break
					
				elif (newhigh >= stoploss):
					
					LOSSES.insert(lose,[date,days,'SL',PerDly]);lose += 1
					break
				
				days += 1
	
	statement(WINS,LOSSES)