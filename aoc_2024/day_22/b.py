from dataclasses import dataclass
from functools import cached_property
from aoc_2024.day_22.parser import Parser


@dataclass
class Day22PartBSolver:
    initial_values: list[int]
    iterations: int = 2000

    @property
    def solution(self) -> int:
        counts = set[int]()
        for change_set in self.all_change_sets:
            count = 0
            for cn in self.first_changes_and_nanners:
                count += cn.get(change_set, 0)
            counts.add(count)
        return max(counts)

    @cached_property
    def all_change_sets(self) -> set[tuple[int, ...]]:
        output = set[tuple[int, ...]]()
        for cn in self.first_changes_and_nanners:
            for changes, _ in cn.items():
                output.add(changes)
        return output

    @cached_property
    def first_changes_and_nanners(self) -> list[dict[tuple[int, ...], int]]:
        return [
            self.get_first_changes_and_nanners(cn) for cn in self.changes_and_nanners
        ]

    def get_first_changes_and_nanners(
        self, changes_and_nanners: list[tuple[tuple[int, ...], int]]
    ) -> dict[tuple[int, ...], int]:
        output: dict[tuple[int, ...], int] = {}
        for changes, nanners in changes_and_nanners:
            if changes not in output:
                output[changes] = nanners
        return output

    @cached_property
    def changes_and_nanners(self) -> list[list[tuple[tuple[int, ...], int]]]:
        return [self.get_changes_and_nanners(seq) for seq in self.value_sequences]

    def get_changes_and_nanners(
        self, value_sequence: list[int]
    ) -> list[tuple[tuple[int, ...], int]]:
        output: list[tuple[tuple[int, ...], int]] = []
        for i in range(4, self.iterations):
            changes = tuple(
                (value_sequence[i - j] % 10) - (value_sequence[i - j - 1]) % 10
                for j in (3, 2, 1, 0)
            )
            nanners = value_sequence[i] % 10
            output.append((changes, nanners))
        return output

    @cached_property
    def value_sequences(self) -> list[list[int]]:
        return [self.get_value_sequence(value) for value in self.initial_values]

    def get_value_sequence(self, value: int) -> list[int]:
        output = [value]
        for _ in range(self.iterations):
            value = ((value * 64) ^ value) % 16777216
            value = ((value // 32) ^ value) % 16777216
            value = ((value * 2048) ^ value) % 16777216
            output.append(value)
        return output


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day22PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_22/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
