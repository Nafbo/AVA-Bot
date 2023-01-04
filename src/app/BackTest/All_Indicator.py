import pickle
import ta
import warnings
import numpy as np
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
    
    def vortex_indicator(self, symbol, timeframe, window=200):
            df = self.load_data_from_db(symbol, timeframe)
            try:
                df['tr1'] = (df['high'] - df['low'])
                df['tr2'] = (df['high'] - df['close'].shift(1))
                df['tr3'] = (df['low'] - df['close'].shift(1))
                df['true_range'] = df[['tr1', 'tr2', 'tr3']].values.max(1)
            except ValueError:
                return np.nan
            min_periods = window
            df['trn'] = df['true_range'].rolling(window, min_periods=min_periods).sum()
            df['vmp'] = np.abs(df['high'] - df['low'].shift(1))
            df['vmm'] = np.abs(df['low'] - df['high'].shift(1))
            df['vip'] = df['vmp'].rolling(window, min_periods=min_periods).sum() / df['trn']
            df['vin'] = df['vmm'].rolling(window, min_periods=min_periods).sum() / df['trn']
            df = df.drop(['trn','vmp', 'vmm', 'tr1', 'tr2', 'tr3', 'true_range'], axis=1)
            return (df)
    
    def indicators(self, symbol, timeframe):
        # df = self.load_data_from_db(symbol, timeframe)
        df = self.vortex_indicator(symbol, timeframe)
    
        df['ema100'] = ta.trend.ema_indicator(close = df['close'], window = 100)
        df['ema200'] = ta.trend.ema_indicator(close = df['close'], window = 200)
        # df['sma_long'] = ta.trend.sma_indicator(close = df['close'], window = 600)
        # df['stoch_rsi'] = ta.momentum.stochrsi(close = df['close'], window = 14)
        
        return(df)   
    
    
        
if __name__ == '__main__':
    allIndicator = All_indicator()
    print(allIndicator.indicators('BTC/USDT','1h')) 
    # print(allIndicator.vortex_indicator('BTC/USDT','1h')) 