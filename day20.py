import sys
from tqdm import tqdm

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day20.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
grid = [list(line) for line in lines]

# ======================================================
M, N = len(grid), len(grid[0])
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = (UP, DOWN, LEFT, RIGHT)
WALL = '#'
INF = 10 ** 9
# ======================================================

original_start = None
original_end = None
walls = set()


def is_wall_breakable(i, j):
    if i == 0 or j == 0 or i == M - 1 or j == N - 1:
        return False
    return any(grid[i + di][j + dj] != WALL for di, dj in directions)


for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == 'S':
            original_start = i, j
            grid[i][j] = '.'
        elif c == 'E':
            original_end = i, j
            grid[i][j] = '.'
        elif grid[i][j] == WALL and is_wall_breakable(i, j):
            walls.add((i, j))

MARGIN = None


def bfs(src=original_start, dst=original_end, cheat=None):
    queue = [(src[0], src[1], 0)]
    visited = {src}

    while len(queue) > 0:
        i, j, d = queue.pop(0)

        if cheat is not None and d > MARGIN - 1:
            return INF

        for di, dj in directions:
            ai, aj = i + di, j + dj
            if (ai, aj) == dst:
                return d + 1

            if (ai, aj) not in visited and (grid[ai][aj] != WALL or (ai, aj) == cheat):
                queue.append((ai, aj, d + 1))
                visited.add((ai, aj))

    return INF


distance = bfs()
MARGIN = distance - 99 if not DEBUG else distance - 39
good_walls = set()
for wall in tqdm(walls):
    if bfs(cheat=wall) < MARGIN:
        good_walls.add(wall)

part_one = len(good_walls)
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
