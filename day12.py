import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day12.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
m, n = len(lines), len(lines[0])
directions = ((-1, 0), (1, 0), (0, 1), (0, -1))


class Region:
    def __init__(self, letter: str):
        self.letter = letter
        self.positions = set()

    def add(self, i: int, j: int):
        self.positions.add((i, j))

    def get_area(self) -> int:
        return len(self.positions)

    def get_single_block_perimeter(self, i: int, j: int) -> int:
        perimeter = 4
        for di, dj in directions:
            ai, aj = i+di, j+dj
            if valid(ai, aj) and (ai, aj) in self.positions:
                perimeter -= 1
        return perimeter

    def get_perimeter(self) -> int:
        return sum(self.get_single_block_perimeter(i, j) for i, j in self.positions)

    def get_cost(self) -> int:
        return self.get_area() * self.get_perimeter()


def valid(i: int, j: int) -> bool:
    return 0 <= i < m and 0 <= j < n


regions = []
visited = [[False] * n for _ in range(m)]
for i, row in enumerate(lines):
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
                if valid(ai, aj) and not visited[ai][aj] and lines[ai][aj] == c:
                    queue.append((ai, aj))
                    visited[ai][aj] = True

        regions.append(new_region)

part_one = sum(region.get_cost() for region in regions)
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
