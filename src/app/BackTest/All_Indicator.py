import pickle
import ta
import warnings
import numpy as np
import pandas as pd
import pandas_ta as pda
import requests
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
    
    def get_n_columns(self, df, columns, n=1):
        df = df.copy()
        for col in columns:
            df["n"+str(n)+"_"+col] = df[col].shift(n)
        return(df)
    
    def chop(self, high, low, close, window=14):
        tr1 = pd.DataFrame(high - low).rename(columns = {0:'tr1'})
        tr2 = pd.DataFrame(abs(high - close.shift(1))).rename(columns = {0:'tr2'})
        tr3 = pd.DataFrame(abs(low - close.shift(1))).rename(columns = {0:'tr3'})
        frames = [tr1, tr2, tr3]
        tr = pd.concat(frames, axis = 1, join = 'inner').dropna().max(axis = 1)
        atr = tr.rolling(1).mean()
        highh = high.rolling(window).max()
        lowl = low.rolling(window).min()
        chop = 100 * np.log10((atr.rolling(window).sum()) / (highh - lowl)) / np.log10(window)
        return pd.Series(chop, name="CHOP")

    def indicators(self, symbol, timeframe):
        df = self.load_data_from_db(symbol, timeframe)
        
        # df['tr1'] = (df['high'] - df['low'])
        # df['tr2'] = (df['high'] - df['close'].shift(1))
        # df['tr3'] = (df['low'] - df['close'].shift(1))
        # df['true_range'] = df[['tr1', 'tr2', 'tr3']].values.max(1)
        # min_periods = 200
        # df['trn'] = df['true_range'].rolling(200, min_periods=min_periods).sum()
        # df['vmp'] = np.abs(df['high'] - df['low'].shift(1))
        # df['vmm'] = np.abs(df['low'] - df['high'].shift(1))
        # df['VIP'] = df['vmp'].rolling(200, min_periods=min_periods).sum() / df['trn']
        # df['VIN'] = df['vmm'].rolling(200, min_periods=min_periods).sum() / df['trn']
        # df = df.drop(['trn','vmp', 'vmm', 'tr1', 'tr2', 'tr3', 'true_range'], axis=1)

        df["VolAnomaly"] = 0
        df['MeanVolume'] = df['volume'].rolling(24).mean()
        df['MeanVolume1'] = df['volume'].rolling(16).mean()
        df.loc[df['volume'] > 1.08 * df['MeanVolume'], "VolAnomaly"] = 1
        df.loc[df['volume'] > 1.1 * df['MeanVolume1'], "VolAnomaly"] = 2
        df = df.drop(['MeanVolume', 'MeanVolume1'], axis=1)


        df['TRIX'] = ta.trend.ema_indicator(ta.trend.ema_indicator(ta.trend.ema_indicator(close=df['close'], window=9), window=9), window=9)
        df['TRIX_PCT'] = df["TRIX"].pct_change()*100
        df['TRIX_SIGNAL'] = ta.trend.sma_indicator(df['TRIX_PCT'],21)
        df['TRIX_HISTO'] = df['TRIX_PCT'] - df['TRIX_SIGNAL']
        df = df.drop(['TRIX_SIGNAL','TRIX_PCT', 'TRIX'], axis=1)
        
        df['EMA5'] = ta.trend.ema_indicator(close = df['close'], window = 5)
        df['EMA15'] = ta.trend.ema_indicator(close = df['close'], window = 15)
        df['EMA21'] = ta.trend.ema_indicator(close = df['close'], window = 21)
        df['EMA50'] = ta.trend.ema_indicator(close = df['close'], window = 50)
        df['EMA200'] = ta.trend.ema_indicator(close = df['close'], window = 200)
        df['EMA300'] = ta.trend.ema_indicator(close = df['close'], window = 300)

        
        df['STOCH_RSI'] = ta.momentum.stochrsi(close=df['close'], window=14, smooth1=3, smooth2=3)

        superTrend = pda.supertrend(df['high'], df['low'], df['close'], length=20, multiplier=3.0)
        df['SUPER_TREND'] = superTrend['SUPERT_'+str(20)+"_"+str(3.0)]
        df['SUPER_TREND_DIRECTION'] = superTrend['SUPERTd_'+str(20)+"_"+str(3.0)]

        # superTrend = pda.supertrend(df['high'], df['low'], df['close'], length=20, multiplier=4.0)
        # df['SUPER_TREND'] = superTrend['SUPERT_'+str(20)+"_"+str(4.0)]
        # df['SUPER_TREND_DIRECTION2'] = superTrend['SUPERTd_'+str(20)+"_"+str(4.0)]

        # superTrend = pda.supertrend(df['high'], df['low'], df['close'], length=40, multiplier=8.0)
        # df['SUPER_TREND'] = superTrend['SUPERT_'+str(40)+"_"+str(8.0)]
        # df['SUPER_TREND_DIRECTION3'] = superTrend['SUPERTd_'+str(40)+"_"+str(8.0)]
        
        df['ADX'] =ta.trend.adx(high=df['high'], low=df['low'], close = df['close'], window = 20)
        
        # df['AO'] = ta.momentum.awesome_oscillator(high=df['high'], low=df['low'], window1=6, window2=22)
        
        # df['WillR'] = ta.momentum.williams_r(high=df['high'], low=df['low'], close=df['close'], lbp=14)
    
        df["BB_%B"] = ta.volatility.bollinger_pband(df['close'], window=20, window_dev=2)
        
        bol_band = ta.volatility.BollingerBands(close=df["close"], window=100, window_dev=2.25)
        df["lower_band"] = bol_band.bollinger_lband()
        df["higher_band"] = bol_band.bollinger_hband()
        df["ma_band"] = bol_band.bollinger_mavg()
        df = self.get_n_columns(df, ["ma_band", "lower_band", "higher_band", "close"], 1)
        
        response = requests.get("https://api.alternative.me/fng/?limit=0&format=json")
        dataResponse = response.json()['data']
        fear = pd.DataFrame(dataResponse, columns = ['timestamp', 'value'])
        fear = fear.set_index(fear['timestamp'])
        fear.index = pd.to_datetime(fear.index, unit='s')
        del fear['timestamp']
        df['fearResult'] = fear['value']
        df['FEAR'] = df['fearResult'].ffill()
        df['FEAR'] = df.FEAR.astype(float)
        df = df.drop(['fearResult'], axis=1)

        df["CHOP"] = self.chop(df['high'],df['low'],df['close'],window=14)
        
        return(df)   
    
    
        
if __name__ == '__main__':
    allIndicator = All_indicator()
    print(allIndicator.indicators('BTC/USDT','1h')) 
    # print(allIndicator.vortex_indicator('BTC/USDT','1h')) 