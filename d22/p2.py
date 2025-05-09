import itertools
import copy
import hashlib

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")


class Node:
    def __init__(self, string: str):
        split_line = string.split()
        self.x = int(split_line[0].split("-")[1][1:])
        self.y = int(split_line[0].split("-")[2][1:])
        self.size = int(split_line[1][:-1])
        self.used = int(split_line[2][:-1])
        self.avail = int(split_line[3][:-1])
        self.has_target_data = False

    def from_repr(repr_string):
        node = Node("/dev/grid/node-x33-y23   94T   67T    27T   71%")
        node.x, node.y, node.size, node.used, node.avail = (
            int(value) for value in repr_string.split(",")[:-1]
        )
        node.has_target_data = (repr_string.split(",")[-1] == "True")
        return node

    def __hash__(self):
        hash((self.x, self.y, self.size, self.used, self.avail, self.has_target_data))

    def __repr__(self):
        return ",".join(
            [
                str(value)
                for value in (
                    self.x,
                    self.y,
                    self.size,
                    self.used,
                    self.avail,
                    self.has_target_data,
                )
            ]
        )

    def __str__(self):
        return repr(self)


XMAX = 0
YMAX = 0

nodes = [Node(line) for line in data[2:]]
for node in nodes:
    if node.x > XMAX:
        XMAX = node.x
    if node.y > YMAX:
        YMAX = node.y

ordered_nodes = [[] for _ in range(YMAX + 1)]

for idx in range(XMAX + 1):
    for node in nodes:
        if node.x == idx:
            ordered_nodes[node.y].append(node)


def serialize_state(nodes: list[Node]):
    return "-".join(
        ";".join(repr(node) for node in node_row) for node_row in ordered_nodes
    )


def deserialize_state(state_string) -> list[list[Node]]:
    return tuple(
        tuple(Node.from_repr(repr_string) for repr_string in row_string.split(";"))
        for row_string in state_string.split("-")
    )


steps_taken = 0

current_states = set((serialize_state(nodes),))
found_solution = False

while not found_solution:
    new_states = set()
    for state in current_states:
        nodes = deserialize_state(state)
        for y, row in enumerate(nodes):
            for x, node in enumerate(row):
                offsets = []
                if x != XMAX:
                    offsets.append((+1, 0))
                if x != 0:
                    offsets.append((-1, 0))
                if y != YMAX:
                    offsets.append((0, +1))
                if y != 0:
                    offsets.append((0, -1))
                for dx, dy in offsets:
                    if nodes[y + dy][x + dx].avail < node.used:
                        continue
                    new_nodes: list[list[Node]] = copy.deepcopy(nodes)
                    target_node = new_nodes[y + dy][x + dx]
                    source_node = new_nodes[y][x]
                    target_node.used += source_node.used
                    target_node.avail += target_node.size - target_node.used
                    target_node.has_target_data = source_node.has_target_data
                    source_node.used = 0
                    source_node.avail = source_node.size
                    source_node.has_target_data = False
                    if target_node.has_target_data and x == 0 and y == 0:
                        found_solution = True
                        break
                    new_states.add(serialize_state(new_nodes))
                if found_solution:
                    break
            if found_solution:
                break
        if found_solution:
            break
    steps_taken += 1
    print(steps_taken)
    for a in new_states:
        break
    print(hash(a)) # this is some stupid code
    current_states = new_states

print(steps_taken)
