import pandas as pd 
import pickle
import ta
import warnings
warnings.filterwarnings('ignore')

class All_Indicator():
    def __init__(self, path_to_data="src/app/DataBase/Crypto_Database/"):
        self.path_to_data = path_to_data
        
        
    def load_data_from_db(self, symbol, timeframe):
        filePath = self.path_to_data+timeframe+'/'+symbol.replace('/','')+'.p'
        dbfile = open(filePath,'rb')
        df = pickle.load(dbfile)
        dbfile.close()
        return(df)
    
    
    def indicators(self, symbol, timeframe):
        df = self.load_data_from_db(symbol, timeframe)
        
        candle = []
        for i in range(len(df)):
            if df.iloc[i]['close'] > df.iloc[i]['open']:
                candle.append('green')
            else:
                candle.append('red')
                
        df['candle'] = candle
        
        df['EMA1']= ta.trend.ema_indicator(close=df['close'], window=7)
        df['EMA2']= ta.trend.ema_indicator(close=df['close'], window=30)
        df['EMA3']= ta.trend.ema_indicator(close=df['close'], window=50)
        df['EMA4']= ta.trend.ema_indicator(close=df['close'], window=100)
        df['EMA5']= ta.trend.ema_indicator(close=df['close'], window=121)
        df['EMA6']= ta.trend.ema_indicator(close=df['close'], window=200)
        
        df['STOCH_RSI'] = ta.momentum.stochrsi(close=df['close'], window=14, smooth1=3, smooth2=3)
        
        df = df.dropna()
        return(df)
    
    
    def openLongCondition_Strategy1(self, row):
        if (row['EMA1'] > row['EMA2'] 
        and row['EMA2'] > row['EMA3'] 
        and row['EMA3'] > row['EMA4'] 
        and row['EMA4'] > row['EMA5'] 
        and row['EMA5'] > row['EMA6'] 
        and row['STOCH_RSI'] < 0.82):
            return True
        else:
            return False
        
    def closeLongCondition_Strategy1(self, row):
        if row['EMA6'] > row['EMA1']:
            return True
        else:
            return False


    def openShortCondition_Strategy1(self, row):
        if ( row['EMA6'] > row['EMA5'] 
        and row['EMA5'] > row['EMA4'] 
        and row['EMA4'] > row['EMA3'] 
        and row['EMA3'] > row['EMA2'] 
        and row['EMA2'] > row['EMA1'] 
        and row['STOCH_RSI'] > 0.2 ):
            return True
        else:
            return False
     
    def closeShortCondition_Strategy1(self, row):
        if row['EMA1'] > row['EMA6']:
            return True
        else:
            return False    
        
if __name__ == '__main__':
    allIndicator = All_Indicator()
    print(allIndicator.indicators('BTC/USDT','1h')) 