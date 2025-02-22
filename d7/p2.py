import itertools

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")


def is_aba(string:str):
    assert len(string) == 3
    return string[0] != string[1] and string[0] == string[2]
    

def contains_abba(string:str):
    if len(string) < 4:
        return False
    for idx in range(len(string) - 3):
        if is_aba(string[idx:idx+4]):
            return True
    return False

def get_abas(string:str):
    abas = []
    if len(string) < 4:
        return abas
    for idx in range(len(string) - 2):
        if is_aba(string[idx:idx+3]):
            abas.append((string[idx], string[idx+1]))
    return abas


count = 0

for row in data:
    sequences = []
    hypernet = []
    sequence_abas = []
    hyper_abas = []
    if "[" not in row:
        sequences.append(row)
    else:
        split_sequence = row.split("[")
        sequences.append(split_sequence[0])
        for piece in split_sequence[1:]:
            hyper,sequence = piece.split("]")
            hypernet.append(hyper)
            sequences.append(sequence)
    supports_ssl = False
    for sequence in sequences:
        abas = get_abas(sequence)
        sequence_abas += abas
    for sequence in hypernet:
        abas = get_abas(sequence)
        hyper_abas += abas
    for aba,bab in itertools.product(sequence_abas, hyper_abas):
        if aba[0] == bab[1] and aba[1] == bab[0]:
            supports_ssl = True
            break
    print(f"{row} does {'' if supports_ssl else 'NOT '}support TLS")
    if supports_ssl:
        count += 1
print(f"{count=}")