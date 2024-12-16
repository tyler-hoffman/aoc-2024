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
class Day16PartBSolver:
    maze: list[list[str]]

    @property
    def solution(self) -> int:
        queue = PriorityQueue[tuple[int, Point, int, tuple[Point, ...]]]()
        queue.put((0, self.start, 0, tuple()))
        best_score: None | int = None
        in_best_path = {self.start, self.end}
        best_score_to_state: dict[tuple[Point, int], int] = {}

        while not queue.empty():
            score, pos, direction_index, path = queue.get()
            if best_score is not None and score > best_score:
                break

            key = (pos, direction_index)
            if key in best_score_to_state:
                if score > best_score_to_state[key]:
                    continue
            else:
                best_score_to_state[key] = score

            if pos == self.end:
                best_score = score
                for p in path:
                    in_best_path.add(p)

            for next_state in self.get_next_states(
                score=score,
                pos=pos,
                direction_index=direction_index,
            ):
                next_score, next_pos, next_direction_index = next_state
                new_key = (next_pos, next_direction_index)
                if (
                    new_key not in best_score_to_state
                    or next_score <= best_score_to_state[new_key]
                ):
                    queue.put(
                        (next_score, next_pos, next_direction_index, path + (pos,))
                    )

        return len(in_best_path)

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
    solver = Day16PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_16/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
