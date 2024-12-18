from dataclasses import dataclass
from aoc_2024.day_18.parser import Parser
from aoc_2024.day_18.solver import Solver
from aoc_2024.utils.point import Point


@dataclass
class Day18PartASolver:
    byte_positions: list[Point]
    grid_size: int

    @property
    def solution(self) -> str:
        left = 0
        right = len(self.byte_positions)
        while left < right:
            mid = (left + right) // 2
            solver = Solver(
                byte_positions=self.byte_positions,
                grid_size=self.grid_size,
                bytes_fallen=mid,
            )
            if solver.min_steps is not None:
                left = mid + 1
            else:
                right = mid
        p = self.byte_positions[left - 1]
        return f"{p.x},{p .y}"


def solve(input: str, grid_size: int = 71, bytes_fallen: int = 1024) -> str:
    data = Parser.parse(input)
    solver = Day18PartASolver(
        data,
        grid_size=grid_size,
    )

    return solver.solution


def get_solution() -> str:
    with open("aoc_2024/day_18/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
