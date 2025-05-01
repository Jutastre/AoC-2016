import itertools
import copy
import hashlib

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

value = int(data[0])


def simulate(number: int):
    elves = [n for n in range(1, number + 1)]
    while len(elves) > 1:
        for n in range(1, number + 1):
            for position, elf in enumerate(elves):
                if elf == n:
                    break
            else:
                position = None
            if position != None:
                elves.pop((position + (len(elves) // 2)) % len(elves))

    return elves[0]


def sim2(number):
    if number <= 1:
        return 1
    number -= 1
    remove = 1
    while number > 0:
        number -= 2**remove
        remove += 1
    number += 2 ** (remove - 1)
    magic = 2 ** (remove - 2)
    if number > magic:
        # number-= 2**(remove-2)
        return magic + (number - magic * 2)

    return number


for n in range(1, 35):
    print(f"{n:6}", end=",")
    print(f"{simulate(n):6}", end=",")
    print(f"{sim2(n):6}")

print(simulate(5))
print(simulate(3001330))
