# Following code reads its source file and computes an HMAC signature for it:
import hmac
import time
import sys
import matplotlib as m
m.use('TkAgg')
import matplotlib.pyplot as mp

x = ['8', '64', '512', '4096', '32768', '262144', '2047152']
y = []
for i in range(1, len(sys.argv)):
    try:
        inputfile = sys.argv[i]
    except:  # except (IndexError, TypeError):
        print("Usage: python tempHMAC.py <inputfile>")
        # /Users/ayfallen/Desktop/NS/Python/venv/bin/python tempHMAC.py 8.txt 64.txt 512.txt 4096.txt 32768.txt 262144.txt 2047152.txt
        sys.exit(1)
    secret_key = b'secret-shared-key-goes-here'
    digest_maker = hmac.new(secret_key)
    f = open(inputfile, 'rb')
    try:
        while True:
            block = f.read(1024)
            if not block:
                break
            digest_maker.update(block)
    finally:
        f.close()
    start = time.time()
    digest = digest_maker.hexdigest()
    finish = time.time()
    duration = finish - start
    print(duration)
    y.append(round(duration * 1000000, 2))
mp.plot(x, y, 'r+')
mp.xlabel('File sizes (bytes)')
mp.ylabel('Time (microseconds)')
mp.title('HMAC signature generation times')
for i, j in zip(x, y):
    mp.annotate(str(j), xy=(i, j))
mp.savefig('hmac.png')
