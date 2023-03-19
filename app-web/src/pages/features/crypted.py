import Flask, jsonify, request

from cryptography.fernet import Fernet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


# Charge la clé Fernet à partir du fichier
def load_key():
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
    return key

# Chiffre un message en utilisant la clé Fernet
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

# Déchiffre un message en utilisant la clé Fernet
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message.encode())
    return decrypted.decode()

# API pour chiffrer un message
@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.json['message']
    encrypted = encrypt_message(message)
    return jsonify({'encrypted': encrypted.decode()})

# API pour déchiffrer un message
@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.json['encrypted']
    decrypted = decrypt_message(encrypted_message)
    return jsonify({'decrypted': decrypted})

if __name__ == '__main__':
    generate_key()
    app.run()
