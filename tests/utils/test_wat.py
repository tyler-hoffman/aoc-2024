from aoc_2024.utils.wat import wat
from tests.utils.from_prompt import EXPECTED_WAT_VALUE


def test_wat() -> None:
    assert wat() == EXPECTED_WAT_VALUE
