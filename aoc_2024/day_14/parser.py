from aoc_2024.utils.point import Point


class Parser:
    @staticmethod
    def parse(input: str) -> list[tuple[Point, Point]]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> tuple[Point, Point]:
        left, right = line.split()
        return Parser.parse_part(left), Parser.parse_part(right)

    @staticmethod
    def parse_part(line: str) -> Point:
        _, point = line.split("=")
        x, y = point.split(",")
        return Point(int(x), int(y))
