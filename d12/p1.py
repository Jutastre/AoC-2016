import itertools
import copy

FILENAME = "tin.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

a,b,c,d = 0,0,0,0
reg = {'a':0,
       'b':0,
       'c':0,
       'd':0,
       }

pc = 0
while pc < len(data):
    split_line = data[pc].split()
    match split_line[0]:
        case "cpy":
            if split_line[1].isnumeric():
                reg[split_line[2]] = int(split_line[1])
            else:
                reg[split_line[2]] = reg[split_line[1]]
            pc += 1
        case "inc":
            reg[split_line[1]] += 1
            pc += 1
        case "dec":
            reg[split_line[1]] -= 1
            pc += 1
        case "jnz":
            if split_line[1].isnumeric():
                operand = int(split_line[1])
            else:
                operand = reg[split_line[1]]
            if operand != 0:
                pc += int(split_line[2])
            else:
                pc += 1
print(reg["a"])