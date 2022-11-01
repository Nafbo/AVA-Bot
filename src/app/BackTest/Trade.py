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
            row['AO'] >= 0
            and previousRow['AO'] > row['AO']
            and row['WillR'] < -85
            and row['EMA100'] > row['EMA200']
        ):
            return(True)
        else:
            return(False)

    def sellCondition(self, row, previousRow=None):
        if (
            (row['AO'] < 0
            and row['STOCH_RSI'] > 0.2)
            or row['WillR'] > -10
        ):
            return(True)
        else:
            return(False)