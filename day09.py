import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day09.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

files = list(map(int, lines[0]))
if len(files) % 2 != 0:
    files.append(0)

n = len(files) // 2
disk = []
for i in range(n):
    disk += [i] * files[2 * i]
    disk += [None] * files[2 * i + 1]


def compress(array: list) -> list:
    arr = [value for value in array]
    i, j = 0, len(arr) - 1

    while j > i and arr[j] is None:
        j -= 1

    while i < j:
        while i < j and arr[i] is not None:
            i += 1

        arr[i], arr[j] = arr[j], arr[i]
        while j > i and arr[j] is None:
            j -= 1

    return arr


def checksum(arr: list) -> int:
    return sum(i * f for i, f in enumerate(arr) if f is not None)


part_one = checksum(compress(disk))
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
