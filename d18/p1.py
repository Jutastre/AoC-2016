import itertools
import copy
import hashlib

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

value = int(data[0])


def simulate(number:int):
    elves = [n for n in range(1,number+1)]
    while len(elves) > 1:
        for n in range(1,number+1):
            for position,elf in enumerate(elves):
                if elf == n:
                    break
            else:
                position = None
            if position != None:
                if position == len(elves)-1:
                    elves.pop(0)
                else:
                    elves.pop(position+1)
                    
    return elves[0]

def sim2(number):
    if number <= 1:
        return 1
    number -= 1
    remove = 1
    while number > 0:
        number-= 2**remove
        remove += 1
    number += (2**(remove-1))
    return (number*2) - 1

for n in range(1,22):
    print(simulate(n),end=",")
    print(n-simulate(n),end=",")
    print(sim2(n))

print(sim2(value))