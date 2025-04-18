import itertools
import copy
import hashlib

FILENAME = "in.txt"

if FILENAME == "tin.txt":
    disk_size = 20
else:
    disk_size = 272

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

def fill_disk(data:list[int], target_size):
    while len(data) < target_size:
        new_data = copy.copy(data)
        new_data.append(0)
        for bit in reversed(data):
            new_data.append(0 if bit == 1 else 1)
        data = new_data
    return data[:target_size]

def calculate_checksum(data):
    while len(data) % 2 == 0:
        new_data = []
        for bit1,bit2 in itertools.batched(data,2):
            new_data.append(1 if bit1 == bit2 else 0)
        data = new_data
    return data

binary_data = [int(char) for char in data[0]]

disk = fill_disk(binary_data, disk_size)

checksum = calculate_checksum(disk)

print("".join(str(bit) for bit in checksum))