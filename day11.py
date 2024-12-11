import sys
from tqdm import tqdm
from collections import defaultdict

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


def evolve2(key: int, value: int, output_counter: dict):
    if key == 0:
        output_counter[1] += value
        return

    s = str(key)
    if len(s) % 2 == 1:
        output_counter[key * 2024] += value
        return

    n1, n2 = s[:len(s) // 2], s[len(s) // 2:]
    output_counter[int(n1)] += value
    output_counter[int(n2)] += value


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

arr = list(map(int, lines[0].split()))

cnt = defaultdict(int)
for num in arr:
    cnt[num] = 1

for _ in tqdm(range(75)):
    new_cnt = defaultdict(int)
    for k, v in cnt.items():
        evolve2(k, v, new_cnt)

    del cnt
    cnt = new_cnt

part_two = sum(cnt.values())
print(f"Part two = {part_two}")
