import pandas as pd 
import pickle
import ta
import warnings
warnings.filterwarnings('ignore')

class All_indicator():
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
        
if __name__ == '__main__':
    allIndicator = All_indicator()
    print(allIndicator.indicators('BTC/USDT','1h')) 