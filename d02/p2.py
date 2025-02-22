FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

def clamp(n, min, max):
    if n < min:
        return min
    if n > max:
        return max
    return n

keypad = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 2, 3, 4, 0, 0],
    [0, 5, 6, 7, 8, 9, 0],
    [0, 0, "A", "B", "C", 0, 0],
    [0, 0, 0, "D", 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

x, y = 2, 2

key_presses = []
last_coordinates = (x, y)
for row in data:
    for char in row:
        match char:
            case "R":
                x += 1
            case "L":
                x -= 1
            case "D":
                y += 1
            case "U":
                y -= 1
        if keypad[y][x] == 0:
            x, y = last_coordinates
        last_coordinates = (x, y)
    key_presses.append(keypad[y][x])
print("".join(str(key_presses)))
