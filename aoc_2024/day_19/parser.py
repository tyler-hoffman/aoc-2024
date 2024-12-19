class Parser:
    @staticmethod
    def parse(input: str) -> tuple[list[str], list[str]]:
        lines = input.strip().splitlines()

        return lines[0].split(", "), lines[2:]
