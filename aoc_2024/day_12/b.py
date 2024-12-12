from dataclasses import dataclass
from functools import cached_property
from aoc_2024.day_12.parser import Parser
from aoc_2024.utils.point import Point


@dataclass
class Day12PartBSolver:
    map: list[list[str]]

    @property
    def solution(self) -> int:
        return sum([self.cost(region) for region in self.regions])

    @cached_property
    def regions(self) -> list[set[Point]]:
        seen: set[Point] = set()
        output: list[set[Point]] = []
        for p in self.map_as_dict:
            if p not in seen:
                new_region = self.get_region_for_point(p)
                seen |= new_region
                output.append(new_region)
        return output

    def cost(self, region: set[Point]) -> int:
        return self.area(region) * self.sides(region)

    def area(self, region: set[Point]) -> int:
        return len(region)

    def sides(self, region: set[Point]) -> int:
        y_with_left_sides_by_x: dict[int, set[int]] = {}
        y_with_right_sides_by_x: dict[int, set[int]] = {}
        x_with_top_sides_by_y: dict[int, set[int]] = {}
        x_with_bottom_sides_by_y: dict[int, set[int]] = {}

        for p in region:
            label = self.map_as_dict[p]
            if self.map_as_dict.get(p.add(Point(-1, 0))) != label:
                if p.x not in y_with_left_sides_by_x:
                    y_with_left_sides_by_x[p.x] = set()
                y_with_left_sides_by_x[p.x].add(p.y)
            if self.map_as_dict.get(p.add(Point(1, 0))) != label:
                if p.x not in y_with_right_sides_by_x:
                    y_with_right_sides_by_x[p.x] = set()
                y_with_right_sides_by_x[p.x].add(p.y)
            if self.map_as_dict.get(p.add(Point(0, -1))) != label:
                if p.y not in x_with_top_sides_by_y:
                    x_with_top_sides_by_y[p.y] = set()
                x_with_top_sides_by_y[p.y].add(p.x)
            if self.map_as_dict.get(p.add(Point(0, 1))) != label:
                if p.y not in x_with_bottom_sides_by_y:
                    x_with_bottom_sides_by_y[p.y] = set()
                x_with_bottom_sides_by_y[p.y].add(p.x)

        output = 0
        for collection in [
            y_with_left_sides_by_x,
            y_with_right_sides_by_x,
            x_with_bottom_sides_by_y,
            x_with_top_sides_by_y,
        ]:
            for values in collection.values():
                output += self.get_contiguous_lines(values)
        return output

    def get_contiguous_lines(self, values: set[int]) -> int:
        sorted_values = sorted(values)
        output = 1
        for i, value in enumerate(sorted_values[1:]):
            if value > sorted_values[i] + 1:
                output += 1
        return output

    def get_region_for_point(self, start: Point) -> set[Point]:
        label = self.map_as_dict[start]
        output = {start}
        to_expand = [start]
        while to_expand:
            p = to_expand.pop()
            for n in p.neighbors:
                if self.map_as_dict.get(n) == label and n not in output:
                    output.add(n)
                    to_expand.append(n)
        return output

    @cached_property
    def map_as_dict(self) -> dict[Point, str]:
        output: dict[Point, str] = {}
        for y, line in enumerate(self.map):
            for x, ch in enumerate(line):
                output[Point(x, y)] = ch
        return output


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day12PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_12/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
