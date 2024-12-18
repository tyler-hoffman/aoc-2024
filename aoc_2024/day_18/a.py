from dataclasses import dataclass
from functools import cached_property
from queue import PriorityQueue
from aoc_2024.day_18.parser import Parser
from aoc_2024.utils.point import Point


@dataclass
class Day18PartASolver:
    byte_positions: list[Point]
    grid_size: int
    bytes_fallen: int

    @property
    def solution(self) -> int:
        seen: set[Point] = set()
        queue = PriorityQueue[tuple[int, int, Point]]()
        queue.put((0, self.start.dist(self.end), self.start))
        while not queue.empty():
            steps, _, pos = queue.get()

            # success
            if pos == self.end:
                return steps

            elif pos not in seen:
                seen.add(pos)
                for n in pos.neighbors:
                    if all(
                        [
                            self.in_bounds(n),
                            n not in seen,
                            n not in self.corrupted_bytes,
                        ]
                    ):
                        queue.put((steps + 1, n.dist(self.end), n))

        assert False, "don't get here plz"

    def in_bounds(self, point: Point) -> bool:
        return 0 <= point.x < self.grid_size and 0 <= point.y < self.grid_size

    @cached_property
    def start(self) -> Point:
        return Point(0, 0)

    @cached_property
    def end(self) -> Point:
        return Point(self.grid_size - 1, self.grid_size - 1)

    @cached_property
    def corrupted_bytes(self) -> set[Point]:
        return set(self.byte_positions[: self.bytes_fallen])


def solve(input: str, grid_size: int = 71, bytes_fallen: int = 1024) -> int:
    data = Parser.parse(input)
    solver = Day18PartASolver(
        data,
        grid_size=grid_size,
        bytes_fallen=bytes_fallen,
    )

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_18/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())