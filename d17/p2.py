import itertools
import copy
import hashlib

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

salt = data[0]

acceptable_hash_symbols = "bcdef"


def possible_directions(path: str, coords):
    x, y = coords
    if (x,y) == (3,3):
        return []
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


longest_path = 0
paths:list[list[str]] = [possible_directions("", (0, 0))]
positions = {"":(0, 0)}
working_path = ""
for direction in paths[-1]:
    nx,ny = positions[working_path]
    match direction:
        case "U":
            ny -= 1
        case "D":
            ny += 1
        case "L":
            nx -= 1
        case "R":
            nx += 1
    positions[working_path + direction] = (nx,ny)
while paths:
    if paths[-1]:
        working_path += paths[-1].pop()
        if positions[working_path] == (3,3):
            #paths.pop()
            if len(working_path) > longest_path:
                if len(working_path) > 40:
                    for n in range(len(working_path)):
                        sub_path = working_path[: 0 - n]
                        print(f"{positions[sub_path]} - {possible_directions(sub_path, positions[sub_path])}")
                longest_path = len(working_path)
                print(f"new longest: {longest_path}")
                # print(working_path)
                # print(positions[working_path])
            working_path = working_path[:-1]
        else:
            # if positions[working_path] == (3,3):
            #     continue
            paths.append(possible_directions(working_path, positions[working_path]))
            for direction in paths[-1]:
                nx,ny = positions[working_path]
                match direction:
                    case "U":
                        ny -= 1
                    case "D":
                        ny += 1
                    case "L":
                        nx -= 1
                    case "R":
                        nx += 1
                positions[working_path + direction] = (nx,ny)
    else:
        paths.pop()
        working_path = working_path[:-1]


print(longest_path)
