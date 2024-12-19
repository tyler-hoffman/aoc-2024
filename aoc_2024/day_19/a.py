from dataclasses import dataclass, field
from functools import cache, cached_property
from aoc_2024.day_19.parser import Parser


@dataclass(frozen=True)
class Day19PartASolver:
    available_towels: list[str] = field(hash=False)
    desired_patterns: list[str] = field(hash=False)

    @property
    def solution(self) -> int:
        return len(self.possible_patterns)

    @cached_property
    def possible_patterns(self) -> list[str]:
        return [p for p in self.desired_patterns if self.is_possible(tuple(p))]

    @cache
    def is_possible(
        self, pattern: tuple[str, ...], so_far: tuple[str, ...] = tuple()
    ) -> bool:
        if so_far == pattern:
            return True
        elif len(so_far) >= len(pattern):
            return False
        elif pattern[: len(so_far)] == so_far:
            for towel in self.available_towel_patterns:
                if self.is_possible(pattern, so_far + tuple(towel)):
                    return True
            return False
        else:
            return False

    @cached_property
    def available_towel_patterns(self) -> list[tuple[str, ...]]:
        return [tuple(t) for t in self.available_towels]


def solve(input: str) -> int:
    available_towels, desired_patterns = Parser.parse(input)
    solver = Day19PartASolver(
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
