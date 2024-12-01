import pytest

from aoc_2024.day_01.a import get_solution, solve
from aoc_2024.day_01.from_prompt import (
    ACTUAL_SOLUTION_A,
    SAMPLE_DATA,
    SAMPLE_SOLUTION_A,
)


def test_solve():
    assert solve(SAMPLE_DATA) == SAMPLE_SOLUTION_A


@pytest.mark.skip
def test_my_solution():
    assert get_solution() == ACTUAL_SOLUTION_A
