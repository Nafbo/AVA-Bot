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
        
        # candle = []
        # for i in range(len(df)):
        #     if df.iloc[i]['close'] > df.iloc[i]['open']:
        #         candle.append('green')
        #     else:
        #         candle.append('red')
                
        # df['candle'] = candle
        
        # df['EMA50']=ta.trend.ema_indicator(df['close'], 50)
        # df['STOCH_RSI']=ta.momentum.stochrsi(df['close'])
        # df['KIJUN'] = ta.trend.ichimoku_base_line(df['high'],df['low'])
        # df['TENKAN'] = ta.trend.ichimoku_conversion_line(df['high'],df['low'])
        # df['SSA'] = ta.trend.ichimoku_a(df['high'],df['low'],3,38).shift(periods=48)
        # df['SSB'] = ta.trend.ichimoku_b(df['high'],df['low'],38,46).shift(periods=48)

        df['AO'] = ta.momentum.awesome_oscillator(df['high'],df['low'],window1=6,window2=22)
    
        df['EMA100'] =ta.trend.ema_indicator(close=df['close'], window=100)
        df['EMA200'] =ta.trend.ema_indicator(close=df['close'], window=200)

        df['STOCH_RSI'] = ta.momentum.stochrsi(close=df['close'], window=14)

        df['WillR'] = ta.momentum.williams_r(high=df['high'], low=df['low'], close=df['close'], lbp=14)
        
        # df = df.dropna()
        return(df)   
        
if __name__ == '__main__':
    allIndicator = All_indicator()
    print(allIndicator.indicators('BTC/USDT','1h')) 