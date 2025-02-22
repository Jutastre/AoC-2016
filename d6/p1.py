FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")


def sorting_function(kv_pair):
    return (kv_pair[1] * 128) + (128 - ord(kv_pair[0]))


code = ""

for idx,_ in enumerate(data[0]):
    letter_counts = {}
    for row in data:
        char = row[idx]
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    most_common = sorted(letter_counts.items(), key=sorting_function, reverse=False)[0][
        0
    ]
    code += most_common

print(code)
