import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day03.txt"
with open(input_file) as f:
    s = f.read()


class Mul:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def result(self):
        return self.a * self.b


def parse_int(s: str, i: int):
    val = 0
    while i < len(s) and s[i].isdigit():
        val = val * 10 + int(s[i])
        i += 1
    return val, i


def parse_mul(s: str, i: int):
    mul = None
    if s[i:i + 4] != "mul(":
        return i + 1, mul

    i = i + 4
    if i >= len(s) or not s[i].isdigit():
        return i, mul

    a, i = parse_int(s, i)
    if i >= len(s) or s[i] != ',':
        return i, mul

    i += 1
    if i >= len(s) or not s[i].isdigit():
        return i, mul

    b, i = parse_int(s, i)
    if i >= len(s) or not s[i] == ')':
        return i, mul

    mul = Mul(a, b)
    return i, mul


I = 0
multiplies = []
while I < len(s):
    I, mul = parse_mul(s, I)
    if mul is not None:
        multiplies.append(mul)

part_one = sum(m.result() for m in multiplies)
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
