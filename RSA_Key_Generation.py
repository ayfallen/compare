import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(2048, random_generator) # generate public and private key
print '=' * 100
f = open('master_bot_private_key.pem', 'wb')
f.write(key.exportKey('PEM').decode('ascii'))
f.close()
print "Wrote Private key to: \"master_bot_private_key.pem\" file"
f = open('master_bot_public_key.pem', 'wb')
f.write(key.publickey().exportKey('PEM').decode('ascii'))
f.close() 
print "Wrote Public key to: \"master_bot_public_key.pem\" file"
print '=' * 100
