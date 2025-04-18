import itertools
import copy

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

floors = [[],[],[],[]]

class thing:
    def __init__(self, string:str, position:int):
        split_string = string.split()
        if split_string[0] == "and":
            split_string.pop(0)
        self.type = "chip" if split_string[1][-5:] == "tible" else "gen"
        self.name = split_string[1].split("-")[0]
        self.position = position
    def __str__(self):
        return f"{self.name} {self.type}"
    def __repr__(self):
        return f"{self.name} {self.type}"

all_things:list[thing] = []

for idx,row in enumerate(data):
    important_part = row.split("contains ")[1]
    if "nothing" in important_part:
        continue
    pieces = important_part.strip(".").split(", ")
    for piece in pieces:
        floors[idx].append(thing(piece, idx))
        all_things.append(floors[idx][-1])


for idx,floor in reversed(list(enumerate(floors))):
    print(f"{idx+1}, {floor}")
    #print(floor)


elevator = 0
state_parts = []
for chip_position,item in enumerate(all_things):
    if item.type == "chip":
        for gen_position,item in enumerate(all_things):
            if item.type == "gen":
                state_parts.append((chip_position,gen_position))
new_state = (elevator,tuple(sorted(state_parts)))

search_space = set((new_state,))

def finished(search_space):
    for state in search_space:
        for pair in state[1]:
            if pair[0] != 3 or pair[1] != 3:
                continue
        else:
            return True
    return False

def dead_state(state):
    if e > 3 or e < 0:
        return True
    for pair1,pair2 in itertools.permutations(state[1],2):
        if pair1[0] != pair1[1] and pair1[0] == pair2[1]:
            return True
    return True
time_spent = 0
while not finished(search_space):
    time_spent += 1
    new_search_space = set()
    for state, time in search_space.items():
        e = state[0]
        floors = [[],[],[],[]]

        for number, pair in enumerate(state[1]):
            floor[pair[0]].append((number,"chip"))
            floor[pair[1]].append((number,"gen"))
        possible_moves = []
        possible_moves.append((e+1,state[1]))
        possible_moves.append((e-1,state[1]))
        for item_to_move in floor[e]:
            for direction in [1, -1]:
                all_things:list[thing] = []
                for floor_number, floor in enumerate(floors):
                    for item in floor:
                        if item is item_to_move:
                            all_things.append((floor_number+direction), item[0], item[1])
                        else:
                            all_things.append((floor_number), item[0], item[1])
                state_parts = []
                for item1,item2 in itertools.combinations(all_things,2):
                    if item1[1] == item2[1]:
                        if item2[2] == "chip":
                            item1, item2 = item2, item1
                        state_parts.append((item1[0], item2[0]))
                new_state = (elevator,tuple(sorted(state_parts)))
                possible_moves.append(new_state)
        for move in possible_moves:
            if not dead_state(move):
                new_search_space.add(new_search_space)
print(f"{time_spent=}")

