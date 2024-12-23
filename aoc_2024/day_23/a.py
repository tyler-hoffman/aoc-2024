from dataclasses import dataclass
from functools import cached_property
from aoc_2024.day_23.parser import Parser


@dataclass
class Day23PartASolver:
    pairs: list[tuple[str, str]]

    @property
    def solution(self) -> int:
        filtered = [g for g in self.groups_of_three if self.has_t_starter(g)]
        return len(filtered)

    def has_t_starter(self, group: frozenset[str]) -> bool:
        return any([node for node in group if node.startswith("t")])

    @cached_property
    def groups_of_three(self) -> set[frozenset[str]]:
        output = set[frozenset[str]]()
        for a in self.nodes:
            for b in self.nodes:
                if b not in self.connections[a]:
                    continue
                else:
                    for c in self.connections[a] & self.connections[b]:
                        output.add(frozenset({a, b, c}))
        return output

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


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day23PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_23/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
