import ccxt
import pandas as pd
import os
import pickle
from time import gmtime, strftime
from datetime import datetime
import time



class DataBase():
    def __init__(self, session=ccxt.binance(), path_to_data="src/app/DataBase/Crypto_Database/"):
        self._session = session
        self.exchange_name = str(self._session)
        self.path_to_data = path_to_data
        
        
    def get_historical_from_api(self, symbol, timeframe, start_date, limit=1000):
        start_date = self._session.parse8601(start_date)
        temp_data = self._session.fetch_ohlcv(symbol, timeframe, start_date, limit=limit)
        dtemp = pd.DataFrame(temp_data)
        result = dtemp.rename(columns={0: 'timestamp', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'})
        result = result.set_index(result['timestamp'])
        result.index = pd.to_datetime(result.index, unit='ms')
        del result['timestamp']
        while datetime.strftime(result.index[-1], '%Y-%m-%d') != strftime('%Y-%m-%d', gmtime()):
            start_date = str(result.index[-1])
            start_date = self._session.parse8601(start_date)
            time.sleep(2)
            temp_data = self._session.fetch_ohlcv(symbol, timeframe, start_date, limit=limit)
            dtNew = pd.DataFrame(temp_data)
            dtNew = dtNew.rename(columns={0: 'timestamp', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'})
            dtNew = dtNew.set_index(dtNew['timestamp'])
            dtNew.index = pd.to_datetime(dtNew.index, unit='ms')
            del dtNew['timestamp']
            dfFinal = pd.concat([result,dtNew])
            result = dfFinal
            dtNew = pd.DataFrame()
        result = result.drop_duplicates()
        return (result)
    
    
    def download_data(self, symbols, timeframes, start_date='2017-01-01T00:00:00'):
        for symbol in symbols:
            for tf in timeframes:
                print(f'-> downloding symbol {symbol} for timeframe {tf}')
                df = self.get_historical_from_api(symbol=symbol, timeframe=tf, start_date=start_date)
                if df is not None and len(df) > 0:
                    fileName = self.path_to_data+tf+'/'+symbol.replace('/','')+'.p'
                    os.makedirs(self.path_to_data+tf, exist_ok=True)
                    if os.path.exists(fileName):
                        os.remove(fileName)
                    dbfile = open(fileName, 'ab')
                    pickle.dump(df, dbfile)					
                    dbfile.close()
                else:
                    return('Error empty dataframe on', symbol)
        return("All it's download")
      
                
    def update_data(self, symbols, timeframes):
        for symbol in symbols:
            for tf in timeframes:
                fileName = self.path_to_data+tf+'/'+symbol.replace('/','')+'.p'
                with open(fileName, 'rb') as file:
                    dfOrigin = pickle.load(file)
                start_date = dfOrigin.index[-1]        
                dfNew = self.get_historical_from_api(symbol, tf, start_date)
                dfNew = dfNew.loc[start_date:].iloc[1:]
                dfFinal = pd.concat([dfOrigin,dfNew]) 
                dfFinal = dfFinal.drop_duplicates()
                with open(fileName, 'wb') as file:
                    pickle.dump(dfFinal, file)
        return("All it's update")   
       
       
             
if __name__ == '__main__':
    database = DataBase(session=ccxt.binance())
    pairList = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT']
    # print(database.get_historical_from_api('ADA/USDT', '1h', '2017-01-01T00:00:00'))
    print(database.download_data(pairList, ['1h']))
    # print(database.update_data(pairList, ['1h']))