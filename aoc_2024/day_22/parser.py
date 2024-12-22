class Parser:
    @staticmethod
    def parse(input: str) -> list[int]:
        return [int(x) for x in input.strip().splitlines()]
