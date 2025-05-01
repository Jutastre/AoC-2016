import itertools
import copy
import hashlib

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")


class Node:
    def __init__(self, string:str):
        split_line = string.split()
        self.x = int(split_line[0].split("-")[1][1:])
        self.y = int(split_line[0].split("-")[2][1:])
        self.size = int(split_line[1][:-1])
        self.used = int(split_line[2][:-1])
        self.avail = int(split_line[3][:-1])

nodes = [Node(line) for line in data[2:]]

count = 0

for n1,n2 in itertools.permutations(nodes,2):
    if n1.used == 0:
        continue
    if n1.used > n2.avail:
        continue
    count += 1

print(count)