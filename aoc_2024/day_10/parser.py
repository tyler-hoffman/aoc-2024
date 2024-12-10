class Parser:
    @staticmethod
    def parse(input: str) -> list[list[int]]:
        lines = input.strip().splitlines()
        return [[int(ch) for ch in line] for line in lines]
