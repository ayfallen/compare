from random import randint

while True:
    length = int(input("Input file length: "))
    filename = "length" + str(length)
    content = ""
    for x in range(length):
        content += str(randint(0, 9))
    with open(filename, "w") as f:
        f.write(content)
