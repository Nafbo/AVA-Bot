import ta
from datetime import datetime
from src.app.LiveBot.BitGet import *
from src.app.LiveBot.CryptoData import *
from src.app.BackTest.Trade import *
import json
import requests as rq


def BotTrading(pairs):
    production = True
    id = str(13)
    url = "https://ttwjs0n6o1.execute-api.eu-west-1.amazonaws.com/items"
    leverage = 1
    takerFee = 0.00051
    wallet, usd_balance = bitget.get_usdt_equity()
    maxActivePositions = 3
    activePositions = 0
    positionInProgress = [''] * len(pairs)
    df = CryptoData().LoadData(pairs, 1000)
    index = (df[0].index.values)[-1]
    
    
    compte = 0
    for pair in pairs:
######################################################################
        if pair == 'BTC/USDT:USDT':
            actualRow = df[compte].iloc[-1]
            previousRow = df[compte].iloc[-2]
            if Trade_Choice.fearAndGreed(actualRow, previousRow) == 2:
                trade = Trade_2()
                takeProfitPercentage = 0.35
                stopLossPercentage = 0.1
                leverage = 2.5
            elif Trade_Choice.fearAndGreed(actualRow, previousRow) == 1:
                trade = Trade_1()
                takeProfitPercentage = 0.25
                stopLossPercentage = 0.04
                leverage = 2
            elif Trade_Choice.fearAndGreed(actualRow, previousRow) == 3:
                trade = Trade_3()
                takeProfitPercentage = 0.2
                stopLossPercentage = 0.04
                leverage = 2
            else:
                trade = Trade_0()
                takeProfitPercentage = 0.13
                stopLossPercentage = 0.03
                leverage = 1.5
