# Backtest 

Stock market data Backtesting to develop a Trading Strategy for Intraday Trades, 
Historical data of stocks was downloaded from NSE(india) website.
This software was made only for personal use, currently I have no intentions of scaling it(improved version, Ofcourse!) for commercial purpose.  
To test your own strategy edit files like - 'Pinbar.py', 'BullEngulf.py' accordingly

To execute the code successfully
1. python version >3.0 required
2. required python packages: pandas, pandastable
3. locate and change below line in Backtest.py file with address for stocks folder you have downloaded/cloned it.
      change address between single quotes('') according to download folder location 
          code ->   with open('change address here' + filename, 'r') as csvfile:
    for example ->
        with open('C:/Downloads/Backtest/stocks/' + filename, 'r') as csvfile:
        caution: while copy pasting address check if address contains forward(/) or backward(\) slash, use forward slash in the code.

output window
1. Profit - target hit, profit was made on that day
2. LOSS - stoploss hit, loss was made on that particular day

future updates 
1. Add textboxes for target and stoploss
2. removal of known bugs
3. removal of stcok enteries with no trades, currently you will observe there are stocks on output window with corresponding empty cells
4. create and save new strategies
5. swing trading(Long Position - holding stock position more than one day) with moving averages(MA)

