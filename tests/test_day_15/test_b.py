from aoc_2024.day_15.b import get_solution, solve
from aoc_2024.day_15.from_prompt import (
    SAMPLE_DATA_LARGE,
    SAMPLE_SOLUTION_B_LARGE,
    SOLUTION_B,
)


def test_solve():
    assert solve(SAMPLE_DATA_LARGE) == SAMPLE_SOLUTION_B_LARGE


def test_my_solution():
    assert get_solution() == SOLUTION_B
