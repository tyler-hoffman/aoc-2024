from dataclasses import dataclass
from functools import cached_property
from typing import Sequence
from aoc_2024.day_04.parser import Parser


@dataclass
class Day04PartBSolver:
    input: Sequence[Sequence[str]]

    @property
    def solution(self) -> int:
        output = 0
        target = (self._forward, self._backward)
        for y in range(self._height - 2):
            for x in range(self._width - 2):
                lr_vals = [self.input[y + i][x + i] for i in range(3)]
                rl_vals = [self.input[y + 2 - i][x + i] for i in range(3)]
                if lr_vals in target and rl_vals in target:
                    output += 1
        return output

    @cached_property
    def _forward(self) -> Sequence[str]:
        return list("MAS")

    @cached_property
    def _backward(self) -> Sequence[str]:
        return self._forward[::-1]

    @cached_property
    def _height(self) -> int:
        return len(self.input)

    @cached_property
    def _width(self) -> int:
        return len(self.input[0])


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day04PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_04/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
