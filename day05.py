import sys
from collections import defaultdict
from functools import cmp_to_key

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day05.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

left = defaultdict(set)
right = defaultdict(set)

while "|" in lines[0]:
    line = lines.pop(0)
    l, r = map(int, line.split("|"))
    left[l].add(r)
    right[r].add(l)


# Left[X] contains all values X is smaller
def comparator(a, b):
    if b in left[a]:
        return -1
    elif a in left[b]:
        return 1
    return 0

class Ordering:
    def __init__(self, line):
        self.arr = list(map(int, line.split(',')))
        self.n = len(self.arr)

    def is_valid(self) -> bool:
        for i, val in enumerate(self.arr):
            if any(self.arr[j] not in left[val] for j in range(i+1, self.n)):
                return False
        return True

    def fix(self):
        new_arr = list(sorted(self.arr, key=cmp_to_key(comparator)))
        return Ordering(",".join(str(val) for val in new_arr))

    def get_middle(self):
        return self.arr[self.n // 2]

lines.pop(0)
orderings = []
for line in lines:
    orderings.append(Ordering(line))


part_one = sum(ordering.get_middle() for ordering in orderings if ordering.is_valid())
print(f"Part one = {part_one}")

part_two = 0
for ordering in orderings:
    if ordering.is_valid():
        continue

    part_two += ordering.fix().get_middle()

print(f"Part two = {part_two}")

