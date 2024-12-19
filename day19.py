import sys
from collections import defaultdict

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day19.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

patterns = {ptr.strip() for ptr in lines[0].split(',')}
cache = {ptr: True for ptr in patterns}


def possible(s: str, i: int = 0) -> bool:
    if i >= len(s):
        return True

    if s[i:] in cache:
        return cache[s[i:]]

    cache[s[i:]] = False
    for j in range(i + 1, len(s)):
        if cache.get(s[i:j], False) and possible(s, j):
            cache[s[i:]] = True
            return True

    return False


part_one = sum(possible(s) for s in lines[2:])
print(f"Part one = {part_one}")

count = defaultdict(int)


def count_ways(s: str, i: int = 0) -> int:
    if i >= len(s) or not possible(s[i:]):
        return 0

    if s[i:] in count:
        return count[s[i:]]

    if s[i:] in patterns:
        count[s[i:]] = 1

    for j in range(i + 1, len(s)):
        if s[i:j] in patterns:
            count[s[i:]] += count_ways(s, j)

    return count[s[i:]]


part_two = sum(count_ways(s) for s in lines[2:])
print(f"Part two = {part_two}")
