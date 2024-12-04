import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day04.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

arr = [list(line) for line in lines]
pattern = "XMAS"
pattern_set = set(pattern)

m, n = len(arr), len(arr[0])


def valid(i: int, j: int):
    return 0 <= i < m and 0 <= j < n


def check_direction(i: int, j: int, di: int, dj: int):
    for c_ptr in pattern:
        if not valid(i, j) or not arr[i][j] == c_ptr:
            return False
        i, j = i + di, j + dj
    return True


directions = []
for di in range(-1, 2):
    for dj in range(-1, 2):
        if (di, dj) != (0, 0):
            directions.append((di, dj))

part_one = 0
for i, row in enumerate(arr):
    for j, c in enumerate(row):
        if c != "X":
            continue

        part_one += sum(check_direction(i, j, di, dj) for (di, dj) in directions)

print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
