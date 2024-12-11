from dataclasses import dataclass
from aoc_2024.day_11.parser import Parser


@dataclass
class Day11PartASolver:
    input: list[int]

    @property
    def solution(self) -> int:
        stones = self.input
        for _ in range(25):
            stones = self.next_state(stones)
        return len(stones)

    def next_state(self, stones: list[int]) -> list[int]:
        output: list[int] = []
        for stone in stones:
            as_str = str(stone)
            if stone == 0:
                output += [1]
            elif len(as_str) % 2 == 0:
                half = len(as_str) // 2
                output += [int(as_str[:half]), int(as_str[half:])]
            else:
                output += [stone * 2024]
        return output


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day11PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_11/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