######################################################################  
        positions_data = bitget.get_open_position([pair])
        if pair in positions_data !=[]:
            url = "https://ttwjs0n6o1.execute-api.eu-west-1.amazonaws.com/items/{}".format(id)
            r = rq.get(url).json()
            df2 = pd.DataFrame(r)  
            df2 = df2[df2['symbol'] == pair].iloc[-1]
            myrow = {
                    'id' : id,
                    'sortKey': str(pair+str(index)),
                    'symbol': df2['symbol'],
                    'date': df2['date'],
                    'position': df2['position'],
                    'price': df2['price'],
                    'usdInvest': df2['usdInvest'],
                    'usd': df2['usd'],
                    'coins' : float(positions_data["contracts"]) * float(positions_data["contractSize"]),
                    'fees': df2['fees'],
                    'wallet': df2['wallet'],
                    'takeProfit' : df2['takeProfit'],
                    'stopLoss' : df2['stopLoss'], 
                    'whenBuy': df2['whenBuy'],
                    'resultat' : df2['resultat'],
                    'performance' : df2['performance']
                    }
            positionInProgress[compte] = myrow
            activePositions+=1
        else:
            compte+=1
            
    compte = 0
    for pair in pairs:
        actualRow = df[compte].iloc[-1]
        previousRow = df[compte].iloc[-2]
        
        if positionInProgress[compte] != '' :
            if positionInProgress[compte]['position'] == 'openLong':
                if trade.takeProfit(actualRow, positionInProgress[compte]['takeProfit'], positionInProgress[compte]['position']):
                    sell = round(actualRow['close'] * positionInProgress[compte]['coins'], 2)
                    buy = round(positionInProgress[compte]['price'] * positionInProgress[compte]['coins'],2)
                    if sell - buy > 0:
                        resultat = 'good'
                        performance = ((sell - buy)/buy)*100
                    else:
                        resultat = 'bad'
                        performance = ((sell - buy)/buy)*100
                    myrow = {
                        'id' : id,
                        'sortKey': str(pair+str(index)),
                        'symbol': pair,
                        'date': str(index),
                        'position': "takeProfitHit",
                        'price': actualRow['close'],
                        'usdInvest': positionInProgress[compte]['usdInvest'],
                        'usd': usd_balance,
                        'coins' : 0,
                        'fees': takerFee*positionInProgress[compte]['usdInvest']*leverage,
                        'wallet': wallet,
                        'takeProfit' : positionInProgress[compte]['takeProfit'],
                        'stopLoss' : positionInProgress[compte]['stopLoss'], 
                        'whenBuy': positionInProgress[compte]['date'],
                        'resultat' : resultat,
                        'performance' : performance
                        }
                    rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})                   
                    if production:
                        close_long_quantity = float(bitget.convert_amount_to_precision(pair, positionInProgress[compte]['coins']))
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)
                    myrow={} 
                    activePositions -= 1

                elif trade.stopLoss(actualRow, positionInProgress[compte]['takeProfit'], positionInProgress[compte]['position']):
                    sell = round(actualRow['close'] * positionInProgress[compte]['coins'], 2)
                    buy = round(positionInProgress[compte]['price'] * positionInProgress[compte]['coins'],2)
                    if sell - buy > 0:
                        resultat = 'good'
                        performance = ((sell - buy)/buy)*100
                    else:
                        resultat = 'bad'
                        performance = ((sell - buy)/buy)*100
                    myrow = {
                        'id' : id,
                        'sortKey': str(pair+str(index)),
                        'symbol': pair,
                        'date': str(index),
                        'position': "stopLossHit",
                        'price': actualRow['close'],
                        'usdInvest': positionInProgress[compte]['usdInvest'],
                        'usd': usd_balance,
                        'coins' : 0,
                        'fees': takerFee*positionInProgress[compte]['usdInvest']*leverage,
                        'wallet': wallet,
                        'takeProfit' : positionInProgress[compte]['takeProfit'],
                        'stopLoss' : positionInProgress[compte]['stopLoss'], 
                        'whenBuy': positionInProgress[compte]['date'],
                        'resultat' : resultat,
                        'performance' : performance
                        }
                    rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                    if production:
                        close_long_quantity = float(bitget.convert_amount_to_precision(pair, positionInProgress[compte]['coins']))
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)
                    myrow={} 
                    activePositions -= 1
                    
                elif trade.closeLongPosition(actualRow, positionInProgress[compte]['takeProfit'], positionInProgress[compte]['position']):
                    sell = round(actualRow['close'] * positionInProgress[compte]['coins'], 2)
                    buy = round(positionInProgress[compte]['price'] * positionInProgress[compte]['coins'],2)
                    if sell - buy > 0:
                        resultat = 'good'
                        performance = ((sell - buy)/buy)*100
                    else:
                        resultat = 'bad'
                        performance = ((sell - buy)/buy)*100
                    myrow = {
                        'id' : id,
                        'sortKey': str(pair+str(index)),
                        'symbol': pair,
                        'date': str(index),
                        'position': "closeLong",
                        'price': actualRow['close'],
                        'usdInvest': positionInProgress[compte]['usdInvest'],
                        'usd': usd_balance,
                        'coins' : 0,
                        'fees': takerFee*positionInProgress[compte]['usdInvest']*leverage,
                        'wallet': wallet,
                        'takeProfit' : positionInProgress[compte]['takeProfit'],
                        'stopLoss' : positionInProgress[compte]['stopLoss'], 
                        'whenBuy': positionInProgress[compte]['date'],
                        'resultat' : resultat,
                        'performance' : performance
                        }
                    rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                    if production:
                        close_long_quantity = float(bitget.convert_amount_to_precision(pair, positionInProgress[compte]['coins']))
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)                   
                    myrow={} 
                    activePositions -= 1

            elif positionInProgress[compte]['position'] == 'openShort':
                if trade.takeProfit(actualRow, positionInProgress[compte]['takeProfit'], positionInProgress[compte]['position']):
                    sell = round(actualRow['close'] * positionInProgress[compte]['coins'], 2)
                    buy = round(positionInProgress[compte]['price'] * positionInProgress[compte]['coins'],2)
                    if sell - buy > 0:
                        resultat = 'good'
                        performance = ((sell - buy)/buy)*100
                    else:
                        resultat = 'bad'
                        performance = ((sell - buy)/buy)*100
                    myrow = {
                        'id' : id,
                        'sortKey': str(pair+str(index)),
                        'symbol': pair,
                        'date': str(index),
                        'position': "takeProfitHit",
                        'price': actualRow['close'],
                        'usdInvest': positionInProgress[compte]['usdInvest'],
                        'usd': usd_balance,
                        'coins' : 0,
                        'fees': takerFee*positionInProgress[compte]['usdInvest']*leverage,
                        'wallet': wallet,
                        'takeProfit' : positionInProgress[compte]['takeProfit'],
                        'stopLoss' : positionInProgress[compte]['stopLoss'], 
                        'whenBuy': positionInProgress[compte]['date'],
                        'resultat' : resultat,
                        'performance' : performance
                        }
                    rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                    if production:
                        close_short_quantity = float(bitget.convert_amount_to_precision(pair, positionInProgress[compte]['coins']))
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)
                    myrow={} 
                    activePositions -= 1
                    
                elif trade.stopLoss(actualRow, positionInProgress[compte]['takeProfit'], positionInProgress[compte]['position']):
                    sell = round(actualRow['close'] * positionInProgress[compte]['coins'], 2)
                    buy = round(positionInProgress[compte]['price'] * positionInProgress[compte]['coins'],2)
                    if sell - buy > 0:
                        resultat = 'good'
                        performance = ((sell - buy)/buy)*100
                    else:
                        resultat = 'bad'
                        performance = ((sell - buy)/buy)*100
                    myrow = {
                        'id' : id,
                        'sortKey': str(pair+str(index)),
                        'symbol': pair,
                        'date': str(index),
                        'position': "stopLossHit",
                        'price': actualRow['close'],
                        'usdInvest': positionInProgress[compte]['usdInvest'],
                        'usd': usd_balance,
                        'coins' : 0,
                        'fees': takerFee*positionInProgress[compte]['usdInvest']*leverage,
                        'wallet': wallet,
                        'takeProfit' : positionInProgress[compte]['takeProfit'],
                        'stopLoss' : positionInProgress[compte]['stopLoss'], 
                        'whenBuy': positionInProgress[compte]['date'],
                        'resultat' : resultat,
                        'performance' : performance
                        }
                    rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                    if production:
                        close_short_quantity = float(bitget.convert_amount_to_precision(pair, positionInProgress[compte]['coins']))
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)
                    myrow={} 
                    activePositions -= 1

                elif trade.closeShortPosition(actualRow, positionInProgress[compte]['takeProfit'], positionInProgress[compte]['position']):
                    sell = round(actualRow['close'] * positionInProgress[compte]['coins'], 2)
                    buy = round(positionInProgress[compte]['price'] * positionInProgress[compte]['coins'],2)
                    if sell - buy > 0:
                        resultat = 'good'
                        performance = ((sell - buy)/buy)*100
                    else:
                        resultat = 'bad'
                        performance = ((sell - buy)/buy)*100
                    myrow = {
                        'id' : id,
                        'sortKey': str(pair+str(index)),
                        'symbol': pair,
                        'date': str(index),
                        'position': "closeShort",
                        'price': actualRow['close'],
                        'usdInvest': positionInProgress[compte]['usdInvest'],
                        'usd': usd_balance,
                        'coins' : 0,
                        'fees': takerFee*positionInProgress[compte]['usdInvest']*leverage,
                        'wallet': wallet,
                        'takeProfit' : positionInProgress[compte]['takeProfit'],
                        'stopLoss' : positionInProgress[compte]['stopLoss'], 
                        'whenBuy': positionInProgress[compte]['date'],
                        'resultat' : resultat,
                        'performance' : performance
                        }
                    rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                    if production:
                        close_short_quantity = float(bitget.convert_amount_to_precision(pair, positionInProgress[compte]['coins']))
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)
                    myrow={} 
                    activePositions -= 1

        if activePositions < maxActivePositions:
            if trade.openLongPosition(actualRow, previousRow) and positionInProgress[compte] == '' and usd_balance>1:
                usdMultiplier = 1/(maxActivePositions-activePositions)  
                usdInvest = usd_balance * usdMultiplier      
                coin = (usdInvest * leverage) / actualRow['close']
                takeProfitValue = actualRow['close'] + takeProfitPercentage * actualRow['close']
                stopLossValue = actualRow['close'] - stopLossPercentage *actualRow['close']
                myrow = {
                        'id' : id,
                        'sortKey': str(pair+str(index)),
                        'symbol': pair,
                        'date': str(index),
                        'position': "openLong",
                        'price': actualRow['close'],
                        'usdInvest': usdInvest,
                        'usd': usd_balance,
                        'coins' : coin,
                        'fees': takerFee*usdInvest*leverage,
                        'wallet': wallet,
                        'takeProfit' : takeProfitValue,
                        'stopLoss' : stopLossValue, 
                        'whenBuy': 'nan',
                        'resultat' : 'nan',
                        'performance' : 'nan'
                        }
                rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                long_quantity_in_usd = usdInvest * leverage
                long_quantity = float(bitget.convert_amount_to_precision(pair, float(bitget.convert_amount_to_precision(pair, long_quantity_in_usd / actualRow['close']))))
                if production:
                    bitget.place_market_order(pair, "buy", long_quantity, reduce=False)
                myrow={} 
                activePositions += 1
                
            if trade.openShortPosition(actualRow, previousRow) and positionInProgress[compte] == '' and usd_balance>1:
                usdMultiplier = 1/(maxActivePositions-activePositions)  
                usdInvest = usd_balance * usdMultiplier      
                coin = (usdInvest * leverage) / actualRow['close']
                takeProfitValue = actualRow['close'] - takeProfitPercentage * actualRow['close']
                stopLossValue = actualRow['close'] + stopLossPercentage *actualRow['close']
                myrow = {
                        'id' : id,
                        'sortKey': str(pair+str(index)),
                        'symbol': pair,
                        'date': str(index),
                        'position': "openShort",
                        'price': actualRow['close'],
                        'usdInvest': usdInvest,
                        'usd': usd_balance,
                        'coins' : coin,
                        'fees': takerFee*usdInvest*leverage,
                        'wallet': wallet,
                        'takeProfit' : takeProfitValue,
                        'stopLoss' : stopLossValue, 
                        'whenBuy': 'nan',
                        'resultat' : 'nan',
                        'performance' : 'nan'
                        }
                rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                short_quantity_in_usd = usdInvest * leverage
                short_quantity = float(bitget.convert_amount_to_precision(pair, float(bitget.convert_amount_to_precision(pair, short_quantity_in_usd / actualRow['close']))))
                if production:
                    bitget.place_market_order(pair, "sell", short_quantity, reduce=False)
                myrow={} 
                activePositions += 1
                
        compte+=1
        
    return
                
        


if __name__ == '__main__':
    f = open("src/app/LiveBot/secret.json")
    secret = json.load(f)
    f.close()

    bitget = Bitget(
        apiKey=secret["bitget_exemple"]["apiKey"],
        secret=secret["bitget_exemple"]["secret"],
        password=secret["bitget_exemple"]["password"])
    pairList = ['BTC/USDT:USDT', 'ETH/USDT:USDT', 'BNB/USDT:USDT', 'XRP/USDT:USDT', 'ADA/USDT:USDT']
    BotTrading(pairList)
