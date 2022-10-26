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
        
    def buyCondition(row):
        if (row['EMA1'] > row['EMA2'] 
        and row['EMA2'] > row['EMA3'] 
        and row['EMA3'] > row['EMA4'] 
        and row['EMA4'] > row['EMA5'] 
        and row['EMA5'] > row['EMA6'] 
        and row['STOCH_RSI']<0.82):
            return True
        else:
            return False

    def sellCondition(row):
        if (row['EMA6'] > row['EMA1'] 
            and row['STOCH_RSI']>0.2):
            return True
        else:
            return False