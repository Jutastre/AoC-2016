import itertools

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")
total_sum = 0
for row_triplet in itertools.batched(data,3):
    row_triplet = [[int(n) for n in row.split()] for row in row_triplet]
    for triangle in zip(*row_triplet):
        small, medium, large = sorted(triangle)
        if small + medium > large:
            total_sum += 1
print(total_sum)