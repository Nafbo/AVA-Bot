import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from src.app.BackTest.All_Indicator import All_Indicator


class BackTest():
    
    def takeProfit(self, row, takeProfitValue):
        if row['high'] > takeProfitValue:
            return(True)
        else:
            return(False)


    def stopLoss(self, row, stopLossValue):
        if row['low'] < stopLossValue:
            return(True)
        else:
            return(False)
      
        
    def trade(self, symbol, timeframe, wallet=100, start_date='2017-01-01T00:00:00'):
        activePositions = ''
        leverage = 3
        makerFee = 0 #0.0002
        takerFee = 0 #0.0007
        longIniPrice = 0
        shortIniPrice = 0
        
        dfTrades = pd.DataFrame(columns=['date', 'symbol','wallet', 'price', 'position'])
        allIndicator = All_Indicator()
        df = allIndicator.indicators(symbol, timeframe)
        df = df.loc[start_date:]
        myrow={}
        myrow_list=[]
        
        for row in range(len(df)):
            actualRow = df.iloc[row]
            previousRow = df.iloc[row-1]
            if activePositions != '':
                if self.stopLoss(actualRow,stopLossValue) and activePositions=='LONG':
                        closePriceWithFee = actualRow['close'] #- takerFee * actualRow['close']
                        pr_change = (closePriceWithFee - longIniPrice) / longIniPrice
                        wallet = wallet + wallet*leverage*pr_change
                        myrow['date'] = df.index[row]
                        myrow['symbol'] = 'BTC/USDT'
                        myrow['wallet'] = wallet
                        myrow['price']  = actualRow['close']
                        myrow['position'] = 'stopLossHit'
                        myrow_list.append(myrow)
                        df_sell = pd.DataFrame(myrow_list)
                        dfTrades = pd.concat([dfTrades,df_sell])
                        myrow={}
                        myrow_list=[]
                        activePositions = ''
                        
                if self.stopLoss(actualRow,stopLossValue) and activePositions=='SHORT':
                        closePriceWithFee = actualRow['close'] #+ takerFee * actualRow['close']
                        pr_change = -(closePriceWithFee - shortIniPrice) / shortIniPrice
                        wallet = wallet + wallet*pr_change*leverage
                        myrow['date'] = df.index[row]
                        myrow['symbol'] = 'BTC/USDT'
                        myrow['wallet'] = wallet
                        myrow['price']  = actualRow['close']
                        myrow['position'] = 'stopLossHit'
                        myrow_list.append(myrow)
                        df_sell = pd.DataFrame(myrow_list)
                        dfTrades = pd.concat([dfTrades,df_sell])
                        myrow={}
                        myrow_list=[]
                        activePositions = ''        
                    
                elif self.takeProfit(actualRow,takeProfitValue) and activePositions=='LONG':
                    closePriceWithFee = actualRow['close'] #- takerFee * actualRow['close']
                    pr_change = (closePriceWithFee - longIniPrice) / longIniPrice
                    wallet = wallet + wallet*pr_change*leverage
                    myrow['date'] = df.index[row]
                    myrow['symbol'] = 'BTC/USDT'
                    myrow['wallet'] = wallet
                    myrow['price']  = actualRow['close']
                    myrow['position'] = 'takeProfitHit'
                    myrow_list.append(myrow)
                    df_sell = pd.DataFrame(myrow_list)
                    dfTrades = pd.concat([dfTrades,df_sell])
                    myrow={}
                    myrow_list=[]
                    activePositions = ''
                
                elif self.takeProfit(actualRow,takeProfitValue) and activePositions=='SHORT':
                    closePriceWithFee = actualRow['close'] #+ takerFee * actualRow['close']
                    pr_change = -(closePriceWithFee - shortIniPrice) / shortIniPrice
                    wallet = wallet + wallet*pr_change*leverage
                    myrow['date'] = df.index[row]
                    myrow['symbol'] = 'BTC/USDT'
                    myrow['wallet'] = wallet
                    myrow['price']  = actualRow['close']
                    myrow['position'] = 'takeProfitHit'
                    myrow_list.append(myrow)
                    df_sell = pd.DataFrame(myrow_list)
                    dfTrades = pd.concat([dfTrades,df_sell])
                    myrow={}
                    myrow_list=[]
                    activePositions = ''
                      
                elif allIndicator.closeLongCondition_Strategy1(actualRow) and activePositions=='LONG':
                    closePriceWithFee = actualRow['close'] #- takerFee * actualRow['close']
                    pr_change = (closePriceWithFee - longIniPrice) / longIniPrice
                    wallet = wallet + wallet*pr_change*leverage
                    myrow['date'] = df.index[row]
                    myrow['symbol'] = 'BTC/USDT'
                    myrow['wallet'] = wallet
                    myrow['price']  = actualRow['close']
                    myrow['position'] = 'closeLong'
                    myrow_list.append(myrow)
                    df_sell = pd.DataFrame(myrow_list)
                    dfTrades = pd.concat([dfTrades,df_sell])
                    myrow={}
                    myrow_list=[]
                    activePositions = ''
                
                elif allIndicator.closeShortCondition_Strategy1(actualRow) and activePositions=='SHORT':
                    closePriceWithFee = actualRow['close'] #+ takerFee * actualRow['close']
                    pr_change = -(closePriceWithFee - shortIniPrice) / shortIniPrice
                    wallet = wallet + wallet*pr_change*leverage
                    myrow['date'] = df.index[row]
                    myrow['symbol'] = 'BTC/USDT'
                    myrow['wallet'] = wallet
                    myrow['price']  = actualRow['close']
                    myrow['position'] = 'closeShort'
                    myrow_list.append(myrow)
                    df_buy = pd.DataFrame(myrow_list)
                    dfTrades = pd.concat([dfTrades,df_buy])
                    myrow={}
                    myrow_list=[]
                    activePositions = ''
                    
            if activePositions=='':
                if allIndicator.openLongCondition_Strategy1(actualRow):
                    longIniPrice = actualRow['close'] #+ takerFee * actualRow['close']
                    myrow['date'] = df.index[row]
                    myrow['symbol'] = 'BTC/USDT'
                    myrow['wallet'] = wallet
                    myrow['price']  = actualRow['close']
                    myrow['position'] = 'openLong'
                    myrow_list.append(myrow)
                    df_buy = pd.DataFrame(myrow_list)
                    dfTrades = pd.concat([dfTrades,df_buy])
                    myrow={}
                    myrow_list=[]
                    activePositions = 'LONG'
                    takeProfitValue = actualRow['close'] + 0.15 * actualRow['close']
                    stopLossValue = actualRow['close'] - 0.04 * actualRow['close']
                
                elif allIndicator.openShortCondition_Strategy1(actualRow):
                    shortIniPrice = actualRow['close'] #- takerFee * actualRow['close']
                    myrow['date'] = df.index[row]
                    myrow['symbol'] = 'BTC/USDT'
                    myrow['wallet'] = wallet
                    myrow['price']  = actualRow['close']
                    myrow['position'] = 'openShort'
                    myrow_list.append(myrow)
                    df_buy = pd.DataFrame(myrow_list)
                    dfTrades = pd.concat([dfTrades,df_buy])
                    myrow={}
                    myrow_list=[]
                    activePositions = 'SHORT'
                    takeProfitValue = actualRow['close'] + 0.15 * actualRow['close']
                    stopLossValue = actualRow['close'] - 0.04 *actualRow['close']
                    
        return(dfTrades.to_csv('test.csv'))            
        
if __name__ == '__main__':
    backtest = BackTest()
    print(backtest.trade('BNB/USDT', '1h',start_date='2021-01-01'))