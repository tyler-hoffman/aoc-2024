from dataclasses import dataclass
from functools import cached_property
from aoc_2024.day_06.parser import Parser
from aoc_2024.utils.point import Point

DIRECTIONS = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]


@dataclass
class Day06PartASolver:
    grid: list[list[str]]

    @property
    def solution(self) -> int:
        visited = set[Point]()
        direction_index = 0
        pos = self.start
        while pos.x >= 0 and pos.y >= 0 and pos.x < self.width and pos.y < self.height:
            visited.add(pos)
            next_pos = pos.add(DIRECTIONS[direction_index])
            if next_pos in self.obstacles:
                direction_index = (direction_index + 1) % 4
            else:
                pos = next_pos
        return len(visited)

    @cached_property
    def width(self) -> int:
        return len(self.grid[0])

    @cached_property
    def height(self) -> int:
        return len(self.grid)

    @cached_property
    def obstacles(self) -> set[Point]:
        output = set[Point]()
        for y, line in enumerate(self.grid):
            for x, char in enumerate(line):
                if char == "#":
                    output.add(Point(x, y))
        return output

    @cached_property
    def start(self) -> Point:
        for y, line in enumerate(self.grid):
            for x, char in enumerate(line):
                if char == "^":
                    return Point(x, y)
        assert False, "How'd we get here?"


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day06PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_06/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
