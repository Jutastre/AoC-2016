
FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split(", ")

x,y,direction = 0,0,0

for row in data:
    match row[0]:
        case "R":
            direction += 1
        case "L":
            direction -= 1
    direction %= 4
    distance = int(row[1:])
    dx,dy = 0,0
    match direction:
        case 0:
            dy = -1
        case 1:
            dx = 1
        case 2:
            dy = 1
        case 3:
            dx = -1
    x += dx * distance
    y += dy * distance
print(abs(x) + abs(y))