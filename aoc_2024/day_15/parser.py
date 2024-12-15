class Parser:
    @staticmethod
    def parse(input: str) -> tuple[list[list[str]], list[str]]:
        lines = input.strip().splitlines()
        space_index = lines.index("")

        return Parser.parse_grid(lines[:space_index]), Parser.parse_instructions(
            lines[space_index + 1 :]
        )

    @staticmethod
    def parse_grid(lines: list[str]) -> list[list[str]]:
        return [list(line) for line in lines]

    @staticmethod
    def parse_instructions(lines: list[str]) -> list[str]:
        combined = "".join(lines)
        return list(combined)
