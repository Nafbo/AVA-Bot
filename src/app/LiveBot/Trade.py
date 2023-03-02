import warnings
warnings.filterwarnings('ignore')
import pandas as pd


class Trade_Choice():
    def volumeAnomaly(self, row, previousRow=None):
        '''Indicator: Volume Anomaly
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A number (0, 1 or 2)
            '''
        if row['VolAnomaly']== 2:
            return(2)
        elif row['VolAnomaly']== 1:
            return(1)
        else: 
            return(0)
        
    def fearAndGreed(self, row, previousRow=None):
        '''Indicator: Fear And Greed
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A number (0, 1, 2 or 3)
            '''
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
        '''Checks if the Take Profit is hit or not
    
            Parameters:
            row (float): Actual Price
            takeProfitValue (float): The value of the Take Profit 
            position (string): If it is a long or a short position
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
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
        '''Checks if the Stop Loss is hit or not
    
            Parameters:
            row (float): Actual Price
            stopLossValue (float): The value of the Stop Loss
            position (string): If it is a long or a short position
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
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
        '''Checks if we can open a Long position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
        if (row['ADX']>25 and
            row['TRIX_HISTO']>0 and
            row['EMA5']>row['EMA21']>row['EMA50']>row['EMA200'] and
            row['STOCH_RSI']<0.3):
            return(True)
        else:
            return(False)
        
    def closeLongPosition(self, row, previousRow=None): 
        '''Checks if we can close a Long position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            ''' 
        if(row['EMA5']<=row['EMA50']):
            return(True)  
        else:
            return(False)
        
    def openShortPosition(self, row, previousRow=None):
        '''Checks if we can open a Short position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
        if (row['STOCH_RSI']>0.7 and
            row['n1_close'] > row['n1_lower_band'] and
            row['close'] < row['lower_band'] and
            (row['n1_higher_band'] - row['n1_lower_band']) / row['n1_lower_band'] > 0 and
            row['EMA5']<row['EMA21']<row['EMA50']<row['EMA200']):
            return(True)
        else:
            return(False)
        
    def closeShortPosition(self, row, previousRow=None):  
        '''Checks if we can close a Short position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
        if(row['EMA5']>=row['EMA21']):
            return(True)  
        else:
            return(False)
        
class Trade_1():
    
    def takeProfit(self, row, takeProfitValue, position):
        '''Checks if the Take Profit is hit or not
    
            Parameters:
            row (float): Actual Price
            takeProfitValue (float): The value of the Take Profit 
            position (string): If it is a long or a short position
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
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
        '''Checks if the Stop Loss is hit or not
    
            Parameters:
            row (float): Actual Price
            stopLossValue (float): The value of the Stop Loss
            position (string): If it is a long or a short position
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
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
        '''Checks if we can open a Long position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
        if (row['ADX']>25 and
            row['TRIX_HISTO']>0 and
            row['EMA5']>row['EMA21']>row['EMA50'] and
            row['STOCH_RSI']<=0.3):
            return(True)
        else:
            return(False)
        
    def closeLongPosition(self, row, previousRow=None): 
        '''Checks if we can close a Long position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''  
        if(row['EMA5']<=row['EMA21']):
            return(True)  
        else:
            return(False)
        
    def openShortPosition(self, row, previousRow=None):
        '''Checks if we can open a Short position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
        if (row['n1_close'] > row['n1_lower_band'] and
            row['close'] < row['lower_band'] and
            (row['n1_higher_band'] - row['n1_lower_band']) / row['n1_lower_band'] > 0 and
            row['STOCH_RSI']>=0.7 and
            row['EMA5']<row['EMA21']<row['EMA50']):
            return(True)
        else:
            return(False)
        
    def closeShortPosition(self, row, previousRow=None):  
        '''Checks if we can close a Short position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
        if(row['EMA5']>=row['EMA21']):
            return(True)  
        else:
            return(False)
   
class Trade_2():
    def takeProfit(self, row, takeProfitValue, position):
        '''Checks if the Take Profit is hit or not
    
            Parameters:
            row (float): Actual Price
            takeProfitValue (float): The value of the Take Profit 
            position (string): If it is a long or a short position
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
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
        '''Checks if the Stop Loss is hit or not
    
            Parameters:
            row (float): Actual Price
            stopLossValue (float): The value of the Stop Loss
            position (string): If it is a long or a short position
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
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
        '''Checks if we can open a Long position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
        if (row['ADX']>25 and
            row['TRIX_HISTO']>0 and
            row['EMA5']>row['EMA21'] and
            row['STOCH_RSI']<=0.35):
            return(True)
        else:
            return(False)
        
    def closeLongPosition(self, row, previousRow=None): 
        '''Checks if we can close a Long position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''  
        if(row['EMA5']<=row['EMA50']):
            return(True)  
        else:
            return(False)
        
    def openShortPosition(self, row, previousRow=None):
        '''Checks if we can open a Short position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
        if (row['TRIX_HISTO']>0 and
            row['n1_close'] > row['n1_lower_band'] and
            row['close'] < row['lower_band'] and
            (row['n1_higher_band'] - row['n1_lower_band']) / row['n1_lower_band'] > 0 and
            row['EMA5']<row['EMA21']):
            return(True)
        else:
            return(False)
        
    def closeShortPosition(self, row, previousRow=None):  
        '''Checks if we can close a Short position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
        if(row['EMA5']>=row['EMA50']):
            return(True)  
        else:
            return(False)
        
class Trade_3():
    
    def takeProfit(self, row, takeProfitValue, position):
        '''Checks if the Take Profit is hit or not
    
            Parameters:
            row (float): Actual Price
            takeProfitValue (float): The value of the Take Profit 
            position (string): If it is a long or a short position
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
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
        '''Checks if the Stop Loss is hit or not
    
            Parameters:
            row (float): Actual Price
            stopLossValue (float): The value of the Stop Loss
            position (string): If it is a long or a short position
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
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
        '''Checks if we can open a Long position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
        if (row['n1_close'] > row['n1_higher_band'] and
            row['close'] < row['higher_band'] and
            (row['n1_higher_band'] - row['n1_lower_band']) / row['n1_lower_band'] > 0 and
            row['EMA5']>row['EMA21']>row['EMA50']):
            return(True)
        else:
            return(False)
        
    def closeLongPosition(self, row, previousRow=None):  
        '''Checks if we can close a Long position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            ''' 
        if(row['EMA5']<=row['EMA21']):
            return(True)  
        else:
            return(False)
        
    def openShortPosition(self, row, previousRow=None):
        '''Checks if we can open a Short position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''
        if (row['ADX']>25 and
            row['TRIX_HISTO']>0 and
            row['EMA5']<row['EMA21']<row['EMA50'] and
            row['STOCH_RSI']<=0.3):
            return(True)
        else:
            return(False)
        
    def closeShortPosition(self, row, previousRow=None): 
        '''Checks if we can close a Short position or not
    
            Parameters:
            row (float): Actual Price
            previousRow (date): Last Price
            
            Returns:
            A boolean: True you can close the position, False you can't
            '''  
        if(row['EMA5']>=row['EMA21']):
            return(True)  
        else:
            return(False)