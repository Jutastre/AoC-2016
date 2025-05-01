import itertools
import copy
import hashlib

FILENAME = "in.txt"

with open(FILENAME) as f:
    data:list[str] = f.read().strip().split("\n")
program:list[list[str]] = []
for row in data:
    program.append(row.split())

registers = {"a":7,"b":0,"c":0,"d":0}
pc = -1



while pc < len(program) - 1:
    pc += 1
    if len(program[pc]) == 2:
        instruction, arg1 = program[pc]
    else:
        instruction, arg1, arg2 = program[pc]
    match instruction:
        case "cpy":
            if (arg1 not in registers and not arg1.isnumeric()) or arg2.isnumeric():
                continue
            registers[arg2] = int(arg1) if arg1.isnumeric() else registers[arg1]
        case "tgl":
            if arg1.isnumeric():
                arg1 = int(arg1)
            else:
                arg1 = registers[arg1]
            if arg1 + pc < 0 or arg1 + pc > len(program):
                continue
            if len(program[pc+arg1]) == 2:
                if program[pc+arg1][0] == "inc":
                    program[pc+arg1][0] = "dec"
                else:
                    program[pc+arg1][0] = "inc"
            else:
                if program[pc+arg1][0] == "jnz":
                    program[pc+arg1][0] = "cpy"
                else:
                    program[pc+arg1][0] = "jnz"
        case "inc":
            if arg1.isnumeric() or arg1 not in registers:
                continue
            
            registers[arg1] += 1
        case "dec":
            if arg1.isnumeric() or arg1 not in registers:
                continue
            registers[arg1] -= 1
        case "jnz":
            if (arg1 not in registers and not arg1.isnumeric()):
                continue
            if arg1.isnumeric():
                arg1 = int(arg1)
            else:
                arg1 = registers[arg1]

            if (arg2 not in registers and not arg2.isnumeric()):
                continue
            if arg2.isnumeric():
                arg2 = int(arg2)
            else:
                arg2 = registers[arg2]
            if arg1 != 0:
                pc += arg2 - 1

print(registers["a"])