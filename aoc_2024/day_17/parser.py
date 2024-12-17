class Parser:
    @staticmethod
    def parse(input: str) -> tuple[dict[str, int], list[int]]:
        lines = input.strip().splitlines()

        return {
            "A": Parser.parse_register_value(lines[0]),
            "B": Parser.parse_register_value(lines[1]),
            "C": Parser.parse_register_value(lines[2]),
        }, [int(x) for x in Parser.get_end(lines[-1]).split(",")]

    @staticmethod
    def parse_register_value(line: str) -> int:
        return int(Parser.get_end(line))

    @staticmethod
    def get_end(line: str) -> str:
        _, value = line.split(": ")
        return value
