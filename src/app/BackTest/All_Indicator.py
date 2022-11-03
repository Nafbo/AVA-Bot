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
        
        df['ema1'] = ta.trend.ema_indicator(close = df['close'], window = 25)
        df['ema2'] = ta.trend.ema_indicator(close = df['close'], window = 45)
        df['sma_long'] = ta.trend.sma_indicator(close = df['close'], window = 600)
        df['stoch_rsi'] = ta.momentum.stochrsi(close = df['close'], window = 14)
        
        # df = df.dropna()
        return(df)   
        
if __name__ == '__main__':
    allIndicator = All_indicator()
    print(allIndicator.indicators('BTC/USDT','1h')) 