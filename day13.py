import sys
import numpy as np

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day13.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
INF = 10 ** 9


def get_target_prize(s: str) -> tuple:
    x_str, y_str = s[7:].split(',')
    x = int(x_str.split('=')[1].strip())
    y = int(y_str.split('=')[1].strip())
    return x, y


def get_button_moves(s: str) -> tuple:
    x_str, y_str = s[10:].split(',')
    x = int(x_str.split('+')[1].strip())
    y = int(y_str.split('+')[1].strip())
    return x, y


class Game:
    def __init__(self, three_linse: list):
        self.a = get_button_moves(three_linse[0])
        self.b = get_button_moves(three_linse[1])
        self.target = get_target_prize(three_linse[2])

    def __str__(self):
        return f"Game( {self.a} $ {self.b} = {self.target} )"

    def __repr__(self):
        return self.__str__()

    def equals(self, push_a: int, push_b: int) -> bool:
        return (push_a * self.a[0] + push_b * self.b[0] == self.target[0] and
                push_a * self.a[1] + push_b * self.b[1] == self.target[1])

    def solve_with_max(self, max_push:int = 100):
        tokens = INF
        for push_a in range(max_push+1):
            for push_b in range(max_push+1):
                if self.equals(push_a, push_b):
                    tokens = min(tokens, 3 * push_a + push_b)

        return 0 if tokens == INF else tokens

games = []
while len(lines) > 0:
    if len(lines[0]) == 0:
        lines.pop(0)

    l = []
    for _ in range(3):
        l.append(lines.pop(0))
    games.append(Game(l))

part_one = sum(game.solve_with_max(100) for game in games)
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
