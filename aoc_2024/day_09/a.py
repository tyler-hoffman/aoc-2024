from dataclasses import dataclass
from typing import Optional
from aoc_2024.day_09.parser import Parser


@dataclass
class Day09PartASolver:
    input: list[int]

    @property
    def solution(self) -> int:
        disk = self.create_disk_list(self.input)
        self.defrag(disk)
        return self.checksum(disk)

    def checksum(self, disk: list[Optional[int]]) -> int:
        output = 0
        for i, val in enumerate(disk):
            if val:
                output += i * val
        return output

    def defrag(self, disk: list[Optional[int]]) -> None:
        blank_indexes = [i for i, val in enumerate(disk) if val is None][::-1]
        val_indexes = [i for i, val in enumerate(disk) if val is not None]

        while val_indexes and blank_indexes and val_indexes[-1] > blank_indexes[-1]:
            val_index = val_indexes.pop()
            blank_index = blank_indexes.pop()
            disk[blank_index], disk[val_index] = disk[val_index], disk[blank_index]

    def create_disk_list(self, inputs: list[int]) -> list[Optional[int]]:
        output: list[Optional[int]] = []
        current_id = 0
        file_mode = True
        for x in inputs:
            if file_mode:
                output += [current_id] * x
                current_id += 1
            else:
                output += [None] * x
            file_mode = not file_mode
        return output


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day09PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_09/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
