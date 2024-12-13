from aoc_2024.day_13.models import ArcadeGame
from aoc_2024.utils.point import Point


class Parser:
    @staticmethod
    def parse(input: str) -> list[ArcadeGame]:
        lines = input.strip().splitlines()
        chunks = [lines[i : i + 4] for i in range(0, len(lines), 4)]
        return [Parser.parse_arcade(chunk) for chunk in chunks]

    @staticmethod
    def parse_arcade(lines: list[str]) -> ArcadeGame:
        return ArcadeGame(
            a=Parser.parse_line(lines[0]),
            b=Parser.parse_line(lines[1]),
            prize=Parser.parse_line(lines[2]),
        )

    @staticmethod
    def parse_line(line: str) -> Point:
        parts = line.split()
        with_x = parts[-2]
        with_y = parts[-1]
        assert with_x.startswith("X+") or with_x.startswith("X=")
        assert with_y.startswith("Y+") or with_y.startswith("Y=")
        return Point(int(with_x[2:-1]), int(with_y[2:]))
