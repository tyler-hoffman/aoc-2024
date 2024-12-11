class Parser:
    @staticmethod
    def parse(input: str) -> list[int]:
        stuff = input.strip().split(" ")
        return [int(x) for x in stuff]
