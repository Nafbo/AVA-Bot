import sys
sys.path.append("./AVA-Bot")
import requests as rq
import json
from src.app.LiveBot.BotTrading import BotTrading

def main(pairs, apiKey, secret, password, id, running, maxActivePositions, telegram, chat_id, mode, withMode):
    BotTrading(pairs, apiKey, secret, password, id, running, maxActivePositions, telegram, chat_id, mode, withMode)
    return

if __name__ == '__main__':
    # url = "https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items"
    # r1 = rq.get(url).json()
    # for i in range(len(r1)):
    #     url = "https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/{}".format(r1[i]['id'])
    #     r = rq.get(url).json()
    #     main(r[0]['pairList'], r[0]['APIkey'], r[0]['APIsecret'], r[0]['APIpassword'], r[0]['id'], r[0]['running'], r[0]['maxActivePositions'], r[0]['telegram'],r[0]['chat_id'], r[0]['mode'], r[0]['withMode'])
   
    id = 'victor.bonnaf@gmail.com'
    url = "https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/{}".format(id)
    r = rq.get(url).json()
  
    main(r[0]['pairList'], r[0]['APIkey'], r[0]['APIsecret'], r[0]['APIpassword'], r[0]['id'], r[0]['running'], r[0]['maxActivePositions'], r[0]['telegram'],r[0]['chat_id'],r[0]['mode'], r[0]['withMode'])