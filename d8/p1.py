import itertools

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

screen: list[list[bool]] = []
for _ in range(6):
    screen.append([])
    for _ in range(50):
        screen[-1].append(False)

def printscreen():
    lit_count = 0      
    for row in screen:
        for pixel in row:
            if pixel:
                lit_count += 1
            print("##" if pixel else "  ", end="")
        print("")
    print(f"{lit_count=}")
for row in data:
    printscreen()
    # input()
    print(row)
    words = row.split()
    match words[0]:
        case "rect":
            A, B = (int(n) for n in words[1].split("x"))
            for x, y in itertools.product(range(A), range(B)):
                screen[y][x] = True
        case "rotate":
            match words[1]:
                case "row":
                    row_idx = int(words[2][2:])
                    shift = int(words[4])
                    for _ in range(shift):
                        screen[row_idx] = [screen[row_idx][-1]] + screen[row_idx][:-1]
                case "column":
                    col_idx = int(words[2][2:])
                    shift = int(words[4])
                    for _ in range(shift):
                        carry = screen[-1][col_idx]
                        for idx in range(5,0,-1):
                            screen[idx][col_idx] = screen[idx-1][col_idx]
                        screen[0][col_idx] = carry

printscreen()