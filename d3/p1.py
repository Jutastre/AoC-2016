FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")
total_sum = 0
for row in data:
    sides = tuple(int(number) for number in row.split())
    small, medium, large = sorted(sides)
    if small + medium > large:
        total_sum += 1
print(total_sum)