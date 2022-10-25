import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from src.app.BackTest.All_Indicator import All_Indicator


class BackTest():
    
    def takeProfit(self, row, takeProfitValue):
        if row['high'] > takeProfitValue:
            return(True)


    def stopLoss(self, row, stopLossValue):
        if row['low'] < stopLossValue:
            return(True)
      
        
    def trade(self, symbol, timeframe, usd=100, coin=0):
        activePositions = 0
        dfTrades = pd.DataFrame(columns=['date', 'symbol','coin', 'usd', 'price', 'position'])
        allIndicator = All_Indicator()
        df = allIndicator.indicators(symbol, timeframe)
        myrow={}
        myrow_list=[]
        
        for row in range(len(df)):
            actualRow = df.iloc[row]
            if coin != 0:
                if self.stopLoss(actualRow,stopLossValue):
                    usd = coin * actualRow['close']
                    coin = 0
                    myrow['date'] = df.index[row]
                    myrow['symbol'] = 'BTC/USDT'
                    myrow['coin'] = coin
                    myrow['usd'] = usd
                    myrow['price']  = actualRow['close']
                    myrow['position'] = 'stopLossHit'
                    myrow_list.append(myrow)
                    df_sell = pd.DataFrame(myrow_list)
                    dfTrades = pd.concat([dfTrades,df_sell])
                    myrow={}
                    myrow_list=[]
                    activePositions = 0
                
                elif self.takeProfit(actualRow,takeProfitValue):
                    usd = coin * actualRow['close']
                    coin = 0
                    myrow['date'] = df.index[row]
                    myrow['symbol'] = 'BTC/USDT'
                    myrow['coin'] = coin
                    myrow['usd'] = usd
                    myrow['price']  = actualRow['close']
                    myrow['position'] = 'takeProfitHit'
                    myrow_list.append(myrow)
                    df_sell = pd.DataFrame(myrow_list)
                    dfTrades = pd.concat([dfTrades,df_sell])
                    myrow={}
                    myrow_list=[]
                    activePositions = 0
                    
                elif allIndicator.sellCondition_Strategy1(actualRow) and activePositions==1:
                    usd = coin * actualRow['close']
                    coin = 0
                    myrow['date'] = df.index[row]
                    myrow['symbol'] = 'BTC/USDT'
                    myrow['coin'] = coin
                    myrow['usd'] = usd
                    myrow['price']  = actualRow['close']
                    myrow['position'] = 'sell'
                    myrow_list.append(myrow)
                    df_sell = pd.DataFrame(myrow_list)
                    dfTrades = pd.concat([dfTrades,df_sell])
                    myrow={}
                    myrow_list=[]
                    activePositions = 0
                
            if allIndicator.buyCondition_Strategy1(actualRow) and activePositions==0:
                coin = usd / actualRow['close']
                usd = 0
                myrow['date'] = df.index[row]
                myrow['symbol'] = 'BTC/USDT'
                myrow['coin'] = coin
                myrow['usd'] = usd
                myrow['price']  = actualRow['close']
                myrow['position'] = 'buy'
                myrow_list.append(myrow)
                df_buy = pd.DataFrame(myrow_list)
                dfTrades = pd.concat([dfTrades,df_buy])
                myrow={}
                myrow_list=[]
                activePositions = 1
                takeProfitValue = actualRow['close'] + 0.15 * actualRow['close']
                stopLossValue = actualRow['close'] - 0.015 * actualRow['close']
        return(dfTrades)            
        
if __name__ == '__main__':
    backtest = BackTest()
    print(backtest.trade('BTC/USDT', '1h'))