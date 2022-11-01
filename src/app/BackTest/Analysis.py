import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from src.app.BackTest.BackTest import BackTest

class Analysis ():
    
    def analyzeBacktest(self, symbols, timeframe, usd=100, start_date='2019-01-01T00:00:00'):
        backtest = BackTest()
        dfTrades,positionInProgress = backtest.trade(pairList, '1h', start_date='2022-01-01')
        dfBuyAnsHold = backtest.trade(pairList, '1h', start_date='2022-01-01')
        
        return

if __name__ == '__main__':
    analysis = Analysis()
    pairList = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT']
    analysis.analyzeBacktest(pairList, '1h', start_date='2022-01-01')