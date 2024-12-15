from dataclasses import dataclass
from functools import cached_property
from aoc_2024.day_15.parser import Parser
from aoc_2024.utils.point import Point


@dataclass
class Day15PartASolver:
    grid: list[list[str]]
    instructions: list[str]

    @property
    def solution(self) -> int:
        # move
        p = self.get_robot()
        for direction in self.directions:
            moved = self.shift(p, direction)
            if moved:
                p = p.add(direction)
            assert self.points[p] == "@"
        # get points:
        boxes = {p for p, ch in self.points.items() if ch == "O"}
        return sum([self.gps_score(box) for box in boxes])

    def shift(self, p: Point, direction: Point) -> bool:
        if self.points[p] == "#":
            return False
        elif self.points[p] == ".":
            return True
        else:
            next = p.add(direction)
            move = self.shift(p=next, direction=direction)
            if move:
                self.points[next] = self.points[p]
                self.points[p] = "."
            return move

    @cached_property
    def directions(self) -> list[Point]:
        return [self.instruction_to_direction(inst) for inst in self.instructions]

    def instruction_to_direction(self, instruction: str) -> Point:
        match instruction:
            case "<":
                return Point(-1, 0)
            case ">":
                return Point(1, 0)
            case "^":
                return Point(0, -1)
            case "v":
                return Point(0, 1)
            case _:
                assert False

    def gps_score(self, p: Point) -> int:
        return p.x + 100 * p.y

    def get_robot(self) -> Point:
        for point, value in self.points.items():
            if value == "@":
                return point
        assert False, "better not get here lol"

    @cached_property
    def points(self) -> dict[Point, str]:
        output: dict[Point, str] = {}
        for y, line in enumerate(self.grid):
            for x, ch in enumerate(line):
                output[Point(x, y)] = ch
        return output


def solve(input: str) -> int:
    grid, instructions = Parser.parse(input)
    solver = Day15PartASolver(
        grid=grid,
        instructions=instructions,
    )

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_15/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
