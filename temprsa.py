from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import sys
import time
import matplotlib as m
m.use('TkAgg')
import matplotlib.pyplot as mp

x = [2, 4, 8, 16, 32, 64, 128]
y1 = []
y2 = []
for i in range(1, len(sys.argv)):
    try:
        inputfile = sys.argv[i]
    except:  # except (IndexError, TypeError):
        print("Usage: python temprsa.py <inputfile>")
        # /Users/ayfallen/Desktop/NS/Python/venv/bin/python temprsa.py 2.txt 4.txt 8.txt 16.txt 32.txt 64.txt 128.txt
        sys.exit(1)
    plain_text = ''
    with open(inputfile) as f:
        for line in f:
            plain_text += line
    private_key = RSA.importKey(open('master_bot_private_key.pem').read())
    public_key = RSA.importKey(open('master_bot_public_key.pem').read())
    encrypter = PKCS1_OAEP.new(public_key)
    start = time.time()
    cipher = encrypter.encrypt(plain_text)
    finish = time.time()
    duration = finish - start
    print(duration)
    y1.append(round(duration * 1000000, 0))

    x = [2, 4, 8, 16, 32, 64, 128]
    decrypter = PKCS1_OAEP.new(private_key)
    start = time.time()
    original = decrypter.decrypt(cipher)
    finish = time.time()
    duration = finish - start
    print(duration)
    y2.append(round(duration * 1000000, 2))
mp.figure(figsize=(20, 5))
mp.plot(x, y1, 'r+', label='encryption')
mp.plot(x, y2, 'b+', label='decryption')
mp.xlabel('File sizes (bytes)')
mp.ylabel('Time (microseconds)')
mp.title('RSA encryption / decryption times')
mp.legend()
for i, j in zip(x, y1):
    mp.annotate(str(j), xy=(i, j))
for i, j in zip(x, y2):
    mp.annotate(str(j), xy=(i, j))
mp.savefig('rsa.png')
