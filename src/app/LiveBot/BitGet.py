import ccxt
import pandas as pd
import time
from multiprocessing.pool import ThreadPool as Pool
import numpy as np


class Bitget():
    def __init__(self, apiKey=None, secret=None, password=None):
        bitget_auth_object = {
            "apiKey": apiKey,
            "secret": secret,
            "password": password,
            "options": {
                        'defaultType': 'swap'}}
        if bitget_auth_object['secret'] == None:
            self._auth = False
            self._session = ccxt.bitget()
        else:
            self._auth = True
            self._session = ccxt.bitget(bitget_auth_object)
        self.market = self._session.load_markets()

    def get_more_historical(self, symbol, limit, timeframe='1h'):
        '''Récupère les données de maintenant jusqu'à limit'''
        full_result = []
        def worker(i):
            try:
                return self._session.fetch_ohlcv(symbol, timeframe, round(time.time() * 1000) - (i*1000*60*60), limit=100)
            except Exception as err:
                raise Exception("Error on last historical on " + symbol + ": " + str(err))

        pool = Pool()
        full_result = pool.map(worker,range(limit, 0, -100))
        full_result = np.array(full_result).reshape(-1,6)
        result = pd.DataFrame(data=full_result)
        result = result.rename(columns={0: 'timestamp', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'})
        result = result.set_index(result['timestamp'])
        result.index = pd.to_datetime(result.index, unit='ms')
        del result['timestamp']
        return (result.sort_index())

    def place_market_order(self, symbol, side, amount, reduce=False):
        '''Ouvrir un ordre'''
        try:
            return self._session.createOrder(
                symbol, 
                'market', 
                side, 
                self.convert_amount_to_precision(symbol, amount),
                None,
                params={"reduceOnly": reduce,
                        'type':'margin', 
                        'isIsolated': 'TRUE'}
            )
        except BaseException as err:
            raise Exception(err)

    def get_open_position(self,symbol=None): 
        '''Sert à savoir si il y a une position ouverte'''
        try:
            positions = self._session.fetchPositions(symbol)
            truePositions = []
            for position in positions:
                if float(position['contracts']) > 0:
                    truePositions.append(position)
            return truePositions
        except BaseException as err:
            raise TypeError("An error occured in get_open_position", err)
        
    def convert_amount_to_precision(self, symbol, amount):
        '''Permet d'avoir notre compte usdt avec précision'''
        return self._session.amount_to_precision(symbol, amount)
    
    def get_usdt_equity(self):
            try:
                usdt_equity = float(self._session.fetch_balance()["info"][0]["usdtEquity"])
                available = float(self._session.fetch_balance()["info"][0]["available"])
            except BaseException as err:
                raise Exception("An error occured", err)
            try:
                return usdt_equity, available
            except:
                return 0
            
        
if __name__ == '__main__':
    bitget = Bitget()
    