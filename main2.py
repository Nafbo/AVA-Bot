import sys
sys.path.append("./AVA-Bot")
import requests as rq
import json
from src.app.LiveBot.BotTrading2 import BotTrading2
from src.app.Cryptage.User import getUsers

def main(pairs, apiKey, secret, password, id, running, maxActivePositions, telegram, chat_id, mode, withMode):
    BotTrading2(pairs, apiKey, secret, password, id, running, maxActivePositions, telegram, chat_id, mode, withMode)
    return

if __name__ == '__main__':
    # url = "https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items"
    # r1 = rq.get(url).json()
    # for i in range(len(r1)):
    #     r = getUsers(r1[i]['id'])
    #     main(r['pairList'], r['APIkey'], r['APIsecret'], r['APIpassword'], r['id'], r['running'], r['maxActivePositions'], r['telegram'],r['chat_id'], r['mode'], r['withMode'])
   
    id = 'victor.bonnaf@gmail.com'
    r = getUsers(id)
    main(r['pairList'], r['APIkey'], r['APIsecret'], r['APIpassword'], r['id'], r['running'], r['maxActivePositions'], r['telegram'],r['chat_id'],r['mode'], r['withMode'])