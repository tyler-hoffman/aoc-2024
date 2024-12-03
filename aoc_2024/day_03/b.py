from functools import cached_property
import re
from dataclasses import dataclass
from aoc_2024.day_03.parser import Parser


@dataclass
class Day03PartBSolver:
    input: str

    @property
    def solution(self) -> int:
        output = 0
        matches = self._pattern.findall(self.input)
        enabled = True
        for match in matches:
            match match:
                case mul, "", "":
                    if enabled:
                        a, b = mul[4:-1].split(",")
                        output += int(a) * int(b)
                case "", _, "":
                    enabled = True
                case "", "", _:
                    enabled = False

        return output

    @cached_property
    def _pattern(self) -> re.Pattern:
        patterns = [
            r"mul\(\d+,\d+\)",
            r"do\(\)",
            r"don't\(\)",
        ]
        return re.compile(r"|".join(f"({p})" for p in patterns))


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day03PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_03/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
