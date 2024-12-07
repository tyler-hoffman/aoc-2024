from dataclasses import dataclass
from typing import Generator
from aoc_2024.day_07.parser import Parser


@dataclass
class Day07PartASolver:
    equations: list[tuple[int, list[int]]]

    @property
    def solution(self) -> int:
        output = 0
        for answer, nums in self.equations:
            if self.can_be_true(answer, nums):
                output += answer
        return output

    def can_be_true(self, answer: int, nums: list[int]) -> bool:
        return True in self.has_solution(answer, nums, nums[0], 1)

    def has_solution(
        self,
        answer: int,
        nums: list[int],
        so_far: int,
        index: int,
    ) -> Generator[bool, None, None]:
        if so_far > answer:
            yield False
        elif index == len(nums):
            yield so_far == answer
        else:
            yield from self.has_solution(answer, nums, so_far + nums[index], index + 1)
            yield from self.has_solution(answer, nums, so_far * nums[index], index + 1)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day07PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_07/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
