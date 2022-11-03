import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from src.app.BackTest.All_indicator import All_indicator

class Trade():
    
    def takeProfit(self, row, takeProfitValue):
        if row['high'] > takeProfitValue:
            return(True)
        else:
            return(False)
    
    def stopLoss(self, row, stopLossValue):
        if row['low'] < stopLossValue:
            return(True)
        else:
            return(False)
        
    def buyCondition(self, row, previousRow):
        if (
            row['ema1'] > row['ema2'] 
            and row['stoch_rsi'] < 0.8 
            and row['close'] > row['sma_long']
        ):
            return(True)
        else:
            return(False)

    def sellCondition(self, row, previousRow=None):
        if (
            row['ema2'] > row['ema1'] 
            and row['stoch_rsi'] > 0.2
        ):
            return(True)
        else:
            return(False)