import itertools
import copy
import hashlib

FILENAME = "in.txt"

with open(FILENAME) as f:
    data = f.read().strip().split("\n")


class mrange:
    def __init__(self):
        self.starts = []
        self.ends = []

    def _flatten(self):
        assert len(self.starts) == len(self.ends)

        new_starts = []
        new_ends = []
        height = 0
        self.starts.sort()
        self.ends.sort()

        while self.starts:
            if self.starts[0] <= self.ends[0]:
                start = self.starts.pop(0)
                height += 1
                if height == 1:
                    new_starts.append(start)
            else:
                end = self.ends.pop(0)
                height -= 1
                if height == 0:
                    new_ends.append(end)

        new_ends.append(self.ends.pop())

        self.starts = new_starts
        self.ends = new_ends

        for _ in range(2):
            for idx in range(len(self.starts) - 1):
                if self.ends[idx] + 1 == self.starts[idx + 1]:
                    self.ends.pop(idx)
                    self.starts.pop(idx + 1)
                    break

    def contains(self, number: int):
        if self.starts[0] > number:
            return False
        idx = 0
        try:
            while self.starts[idx + 1] <= number:
                idx += 1
        except IndexError:
            return False
        return self.ends[idx] >= number

    def digest(self, string):
        start, end = (int(n) for n in string.split("-"))
        assert start <= end
        self.starts.append(start)
        self.ends.append(end)
        self._flatten()

    def invert(self, max:int):
        new_starts = []
        new_ends = []
        

ranges = mrange()
for row in data:
    ranges.digest(row)

print(ranges.ends[0] + 1)
