import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from src.app.BackTest.All_indicator import All_indicator
from src.app.BackTest.Trade import Trade


class BackTest():
    
    def trade(self, symbols, timeframe, usd=100, start_date='2019-01-01T00:00:00'):
        allIndicator = All_indicator()
        trade = Trade()
        
        # -- Load Data --
        df = []
        dfTrades = pd.DataFrame()
        for pair in symbols:   
            df_symbol = allIndicator.indicators(pair, timeframe)
            df_symbol = df_symbol.loc[start_date:]
            df_symbol = df_symbol.sort_index()
            df.append(df_symbol)

        # -- Parameters --
        activePositions = 0
        maxActivePositions = 3
        
        myrow_list=[]
        walletUsdArray = [0] * len(symbols)
        positionInProgress = [''] * len(df)
        lastIndex = df[0].index.values[1]
        
        
        for index, row in df[0].iterrows(): 
            if positionInProgress != [''] * len(df):
                for i in range(len(df)): 
                    actualRow = df[i].loc[index]
                    if positionInProgress[i] != '':
                        if trade.takeProfit(actualRow, positionInProgress[i]['takeProfit']):
                            usd = usd + positionInProgress[i]['takeProfit'] * positionInProgress[i]['coins']
                            sell = round(positionInProgress[i]['takeProfit'] * positionInProgress[i]['coins'], 2)
                            buy = round(positionInProgress[i]['price'] * positionInProgress[i]['coins'],2)
                            walletUsdArray[i] = 0
                            if sell - buy > 0:
                                resultat = 'good'
                                performance = ((sell - buy)/buy)*100
                            else:
                                resultat = 'bad'
                                performance = ((sell - buy)/buy)*100
                            myrow = {
                                'symbol': symbols[i],
                                'date': index,
                                'position': "takeProfitHit",
                                'price': positionInProgress[i]['takeProfit'],
                                'usd': usd,
                                'coins': 0,
                                'wallet': sum(walletUsdArray) + usd,
                                'takeProfit' : positionInProgress[i]['takeProfit'],
                                'stopLoss' : positionInProgress[i]['stopLoss'], 
                                'whenBuy': positionInProgress[i]['date'],
                                'resultat' : resultat,
                                'performance' : performance
                                }
                            myrow_list.append(myrow)
                            df_buy = pd.DataFrame(myrow_list)
                            dfTrades = pd.concat([dfTrades,df_buy])
                            myrow_list=[]  
                            myrow={} 
                            activePositions -= 1
                            positionInProgress[i] = ''
                            
                            
                        elif trade.stopLoss(actualRow, positionInProgress[i]['stopLoss']):
                            usd = usd + positionInProgress[i]['stopLoss'] * positionInProgress[i]['coins']
                            sell = round(positionInProgress[i]['stopLoss'] * positionInProgress[i]['coins'],2)
                            buy = round(positionInProgress[i]['price'] * positionInProgress[i]['coins'],2)
                            walletUsdArray[i] = 0
                            if sell - buy > 0:
                                resultat = 'good'
                                performance = ((sell - buy)/buy)*100
                            else:
                                resultat = 'bad'
                                performance = ((sell - buy)/buy)*100
                            myrow = {
                                'symbol': symbols[i],
                                'date': index,
                                'position': "stopLossHit",
                                'price': positionInProgress[i]['stopLoss'],
                                'usd': usd,
                                'coins': 0,
                                'wallet': sum(walletUsdArray) + usd,
                                'takeProfit' : positionInProgress[i]['takeProfit'],
                                'stopLoss' : positionInProgress[i]['stopLoss'], 
                                'whenBuy': positionInProgress[i]['date'],
                                'resultat' : resultat,
                                'performance' : performance
                                }
                            myrow_list.append(myrow)
                            df_buy = pd.DataFrame(myrow_list)
                            dfTrades = pd.concat([dfTrades,df_buy])
                            myrow_list=[]  
                            myrow={} 
                            activePositions -= 1
                            positionInProgress[i] = ''
                            
                            
                        elif trade.sellCondition(actualRow):
                            usd = usd + actualRow['close'] * positionInProgress[i]['coins']
                            sell = round(actualRow['close'] * positionInProgress[i]['coins'],2)
                            buy = round(positionInProgress[i]['price'] * positionInProgress[i]['coins'], 2)
                            walletUsdArray[i] = 0
                            if sell - buy > 0:
                                resultat = 'good'
                                performance = ((sell - buy)/buy)*100
                            else:
                                resultat = 'bad'
                                performance = ((sell - buy)/buy)*100
                            myrow = {
                                'symbol': symbols[i],
                                'date': index,
                                'position': "Sell",
                                'price': actualRow['close'],
                                'usd': usd,
                                'coins': 0,
                                'wallet': sum(walletUsdArray) + usd,
                                'takeProfit' : positionInProgress[i]['takeProfit'],
                                'stopLoss' : positionInProgress[i]['stopLoss'], 
                                'whenBuy': positionInProgress[i]['date'],
                                'resultat' : resultat,
                                'performance' : performance
                                }
                            myrow_list.append(myrow)
                            df_buy = pd.DataFrame(myrow_list)
                            dfTrades = pd.concat([dfTrades,df_buy])
                            myrow_list=[]  
                            myrow={} 
                            activePositions -= 1
                            positionInProgress[i] = ''
                              
                            
            if activePositions < maxActivePositions:  
                for i in range(len(df)):
                    actualRow = df[i].loc[index]
                    previousRow = df[i].loc[lastIndex]
                    if trade.buyCondition(actualRow, previousRow) and positionInProgress[i] == '' and usd>1:
                        usdMultiplier = 1/(maxActivePositions-activePositions)        
                        coin = (usd * usdMultiplier) / actualRow['close']
                        usd = usd - (usd * usdMultiplier)
                        walletUsdArray[i] = coin * actualRow['close']
                        takeProfitValue = actualRow['close'] + 0.15 * actualRow['close']
                        stopLossValue = actualRow['close'] - 0.04 *actualRow['close']
                        myrow = {
                            'symbol': symbols[i],
                            'date': index,
                            'position': "Buy",
                            'price': actualRow['close'],
                            'usd': usd,
                            'coins': coin,
                            'wallet': sum(walletUsdArray) + usd,
                            'takeProfit' : takeProfitValue,
                            'stopLoss' : stopLossValue
                        }
                    
                        positionInProgress[i] = myrow
                        myrow_list.append(myrow)
                        df_buy = pd.DataFrame(myrow_list)
                        dfTrades = pd.concat([dfTrades,df_buy])
                        myrow_list=[]  
                        myrow={} 
                        activePositions += 1
            lastIndex = index 
        # dfTrades = dfTrades.set_index(dfTrades['date'])
        # del dfTrades['date']
        return(dfTrades,positionInProgress)                  
    
    
    def buyAndHold(self, symbols, timeframe, usd=100, start_date='2019-01-01T00:00:00'):
        allIndicator = All_indicator()
        df = pd.DataFrame()
        dfBuyAnsHold = pd.DataFrame()
        myrow_list=[] 
    
        df = []
        for pair in symbols:   
            df_symbol = allIndicator.indicators(pair, timeframe)
            df_symbol = df_symbol.loc[start_date:]
            df_symbol = df_symbol.sort_index()
            df.append(df_symbol)
        
        usd = usd / len(symbols)      
        for i in range(len(symbols)):
            firstRow = df[i].iloc[0]
            lastRow = df[i].iloc[-1]      
            coin = usd / firstRow['close']
            usdFinal = lastRow['close'] * coin
            myrow = {
                 'symbol': symbols[i],
                 'position' : 'buyAndHold',
                 'startingBalance' : usd,
                 'finalBalance' : usdFinal
             }
            myrow_list.append(myrow)
            df_buy_and_hold = pd.DataFrame(myrow_list)
            dfBuyAnsHold = pd.concat([dfBuyAnsHold,df_buy_and_hold])
            myrow_list=[]  
            myrow={} 
        return(dfBuyAnsHold)
        
        
        
        
if __name__ == '__main__':
    backtest = BackTest()
    pairList = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT']
    print(backtest.trade(pairList, '1h', start_date='2022-01-01'))
    # print(backtest.buyAndHold(pairList, '1h', start_date='2017-01-01'))