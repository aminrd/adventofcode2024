import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day17.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


def parse_registry(line: str) -> int:
    return int(line.split(':')[1].strip())


registery = [parse_registry(line) for line in lines[:3]]
program = list(map(int, lines[-1].split(':')[1].strip().split(',')))
idx_pointer = 0
output = []


def get_compo(operand: int) -> int:
    return registery[operand - 4] if operand > 3 else operand


def adv(operand: int):
    registery[0] = registery[0] // 2 ** get_compo(operand)


def bxl(operand: int):
    registery[1] = registery[1] ^ operand


def bst(operand: int):
    registery[1] = get_compo(operand) % 8


def jnz(operand: int):
    global idx_pointer
    if registery[0] != 0:
        idx_pointer = operand - 2


def bxc(operand: int):
    registery[1] = registery[1] ^ registery[2]


def out(operand: int):
    global output
    output.append(get_compo(operand) % 8)


def bdv(operand: int):
    registery[1] = registery[0] // 2 ** get_compo(operand)


def cdv(operand: int):
    registery[2] = registery[0] // 2 ** get_compo(operand)


functions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


def run():
    global idx_pointer
    while idx_pointer < len(program) - 1:
        opcode, operand = program[idx_pointer], program[idx_pointer + 1]
        if DEBUG:
            print(f"Running {functions[opcode].__name__}({operand})")
        functions[opcode](operand)
        idx_pointer += 2
        pass

run()
part_one = ",".join(str(value) for value in output)
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
