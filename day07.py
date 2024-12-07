import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day07.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


def get_ints(s: str):
    return list(map(int, s.strip().split()))


def concat(a: int, b: int):
    return int(str(a) + str(b))


def add(a: int, b: int):
    return a + b


def mult(a: int, b: int):
    return a * b


def backtrack(target: int, arr: list, value: int, i: int = 0):
    if value > target:
        return False

    if i >= len(arr):
        return target == value

    return any(backtrack(target, arr, operation(value, arr[i]), i + 1) for operation in (add, mult))


def backtrack2(target: int, arr: list, value: int, i: int = 0):
    if i >= len(arr):
        return target == value

    if value >= target:
        return False

    return any(backtrack2(target, arr, operation(value, arr[i]), i + 1) for operation in (add, mult, concat))


class Equation:
    def __init__(self, line: str):
        left_str, right_str = line.split(':')
        self.left = get_ints(left_str)[0]
        self.right = get_ints(right_str)
        self.can_form_simple = False

    def can_form(self) -> bool:
        if len(self.right) < 2:
            self.can_form_simple = self.left == self.right[1]
        else:
            self.can_form_simple = backtrack(self.left, self.right, self.right[0], 1)
        return self.can_form_simple

    def can_form2(self):
        if self.can_form_simple:
            return True
        if len(self.right) < 2:
            return self.left == self.right[1]
        return backtrack2(self.left, self.right, self.right[0], 1)


equations = [Equation(line) for line in lines]

part_one = sum(equation.left for equation in equations if equation.can_form())
print(f"Part one = {part_one}")

part_two = sum(equation.left for equation in equations if equation.can_form2())
print(f"Part two = {part_two}")
