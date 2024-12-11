import sys
from tqdm import tqdm

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day11.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
arr = list(map(int, lines[0].split()))


def evolve(num, output: list):
    if num == 0:
        output.append(1)
        return

    s = str(num)
    if len(s) % 2 == 1:
        output.append(num * 2024)
        return

    n1, n2 = s[:len(s) // 2], s[len(s) // 2:]
    output.append(int(n1))
    output.append(int(n2))


number_of_iterations = 25
for _ in tqdm(range(number_of_iterations)):
    output = []
    for num in arr:
        evolve(num, output)
    arr = output

    if len(arr) >= 10 ** 8:
        raise Exception("Growing too much!")


part_one = len(arr)
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
