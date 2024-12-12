from dataclasses import dataclass
from functools import cached_property
from aoc_2024.day_12.parser import Parser
from aoc_2024.utils.point import Point


@dataclass
class Day12PartASolver:
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
        return self.area(region) * self.perimeter(region)

    def area(self, region: set[Point]) -> int:
        return len(region)

    def perimeter(self, region: set[Point]) -> int:
        output = 0
        for p in region:
            for n in p.neighbors:
                if self.map_as_dict.get(n) != self.map_as_dict[p]:
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
    solver = Day12PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_12/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
