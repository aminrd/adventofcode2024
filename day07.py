import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day07.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


def get_ints(s: str):
    return list(map(int, s.strip().split()))


def backtrack(target: int, arr: list, value: int, i: int = 0):
    if value > target:
        return False

    if i >= len(arr):
        return target == value

    return backtrack(target, arr, value + arr[i], i + 1) or backtrack(target, arr, value * arr[i], i + 1)


class Equation:
    def __init__(self, line: str):
        left_str, right_str = line.split(':')
        self.left = get_ints(left_str)[0]
        self.right = get_ints(right_str)

    def can_form(self) -> bool:
        if len(self.right) < 2:
            return self.left == self.right[1]
        return backtrack(self.left, self.right, self.right[0], 1)

equations = [Equation(line) for line in lines]

part_one = sum(equation.left for equation in equations if equation.can_form())
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
