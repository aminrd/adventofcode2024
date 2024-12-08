import sys
from collections import defaultdict

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day08.txt"
with open(input_file) as f:
    lines = f.readlines()

grid = [line.strip() for line in lines]
m, n = len(grid), len(grid[0])
freq = defaultdict(list)


def valid(i, j):
    return 0 <= i < m and 0 <= j < n


def get_valid_antinodes(loc1: tuple, loc2: tuple):
    x1, y1 = loc1
    x2, y2 = loc2
    diff_x = x1 - x2
    diff_y = y1 - y2
    output = [(x1 + diff_x, y1 + diff_y), (x2 - diff_x, y2 - diff_y)]
    return [(x, y) for (x, y) in output if valid(x, y)]


def get_valid_antinodes_many(loc1: tuple, loc2: tuple):
    x1, y1 = loc1
    x2, y2 = loc2
    diff_x = x1 - x2
    diff_y = y1 - y2

    output = []
    while valid(x1, y1):
        output.append((x1, y1))
        x1 += diff_x
        y1 += diff_y

    while valid(x2, y2):
        output.append((x2, y2))
        x2 -= diff_x
        y2 -= diff_y

    return output


for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val != '.':
            freq[val].append((i, j))

antinodes = set()
for arr in freq.values():
    if len(arr) < 2:
        continue

    for i, loc1 in enumerate(arr):
        for loc2 in arr[i + 1:]:
            for (x, y) in get_valid_antinodes(loc1, loc2):
                antinodes.add((x, y))

part_one = len(antinodes)
print(f"Part one = {part_one}")

antinodes2 = set()
for arr in freq.values():
    if len(arr) < 2:
        continue

    for i, loc1 in enumerate(arr):
        for loc2 in arr[i + 1:]:
            for (x, y) in get_valid_antinodes_many(loc1, loc2):
                antinodes2.add((x, y))

part_two = len(antinodes2)
print(f"Part two = {part_two}")
