from dataclasses import dataclass
from typing import Iterator
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


@dataclass
class Machine:
    registers: dict[str, int]
    instructions: list[int]
    instruction_pointer: int = 0

    def get_output(self) -> str:
        return ",".join(str(x) for x in self.run())

    def run(self) -> Iterator[int]:
        while True:
            try:
                yield from self.next_run()
            except IndexError:
                break

    def next_run(self) -> Iterator[int]:
        r = self.registers
        if self.instruction_pointer % 2:
            assert False, "hm"
        match self.opcode:
            case 0:
                r["A"] = r["A"] // 2 ** self.combo(self.operand)
            case 1:
                r["B"] = r["B"] ^ self.operand
            case 2:
                r["B"] = self.combo(self.operand) % 8
            case 3:
                if r["A"]:
                    self.instruction_pointer = self.operand - 2
            case 4:
                r["B"] = r["B"] ^ r["C"]
            case 5:
                yield self.combo(self.operand) % 8
            case 6:
                r["B"] = r["A"] // 2 ** self.combo(self.operand)
            case 7:
                r["C"] = r["A"] // 2 ** self.combo(self.operand)
        self.instruction_pointer += 2

    @property
    def opcode(self) -> int:
        return self.instructions[self.instruction_pointer]

    @property
    def operand(self) -> int:
        return self.instructions[self.instruction_pointer + 1]

    def combo(self, val: int) -> int:
        match val:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return self.registers["A"]
            case 5:
                return self.registers["B"]
            case 6:
                return self.registers["C"]
            case _:
                assert False


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
