import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day15.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

BOX = 'O'
WALL = '#'
ROBOT = '@'
SPACE = '.'

directions = (UP, DOWN, LEFT, RIGHT)
c2dir = {
    '<': LEFT,
    '>': RIGHT,
    '^': UP,
    'v': DOWN
}

grid = []
while len(lines) > 0:
    line = lines.pop(0)
    if len(line) == 0:
        break
    grid.append(list(line))


def gps(i: int, j: int) -> int:
    return 100 * i + j


def find_robot():
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == ROBOT:
                return i, j


def find_boxes():
    boxes = []
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == BOX:
                boxes.append((i, j))

    return boxes


def move(i, j, direction):
    di, dj = direction
    ai, aj = i + di, j + dj

    # Empty space
    if grid[ai][aj] == SPACE:
        grid[ai][aj] = ROBOT
        grid[i][j] = SPACE
        return ai, aj

    # Wall
    if grid[ai][aj] == WALL:
        return i, j

    # Box
    bi, bj = ai, aj
    while grid[bi][bj] == BOX:
        bi, bj = bi + di, bj + dj

    if grid[bi][bj] == WALL:
        return i, j

    # Found an empty space to move the boxes
    grid[bi][bj] = BOX
    grid[ai][aj] = ROBOT
    grid[i][j] = SPACE
    return ai, aj


ri, rj = find_robot()
for command_line in lines:
    for c in command_line:
        ri, rj = move(ri, rj, c2dir[c])

part_one = sum(gps(i, j) for i, j in find_boxes())
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
