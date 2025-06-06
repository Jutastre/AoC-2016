FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")
total_sum = 0

def sorting_function(kv_pair):
    return (kv_pair[1] * 128) + (128-ord(kv_pair[0]))

for row in data:
    code,checksum = row.split("[")
    checksum = checksum[:-1]
    code = code.split("-")
    id = int(code.pop())
    code = "".join(code)
    letter_counts = {}
    for char in code:
        if char not in letter_counts:
            letter_counts[char] = 1
            continue
        letter_counts[char]+=1
    sorted_counts = sorted(letter_counts.items(),key = sorting_function, reverse=True)
    correct = True
    for char, counted_char in zip(checksum, sorted_counts):
        if char != counted_char[0]:
            correct = False
    if correct:
        total_sum += id

print(total_sum)
