import itertools
import copy
import hashlib

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

salt = data[0]

acceptable_hash_symbols = "abcdef"


def possible_directions( path: str,coords):
    x,y = coords
    hash_value = hashlib.md5((salt + path).encode()).hexdigest()
    directions = []
    if y > 0 and hash_value[0] in acceptable_hash_symbols:
        directions.append("U")
    if y < 3 and hash_value[1] in acceptable_hash_symbols:
        directions.append("D")
    if x > 0 and hash_value[2] in acceptable_hash_symbols:
        directions.append("L")
    if x < 3 and hash_value[3] in acceptable_hash_symbols:
        directions.append("R")
    return directions

paths = [""]
positions = [(0,0)]
while (3,3) not in positions:
    new_paths = []
    new_positions = []
    for path,coord in zip(paths,positions):
        directions = possible_directions(path,coord)
        for direction in directions:
            new_paths.append(path + direction)
            nx,ny = coord
            match direction:
                case 'U':
                    ny -= 1
                case 'D':
                    ny += 1
                case 'L':
                    nx -= 1
                case 'R':
                    nx += 1
            new_positions.append((nx,ny))
    paths = new_paths
    positions = new_positions

for path,position in zip(paths,positions):
    if position == (3,3):
        print(path)