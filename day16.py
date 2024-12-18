import sys
import heapq
from collections import defaultdict

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day16.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
grid = [list(row) for row in lines]

INF = 10 ** 9
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = (UP, DOWN, LEFT, RIGHT)
rotate_right = {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP
}
rotate_left = {
    UP: LEFT,
    LEFT: DOWN,
    DOWN: RIGHT,
    RIGHT: UP
}

start = None
target = None
for i, row in enumerate(grid):
    if start is not None and target is not None:
        break
    for j, c in enumerate(row):
        if c == 'S':
            start = i, j
            grid[i][j] = '.'
        elif c == 'E':
            grid[i][j] = '.'
            target = i, j

M, N = len(grid), len(grid[0])


def move(position, direction, reverse=False):
    if not reverse:
        return position[0] + direction[0], position[1] + direction[1]
    else:
        return position[0] - direction[0], position[1] - direction[1]


def valid(position):
    pi, pj = position
    return 0 <= pi < M and 0 <= pj < N and grid[pi][pj] != '#'


def bfs(position=start, start_direction=RIGHT):
    # Construcing heap with (score, position, direction)
    visited = {(position, start_direction)}
    h = [(0, position, start_direction)]

    while len(h) > 0:
        score, p, d = heapq.heappop(h)
        if p == target:
            return score

        adj = move(p, d)
        if valid(adj) and (adj, d) not in visited:
            visited.add((adj, d))
            heapq.heappush(h, (score + 1, adj, d))

        for d_new in (rotate_right[d], rotate_left[d]):
            if (p, d_new) not in visited:
                heapq.heappush(h, (score + 1000, p, d_new))
                visited.add((p, d_new))

    return INF


part_one = bfs(start, RIGHT)
print(f"Part one = {part_one}")


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def minimum_remaining_cost(p):
    return manhattan(p, target) + 1000 * (p[0] != target[0] and p[1] != target[1])


def disjstra(position=start, start_direction=RIGHT, reverse=False):
    dist = {(start, start_direction): 0}
    # Construcing heap with (score, position, direction)

    h = [(0, position, start_direction)]
    while len(h) > 0:
        score, p, d = heapq.heappop(h)
        adj = move(p, d, reverse)
        if valid(adj) and (adj, d) not in dist:
            dist[(adj, d)] = score + 1
            heapq.heappush(h, (score + 1, adj, d))

        for d_new in (rotate_right[d], rotate_left[d]):
            if (p, d_new) not in dist:
                heapq.heappush(h, (score + 1000, p, d_new))
                dist[(p, d_new)] = score + 1000

    return dist


from_source = disjstra(start, RIGHT)
from_target = disjstra(target, UP, reverse=True)

good_cells = {start, target}

for k,v in from_source.items():
    if v + from_target.get(k, INF) <= part_one:
        good_cells.add(k[0])

part_two = len(good_cells)
print(f"Part two = {part_two}")
