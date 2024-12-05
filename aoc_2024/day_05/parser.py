class Parser:
    @staticmethod
    def parse(input: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
        lines = input.strip().splitlines()
        blank_index = lines.index("")
        first_part = lines[:blank_index]
        second_part = lines[blank_index + 1 :]

        first_part_parsed = [Parser.parse_first_part(line) for line in first_part]
        second_part_parsed = [Parser.parse_second_part(line) for line in second_part]

        return first_part_parsed, second_part_parsed

    @staticmethod
    def parse_first_part(line: str) -> tuple[int, int]:
        a, b = line.split("|")
        return (int(a), int(b))

    @staticmethod
    def parse_second_part(line: str) -> list[int]:
        parts = line.split(",")
        return [int(p) for p in parts]
