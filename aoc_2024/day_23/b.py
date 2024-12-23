from dataclasses import dataclass
from functools import cached_property
from aoc_2024.day_23.parser import Parser


@dataclass
class Day23PartBSolver:
    pairs: list[tuple[str, str]]

    @property
    def solution(self) -> str:
        return ",".join(sorted(self.biggest_group))

    @cached_property
    def biggest_group(self) -> frozenset[str]:
        return self.get_biggest_group({frozenset(pair) for pair in self.pairs})

    def get_biggest_group(self, groups: set[frozenset[str]]) -> frozenset[str]:
        if len(groups) == 1:
            return next(g for g in groups)

        new_groups = set[frozenset[str]]()
        for group in groups:
            for node in self.nodes - group:
                compatible = True
                for x in group:
                    if x not in self.connections[node]:
                        compatible = False
                        break
                if compatible:
                    new_groups.add(group | {node})

        return self.get_biggest_group(new_groups)

    @cached_property
    def nodes(self) -> set[str]:
        return set(self.connections.keys())

    @cached_property
    def connections(self) -> dict[str, set[str]]:
        output: dict[str, set[str]] = {}
        for a, b in self.pairs:
            if a not in output:
                output[a] = set[str]()
            if b not in output:
                output[b] = set[str]()
            output[a].add(b)
            output[b].add(a)
        return output


def solve(input: str) -> str:
    data = Parser.parse(input)
    solver = Day23PartBSolver(data)

    return solver.solution


def get_solution() -> str:
    with open("aoc_2024/day_23/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
