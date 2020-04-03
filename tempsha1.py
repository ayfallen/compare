import hashlib
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
        print("Usage: python tempsha1.py <inputfile>")
        # /Users/ayfallen/Desktop/NS/Python/venv/bin/python tempsha1.py 8.txt 64.txt 512.txt 4096.txt 32768.txt 262144.txt 2047152.txt
        sys.exit(1)
    text = ''
    with open(inputfile) as f:
        for line in f:
            text += line
    start = time.time()
    result = hashlib.sha1(text.encode())
    finish = time.time()
    duration = finish - start
    # print(result.hexdigest())
    print(duration)
    y.append(round(duration * 1000000, 2))
mp.plot(x, y, 'r+')
mp.xlabel('File sizes (bytes)')
mp.ylabel('Time (microseconds)')
mp.title('SHA-1 digest generation times')
for i, j in zip(x, y):
    mp.annotate(str(j), xy=(i, j))
mp.savefig('sha1.png')
