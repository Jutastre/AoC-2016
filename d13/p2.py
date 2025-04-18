import itertools
import copy

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

magic_number = int(data[0])

def is_wall(x:int,y:int):
    return (x*x + 3*x + 2*x*y + y + y*y + magic_number).bit_count() % 2 == 1

visited_positions = set()
found_walls = set()
to_check = [(1,1)]
steps_taken = 0
if FILENAME == "tin.txt":
    destination = (7,4)
else:
    destination = (31,39)

while steps_taken < 50:
    steps_taken += 1
    to_check_later = []
    for x,y in to_check:
        for nx,ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
            if ny < 0 or nx < 0:
                continue
            if (nx,ny) in visited_positions:
                continue
            if (nx,ny) in found_walls:
                continue
            if is_wall(nx,ny):
                found_walls.add((nx,ny))
                continue
            to_check_later.append((nx,ny))
            visited_positions.add((nx,ny))
    to_check = to_check_later


for y in range(50):
    for x in range(50):
        if (x,y) in visited_positions:
            print("O",end="")
        elif (x,y) in found_walls:
            print("#",end="")
        else:
            print(" ",end="")
    print("")


print(len(visited_positions))