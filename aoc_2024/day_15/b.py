from dataclasses import dataclass
from functools import cached_property
from aoc_2024.day_15.parser import Parser
from aoc_2024.utils.point import Point

UP = Point(0, -1)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)


@dataclass
class Day15PartBSolver:
    grid: list[list[str]]
    instructions: list[str]

    @property
    def solution(self) -> int:
        # move
        p = self.get_robot()
        for direction in self.directions:
            can_shift = self.can_shift(p, direction)
            if can_shift:
                self.shift(p, direction)
                p = p.add(direction)
            assert self.points[p] == "@"

        # get points:
        boxes = {p for p, ch in self.points.items() if ch == "["}
        return sum([self.gps_score(box) for box in boxes])

    def can_shift(self, p: Point, direction: Point) -> bool:
        char = self.points[p]
        if char == "#":
            return False
        elif char == ".":
            return True
        elif direction in {LEFT, RIGHT} or char == "@":
            next = p.add(direction)
            return self.can_shift(p=next, direction=direction)
        else:
            assert direction in {UP, DOWN}
            next = p.add(direction)
            if self.points[p] == "[":
                move_left = self.can_shift(p=next, direction=direction)
                move_right = self.can_shift(p=next.add(RIGHT), direction=direction)
                return move_left and move_right
            elif self.points[p] == "]":
                move_left = self.can_shift(p=next.add(LEFT), direction=direction)
                move_right = self.can_shift(p=next, direction=direction)
                return move_left and move_right
            else:
                assert False, "invalid?"

    def shift(self, p: Point, direction: Point) -> None:
        char = self.points[p]
        if char in "[@]":
            if direction in {LEFT, RIGHT} or char not in "[]":
                next = p.add(direction)
                self.shift(next, direction)
                self.points[next] = self.points[p]
                self.points[p] = "."
            else:
                if char == "[":
                    left = p
                    right = p.add(RIGHT)
                elif char == "]":
                    left = p.add(LEFT)
                    right = p
                next_left = left.add(direction)
                next_right = right.add(direction)

                self.shift(next_left, direction)
                self.shift(next_right, direction)

                self.points[next_left] = self.points[left]
                self.points[next_right] = self.points[right]
                self.points[left] = "."
                self.points[right] = "."

    @cached_property
    def directions(self) -> list[Point]:
        return [self.instruction_to_direction(inst) for inst in self.instructions]

    def instruction_to_direction(self, instruction: str) -> Point:
        return {
            "<": LEFT,
            ">": RIGHT,
            "^": UP,
            "v": DOWN,
        }[instruction]

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
                left = Point(x * 2, y)
                right = left.add(RIGHT)
                match ch:
                    case "#":
                        output[left] = "#"
                        output[right] = "#"
                    case ".":
                        output[left] = "."
                        output[right] = "."
                    case "O":
                        output[left] = "["
                        output[right] = "]"
                    case "@":
                        output[left] = "@"
                        output[right] = "."
        return output


def solve(input: str) -> int:
    grid, instructions = Parser.parse(input)
    solver = Day15PartBSolver(
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
