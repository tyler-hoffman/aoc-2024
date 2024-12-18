from aoc_2024.utils.point import Point


class Parser:
    @staticmethod
    def parse(input: str) -> list[Point]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Point:
        x, y = line.split(",")
        return Point(int(x), int(y))
