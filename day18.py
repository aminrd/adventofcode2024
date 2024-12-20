import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day18.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

N = 6 if DEBUG else 70
max_bytes_part_one = 12 if DEBUG else 1024

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = (UP, DOWN, LEFT, RIGHT)


def get_pair(line: str) -> tuple:
    return tuple(map(int, line.split(',')))


pairs = [get_pair(line) for line in lines]
blocks_part_one = {pair for pair in pairs[:max_bytes_part_one]}


def valid(i: int, j: int) -> bool:
    return 0 <= i <= N and 0 <= j <= N


def bfs(src=(0, 0), dst=(N, N), blocks: set=blocks_part_one):
    queue = [(src[0], src[1], 0)]
    visited = {src}

    while len(queue) > 0:
        i, j, d = queue.pop(0)
        for di, dj in directions:
            ai, aj = i+di, j+dj
            if (ai, aj) == dst:
                return d+1
            if valid(ai, aj) and (ai, aj) not in visited and (ai, aj) not in blocks:
                visited.add((ai, aj))
                queue.append((ai, aj, d+1))
    return 10 ** 9


part_one = bfs()
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
