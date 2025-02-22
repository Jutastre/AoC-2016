import itertools

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")


def decomp(string: str):
    count = 0
    idx = 0
    while idx < len(string):
        if string[idx] == "(":
            marker_end = string.find(")", idx)
            marker = string[idx + 1 : marker_end]
            marker1, marker2 = (int(n) for n in marker.split("x"))
            idx += 2 + len(marker)
            count += marker2 * decomp(string[idx : idx + marker1])
            idx += marker1
        else:
            idx += 1
            count += 1
    return count


count = 0
for row in data:
    count += decomp(row)
print(f"{len('XABCABCABCABCABCABCY')=}")
print(f"{count=}")
