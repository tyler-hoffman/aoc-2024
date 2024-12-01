from aoc_2024.day_01.b import get_solution, solve
from aoc_2024.day_01.from_prompt import (
    ACTUAL_SOLUTION_B,
    SAMPLE_DATA,
    SAMPLE_SOLUTION_B,
)


def test_solve():
    assert solve(SAMPLE_DATA) == SAMPLE_SOLUTION_B


def test_my_solution():
    assert get_solution() == ACTUAL_SOLUTION_B
