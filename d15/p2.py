import itertools
import copy
import hashlib

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")


class disc:
    def __init__(self, positions: int, start_position: int):
        self.positions = positions
        self.start_position = start_position
        # self.zero = (positions - start_position) % start_position

    def get_position(self, time: int):
        return ((time + self.start_position) % self.positions)

    def is_open(self, time: int):
        return self.get_position(time) == 0


discs = []
for line in data:
    words = line.split()
    positions = int(words[3])
    start_position = int(words[11].strip("."))
    discs.append(disc(positions, start_position))

for start_time in range(0 - (len(discs) + 1),99999999, 11): # dirty but fast p2 modification
    for disc_idx, disc in enumerate(discs):
        if not disc.is_open(start_time + 1 + disc_idx):
            print(f"drop at time {start_time} failed at disc #{disc_idx + 1}")
            break
    else:
        print(f"successful drop at time {start_time}")
        exit()
