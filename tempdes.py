from Crypto.Cipher import DES
from Crypto import Random
import sys
import binascii
import time

# cbc_key = "\x40\xfe\xdf\x38\x6d\xa1\x3d\x57"
# iv = Random.get_random_bytes(8)

try:
    cbc_key = binascii.unhexlify(sys.argv[2])
    iv = binascii.unhexlify(sys.argv[1])
    inputfile = sys.argv[3]
    outputfile = sys.argv[4]
except:  # except (IndexError, TypeError):
    print "Usage: python tempdes.py <iv> <key> <inputfile> <outputfile>"
    # python2 tempdes.py fecdba9876543210 0123456789abcdef test.txt mytest.des
    sys.exit(1)
print '=' * 100
print 'Key used: ', [x for x in cbc_key]
print "IV used: ", [x for x in iv]

plain_text = ""
with open(inputfile) as f:
    for line in f:
        plain_text += line
plain_text += "\x00" * (8 - len(plain_text) % 8)
print '=' * 100
print "Plaintext is: ", plain_text

beforeEncryption = time.time()
des1 = DES.new(cbc_key, DES.MODE_CBC, iv)
afterEncryption = time.time()
cipher_text = des1.encrypt(plain_text)
print "Ciphertext is: ", cipher_text
print "Encryption takes: ", afterEncryption - beforeEncryption

f = open(outputfile, "wb")
f.write(cipher_text)

des2 = DES.new(cbc_key, DES.MODE_CBC, iv)
beforeDecryption = time.time()
msg = des2.decrypt(cipher_text)
afterDecryption = time.time()
print "Decryption takes: ", afterDecryption - beforeDecryption
print "Original Message is: ", msg
print '=' * 100
