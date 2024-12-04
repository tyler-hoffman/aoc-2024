from typing import Sequence


class Parser:
    @staticmethod
    def parse(input: str) -> Sequence[Sequence[str]]:
        lines = input.strip().splitlines()
        return [list(line) for line in lines]
