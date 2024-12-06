import sys
from tqdm import tqdm

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day06.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
grid = [list(line) for line in lines]

m, n = len(grid), len(grid[0])


def valid(i: int, j: int) -> bool:
    return 0 <= i < m and 0 <= j < n


GI, GJ = None, None
for i, row in enumerate(grid):
    if (GI, GJ) != (None, None):
        break
    for j, val in enumerate(row):
        if val == '^':
            GI, GJ = i, j
            grid[i][j] = '.'
            break

di, dj = -1, 0
gi, gj = GI, GJ

director = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

visited = {(gi, gj)}
while valid(gi, gj):
    next_i, next_j = gi + di, gj + dj
    if valid(next_i, next_j):
        if grid[next_i][next_j] == '#':
            di, dj = director[(di, dj)]
        else:
            gi, gj = next_i, next_j
            visited.add((gi, gj))
    else:
        gi, gj = next_i, next_j

part_one = len(visited)
print(f"Part one = {part_one}")


def creates_loop(block_i, block_j):
    # Copy the gird first
    arr = [[val for val in row] for row in grid]
    arr[block_i][block_j] = '#'
    di, dj = -1, 0
    gi, gj = GI, GJ
    visited = {(gi, gj, di, dj)}

    while valid(gi, gj):
        next_i, next_j = gi + di, gj + dj
        if valid(next_i, next_j):
            if (next_i, next_j, di, dj) in visited:
                return True
            if arr[next_i][next_j] == '#':
                di, dj = director[(di, dj)]
            else:
                gi, gj = next_i, next_j
            visited.add((gi, gj, di, dj))
        else:
            gi, gj = next_i, next_j

    return False


part_two = 0
for bi, row in tqdm(enumerate(grid), total=len(grid)):
    for bj, val in enumerate(row):
        if grid[bi][bj] != '#' and (bi, bj) != (GI, GJ) and creates_loop(bi, bj):
            part_two += 1

print(f"Part two = {part_two}")
