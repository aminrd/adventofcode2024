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

class Block:
    def __init__(self, index: int, size: int):
        self.index = index
        self.size = size


file_meta = dict()
free_blocks = []

for i in range(n):
    file_block = Block(len(disk), files[2 * i])
    file_meta[i] = file_block
    disk += [i] * files[2 * i]

    free_block = Block(len(disk), files[2 * i + 1])
    disk += [None] * files[2 * i + 1]
    free_blocks.append(free_block)


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


def fragment(array: list) -> list:
    arr = [value for value in array]

    for file_id in range(n-1, -1, -1):
        file_block = file_meta[file_id]

        for j, free_block in enumerate(free_blocks):
            if free_block.index > file_block.index:
                break

            if free_block.size < file_block.size:
                continue

            for k in range(file_block.size):
                arr[file_block.index + k] = None
                arr[free_block.index + k] = file_id

            free_block.size -= file_block.size
            free_block.index += file_block.size
            if free_block.size == 0:
                free_blocks.pop(j)

            break
    return arr


def checksum(arr: list) -> int:
    return sum(i * f for i, f in enumerate(arr) if f is not None)


part_one = checksum(compress(disk))
print(f"Part one = {part_one}")

part_two = checksum(fragment(disk))
print(f"Part two = {part_two}")
