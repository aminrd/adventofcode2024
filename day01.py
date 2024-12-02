import sys
from collections import defaultdict

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day01.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

left = []
right = []
cnt = defaultdict(int)

for line in lines:
    l, r = map(int, line.split())
    left.append(l)
    right.append(r)
    cnt[r] += 1

part_one = sum(abs(l-r) for l, r in zip(sorted(left), sorted(right)))
print(f"Part one = {part_one}")

part_two = sum(val * cnt[val] for val in left)
print(f"Part two = {part_two}")

