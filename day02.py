import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day02.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


class Report:
    def __init__(self, line):
        if isinstance(line, str):
            self.arr = list(map(int, line.split()))
        elif isinstance(line, list):
            self.arr = line
        else:
            raise Exception("Only list or str is supported!")

    def increasing(self):
        return all(a < b for a, b in zip(self.arr[:-1], self.arr[1:]))

    def decreasing(self):
        return all(a > b for a, b in zip(self.arr[:-1], self.arr[1:]))

    def safe_diff(self, min_diff=1, max_diff=3):
        return all(min_diff <= abs(a - b) <= max_diff for a, b in zip(self.arr[:-1], self.arr[1:]))

    def is_safe(self, min_diff=1, max_diff=3):
        return self.safe_diff(min_diff, max_diff) and (self.decreasing() or self.increasing())

    def is_safe_with_remove(self):
        # If it's already safe, return True
        if self.is_safe():
            return True

        # Non-efficient way for checking if removing one element can fix it as total number of elemetns on small
        for i in range(len(self.arr)):
            new_arr = self.arr[:i] + self.arr[i + 1:]
            new_report = Report(new_arr)
            if new_report.is_safe():
                return True

        return False


reports = [Report(line) for line in lines]
part_one = sum(report.is_safe() for report in reports)
print(f"Part one = {part_one}")

part_two = sum(report.is_safe_with_remove() for report in reports)
print(f"Part two = {part_two}")
