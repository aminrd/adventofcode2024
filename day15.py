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
BOX_LEFT = '['
BOX_RIGHT = ']'
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
grid2 = []
while len(lines) > 0:
    line = lines.pop(0)
    if len(line) == 0:
        break
    grid.append(list(line))

    new_row = []
    for c in line:
        if c == WALL or c == SPACE:
            new_row.append(c)
            new_row.append(c)
        elif c == BOX:
            new_row.append(BOX_LEFT)
            new_row.append(BOX_RIGHT)
        elif c == ROBOT:
            new_row.append(ROBOT)
            new_row.append(SPACE)

    grid2.append(new_row)


def print_board(arr: list):
    print('=' * 30)
    for row in arr:
        print("".join(row))
    print('=' * 30)


def gps(i: int, j: int) -> int:
    return 100 * i + j


def find_robot(arr):
    for i, row in enumerate(arr):
        for j, c in enumerate(row):
            if c == ROBOT:
                return i, j


def find_boxes(arr, box_char=BOX):
    boxes = []
    for i, row in enumerate(arr):
        for j, c in enumerate(row):
            if c == box_char:
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


def can_move2(i, j, direction):
    if grid2[i][j] == WALL:
        return False

    if grid2[i][j] == SPACE:
        return True

    # BOXES
    if direction == LEFT:
        return can_move2(i, j - 2, direction)
    elif direction == RIGHT:
        return can_move2(i, j + 2, direction)

    box_coordinates = [(i, j)]
    if grid2[i][j] == BOX_LEFT:
        box_coordinates.append((i, j + 1))
    else:
        box_coordinates.append((i, j - 1))

    di, dj = direction
    return all(can_move2(bi + di, bj + dj, direction) for bi, bj in box_coordinates)


def do_move(i, j, direction):
    if grid2[i][j] == SPACE:
        return

    box_coordinates = [(i, j)]
    if grid2[i][j] == '[':
        box_coordinates.append((i, j + 1))
    else:
        box_coordinates.append((i, j - 1))

    if box_coordinates[0] > box_coordinates[1]:
        box_coordinates.append(box_coordinates.pop(0))

    # BOXES
    di, dj = direction

    if direction == LEFT:
        do_move(box_coordinates[0][0], box_coordinates[0][1] - 1, LEFT)
    elif direction == RIGHT:
        do_move(box_coordinates[1][0], box_coordinates[1][1] + 1, RIGHT)
    else:
        for bi, bj in box_coordinates:
            do_move(bi + di, bj + dj, direction)

    for k, (bi, bj) in enumerate(box_coordinates):
        grid2[bi + di][bj + dj] = '[]'[k]

    if direction == RIGHT:
        grid2[box_coordinates[0][0]][box_coordinates[0][1]] = SPACE
    elif direction == LEFT:
        grid2[box_coordinates[1][0]][box_coordinates[1][1]] = SPACE
    else:
        for bi, bj in box_coordinates:
            grid2[bi][bj] = SPACE


def move2(i, j, direction):
    di, dj = direction
    ai, aj = i + di, j + dj

    # Empty space
    if grid2[ai][aj] == SPACE:
        grid2[ai][aj] = ROBOT
        grid2[i][j] = SPACE
        return ai, aj

    # Wall
    if grid2[ai][aj] == WALL:
        return i, j

    # Box
    if can_move2(ai, aj, direction):
        do_move(ai, aj, direction)
        grid2[ai][aj] = ROBOT
        grid2[i][j] = SPACE
        i, j = ai, aj

    return i, j


ri, rj = find_robot(grid)
for command_line in lines:
    for c in command_line:
        ri, rj = move(ri, rj, c2dir[c])

part_one = sum(gps(i, j) for i, j in find_boxes(grid))
print(f"Part one = {part_one}")

ri, rj = find_robot(grid2)
for command_line in lines:
    for c in command_line:
        ri, rj = move2(ri, rj, c2dir[c])
        if DEBUG:
            print_board(grid2)

part_two = sum(gps(i, j) for i, j in find_boxes(grid2, BOX_LEFT))
print(f"Part two = {part_two}")
