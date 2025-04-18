import itertools
import copy
import hashlib

FILENAME = "in.txt"

if FILENAME == "tin.txt":
    salt = "abc"
else:
    with open(FILENAME) as f:
        salt = f.read().strip()

def find_sequence(string, length):
    found_chars = []
    for idx in range(0,len(string) - (length-1)):
        for idx2 in range(length-1):
            if string[idx] != string[idx+1+idx2]:
                break
        else:
            found_chars.append(string[idx])
    return found_chars

memoization = {}

def get_hash(string:str):
    if string in memoization:
        return memoization[string]
    else:
        hash_value = hashlib.md5(string.encode()).hexdigest()
        memoization[string] = hash_value
        return hash_value

idx = 0
found_pad_indices = []
found_sets = 0

while found_sets < 64:
    hash_value = get_hash(salt + str(idx))
    for sequence_char in find_sequence(hash_value, 5):
        good_set = False
        for idx2 in range(max(0,idx-1000), idx):
            hash_value2 = get_hash(salt + str(idx2))
            sequences = find_sequence(hash_value2, 3)
            if sequences and sequence_char == sequences[0]:
                found_pad_indices.append(idx2)
                good_set = True
        if good_set:
            found_sets += 1
    idx += 1
print(sorted(found_pad_indices))
print(sorted(set(found_pad_indices)))
print(sorted(set(found_pad_indices))[63])




# string = "abc"
# print(string)
# print(find_sequence(string,5))
# string = "aaaabc"
# print(string)
# print(find_sequence(string,5))
# string = "aaaaabc"
# print(string)
# print(find_sequence(string,5))
# string = "bcaaaaa"
# print(string)
# print(find_sequence(string,5))