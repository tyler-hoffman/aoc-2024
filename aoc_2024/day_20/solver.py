from dataclasses import dataclass
from functools import cached_property
from queue import PriorityQueue
from typing import Iterator
from aoc_2024.utils.point import Point


@dataclass
class Day20Solver:
    grid: list[list[str]]
    min_seconds_to_save: int
    max_cheat: int

    @property
    def solution(self) -> int:
        return len([c for c in self.cheats if c >= self.min_seconds_to_save])

    @cached_property
    def cheats(self) -> Iterator[int]:
        for p, p_dist in self.dists_to_end.items():
            for offset in self.offsets:
                n = p.add(offset)
                travelled = n.dist(p)
                if travelled <= self.max_cheat and n in self.non_walls:
                    n_dist = self.dists_to_end[n]
                    yield p_dist - n_dist - travelled

    def second_neighbors(self, p: Point) -> Iterator[Point]:
        for a in p.neighbors:
            for b in a.neighbors:
                yield b

    @cached_property
    def offsets(self) -> set[Point]:
        center = Point(0, 0)
        output = set[Point]()
        for y in range(-self.max_cheat, self.max_cheat + 1):
            for x in range(-self.max_cheat, self.max_cheat + 1):
                n = Point(x, y)
                travelled = n.dist(center)
                if travelled <= self.max_cheat:
                    output.add(n)
        return output

    @cached_property
    def dists_to_end(self) -> dict[Point, int]:
        output: dict[Point, int] = {}
        visited = set[Point]()
        queue = PriorityQueue[tuple[int, Point]]()

        queue.put((0, self.end))
        while not queue.empty():
            dist, p = queue.get()
            if p in visited:
                continue
            output[p] = dist
            visited.add(p)

            for n in p.neighbors:
                if n not in visited and n in self.non_walls:
                    queue.put((dist + 1, n))
        return output

    def in_bounds(self, p: Point) -> bool:
        return 0 <= p.x < self.width and 0 <= p.y < self.height

    @cached_property
    def non_walls(self) -> set[Point]:
        output = set[Point]()
        for y, line in enumerate(self.grid):
            for x, ch in enumerate(line):
                if ch != "#":
                    output.add(Point(x, y))

        return output

    @cached_property
    def start(self) -> Point:
        for y, line in enumerate(self.grid):
            for x, ch in enumerate(line):
                if ch == "S":
                    return Point(x, y)
        assert False

    @cached_property
    def end(self) -> Point:
        for y, line in enumerate(self.grid):
            for x, ch in enumerate(line):
                if ch == "E":
                    return Point(x, y)
        assert False

    @cached_property
    def width(self) -> int:
        return len(self.grid[0])

    @cached_property
    def height(self) -> int:
        return len(self.grid)
