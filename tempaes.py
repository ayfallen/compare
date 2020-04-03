from Crypto.Cipher import AES
import sys
import binascii
import time
import matplotlib as m
m.use('TkAgg')
import matplotlib.pyplot as mp

x = ['8', '64', '512', '4096', '32768', '262144', '2047152']
y1 = []
y2 = []
for i in range(3, len(sys.argv)):
    try:
        iv = binascii.unhexlify(sys.argv[1])
        cbc_key = binascii.unhexlify(sys.argv[2])
        inputfile = sys.argv[i]
    except:  # except (IndexError, TypeError):
        print("Usage: python tempaes.py <iv> <key> <inputfile>")
        # /Users/ayfallen/Desktop/NS/Python/venv/bin/python tempaes.py fecdba9876543210fecdba9876543210 0123456789abcdef0123456789abcdef 8.txt 64.txt 512.txt 4096.txt 32768.txt 262144.txt 2047152.txt
        sys.exit(1)
    plain = ''
    with open(inputfile) as f:
        for line in f:
            plain += line
    length = 16 - (len(plain) % 16)
    plain += chr(length) * length
    aes1 = AES.new(cbc_key, AES.MODE_CBC, iv)
    start = time.time()
    cipher = aes1.encrypt(plain)
    finish = time.time()
    duration = finish - start
    print(duration)
    y1.append(round(duration * 1000000))
    aes2 = AES.new(cbc_key, AES.MODE_CBC, iv)
    before_decryption = time.time()
    original = aes2.decrypt(cipher)
    after_decryption = time.time()
    duration = finish - start
    print(duration)
    y2.append(round(duration * 1000000, 2))
mp.plot(x, y1, 'r+', label='encryption')
mp.plot(x, y2, 'bx', label='decryption')
mp.xlabel('File sizes (bytes)')
mp.ylabel('Time (microseconds)')
mp.title('AES encryption / decryption times')
mp.legend()
for i, j in zip(x, y1):
    mp.annotate(str(j), xy=(i, j))
for i, j in zip(x, y2):
    mp.annotate(str(j), xy=(i, j))
mp.savefig('aes.png')
