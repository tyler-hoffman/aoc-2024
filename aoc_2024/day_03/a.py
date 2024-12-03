from functools import cached_property
import re
from dataclasses import dataclass
from aoc_2024.day_03.parser import Parser


@dataclass
class Day03PartASolver:
    input: str

    @property
    def solution(self) -> int:
        output = 0
        matches = self._pattern.findall(self.input)
        for match in matches:
            a, b = match[4:-1].split(",")
            output += int(a) * int(b)
        return output

    @cached_property
    def _pattern(self) -> re.Pattern:
        return re.compile(r"mul\(\d+,\d+\)")


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day03PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_03/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
