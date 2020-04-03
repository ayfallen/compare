from Crypto.Cipher import DES
import sys
import binascii
import time

try:
    iv = binascii.unhexlify(sys.argv[1])
    cbc_key = binascii.unhexlify(sys.argv[2])
    inputfile = sys.argv[3]
    outputfile = sys.argv[4]
except:  # except (IndexError, TypeError):
    print("Usage: python tempdes.py <iv> <key> <inputfile> <outputfile>")
    # python tempdes.py fecdba9876543210 0123456789abcdef test.txt mytest.des
    sys.exit(1)

plain = ''
with open(inputfile) as f:
    for line in f:
        plain += line

des1 = DES.new(cbc_key, DES.MODE_CBC, iv)
des2 = DES.new(cbc_key, DES.MODE_CBC, iv)

start = time.time()
cipher = des1.encrypt(plain)
finish = time.time()
duration = finish - start
print(duration * 1000)

f = open(outputfile, "wb")
f.write(cipher)

start = time.time()
original = des2.decrypt(cipher)
finish = time.time()
duration = finish - start
print(duration * 1000)
