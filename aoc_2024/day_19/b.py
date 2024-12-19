from dataclasses import dataclass, field
from functools import cache, cached_property
from aoc_2024.day_19.parser import Parser


@dataclass(frozen=True)
class Day19PartBSolver:
    available_towels: list[str] = field(hash=False)
    desired_patterns: list[str] = field(hash=False)

    @property
    def solution(self) -> int:
        return sum(self.possibilities(tuple(p)) for p in self.desired_patterns)

    @cache
    def possibilities(
        self, pattern: tuple[str, ...], so_far: tuple[str, ...] = tuple()
    ) -> int:
        if so_far == pattern:
            return 1
        elif len(so_far) >= len(pattern):
            return 0
        elif pattern[: len(so_far)] == so_far:
            return sum(
                self.possibilities(pattern=pattern, so_far=so_far + t)
                for t in self.available_towel_patterns
            )
        else:
            return 0

    @cached_property
    def available_towel_patterns(self) -> list[tuple[str, ...]]:
        return [tuple(t) for t in self.available_towels]


def solve(input: str) -> int:
    available_towels, desired_patterns = Parser.parse(input)
    solver = Day19PartBSolver(
        available_towels=available_towels,
        desired_patterns=desired_patterns,
    )

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_19/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
