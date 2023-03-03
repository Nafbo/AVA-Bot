import requests as rq

def User():
    '''Creating or Uptade an user acount
    
    Parameters:
    
    Returns:
    '''
    myrow = {
        'id' : 'victor.bonnaf@gmail.com',
        'password' : 'Victor110',
        'APIkey' : "bg_0de09c69d3f3446cebe1d6b67576af05",
        'APIsecret' : "7a2ff0c5ed09e9caa13d1bee91ff90064dd48f3680c4be4f2bb69f113f95850c",
        'APIpassword' : "Victor1103",
        'pairList' : ['BTC/USDT:USDT', 'ETH/USDT:USDT', 'BNB/USDT:USDT', 'XRP/USDT:USDT', 'ADA/USDT:USDT'],
        'maxActivePositions' : 3,
        'running' : True
        }
    url = 'https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items'
    rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
    return()


if __name__ == '__main__':
    User()