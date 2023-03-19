import requests as rq
from cryptography.fernet import Fernet
import bcrypt

def createUser():
    '''Creating or Uptade an user acount
    
    Parameters:
    
    Returns:
    '''
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
    f = Fernet(key)
    APIkey = "bg_0de09c69d3f3446cebe1d6b67576af05"
    APIsecret = "7a2ff0c5ed09e9caa13d1bee91ff90064dd48f3680c4be4f2bb69f113f95850c"
    APIpassword = "Victor1103"
    APIkey = APIkey.encode()
    APIsecret = APIsecret.encode()
    APIpassword = APIpassword.encode()
    APIkey = f.encrypt(APIkey) 
    APIsecret = f.encrypt(APIsecret)
    APIpassword = f.encrypt(APIpassword)
    APIkey = APIkey.decode()
    APIsecret = APIsecret.decode()
    APIpassword = APIpassword.decode()
    password =  'Victor110'
    salt_rounds = 10
    password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(salt_rounds))
    password = password.decode()
    myrow = {
        'id' : 'victor.bonnaf@gmail.com',
        'password' : password,
        'username' : 'Nafbo',
        'APIkey' : APIkey,
        'APIsecret' : APIsecret,
        'APIpassword' : APIpassword,
        'pairList' : ['BTC/USDT:USDT', 'ETH/USDT:USDT', 'BNB/USDT:USDT', 'XRP/USDT:USDT', 'ADA/USDT:USDT'],
        'maxActivePositions' : 3,
        'running' : True,
        'telegram' : False,
        'chat_id' : 'nan',
        'mode' : 'automatic',
        'withMode' : 'NaN'       
        }
    url = 'https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items'
    rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
    return()

def getUsers(id):
    '''Get an user acount
    
    Parameters: 
    id (string): id of the user
    
    Returns:
    '''
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
    f = Fernet(key)
    url = "https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/{}".format(id)
    r = rq.get(url).json()
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
    f = Fernet(key)

    APIkey = r[0]['APIkey']
    APIsecret = r[0]['APIsecret']
    APIpassword = r[0]['APIpassword']
    APIkey = APIkey.encode()
    APIsecret = APIsecret.encode()
    APIpassword = APIpassword.encode()
    APIkey = f.decrypt(APIkey)
    APIsecret = f.decrypt(APIsecret)
    APIpassword = f.decrypt(APIpassword)
    APIkey = APIkey.decode()
    APIsecret = APIsecret.decode()
    APIpassword = APIpassword.decode()

    myrow = {
        'id' : r[0]['id'],
        'password' : r[0]['password'],
        'username' : r[0]['username'],
        'APIkey' : APIkey,
        'APIsecret' : APIsecret,
        'APIpassword' : APIpassword,
        'pairList' : r[0]['pairList'],
        'maxActivePositions' : r[0]['maxActivePositions'],
        'running' : r[0]['running'],
        'telegram' : r[0]['telegram'],
        'chat_id' : r[0]['chat_id'],
        'mode' : r[0]['mode'],
        'withMode' : r[0]['withMode'] 
        }
    return(myrow)
    

if __name__ == '__main__':
    createUser()
    print(getUsers('victor.bonnaf@gmail.com'))