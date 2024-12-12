import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day12.txt"
with open(input_file) as f:
    grid = f.readlines()
grid = [line.strip() for line in grid]
m, n = len(grid), len(grid[0])

LEFT = (0, -1)
RIGHT = (0, 1)
TOP = (-1, 0)
DOWN = (1, 0)
directions = (LEFT, DOWN, RIGHT, TOP)


def get_block_line(i: int, j: int, di: int, dj: int) -> tuple:
    if (di, dj) == (0, -1):  # left
        return (i, j), (i + 1, j)
    elif (di, dj) == (-1, 0):  # top
        return (i, j), (i, j + 1)
    elif (di, dj) == (0, 1):  # right
        return (i, j + 1), (i + 1, j + 1)
    else:
        return (i + 1, j), (i + 1, j + 1)


def is_horizontal(point1, point2):
    return point1[0] == point2[0]


def is_vertical(point1, point2):
    return point1[1] == point2[1]


def get_line_directions(p1, p2):
    if is_horizontal(p1, p2):
        return (0, 1), (0, -1)
    else:
        return (1, 0), (-1, 0)


def move_point(p: tuple, d: tuple):
    return p[0] + d[0], p[1] + d[1]


def move_line(p1: tuple, p2: tuple, d):
    p1 = move_point(p1, d)
    p2 = move_point(p2, d)
    return (p1, p2) if p1 < p2 else (p2, p1)


def get_cell_by_edge(e: tuple, d: tuple):
    base_i, base_j = e[0]
    if d == DOWN:
        i, j = base_i, base_j
    elif d == TOP:
        i, j = base_i - 1, base_j
    elif d == LEFT:
        i, j = base_i, base_j - 1
    elif d == RIGHT:
        i, j = base_i, base_j

    if valid(i, j):
        return grid[i][j]


def are_neighbour_edges_same_side(e1: tuple, e2: tuple):
    if is_horizontal(*e1):
        return get_cell_by_edge(e1, TOP) == get_cell_by_edge(e2, TOP) or get_cell_by_edge(e1, DOWN) == get_cell_by_edge(e2, DOWN)
    else:
        return get_cell_by_edge(e1, LEFT) == get_cell_by_edge(e2, LEFT) or get_cell_by_edge(e1, RIGHT) == get_cell_by_edge(e2, RIGHT)


class Region:
    def __init__(self, letter: str):
        self.letter = letter
        self.positions = set()
        self.perimeter_lines = set()
        self.cached_perimiter = None

    def __str__(self):
        return f"Region({self.letter})"

    def __repr__(self):
        return self.__str__()

    def add(self, i: int, j: int):
        self.positions.add((i, j))

    def get_area(self) -> int:
        return len(self.positions)

    def get_single_block_perimeter(self, i: int, j: int) -> int:
        perimeter = 4
        for di, dj in directions:
            ai, aj = i + di, j + dj
            if valid(ai, aj) and (ai, aj) in self.positions:
                perimeter -= 1
            else:
                self.perimeter_lines.add(get_block_line(i, j, di, dj))
        return perimeter

    def get_perimeter(self) -> int:
        if self.cached_perimiter is None:
            self.cached_perimiter = sum(self.get_single_block_perimeter(i, j) for i, j in self.positions)
        return self.cached_perimiter

    def get_cost(self) -> int:
        return self.get_area() * self.get_perimeter()

    def count_sides(self) -> int:
        cnt = 0
        edges = {edge for edge in self.perimeter_lines}

        for (p1, p2) in self.perimeter_lines:
            if (p1, p2) not in edges:
                # we must already visited that edge
                continue

            # Found a new side
            cnt += 1
            line_directions = get_line_directions(p1, p2)
            edges.remove((p1, p2))

            # Move the line left<->right or up<->down
            for line_direction in line_directions:
                previous_edge = (p1, p2)
                edge = move_line(p1, p2, line_direction)
                while edge in edges and are_neighbour_edges_same_side(previous_edge, edge):
                    edges.remove(edge)
                    previous_edge = edge
                    edge = move_line(edge[0], edge[1], line_direction)

        return cnt


def valid(i: int, j: int) -> bool:
    return 0 <= i < m and 0 <= j < n


regions = []
visited = [[False] * n for _ in range(m)]
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if visited[i][j]:
            continue

        new_region = Region(c)
        queue = [(i, j)]
        visited[i][j] = True

        while len(queue) > 0:
            qi, qj = queue.pop(0)
            new_region.add(qi, qj)

            for di, dj in directions:
                ai, aj = qi + di, qj + dj
                if valid(ai, aj) and not visited[ai][aj] and grid[ai][aj] == c:
                    queue.append((ai, aj))
                    visited[ai][aj] = True

        regions.append(new_region)

part_one = sum(region.get_cost() for region in regions)
print(f"Part one = {part_one}")

part_two = sum(region.get_area() * region.count_sides() for region in regions)
print(f"Part two = {part_two}")