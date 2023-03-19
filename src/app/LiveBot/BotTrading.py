import sys
sys.path.append("./AVA-Bot")
from src.app.LiveBot.BitGet import *
from src.app.LiveBot.CryptoData import *
from src.app.Telegram.message import *
from src.app.LiveBot.Trade import *
import json
import requests as rq


def BotTrading(pairs, apiKey, secret, password, id, running, maxActivePositions, telegram, chat_id, mode, withMode):
    '''Trading Robot Code with Strategy
    
    Parameters:
    pairs (array): The crypto-currencies you want to trade
    apiKey (string): API Key of Bitget
    secretKey (string): Secret Key of Bitget
    password (string): Paswword of the API Key of Bitget
    id (string): Account ID
    runnig (boolean): True if you want to trade, False if you want to pause the robot
    maxActivePositions (int): Maximum number of orders open at the same time
    
    Returns:
    Nothing
    '''
    bitget = Bitget(
        apiKey=apiKey,
        secret=secret,
        password=password,
        )
    
    url = "https://ttwjs0n6o1.execute-api.eu-west-1.amazonaws.com/items"
    leverage = 1
    takerFee = 0.00051
    wallet, usd_balance = bitget.get_usdt_equity() #usd_balance= ce que j'ai pour le moment/ wallet= wallet total
    activePositions = 0
    positionInProgress = [''] * len(pairs)
    df = CryptoData().LoadData(pairs, 1000)
    index = (df[0].index.values)[-1]
    timestamp = str(int(time.time() * 1000))
    endpoint_marginMode = '/api/mix/v1/account/setMarginMode'
    url_marginMode = "https://api.bitget.com/api/mix/v1/account/setMarginMode"
    url_leverage = 'https://api.bitget.com/api/mix/v1/account/setLeverage'
    endpoint_leverage = '/api/mix/v1/account/setLeverage'
    
    compte = 0
    for pair in pairs:
        body_marginMode = {"symbol": str(pair[:3] + 'USDT_UMCBL'), "marginCoin": "USDT", "marginMode": "fixed"}
        body_str = json.dumps(body_marginMode)
        signStr = bitget.sign(bitget.pre_hash(timestamp, 'POST', endpoint_marginMode, str(body_str)), secret)
        headers_marginMode = {'ACCESS-KEY': apiKey,'ACCESS-SIGN': signStr,'ACCESS-PASSPHRASE': password,'ACCESS-TIMESTAMP': timestamp,'locale': 'en-US','Content-Type': 'application/json'}
        rq.post(url_marginMode, headers=headers_marginMode, data=body_str)
######################################################################
        if pair == 'BTC/USDT:USDT' and mode == 'automatic':
            actualRow = df[compte].iloc[-1]
            previousRow = df[compte].iloc[-2]
            if Trade_Choice.fearAndGreed(actualRow, previousRow) == 2:
                trade = Trade_2()
                takeProfitPercentage = 0.35
                stopLossPercentage = 0.1
                leverage = 5
            elif Trade_Choice.fearAndGreed(actualRow, previousRow) == 1:
                trade = Trade_1()
                takeProfitPercentage = 0.2
                stopLossPercentage = 0.04
                leverage = 3
            elif Trade_Choice.fearAndGreed(actualRow, previousRow) == 3:
                trade = Trade_3()
                takeProfitPercentage = 0.2
                stopLossPercentage = 0.04
                leverage = 2
            else:
                trade = Trade_0()
                takeProfitPercentage = 0.13
                stopLossPercentage = 0.03
                leverage = 1
                
        if mode == 'manual':
            if withMode == 'hard':
                trade = Trade_2()
                takeProfitPercentage = 0.35
                stopLossPercentage = 0.1
                leverage = 5
            elif withMode == 'medium':
                trade = Trade_1()
                takeProfitPercentage = 0.2
                stopLossPercentage = 0.04
                leverage = 3
            elif withMode == 'soft':
                trade = Trade_0()
                takeProfitPercentage = 0.13
                stopLossPercentage = 0.03
                leverage = 1
                
        body_leverageLong = {'symbol': str(pair[:3] + 'USDT_UMCBL'),'marginCoin': 'USDT','leverage': leverage,'holdSide': 'long'}
        body_leverageShort = {'symbol': str(pair[:3] + 'USDT_UMCBL'),'marginCoin': 'USDT','leverage': leverage,'holdSide': 'short'}

        body_str_leverage = json.dumps(body_leverageLong)
        signStr = bitget.sign(bitget.pre_hash(timestamp, 'POST', endpoint_leverage, str(body_str_leverage)), secret)
        headers_leverage = {'ACCESS-KEY': apiKey,'ACCESS-SIGN': signStr,'ACCESS-PASSPHRASE': password,'ACCESS-TIMESTAMP': timestamp,'locale': 'en-US','Content-Type': 'application/json'}
        rq.post(url_leverage, headers=headers_leverage, data=body_str_leverage)
        
        body_str_leverage = json.dumps(body_leverageShort)
        signStr = bitget.sign(bitget.pre_hash(timestamp, 'POST', endpoint_leverage, str(body_str_leverage)), secret)
        headers_leverage = {'ACCESS-KEY': apiKey,'ACCESS-SIGN': signStr,'ACCESS-PASSPHRASE': password,'ACCESS-TIMESTAMP': timestamp,'locale': 'en-US','Content-Type': 'application/json'}
        rq.post(url_leverage, headers=headers_leverage, data=body_str_leverage)
