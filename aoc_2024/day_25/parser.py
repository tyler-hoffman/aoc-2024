class Parser:
    @staticmethod
    def parse(input: str) -> list[list[list[str]]]:
        output: list[list[list[str]]] = []
        lines = input.strip().splitlines()
        for i in range(0, len(lines), 8):
            line_set = lines[i : i + 7]
            output.append([list(line) for line in line_set])
        return output
