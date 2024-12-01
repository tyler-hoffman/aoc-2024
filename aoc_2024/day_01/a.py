from dataclasses import dataclass
from functools import cached_property
from typing import Sequence
from aoc_2024.day_01.parser import Parser


@dataclass
class Day01PartASolver:
    input: Sequence[tuple[int, int]]

    @property
    def solution(self) -> int:
        output = 0
        for a, b in zip(self.sorted_list_1, self.sorted_list_2):
            output += abs(a - b)
        return output

    @cached_property
    def sorted_list_1(self) -> Sequence[int]:
        return sorted([a for a, _ in self.input])

    @cached_property
    def sorted_list_2(self) -> Sequence[int]:
        return sorted([b for _, b in self.input])


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day01PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_01/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
