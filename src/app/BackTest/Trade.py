import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from src.app.BackTest.All_indicator import All_indicator

class Trade():
    
    def takeProfit(self, row, takeProfitValue, position):
        if position == 'openLong':
            if row['high'] > takeProfitValue:
                return(True)
            else:
                return(False)
        elif position == 'openShort':
            if row['low'] < takeProfitValue:
                return(True)
            else:
                return(False)
    
    def stopLoss(self, row, stopLossValue, position):
        if position == 'openLong':
            if row['low'] < stopLossValue:
                return(True)
            else:
                return(False)
        elif position == 'openShort':
            if row['high'] > stopLossValue:
                return(True)
            else:
                return(False)
        
    def openLongPosition(self, row, previousRow=None):
        if (row['ema100']>row['ema200'] and
            row['vip']>=row['vin']):
            return(True)
        else:
            return(False)
        
    def closeLongPosition(self, row, previousRow=None):  
        if(row['vip']<=row['vin']):
            return(True)  
        else:
            return(False)
        
    def openShortPosition(self, row, previousRow=None):
        if (row['ema100']<row['ema200'] and
            row['vip']<=row['vin']):
            return(True)
        else:
            return(False)
        
    def closeShortPosition(self, row, previousRow=None):  
        if(row['vip']>=row['vin']):
            return(True)  
        else:
            return(False)
        
    
    