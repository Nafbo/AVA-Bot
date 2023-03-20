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
    myrow (json): all the account information
    '''
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
    # key = 'ma_clé_secrète'
    # key = key.encode()
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
    
from Crypto import Random
from Crypto.Cipher import AES
import base64
from hashlib import md5

BLOCK_SIZE = 16

def pad(data):
    length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + (chr(length)*length).encode()

def unpad(data):
    return data[:-(data[-1] if type(data[-1]) == int else ord(data[-1]))]

def bytes_to_key(data, salt, output=48):
    assert len(salt) == 8, len(salt)
    data += salt
    key = md5(data).digest()
    final_key = key
    while len(final_key) < output:
        key = md5(key + data).digest()
        final_key += key
    return final_key[:output]

def encrypt(message, passphrase):
    salt = Random.new().read(8)
    key_iv = bytes_to_key(passphrase, salt, 32+16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(b"Salted__" + salt + aes.encrypt(pad(message).decode()))

def decrypt(encrypted, passphrase):
    encrypted = base64.b64decode(encrypted)
    assert encrypted[0:8] == b"Salted__"
    salt = encrypted[8:16]
    key_iv = bytes_to_key(passphrase, salt, 32+16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(encrypted[16:]))


password = "asdbchituenHGUBUYfdoznchioryoizf".encode()
ct_b64 = "U2FsdGVkX19NqFbsRQaxInvQLi9THdss6H1Po3mTBlJjDJilL8Roj9oDNhGh1VqdfQVnFdp1pWjbVWhZZxfrWxMZoFlKn+QHuZb5PMDwO4olDzxJT4hWDW7TtEY4tLqj"

pt = decrypt(ct_b64, password)
print("pt", pt.decode())


# if __name__ == '__main__':
    # createUser()
    # print(getUsers('victor.bonnaf@gmail.com'))