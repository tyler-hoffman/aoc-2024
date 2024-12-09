class Parser:
    @staticmethod
    def parse(input: str) -> list[int]:
        chars = list(input.strip())
        return [int(x) for x in chars]
