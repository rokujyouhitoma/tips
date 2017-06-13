import base64
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Util import randpool
from Crypto import Random

iv = Random.new().read(AES.block_size)
bs = AES.block_size

def pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def encrypt(key, plain):
    plain = pad(plain)
    aes = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(aes.encrypt(plain))

def decrypt(key, content):
    content = base64.b64decode(content)
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(content))

class Client():
    def __init__(self):
        rsa = RSA.generate(1024, randpool.RandomPool().get_bytes)
        self.rsa_public_key = rsa.publickey().exportKey("PEM") 
        self.rsa_private_key = RSA.construct((rsa.n, rsa.e, rsa.d)).exportKey("PEM") 

    def connect(self, server):
        self.server = server

    def request(self):
        server_key, content = self.server.response(self.rsa_public_key)
        rsa = RSA.importKey(self.rsa_private_key)
        key = rsa.decrypt(server_key)
        print("server key at client '%s'" % key)
        raw = decrypt(key, content)
        return raw

class Server():
    def __init__(self, key, raw):
        self.key = key
        self.content = encrypt(key, raw)

    def response(self, client_public_key):
        rsa = RSA.importKey(client_public_key)
        print("server key at server: '%s'" % self.key)
        return rsa.encrypt(self.key, ""), self.content

client = Client()
server = Server(pad("this is key"), "hello world")

client.connect(server)
raw = client.request()
print("cleint get: '%s'" % raw)
