from Crypto import Random
from Crypto.Cipher import AES
import base64
from hashlib import md5
import requests as rq

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


def decrypt(encrypted, passphrase):
    encrypted = base64.b64decode(encrypted)
    assert encrypted[0:8] == b"Salted__"
    salt = encrypted[8:16]
    key_iv = bytes_to_key(passphrase, salt, 32+16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(encrypted[16:]))

def getUsers(id):
    '''Get an user acount
    
    Parameters: 
    id (string): id of the user
    
    Returns:
    myrow (json): all the account information
    '''
    url = "https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/{}".format(id)
    r = rq.get(url).json()
    with open('AVA-Bot/mykey.key', 'rb') as mykey: # Ajouter AVA-Bot/ sur ubuntu
        key = mykey.read()
    APIkey = r[0]['APIkey']
    APIsecret = r[0]['APIsecret']
    APIpassword = r[0]['APIpassword']
    APIkey = decrypt(APIkey, key)
    APIsecret = decrypt(APIsecret, key)
    APIpassword = decrypt(APIpassword, key)
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
    print(getUsers('victor.bonnaf@gmail.com')['id'])