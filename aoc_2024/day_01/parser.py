from typing import Sequence


class Parser:
    @staticmethod
    def parse(input: str) -> Sequence[tuple[int, int]]:
        raw_lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in raw_lines]

    @staticmethod
    def parse_line(line: str) -> tuple[int, int]:
        a, b = line.split()
        return (int(a), int(b))
