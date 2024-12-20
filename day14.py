import sys
from collections import defaultdict

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day14.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

N, M = 103, 101
if DEBUG:
    N, M = 7, 11


def parse_val(s: str) -> tuple:
    v1, v2 = s.strip().split('=')[1].split(',')
    return int(v1), int(v2)


class Robot:
    def __init__(self, line: str):
        if len(line) > 0:
            pstr, vstr = line.split(' ')
            self.p = parse_val(pstr)
            self.v = parse_val(vstr)

    def move(self):
        px, py = self.p
        px = (M + px + self.v[0]) % M
        py = (N + py + self.v[1]) % N
        self.p = (px, py)

    def move_period(self, seconds: int = 100):
        for _ in range(seconds):
            self.move()

    def get_quarter_id(self):
        px, py = self.p
        if px == (M - 1) // 2 or py == (N - 1) // 2:
            return None

        return px < (M - 1) // 2, py < (N - 1) // 2

    def __str__(self):
        return f"Robot(p={self.p}, v={self.v})"

    def __repr__(self):
        return self.__str__()

    def copy(self):
        new_robot = Robot("")
        new_robot.p = self.p
        new_robot.v = self.v
        return new_robot


original_robots = [Robot(line) for line in lines]
robots = [robot.copy() for robot in original_robots]

cnt = defaultdict(int)
for robot in robots:
    robot.move_period(100)
    if (quarter_id := robot.get_quarter_id()) is not None:
        cnt[quarter_id] += 1

part_one = 1
for value in cnt.values():
    part_one *= value
print(f"Part one = {part_one}")

iter_count = 0
max_iter = 10000
robots = [robot.copy() for robot in original_robots]


def valid(i: int, j: int) -> bool:
    return 0 <= i < M and 0 <= j < N


def edge(grid, i, j):
    return valid(i, j) and grid[i][j] == '*'


def has_frame(grid, list_of_robots: list) -> bool:
    for robot in list_of_robots:
        i, j = robot.p
        if not edge(grid, i, j + 1) or not edge(grid, i + 1, j):
            continue

        I = i + 1
        while edge(grid, I, j):
            I += 1

        J = j + 1
        while edge(grid, i, J):
            J += 1

        if (I-i) < 10 or (J-j) < 10:
            continue

        if all(grid[x][J - 1] == '*' for x in range(i, I)) and all(grid[I - 1][y] == '*' for y in range(j, J)):
            return True

    return False


def print_grid(grid):
    print('=' * 105)
    for row in grid:
        print("".join(row))


while iter_count < max_iter:
    iter_count += 1
    grid = [[' '] * N for _ in range(M)]
    for robot in robots:
        robot.move()
        rx, ry = robot.p
        grid[rx][ry] = '*'

    if has_frame(grid, robots):
        print_grid(grid)
        break

part_two = iter_count
print(f"Part two = {part_two}")
