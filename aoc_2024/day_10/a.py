from dataclasses import dataclass, field
from functools import cache, cached_property
from aoc_2024.day_10.parser import Parser
from aoc_2024.utils.point import Point


@dataclass(frozen=True)
class Day10PartASolver:
    grid: list[list[int]] = field(hash=False)

    @property
    def solution(self) -> int:
        output = 0
        for trailhead in self.trailheads:
            output += len(self.tops_of_trail(trailhead))
        return output

    @cached_property
    def width(self) -> int:
        return len(self.grid[0])

    @cached_property
    def height(self) -> int:
        return len(self.grid)

    @cached_property
    def trailheads(self) -> set[Point]:
        output = set[Point]()
        for y, line in enumerate(self.grid):
            for x, digit in enumerate(line):
                if digit == 0:
                    output.add(Point(x, y))
        return output

    @cache
    def tops_of_trail(self, point: Point) -> set[Point]:
        value = self.grid[point.y][point.x]
        if value == 9:
            return {point}

        else:
            output = set[Point]()
            for neighbor in self.neighbors(point):
                new_value = self.grid[neighbor.y][neighbor.x]
                if new_value == value + 1:
                    output |= self.tops_of_trail(neighbor)
            return output

    def neighbors(self, point: Point) -> set[Point]:
        return {
            n
            for n in point.neighbors
            if 0 <= n.x < self.width and 0 <= n.y < self.height
        }


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day10PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_10/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())