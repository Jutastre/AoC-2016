FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")


def clamp(n, min, max):
    if n < min:
        return min
    if n > max:
        return max
    return n


x, y = 1, 1

key_presses = []

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
        x = clamp(x, 0, 2)
        y = clamp(y, 0, 2)
    press = 1
    press += x
    press += y * 3
    key_presses.append(press)
print("".join(str(key_presses)))
