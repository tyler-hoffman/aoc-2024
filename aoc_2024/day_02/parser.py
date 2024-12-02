from typing import Sequence


class Parser:
    @staticmethod
    def parse(input: str) -> Sequence[Sequence[int]]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Sequence[int]:
        vals = line.split()
        return [int(x) for x in vals]
