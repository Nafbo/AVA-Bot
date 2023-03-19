from cryptography.fernet import Fernet

def encrypt_message(message):
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    with open('encrypted_data.txt', 'wb') as outfile:
        outfile.write(encrypted_message)


