from dataclasses import dataclass
from typing import Sequence
from aoc_2024.day_02.parser import Parser


@dataclass
class Day02PartBSolver:
    data: Sequence[Sequence[int]]

    @property
    def solution(self) -> int:
        safe_reports = [report for report in self.data if self._is_safe(report)]
        return len(safe_reports)

    def _is_safe(self, report: Sequence[int]) -> bool:
        if self._is_ascending(report) or self._is_descending(report):
            return True
        else:
            for i in range(len(report)):
                modified_report = [*report[:i], *report[i + 1 :]]
                if self._is_ascending(modified_report) or self._is_descending(
                    modified_report
                ):
                    return True
            return False

    def _is_ascending(self, report: Sequence[int]) -> bool:
        prev = report[0]
        for val in report[1:]:
            if val < prev + 1 or val > prev + 3:
                return False
            else:
                prev = val
        return True

    def _is_descending(self, report: Sequence[int]) -> bool:
        prev = report[0]
        for val in report[1:]:
            if val < prev - 3 or val > prev - 1:
                return False
            else:
                prev = val
        return True


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day02PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
