import warnings
warnings.filterwarnings('ignore')
import pandas as pd


class Trade_Choice():
    def volumeAnomaly(self, row, previousRow=None):
        if row['VolAnomaly']== 2:
            return(2)
        elif row['VolAnomaly']== 1:
            return(1)
        else: 
            return(0)
        
    def fearAndGreed(self, row, previousRow=None):
        if row['FEAR'] >= 80:
            return(2)
        elif 50 < row['FEAR'] < 80:
            return(1)
        elif 30 <= row['FEAR'] <= 50:
            return(3)
        else: 
            return(0)


class Trade_0():
    
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
        if (row['ADX']>25 and
            row['TRIX_HISTO']>0 and
            row['EMA5']>row['EMA21']>row['EMA50']>row['EMA200'] and
            row['STOCH_RSI']<0.3):
            return(True)
        else:
            return(False)
        
    def closeLongPosition(self, row, previousRow=None):  
        if(row['EMA5']<=row['EMA50']):
            return(True)  
        else:
            return(False)
        
    def openShortPosition(self, row, previousRow=None):
        if (row['STOCH_RSI']>0.7 and
            row['n1_close'] > row['n1_lower_band'] and
            row['close'] < row['lower_band'] and
            (row['n1_higher_band'] - row['n1_lower_band']) / row['n1_lower_band'] > 0 and
            row['EMA5']<row['EMA21']<row['EMA50']<row['EMA200']):
            return(True)
        else:
            return(False)
        
    def closeShortPosition(self, row, previousRow=None):  
        if(row['EMA5']>=row['EMA21']):
            return(True)  
        else:
            return(False)
        
class Trade_1():
    
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
        if (row['ADX']>25 and
            row['TRIX_HISTO']>0 and
            row['EMA5']>row['EMA21']>row['EMA50'] and
            row['STOCH_RSI']<=0.3):
            return(True)
        else:
            return(False)
        
    def closeLongPosition(self, row, previousRow=None):  
        if(row['EMA5']<=row['EMA21']):
            return(True)  
        else:
            return(False)
        
    def openShortPosition(self, row, previousRow=None):
        if (row['n1_close'] > row['n1_lower_band'] and
            row['close'] < row['lower_band'] and
            (row['n1_higher_band'] - row['n1_lower_band']) / row['n1_lower_band'] > 0 and
            row['STOCH_RSI']>=0.7 and
            row['EMA5']<row['EMA21']<row['EMA50']):
            return(True)
        else:
            return(False)
        
    def closeShortPosition(self, row, previousRow=None):  
        if(row['EMA5']>=row['EMA21']):
            return(True)  
        else:
            return(False)
   
class Trade_2():
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
        if (row['ADX']>25 and
            row['TRIX_HISTO']>0 and
            row['EMA5']>row['EMA21'] and
            row['STOCH_RSI']<=0.35):
            return(True)
        else:
            return(False)
        
    def closeLongPosition(self, row, previousRow=None):  
        if(row['EMA5']<=row['EMA50']):
            return(True)  
        else:
            return(False)
        
    def openShortPosition(self, row, previousRow=None):
        if (row['TRIX_HISTO']>0 and
            row['n1_close'] > row['n1_lower_band'] and
            row['close'] < row['lower_band'] and
            (row['n1_higher_band'] - row['n1_lower_band']) / row['n1_lower_band'] > 0 and
            row['EMA5']<row['EMA21']):
            return(True)
        else:
            return(False)
        
    def closeShortPosition(self, row, previousRow=None):  
        if(row['EMA5']>=row['EMA50']):
            return(True)  
        else:
            return(False)
        
class Trade_3():
    
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
        if (row['n1_close'] > row['n1_higher_band'] and
            row['close'] < row['higher_band'] and
            (row['n1_higher_band'] - row['n1_lower_band']) / row['n1_lower_band'] > 0 and
            row['EMA5']>row['EMA21']>row['EMA50']):
            return(True)
        else:
            return(False)
        
    def closeLongPosition(self, row, previousRow=None):  
        if(row['EMA5']<=row['EMA21']):
            return(True)  
        else:
            return(False)
        
    def openShortPosition(self, row, previousRow=None):
        if (row['ADX']>25 and
            row['TRIX_HISTO']>0 and
            row['EMA5']<row['EMA21']<row['EMA50'] and
            row['STOCH_RSI']<=0.3):
            return(True)
        else:
            return(False)
        
    def closeShortPosition(self, row, previousRow=None):  
        if(row['EMA5']>=row['EMA21']):
            return(True)  
        else:
            return(False)