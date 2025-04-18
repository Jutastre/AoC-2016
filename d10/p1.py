import itertools

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")


bots = {}

outputs = {}

rules = {}

for row in data:
    split_row = row.split()
    if split_row[0] == "value":
        value = int(split_row[1])
        bot_number = int(split_row[5])
        if bot_number in bots:
            bots[bot_number] = sorted(bots[bot_number] + [value])
        else:
            bots[bot_number] = [value]
    if split_row[0] == "bot":
        bot_number = int(split_row[1])
        low = int(split_row[6])
        low_type = split_row[5]
        high = int(split_row[11])
        high_type = split_row[10]
        rules[bot_number] = ((low_type, low), (high_type, high))
while True:
    for bot_number, chips in bots.items():
        if len(chips) == 2:
            break
    if chips[0] == 17 and chips[1] == 61:
        break
    bot_rules = rules[bot_number]
    for rule, chip in zip(bot_rules, chips):
        if rule[0] == "bot":
            if rule[1] in bots:
                bots[rule[1]] = sorted(bots[rule[1]] + [chip])
            else:
                bots[rule[1]] = [chip]
        elif rule[0] == "output":
            if rule[1] in outputs:
                outputs[rule[1]].append(chip)
            else:
                outputs[rule[1]] = [chip]
    bots[bot_number] = []
print(bot_number)