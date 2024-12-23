class Parser:
    @staticmethod
    def parse(input: str) -> list[tuple[str, str]]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> tuple[str, str]:
        a, b = line.split("-")
        return a, b
