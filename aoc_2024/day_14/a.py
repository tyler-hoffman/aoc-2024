from dataclasses import dataclass
from functools import cached_property
from aoc_2024.day_14.parser import Parser
from aoc_2024.utils.point import Point


@dataclass
class Day14PartASolver:
    robots: list[tuple[Point, Point]]
    width: int
    height: int
    seconds: int = 100

    @property
    def solution(self) -> int:
        mid_x = self.width // 2
        mid_y = self.height // 2

        top_left = [p for p in self.end_positions if p.x < mid_x and p.y < mid_y]
        top_right = [p for p in self.end_positions if p.x > mid_x and p.y < mid_y]
        bottom_left = [p for p in self.end_positions if p.x < mid_x and p.y > mid_y]
        bottom_right = [p for p in self.end_positions if p.x > mid_x and p.y > mid_y]

        return len(top_left) * len(top_right) * len(bottom_left) * len(bottom_right)

    @cached_property
    def end_positions(self) -> list[Point]:
        return [self.get_end_position(p, v, self.seconds) for p, v in self.robots]

    def get_end_position(self, p: Point, v: Point, s: int) -> Point:
        end = p.add(v.multiply(s))
        return Point(end.x % self.width, end.y % self.height)


def solve(input: str, width: int = 101, height: int = 103) -> int:
    data = Parser.parse(input)
    solver = Day14PartASolver(robots=data, width=width, height=height)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_14/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
