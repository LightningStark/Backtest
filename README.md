# Testing of Intraday Trades
# run Main.py using python interpreter to use interactive window
# At first click on browse and select stocks Folder


Stock market data Backtesting to develop and Test Trading Strategy for Intraday Trades, 
Historical data of stocks were downloaded from India Stock Exchange's website.
This software was made only for personal use, currently I have no intentions of scaling it (improved version, Ofcourse!) for commercial purpose.  
To create your own strategy create new files similar to - 'Pinbar/HangingMan/BearEngulg/BullEnguls'.py, and add to Main.py

To execute the code successfully
1. python version >3.0 required
2. required python packages: pandas, PyQt5

output window
1. Profit - target hit, profit was made on that day
2. LOSS - stoploss hit, loss was made on that particular day

Alpha version
- first implemantation of gui with Tkinkter

Beta Version(current)
-Better Gui with PyQt5

future updates 
1. executable File, for 1 Click Install and run
2. removal of stock enteries with no trades, currently you will observe there are stocks on output window with corresponding empty cells
3. create and save new strategies
4. swing trading(Long Position - holding stock position more for than one day) with moving averages(MA)

