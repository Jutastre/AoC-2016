import itertools
import copy

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")

floors = [[], [], [], []]


class thing:
    # def __init__(self, string: str, position: int):
    def __init__(self, string: str):
        split_string = string.split()
        if split_string[0] == "and":
            split_string.pop(0)
        self.is_chip = True if split_string[1][-5:] == "tible" else False
        self.name = split_string[1].split("-")[0]
        #self.position = position

    def __str__(self):
        return f'{self.name} {"chip" if self.is_chip else "gen"}'

    def __repr__(self):
        return f'{self.name} {"chip" if self.is_chip else "gen"}'

    def __hash__(self):
        return hash(str(self))
    def __lt__(self,other):
        return str(self) < str(other)


all_things: list[thing] = []

for floor_idx, row in enumerate(data):
    important_part = row.split("contains ")[1]
    if "nothing" in important_part:
        continue
    important_part = important_part.replace(" and ", ", ")
    pieces = important_part.strip(".").split(", ")
    for piece in pieces:
        floors[floor_idx].append(thing(piece))
        all_things.append(floors[floor_idx][-1])


def stringify_state(floors, elevator_position):
    string = ""
    for idx, floor in reversed(list(enumerate(floors))):
        string += f"{idx+1}, {floor} {'E' if elevator_position == idx else ''}\n"
    return string.strip("\n")


def make_hashable(floors, elevator):
    return (tuple(tuple(sorted(floor)) for floor in floors), elevator)


def reverse_hashability(hashable):
    return list(set(floor) for floor in hashable[0]), hashable[1]


def is_state_dead(floors: list[list[thing]]):
    for floor in floors:
        for item in floor:
            if not item.is_chip:  # find a chip
                continue
            safe = False  # assume its unshielded
            for item2 in floor:
                if item2.is_chip:  # find generators
                    continue
                if item.name == item2.name:  # if it matches, chip is shielded
                    safe = True
            if not safe:  # if not shielded:
                for item2 in floor:
                    if not item2.is_chip:  # and there is a generator on the floor
                        return True  # the state is dead
    return False

def is_state_win(floors):
    for floor in floors[:-1]:
        if len(floor) != 0:
            return False
    return True


## extra part 2 conditions:

floors[0].append(thing("an elerium generator"))
floors[0].append(thing("an dilithium-compatible microchip"))
floors[0].append(thing("an dilithium generator"))
floors[0].append(thing("an dilithium-compatible microchip"))


elevator = 0
print(stringify_state(floors, elevator))

states = {make_hashable(floors, elevator): 0}

done = False
winning_state = None
steps_taken = 0
while not done:
    steps_taken += 1
    print(f"step #{steps_taken}")
    states_to_check = [(state, step_count) for state, step_count in states.items()]
    for state, step_count in states_to_check:
        if step_count + 1 < steps_taken:
            continue
        reachable_states = []
        # print(stringify_state(floors, elevator))
        floors, elevator = reverse_hashability(state)
        # up:
        floor_target_offsets = []

        if elevator != 3:
            floor_target_offsets.append(1)
        if elevator != 0:
            floor_target_offsets.append(-1)
        for floor_target_offset in floor_target_offsets: #directions
            for item_to_bring in floors[elevator]:# single items
                new_floors = []
                for floor_idx, floor in enumerate(floors):
                    if floor_idx == (elevator + floor_target_offset):
                        new_floor = floor.union(set((item_to_bring,)))
                        new_floors.append(new_floor)
                    elif floor_idx == elevator:
                        new_floor = floor.difference(set((item_to_bring,)))
                        new_floors.append(new_floor)
                    else:
                        new_floors.append(floor)
                reachable_states.append((new_floors, elevator + floor_target_offset))
            for items_to_bring in itertools.combinations(floors[elevator],2):# double items
                new_floors = []
                for floor_idx, floor in enumerate(floors):
                    if floor_idx == (elevator + floor_target_offset):
                        new_floor = floor.union(set(items_to_bring))
                        new_floors.append(new_floor)
                    elif floor_idx == elevator:
                        new_floor = floor.difference(set(items_to_bring))
                        new_floors.append(new_floor)
                    else:
                        new_floors.append(floor)
                reachable_states.append((new_floors, elevator + floor_target_offset))
        
        for reachable_state, elevator in reachable_states:
            if is_state_dead(reachable_state):
                continue
            if is_state_win(reachable_state):
                done = True
                winning_state = (reachable_state, elevator)
            hashable = make_hashable(reachable_state, elevator)
            if hashable not in states:
                states[hashable] = step_count + 1
            else:
                if states[hashable] > step_count + 1:
                    states[hashable] = step_count + 1

print(stringify_state(*winning_state))
print(winning_state)
print( states[make_hashable(*winning_state)])