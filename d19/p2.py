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
    remainder = number
    iteration = 0
    last_cube = 1
    cube = 3**iteration
    while number > cube:
        #remainder -= cube
        iteration += 1
        last_cube = cube
        cube = 3**iteration
    remainder = number - last_cube
    # return number
    if number == cube:
        return number
    if remainder == 0:
        return 1
    if remainder <= last_cube:
        return remainder
    else:
        return last_cube + (((remainder) - last_cube) * 2)


for n in range(1, 99):
    print(f"{n:6}", end=",")
    print(f"{simulate(n):6}", end=",")
    print(f"{sim2(n):6}")

print(simulate(5))
print(sim2(3001330))
