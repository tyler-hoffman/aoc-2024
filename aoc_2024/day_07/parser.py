class Parser:
    @staticmethod
    def parse(input: str) -> list[tuple[int, list[int]]]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> tuple[int, list[int]]:
        left, right = line.split(": ")
        return int(left), [int(num) for num in right.split(" ")]
