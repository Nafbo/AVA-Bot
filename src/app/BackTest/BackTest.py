import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from src.app.BackTest.All_indicator import All_indicator
from src.app.BackTest.Trade import Trade


class BackTest():
    
    def trade(self, symbols, timeframe, usd=100, start_date='2019-01-01T00:00:00', leverage=1):
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
        takerFee = 0.00051
        
        myrow_list=[]
        usdArray = [usd]
        walletUsdArray = [0] * len(symbols)
        positionInProgress = [''] * len(df)
        lastIndex = df[0].index.values[1]
        
        
        for index, row in df[0].iterrows(): 
            if positionInProgress != [''] * len(df):
                for i in range(len(df)): 
                    actualRow = df[i].loc[index]
                    if positionInProgress[i] != '':
                        
                        if positionInProgress[i]['position'] == 'openLong':
                            
                            if actualRow['low'] < positionInProgress[i]['liquidation']:
                                print('/!\ YOUR LONG HAVE BEEN LIQUIDATED the',index)
                                break
                            
                            if trade.takeProfit(actualRow, positionInProgress[i]['takeProfit'], positionInProgress[i]['position']):
                                pr_change = ((actualRow['close']-takerFee*actualRow['close']) - positionInProgress[i]['price']) / positionInProgress[i]['price']
                                usd = positionInProgress[i]['usdInvest'] + positionInProgress[i]['usdInvest']*pr_change*leverage  
                                usdArray.append(usdArray[-1]+usd)                          
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
                                    'usdInvest': usdInvest,
                                    'usd': usdArray[-1],
                                    'coins' : 0,
                                    'fees': takerFee*usdInvest*leverage,
                                    'wallet': sum(walletUsdArray) + usdArray[-1],
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
                                
                                
                            elif trade.stopLoss(actualRow, positionInProgress[i]['stopLoss'], positionInProgress[i]['position']):
                                pr_change = ((actualRow['close']-takerFee*actualRow['close']) - positionInProgress[i]['price']) / positionInProgress[i]['price']
                                usd = positionInProgress[i]['usdInvest'] + positionInProgress[i]['usdInvest']*pr_change*leverage      
                                usdArray.append(usdArray[-1]+usd)              
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
                                    'usdInvest': usdInvest,
                                    'usd': usdArray[-1],
                                    'coins' : 0,
                                    'fees': takerFee*usdInvest*leverage,
                                    'wallet': sum(walletUsdArray) + usdArray[-1],
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
                                
                                
                            elif trade.closeLongPosition(actualRow) and positionInProgress[i] == 'openLong':
                                pr_change = ((actualRow['close']-takerFee*actualRow['close']) - positionInProgress[i]['price']) / positionInProgress[i]['price']
                                usd = positionInProgress[i]['usdInvest'] + positionInProgress[i]['usdInvest']*pr_change*leverage 
                                usdArray.append(usdArray[-1]+usd)                        
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
                                    'position': "closeLong",
                                    'price': actualRow['close'],
                                    'usdInvest': usdInvest,
                                    'usd': usdArray[-1],
                                    'coins' : 0,
                                    'fees': takerFee*usdInvest*leverage,
                                    'wallet': sum(walletUsdArray) + usdArray[-1],
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
                                
                                
                        elif positionInProgress[i]['position'] == 'openShort':
                            
                            if actualRow['high'] > positionInProgress[i]['liquidation']:
                                print('/!\ YOUR SHORT HAVE BEEN LIQUIDATED the',index)
                                break
                                
                            if trade.takeProfit(actualRow, positionInProgress[i]['takeProfit'], positionInProgress[i]['position']):
                                pr_change = -((actualRow['close']+takerFee*actualRow['close']) - positionInProgress[i]['price']) / positionInProgress[i]['price']
                                usd = positionInProgress[i]['usdInvest'] + positionInProgress[i]['usdInvest']*pr_change*leverage  
                                usdArray.append(usdArray[-1]+usd)                        
                                sell = round((positionInProgress[i]['price'] + (positionInProgress[i]['price'] - positionInProgress[i]['takeProfit'])) * positionInProgress[i]['coins'],2)
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
                                    'position': "takeProfitHit",
                                    'price': positionInProgress[i]['takeProfit'],
                                    'usdInvest': usdInvest,
                                    'usd': usdArray[-1],
                                    'coins' : 0,
                                    'fees': takerFee*usdInvest*leverage,
                                    'wallet': sum(walletUsdArray) + usdArray[-1],
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
                                
                                
                            elif trade.stopLoss(actualRow, positionInProgress[i]['stopLoss'], positionInProgress[i]['position']):
                                pr_change = -((actualRow['close']+takerFee*actualRow['close']) - positionInProgress[i]['price']) / positionInProgress[i]['price']
                                usd = positionInProgress[i]['usdInvest'] + positionInProgress[i]['usdInvest']*pr_change*leverage                                 
                                usdArray.append(usdArray[-1]+usd)
                                sell = round((positionInProgress[i]['price'] + (positionInProgress[i]['price'] - positionInProgress[i]['stopLoss'])) * positionInProgress[i]['coins'],2)
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
                                    'position': "stopLossHit",
                                    'price': positionInProgress[i]['stopLoss'],
                                    'usdInvest': usdInvest,
                                    'usd': usdArray[-1],
                                    'coins' : 0,
                                    'fees': takerFee*usdInvest*leverage,
                                    'wallet': sum(walletUsdArray) + usdArray[-1],
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
                                
                            elif trade.closeShortPosition(actualRow) :
                                pr_change = -((actualRow['close']+takerFee*actualRow['close']) - positionInProgress[i]['price']) / positionInProgress[i]['price']
                                usd = positionInProgress[i]['usdInvest'] + positionInProgress[i]['usdInvest']*pr_change*leverage
                                usdArray.append(usdArray[-1]+usd)
                                sell = round((positionInProgress[i]['price'] + (positionInProgress[i]['price'] - actualRow['close'])) * positionInProgress[i]['coins'],2)
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
                                    'position': "closeShort",
                                    'price': actualRow['close'],
                                    'usdInvest': usdInvest,
                                    'usd': usdArray[-1],
                                    'coins' : 0,
                                    'fees': takerFee*usdInvest*leverage,
                                    'wallet': sum(walletUsdArray) + usdArray[-1],
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
                    
                    if trade.openLongPosition(actualRow, previousRow) and positionInProgress[i] == '' and usdArray[-1]>1:
                        usdMultiplier = 1/(maxActivePositions-activePositions)  
                        usdInvest = usdArray[-1] * usdMultiplier      
                        coin = (usdInvest * leverage) / actualRow['close']
                        usdArray.append(usdArray[-1] - usdInvest)
                        walletUsdArray[i] = usdInvest
                        takeProfitValue = actualRow['close'] + 0.1 * actualRow['close']
                        stopLossValue = actualRow['close'] - 0.04 *actualRow['close']
                        liquidation = actualRow['close'] - (usdInvest/coin)
                        myrow = {
                            'symbol': symbols[i],
                            'date': index,
                            'position': "openLong",
                            'price': actualRow['close']+takerFee*actualRow['close'],
                            'usdInvest': usdInvest,
                            'usd': usdArray[-1],
                            'coins' : coin,
                            'fees': takerFee*usdInvest*leverage,
                            'wallet': sum(walletUsdArray) + usdArray[-1],
                            'liquidation' : liquidation,
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
                        
                    elif trade.openShortPosition(actualRow, previousRow) and positionInProgress[i] == '' and usdArray[-1]>1:
                        usdMultiplier = 1/(maxActivePositions-activePositions)  
                        usdInvest = usdArray[-1] * usdMultiplier      
                        coin = (usdInvest * leverage) / actualRow['close']
                        usdArray.append(usdArray[-1] - usdInvest)
                        walletUsdArray[i] = usdInvest
                        liquidation = actualRow['close'] + (usdInvest/coin)
                        takeProfitValue = actualRow['close'] - 0.1 * actualRow['close']
                        stopLossValue = actualRow['close'] + 0.04 *actualRow['close']
                        myrow = {
                            'symbol': symbols[i],
                            'date': index,
                            'position': "openShort",
                            'price': actualRow['close']-takerFee*actualRow['close'],
                            'usdInvest': usdInvest,
                            'usd' : usdArray[-1],
                            'coins': coin,
                            'fees': takerFee*usdInvest*leverage,
                            'wallet': sum(walletUsdArray) + usdArray[-1],
                            'liquidation':liquidation,
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
        dfTrades = dfTrades.set_index(dfTrades['date'])
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
    print(backtest.trade(pairList, '1h', start_date='2022-01-01', leverage=2))
    # print(backtest.buyAndHold(pairList, '1h', start_date='2017-01-01'))