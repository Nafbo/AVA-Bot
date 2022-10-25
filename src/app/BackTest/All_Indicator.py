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
        df['EMA200'] =ta.trend.ema_indicator(close=df['close'], window=200)
        df['EMA100'] =ta.trend.ema_indicator(close=df['close'], window=100)
        df = df.dropna()
        return(df)
    
    
    def buyCondition_Strategy1(self, row):
        if row['EMA100'] > row['EMA200']:
            return(True)
        else:
            return(False)


    def sellCondition_Strategy1(self, row):
        if row['EMA200'] > row['EMA100']:
            return(True)
        else:
            return(False)
        
        
if __name__ == '__main__':
    allIndicator = All_Indicator()
    print(allIndicator.indicators('BTC/USDT','1h')) 