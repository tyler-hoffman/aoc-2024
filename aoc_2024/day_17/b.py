from dataclasses import dataclass
from aoc_2024.day_17.machine import Machine
from aoc_2024.day_17.parser import Parser


@dataclass
class Day17PartBSolver:
    """Oof, I've failed today. I'm not clever enough do the totally generic solution.

    This solution was done by analyzing what my input program did and then implementing
    that get_a below.
    """

    registers: dict[str, int]
    instructions: list[int]

    @property
    def solution(self) -> int:
        to_get = self.instructions[::]

        output = self.get_a(old_a=0, to_get=to_get)
        assert output is not None

        m = Machine({"A": output}, self.instructions)
        verification = m.get_output()
        assert verification == ",".join([str(x) for x in self.instructions])

        return output

    def get_a(self, old_a: int, to_get: list[int]) -> int | None:
        if not to_get:
            return old_a

        target = to_get.pop()

        a = old_a * 8
        for a in range(old_a * 8, (old_a + 1) * 8):
            b = a % 8
            b = b ^ 2
            c = a // (2**b)
            b = b ^ c
            b = b ^ 7
            b = b % 8
            if b == target:
                output = self.get_a(a, to_get)
                if output is not None:
                    return output
            a += 1
        to_get.append(target)
        return None


def solve(input: str) -> int:
    initial_registers, instructions = Parser.parse(input)
    solver = Day17PartBSolver(
        registers=initial_registers,
        instructions=instructions,
    )

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_17/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
