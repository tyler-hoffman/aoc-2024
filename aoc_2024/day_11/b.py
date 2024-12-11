from dataclasses import dataclass, field
from functools import cache, cached_property
from aoc_2024.day_11.parser import Parser


@dataclass(frozen=True)
class Day11PartBSolver:
    input: list[int] = field(hash=False)

    @property
    def solution(self) -> int:
        output = 0
        for stone in self.input:
            output += self.compute(stone, iterations=75)
        return output

    @cache
    def compute(self, stone: int, iterations: int) -> int:
        as_str = str(stone)
        if iterations == 0:
            return 1
        elif stone == 0:
            return self.compute(1, iterations - 1)
        elif len(as_str) % 2 == 0:
            half = len(as_str) // 2
            return sum(
                [
                    self.compute(int(as_str[:half]), iterations - 1),
                    self.compute(int(as_str[half:]), iterations - 1),
                ]
            )
        else:
            return self.compute(stone * 2024, iterations - 1)

    def next_state(self, stone: int) -> list[int]:
        as_str = str(stone)
        if stone == 0:
            return [1]
        elif len(as_str) % 2 == 0:
            half = len(as_str) // 2
            return [int(as_str[:half]), int(as_str[half:])]
        else:
            return [stone * 2024]

    @cached_property
    def computed(self) -> dict[int, list[list[int]]]:
        return {}


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day11PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_11/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
