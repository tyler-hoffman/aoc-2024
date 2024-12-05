from dataclasses import dataclass
from functools import cached_property
import functools
from typing import Mapping
from aoc_2024.day_05.parser import Parser


@dataclass
class Day05PartBSolver:
    ordering_rules: list[tuple[int, int]]
    updates: list[list[int]]

    @property
    def solution(self) -> int:
        output = 0
        for update in self._invalid_updates:
            sorted_update = self._sort(update)
            output += self._get_middle(sorted_update)
        return output

    @cached_property
    def _invalid_updates(self) -> list[list[int]]:
        return [update for update in self.updates if not self._is_valid(update)]

    @cached_property
    def _prereqs(self) -> Mapping[int, set[int]]:
        output: dict[int, set[int]] = {}
        for a, b in self.ordering_rules:
            if b not in output:
                output[b] = set()
            output[b].add(a)
        return output

    def _get_middle(self, update: list[int]) -> int:
        mid = len(update) // 2
        return update[mid]

    def _is_valid(self, update: list[int]) -> bool:
        for index, a in enumerate(update):
            for b in update[index + 1 :]:
                if a in self._prereqs and b in self._prereqs[a]:
                    return False
        return True

    def _sort(self, update: list[int]) -> list[int]:
        return sorted(update, key=functools.cmp_to_key(self._compare))

    def _compare(self, a: int, b: int) -> int:
        if a in self._prereqs and b in self._prereqs[a]:
            return -1
        else:
            return 1


def solve(input: str) -> int:
    ordering_rules, updates = Parser.parse(input)
    solver = Day05PartBSolver(ordering_rules=ordering_rules, updates=updates)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_05/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
