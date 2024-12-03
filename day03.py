import re
import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day03.txt"
with open(input_file) as f:
    content = f.read()


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


def get_multiplies(s: str):
    I = 0
    multiplies = []
    while I < len(s):
        I, mul = parse_mul(s, I)
        if mul is not None:
            multiplies.append(mul)

    return multiplies


def get_multiplies_2(s: str):
    i = s.find("don't()")
    if i >= 0:
        s = s[:i]

    I = 0
    multiplies = []
    while I < len(s):
        I, mul = parse_mul(s, I)
        if mul is not None:
            multiplies.append(mul)

    return multiplies


part_one = sum(m.result() for m in get_multiplies(content))
print(f"Part one = {part_one}")

s = "do()" + content + "do()"
part_two = 0
while len(s) > 0:
    do_index = s.find("do()")
    if do_index < 0:
        break

    s = s[do_index + 4:]
    if len(s) < 1:
        break

    i_next = s.find("do()")

    if i_next >= 0:
        mults = get_multiplies_2(s[:i_next])
        for mult in mults:
            part_two += mult.result()
        s = s[i_next:]
    else:
        s = ""

print(f"Part two = {part_two}")
