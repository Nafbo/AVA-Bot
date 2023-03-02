from src.app.LiveBot.BitGet import *
import ta
import requests
import warnings
warnings.filterwarnings('ignore')

class CryptoData():
    
    def get_n_columns(self, df, columns, n=1):
        '''Shifts & column of a row and adds it in a new column
    
            Parameters:
            df (DataFrame): The dataframe with all the price data 
            columns (string): Name of what column do you want to change
            n (int): Of how many row do you want to shift
            
            Returns:
            df (DataFrame): Return the new dataframe with the new column
            '''
        df = df.copy()
        for col in columns:
            df["n"+str(n)+"_"+col] = df[col].shift(n)
        return(df)
        
    def Indicators(self, pair, limit):
        '''Creation of the dataframe with all the indicators
    
            Parameters:
            pair (array): All the crypto currency do you want to trade
            limit (date): Limit of the date 
            
            Returns:
            df (DataFrame): Return the new dataframe with the indicators
            '''
        df = Bitget().get_more_historical(pair, limit, '1h')
        df.drop(columns=df.columns.difference(['open','high','low','close','volume']), inplace=True)

        
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

        df['ADX'] =ta.trend.adx(high=df['high'], low=df['low'], close = df['close'], window = 20)

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
        
        return(df)
    
    def LoadData(self, pairs, limit):
        '''Load the price data
    
            Parameters:
            pair (array): All the crypto currency do you want to trade
            limit (date): Limit of the date 
            
            Returns:
            df (DataFrame): Return the dataframe with the all the base informations
            '''
        df = []
        for pair in pairs:   
            df_symbol = self.Indicators(pair, limit)
            df_symbol = df_symbol.sort_index()
            df.append(df_symbol)
        return(df)
    

        
        