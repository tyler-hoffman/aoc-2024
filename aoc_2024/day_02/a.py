from dataclasses import dataclass
import itertools
from typing import Sequence
from aoc_2024.day_02.parser import Parser


@dataclass
class Day02PartASolver:
    data: Sequence[Sequence[int]]

    @property
    def solution(self) -> int:
        safe_reports = [report for report in self.data if self._is_safe(report)]
        return len(safe_reports)

    def _is_safe(self, report: Sequence[int]) -> bool:
        return self._is_ascending(report) or self._is_descending(report)

    def _is_ascending(self, report: Sequence[int]) -> bool:
        pairs = itertools.pairwise(report)
        return all(1 <= b - a <= 3 for a, b in pairs)

    def _is_descending(self, report: Sequence[int]) -> bool:
        pairs = itertools.pairwise(report)
        return all(1 <= a - b <= 3 for a, b in pairs)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day02PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
