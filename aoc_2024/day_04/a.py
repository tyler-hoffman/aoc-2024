from dataclasses import dataclass
from functools import cached_property
from typing import Sequence
from aoc_2024.day_04.parser import Parser


@dataclass
class Day04PartASolver:
    input: Sequence[Sequence[str]]

    @property
    def solution(self) -> int:
        return sum(
            [
                self._vertical_count,
                self._horizontal_count,
                self._lr_diagonal_count,
                self._rl_diagonal_count,
            ]
        )

    @cached_property
    def _forward(self) -> Sequence[str]:
        return list("XMAS")

    @cached_property
    def _backward(self) -> Sequence[str]:
        return self._forward[::-1]

    @cached_property
    def _height(self) -> int:
        return len(self.input)

    @cached_property
    def _width(self) -> int:
        return len(self.input[0])

    @cached_property
    def _vertical_count(self) -> int:
        output = 0
        for y in range(self._height - 3):
            for x in range(self._width):
                vals = [self.input[y + i][x] for i in range(4)]
                if vals in (self._forward, self._backward):
                    output += 1
        return output

    @cached_property
    def _horizontal_count(self) -> int:
        output = 0
        for y in range(self._height):
            for x in range(self._width - 3):
                vals = [self.input[y][x + i] for i in range(4)]
                if vals in (self._forward, self._backward):
                    output += 1
        return output

    @cached_property
    def _lr_diagonal_count(self) -> int:
        output = 0
        for y in range(self._height - 3):
            for x in range(self._width - 3):
                vals = [self.input[y + i][x + i] for i in range(4)]
                if vals in (self._forward, self._backward):
                    output += 1
        return output

    @cached_property
    def _rl_diagonal_count(self) -> int:
        output = 0
        for y in range(self._height - 3):
            for x in range(self._width - 3):
                vals = [self.input[y + 3 - i][x + i] for i in range(4)]
                if vals in (self._forward, self._backward):
                    output += 1
        return output


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day04PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_04/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
