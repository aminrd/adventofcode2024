import sys
import itertools

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day10.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
grid = [list(map(int, line)) for line in lines]

directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
m, n = len(grid), len(grid[0])


def valid(i: int, j: int) -> bool:
    return 0 <= i < m and 0 <= j < n


def get_score(i: int, j: int) -> int:
    if grid[i][j] != 0:
        return 0

    score = 0
    queue = [(i, j)]
    visited = {(i, j)}
    while len(queue) != 0:
        qi, qj = queue.pop(0)
        if grid[qi][qj] == 9:
            score += 1
            continue

        for di, dj in directions:
            ai, aj = qi + di, qj + dj
            adj = (ai, aj)
            if valid(ai, aj) and adj not in visited and grid[ai][aj] == grid[qi][qj] + 1:
                queue.append(adj)
                visited.add(adj)
    return score


part_one = sum(get_score(i, j) for i, j in itertools.product(range(m), range(n)))
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
