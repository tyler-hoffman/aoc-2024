from dataclasses import dataclass
from functools import cached_property
from typing import Mapping
from aoc_2024.day_05.parser import Parser


@dataclass
class Day05PartASolver:
    ordering_rules: list[tuple[int, int]]
    updates: list[list[int]]

    @property
    def solution(self) -> int:
        output = 0
        for update in self._valid_updates:
            output += self._get_middle(update)
        return output

    @cached_property
    def _valid_updates(self) -> list[list[int]]:
        return [update for update in self.updates if self._is_valid(update)]

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


def solve(input: str) -> int:
    ordering_rules, updates = Parser.parse(input)
    solver = Day05PartASolver(ordering_rules=ordering_rules, updates=updates)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_05/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
