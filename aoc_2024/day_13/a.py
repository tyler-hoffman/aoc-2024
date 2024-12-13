from dataclasses import dataclass
from aoc_2024.day_13.models import ArcadeGame
from aoc_2024.day_13.parser import Parser

COST_PER_A = 3
COST_PER_B = 1


@dataclass
class Day13PartASolver:
    arcade_games: list[ArcadeGame]

    @property
    def solution(self) -> int:
        output = 0
        for game in self.arcade_games:
            output += self.get_cost(game) or 0
        return output

    def get_cost(self, game: ArcadeGame) -> int | None:
        a, b, p = game.a, game.b, game.prize
        n = (a.y * p.x - a.x * p.y) / (a.y * b.x - a.x * b.y)
        m = (p.x - b.x * n) / a.x
        if n != int(n) or m != int(m):
            return None
        else:
            return COST_PER_A * int(m) + COST_PER_B * int(n)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day13PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2024/day_13/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