######################################################################  
        positions_data = bitget.get_open_position(pair)
        if positions_data !=[]:
            url2 = "https://ttwjs0n6o1.execute-api.eu-west-1.amazonaws.com/items/{}".format(id)
            r = rq.get(url2).json()
            df2 = pd.DataFrame(r)  
            df2 = df2[df2['symbol'] == pair].iloc[-1]
            if df2['position'] == 'openLong':
                coins = float(positions_data[1]['info']['marketPrice']) * float(positions_data[0]["contractSize"])
            else: 
                coins = float(positions_data[0]['info']['marketPrice']) * float(positions_data[1]["contractSize"])
            myrow = {
                    'id' : id,
                    'sortKey': str(pair+str(index)),
                    'symbol': df2['symbol'],
                    'date': df2['date'],
                    'position': df2['position'],
                    'price': df2['price'],
                    'usdInvest': df2['usdInvest'],
                    'usd': df2['usd'],
                    'coins' : coins,
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
            compte+=1
        else:
            positionInProgress[compte] = ''
            compte+=1
    compte = 0
    for pair in pairs:
        actualRow = df[compte].iloc[-1]
        previousRow = df[compte].iloc[-2]
        
        if positionInProgress[compte] != '' :
            if positionInProgress[compte]['position'] == 'openLong':
                if trade.takeProfit(actualRow, positionInProgress[compte]['takeProfit'], positionInProgress[compte]['position']):
                    try:
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
                            'sortKey':str(pair+str(index)),
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
                        close_long_quantity = float(bitget.convert_amount_to_precision(pair, positionInProgress[compte]['coins']))
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)  
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)
                        rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})                   
                        myrow={} 
                        activePositions -= 1
                        if telegram == True:
                            Telegram(chat_id).messageClose('openLong', str(index), resultat, pair, 'take profit touché', performance, round(positionInProgress[compte]['usdInvest'] * performance), actualRow['close'])
                    except Exception as e:
                        print(e)

                elif trade.stopLoss(actualRow, positionInProgress[compte]['takeProfit'], positionInProgress[compte]['position']):
                    try:
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
                        close_long_quantity = float(bitget.convert_amount_to_precision(pair, positionInProgress[compte]['coins']))
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)  
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)
                        rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                        myrow={} 
                        activePositions -= 1
                        if telegram == True:
                            Telegram(chat_id).messageClose('openLong', str(index), resultat, pair, 'stop loss touché', performance, round(positionInProgress[compte]['usdInvest'] * performance), actualRow['close'])
                    except Exception as e:
                        print(e)
                    
                elif trade.closeLongPosition(actualRow, positionInProgress[compte]['takeProfit'], positionInProgress[compte]['position']):
                    try:
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
                        close_long_quantity = float(bitget.convert_amount_to_precision(pair, positionInProgress[compte]['coins']))
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)  
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)
                        bitget.place_market_order(pair, "sell", close_long_quantity, reduce=True)
                        rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})                 
                        myrow={} 
                        activePositions -= 1
                        if telegram == True:
                            Telegram(chat_id).messageClose('openLong', str(index), resultat, pair, 'indicateur touché', performance, round(positionInProgress[compte]['usdInvest'] * performance), actualRow['close'])
                    except Exception as e:
                        print(e)

            elif positionInProgress[compte]['position'] == 'openShort':
                if trade.takeProfit(actualRow, positionInProgress[compte]['takeProfit'], positionInProgress[compte]['position']):
                    try:
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
                        close_short_quantity = float(bitget.convert_amount_to_precision(pair, positionInProgress[compte]['coins']))
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)  
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)
                        rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                        myrow={} 
                        activePositions -= 1
                        if telegram == True:
                            Telegram(chat_id).messageClose('openShort', str(index), resultat, pair, 'take profit touché', performance, round(positionInProgress[compte]['usdInvest'] * performance), actualRow['close'])
                    except Exception as e:
                        print(e)
                    
                elif trade.stopLoss(actualRow, positionInProgress[compte]['takeProfit'], positionInProgress[compte]['position']):
                    try:
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
                        close_short_quantity = float(bitget.convert_amount_to_precision(pair, positionInProgress[compte]['coins']))
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)  
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)
                        rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                        myrow={} 
                        activePositions -= 1
                        if telegram == True:
                            Telegram(chat_id).messageClose('openShort', str(index), resultat, pair, 'stop loss touché', performance, round(positionInProgress[compte]['usdInvest'] * performance), actualRow['close'])
                    except Exception as e:
                        print(e)

                elif trade.closeShortPosition(actualRow, positionInProgress[compte]['takeProfit'], positionInProgress[compte]['position']):
                    try:
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
                        close_short_quantity = float(bitget.convert_amount_to_precision(pair, positionInProgress[compte]['coins']))
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)  
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)
                        bitget.place_market_order(pair, "buy", close_short_quantity, reduce=True)
                        rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                        myrow={} 
                        activePositions -= 1
                        if telegram == True:
                            Telegram(chat_id).messageClose('openShort', str(index), resultat, pair, 'indicateur touché', performance, round(positionInProgress[compte]['usdInvest'] * performance), actualRow['close'])
                    except Exception as e:
                        print(e)

        if activePositions < maxActivePositions:   
            if trade.openLongPosition(actualRow, previousRow) and positionInProgress[compte] == '' and usd_balance>1 and running == True: 
                f2 = open("src/app/LiveBot/TradeMax.json") #Ajouter AVA-Bot/ pour unbuntu
                TradeMax = json.load(f2)
                f2.close()
                try:    
                    usdMultiplier = 1/(maxActivePositions-activePositions)  
                    usdInvest = usd_balance * usdMultiplier  
                    if usdInvest > TradeMax[pair][str(leverage)]:
                        usdInvest = TradeMax[pair][str(leverage)]
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
                    long_quantity = float(usdInvest / actualRow['close'])
                    bitget.place_market_order(pair, "buy", long_quantity, reduce=False)
                    rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                    myrow={} 
                    activePositions += 1
                    if telegram == True:
                        Telegram(chat_id).messageOpen("openLong", str(index), pair, usdInvest, actualRow['close'], leverage, stopLossValue, takeProfitValue)
                except Exception as e:
                    print(e)
                
            if trade.openShortPosition(actualRow, previousRow) and positionInProgress[compte] == '' and usd_balance>1 and running == True: 
                f2 = open("src/app/LiveBot/TradeMax.json") #Ajouter AVA-Bot/ pour unbuntu
                TradeMax = json.load(f2)
                f2.close()
                try: 
                    usdMultiplier = 1/(maxActivePositions-activePositions)  
                    usdInvest = usd_balance * usdMultiplier 
                    if usdInvest > TradeMax[pair][str(leverage)]:
                        usdInvest = TradeMax[pair][str(leverage)]     
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
                    short_quantity = float(usdInvest / actualRow['close']) 
                    bitget.place_market_order(pair, "sell", short_quantity, reduce=False)
                    rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
                    myrow={} 
                    activePositions += 1
                    if telegram == True:
                        Telegram(chat_id).messageOpen("openShort", str(index), pair, usdInvest, actualRow['close'], leverage, stopLossValue, takeProfitValue)
                except Exception as e:
                    print(e)
                
        compte+=1      
    return
                
        


if __name__ == '__main__':
    id = 'victor.bonnaf@gmail.com'
    url = "https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/{}".format(id)
    r = rq.get(url).json()
    BotTrading(r[0]['pairList'], r[0]['APIkey'], r[0]['APIsecret'], r[0]['APIpassword'], r[0]['id'], r[0]['running'], r[0]['maxActivePositions'], r[0]['telegram'],r[0]['chat_id'], r[0]['mode'], r[0]['withMode'])
