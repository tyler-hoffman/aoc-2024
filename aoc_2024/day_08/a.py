import itertools
from dataclasses import dataclass
from functools import cached_property
from aoc_2024.day_08.parser import Parser
from aoc_2024.utils.point import Point


@dataclass
class Day08PartASolver:
    grid: list[list[str]]

    @property
    def solution(self) -> int:
        in_bounds = [
            antinode
            for antinode in self.antinodes
            if 0 <= antinode.x < self.width and 0 <= antinode.y < self.height
        ]
        return len(in_bounds)

    @cached_property
    def width(self) -> int:
        return len(self.grid[0])

    @cached_property
    def height(self) -> int:
        return len(self.grid)

    @cached_property
    def antinodes(self) -> set[Point]:
        output = set[Point]()
        for _, antennas in self.antennas.items():
            antenna_list = list(antennas)
            for a, b in itertools.product(antenna_list, antenna_list):
                if a != b:
                    x_diff = b.x - a.x
                    y_diff = b.y - a.y
                    output.add(Point(a.x - x_diff, a.y - y_diff))

        return output

    @cached_property
    def antennas(self) -> dict[str, set[Point]]:
        output = dict[str, set[Point]]()
        for y, line in enumerate(self.grid):
            for x, ch in enumerate(line):
                if ch != ".":
                    point = Point(x, y)
                    if ch not in output:
                        output[ch] = set()
                    output[ch].add(point)
        return output


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day08PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_08/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())