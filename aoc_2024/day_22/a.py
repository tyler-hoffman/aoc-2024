from dataclasses import dataclass
from aoc_2024.day_22.parser import Parser


@dataclass
class Day22PartASolver:
    initial_values: list[int]
    iterations: int = 2000

    @property
    def solution(self) -> int:
        return sum([self.get_final_value(x) for x in self.initial_values])

    def get_final_value(self, value: int) -> int:
        for _ in range(self.iterations):
            value = ((value * 64) ^ value) % 16777216
            value = ((value // 32) ^ value) % 16777216
            value = ((value * 2048) ^ value) % 16777216
        return value


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day22PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_22/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
