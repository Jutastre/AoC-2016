import itertools
import copy
import hashlib

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

starting_password = "fbgdceah"

password = [char for char in starting_password]


def rotate_right(password, count):
    count %= len(password)
    if count == 0:
        return password
    return password[-count:] + password[: (-count)]

starting_length = len(password)

for line in reversed(data):
    words = line.split()
    match words[0]:
        case "swap":
            if words[1] == "position":
                idx1 = int(words[2])
                idx2 = int(words[5])
                temp = password[idx1]
                password[idx1] = password[idx2]
                password[idx2] = temp
            else:
                char1 = words[2]
                char2 = words[5]
                idx1 = password.index(char1)
                idx2 = password.index(char2)
                password[idx1] = char2
                password[idx2] = char1
        case "rotate":
            if words[1] == "left" or words[1] == "right":
                count = int(words[2])
                if words[1] == "right":
                    count = len(password) - count
                if count != 0:
                    password = rotate_right(password, count)
            elif words[1] == "based": # this kills the crab
                rotations = 1
                password = rotate_right(password, len(password) - 1)
                while password.index(words[6]) != rotations - 1 - (1 if password.index(words[6]) >= 4 else 0):
                    password = rotate_right(password, len(password) - 1)
                    rotations += 1
        case "reverse":
            idx1 = int(words[2])
            idx2 = int(words[4])
            before = password[: idx1] if idx1 > 0 else []
            after = password[idx2 + 1 :] if idx2 < len(password) else []
            middle = list(reversed(password[idx1:idx2 + 1]))
            password = before + middle + after
        case "move":
            idx1 = int(words[2])
            idx2 = int(words[5])
            temp = password.pop(idx2)
            password.insert(idx1, temp)
    assert len(password) == starting_length

# print(password)
print("".join(password))