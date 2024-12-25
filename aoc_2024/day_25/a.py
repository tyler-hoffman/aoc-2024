from dataclasses import dataclass
from functools import cached_property
from aoc_2024.day_25.parser import Parser


@dataclass
class Day25PartASolver:
    input: list[list[list[str]]]

    @property
    def solution(self) -> int:
        output = 0
        for key in self.keys:
            for lock in self.locks:
                if all(key[i] + lock[i] <= 5 for i in range(5)):
                    output += 1
        return output

    @cached_property
    def keys(self) -> list[list[int]]:
        to_use = [x for x in self.input if x[0] == ["."] * 5]
        return [self.count_hashes(x) for x in to_use]

    @cached_property
    def locks(self) -> list[list[int]]:
        to_use = [x for x in self.input if x[0] == ["#"] * 5]
        return [self.count_hashes(x) for x in to_use]

    def count_hashes(self, thing: list[list[str]]) -> list[int]:
        output: list[int] = []
        for x in range(5):
            output.append(len([1 for y in range(7) if thing[y][x] == "#"]) - 1)
        return output


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day25PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_25/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
