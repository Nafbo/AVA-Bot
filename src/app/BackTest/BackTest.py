import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from src.app.BackTest.All_indicator import All_indicator
from src.app.BackTest.Trade import Trade

class BackTest():
      
        
    def trade(self, symbols, timeframe, usd=100, start_date='2017-01-01T00:00:00'):
        # -- Parameters --
        activePositions = 1
        maxActivePositions = 3
        walletCoinArray = [0] * len(symbols)
        walletUsdArray = [0] * len(symbols)
        dfTrades = pd.DataFrame(columns=['date', 'symbol','wallet', 'coins', 'price', 'position'])
        allIndicator = All_indicator()
        myrow={}
        myrow_list=[]
        
        # -- Load Data --
        dfList = []
        for pair in symbols:    
            df = allIndicator.indicators(pair, timeframe)
            df = df.loc[start_date:]
            dfList.append(df)
        
        for cryptoCurrency in dfList:
            for row in range(len(cryptoCurrency)):
                actualRow = cryptoCurrency.iloc[row]            
                
                # elif allIndicator.openShortCondition_Strategy1(actualRow):
                #     shortIniPrice = actualRow['close'] #- takerFee * actualRow['close']
                #     myrow['date'] = df.index[row]
                #     myrow['symbol'] = 'BTC/USDT'
                #     myrow['wallet'] = wallet
                #     myrow['price']  = actualRow['close']
                #     myrow['position'] = 'openShort'
                #     myrow_list.append(myrow)
                #     df_buy = pd.DataFrame(myrow_list)
                #     dfTrades = pd.concat([dfTrades,df_buy])
                #     myrow={}
                #     myrow_list=[]
                #     activePositions = 'SHORT'
                #     takeProfitValue = actualRow['close'] + 0.15 * actualRow['close']
                #     stopLossValue = actualRow['close'] - 0.04 *actualRow['close']
                    
        return(dfTrades)            
        
if __name__ == '__main__':
    backtest = BackTest()
    pairList = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT']
    print(backtest.trade(pairList[:1], '1h',start_date='2021-01-01'))