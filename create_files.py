from random import randint

for length in [8, 64, 512, 4096, 32768, 262144, 2047152]:
    filename = str(length) + ".txt"
    content = ""
    for x in range(length):
        content += str(randint(0, 9))
    with open(filename, "w") as f:
        f.write(content)

for length in [2, 4, 16, 32, 128]:
    filename = str(length) + ".txt"
    content = ""
    for x in range(length):
        content += str(randint(0, 9))
    with open(filename, "w") as f:
        f.write(content)
