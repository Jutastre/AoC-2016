import hashlib
import random

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip()

password = "________"

index = 0
# print(password)

random.seed()


def printpass(password):
    print(chr(13), end="")
    for char in password:
        if char == "_":
            print(f"{chr(random.randint(33,126))}", end=" ")
        else:
            print(char, end=" ")
    #print("")


while True:
    index += 1
    if not index % 50000:
        printpass(password)
    hash = hashlib.md5((data + str(index)).encode("utf-8"), usedforsecurity=False)
    # print(str(hash.hexdigest()[:5]))
    digest = hash.hexdigest()
    if digest[:5] == "00000":
        if not digest[:6].isnumeric():
            continue
        position = int(digest[5])
        char = digest[6]
        if position > 7:
            continue
        if password[position] != "_":
            continue
        password = password[:position] + char + password[position + 1 :]
        printpass(password)
        if "_" not in password:
            break

print(password)
