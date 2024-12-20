from dataclasses import dataclass
from functools import cached_property
from aoc_2024.day_20.parser import Parser
from aoc_2024.day_20.solver import Day20Solver


@dataclass
class Day20PartBSolver:
    grid: list[list[str]]
    min_seconds_to_save: int

    @property
    def solution(self) -> int:
        return self.solver.solution

    @cached_property
    def solver(self) -> Day20Solver:
        return Day20Solver(
            grid=self.grid,
            min_seconds_to_save=self.min_seconds_to_save,
            max_cheat=20,
        )


def solve(input: str, min_seconds_to_save: int = 100) -> int:
    data = Parser.parse(input)
    solver = Day20PartBSolver(data, min_seconds_to_save=min_seconds_to_save)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_20/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
