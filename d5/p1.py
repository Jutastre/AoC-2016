import hashlib

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip()

password = ""

index = 0
while True:
    hash = hashlib.md5((data + str(index)).encode("utf-8"),usedforsecurity=False)
    # print(str(hash.hexdigest()[:5]))
    if hash.hexdigest()[:5] == "00000":
        password += hash.hexdigest()[5]
        print(password)
        if len(password) == 8:
            break
    index += 1

print(password)