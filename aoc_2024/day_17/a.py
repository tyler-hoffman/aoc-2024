from dataclasses import dataclass
from aoc_2024.day_17.machine import Machine
from aoc_2024.day_17.parser import Parser


@dataclass
class Day17PartASolver:
    registers: dict[str, int]
    instructions: list[int]

    @property
    def solution(self) -> str:
        machine = Machine(
            registers=self.registers,
            instructions=self.instructions,
        )
        return machine.get_output()


def solve(input: str) -> str:
    initial_registers, instructions = Parser.parse(input)
    solver = Day17PartASolver(
        registers=initial_registers,
        instructions=instructions,
    )

    return solver.solution


def get_solution() -> str:
    with open("aoc_2024/day_17/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
