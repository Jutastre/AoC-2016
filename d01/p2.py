
FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split(", ")

x,y,direction = 0,0,0
visited_locations = set()
visited_locations.add((0,0))
bunny_hq = None
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
    for _ in range(distance):
        x += dx
        y += dy
        if (x,y) in visited_locations:
            bunny_hq = (x,y)
            break
        visited_locations.add((x,y))
    if bunny_hq:
        break
x,y = bunny_hq
print(abs(x) + abs(y))
