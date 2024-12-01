from dataclasses import dataclass
from functools import cached_property
from typing import Mapping, Sequence
from aoc_2024.day_01.parser import Parser
from aoc_2024.utils.freq_map import freq_map


@dataclass
class Day01PartBSolver:
    input: Sequence[tuple[int, int]]

    @property
    def solution(self) -> int:
        output = 0
        for val, count in self.left_nums.items():
            if val in self.right_nums:
                output += val * count * self.right_nums[val]
        return output

    @cached_property
    def left_nums(self) -> Mapping[int, int]:
        return freq_map([a for a, _ in self.input])

    @cached_property
    def right_nums(self) -> Mapping[int, int]:
        return freq_map([b for _, b in self.input])


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day01PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_01/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
