from dataclasses import dataclass
from functools import cached_property
from queue import PriorityQueue
from typing import Generator
from aoc_2024.day_16.parser import Parser
from aoc_2024.utils.point import Point


DIRECTIONS = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
]

MOVE_COST = 1
ROTATE_COST = 1000


@dataclass
class Day16PartASolver:
    maze: list[list[str]]

    @property
    def solution(self) -> int:
        visited = set[tuple[Point, int]]()
        queue = PriorityQueue[tuple[int, Point, int]]()
        queue.put((0, self.start, 0))

        while not queue.empty():
            score, pos, direction_index = queue.get()
            if (pos, direction_index) in visited:
                continue

            if pos == self.end:
                return score

            visited.add((pos, direction_index))
            for next_state in self.get_next_states(
                score=score,
                pos=pos,
                direction_index=direction_index,
            ):
                _, next_pos, next_direction_index = next_state
                if (next_pos, next_direction_index) not in visited:
                    queue.put(next_state)
        assert False, "uh oh"

    def get_next_states(
        self,
        score: int,
        pos: Point,
        direction_index: int,
    ) -> Generator[tuple[int, Point, int]]:
        move_forward = pos.add(DIRECTIONS[direction_index])
        if self.maze[move_forward.y][move_forward.x] != "#":
            yield score + MOVE_COST, move_forward, direction_index
        yield score + ROTATE_COST, pos, (direction_index - 1) % 4
        yield score + ROTATE_COST, pos, (direction_index + 1) % 4

    @cached_property
    def start(self) -> Point:
        x = 1
        y = len(self.maze) - 2
        assert self.maze[y][x] == "S"
        return Point(x, y)

    @cached_property
    def end(self) -> Point:
        x = len(self.maze[0]) - 2
        y = 1
        assert self.maze[y][x] == "E"
        return Point(x, y)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day16PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_16/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
