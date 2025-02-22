import itertools

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")


def is_abba(string:str):
    assert len(string) == 4
    return string[0] != string[1] and string[0] == string[3] and string[1] == string[2]

def contains_abba(string:str):
    if len(string) < 4:
        return False
    for idx in range(len(string) - 3):
        if is_abba(string[idx:idx+4]):
            return True
    return False

count = 0

for row in data:
    sequences = []
    hypernet = []
    if "[" not in row:
        sequences.append(row)
    else:
        split_sequence = row.split("[")
        sequences.append(split_sequence[0])
        for piece in split_sequence[1:]:
            hyper,sequence = piece.split("]")
            hypernet.append(hyper)
            sequences.append(sequence)
    supports_tls = False
    for sequence in sequences:
        if contains_abba(sequence):
            supports_tls = True
            break
    for sequence in hypernet:
        if contains_abba(sequence):
            supports_tls = False
            break
    print(f"{row} does {'' if supports_tls else 'NOT '}support TLS")
    if supports_tls:
        count += 1
print(f"{count=}")