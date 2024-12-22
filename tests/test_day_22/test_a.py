from aoc_2024.day_22.a import get_solution, solve
from aoc_2024.day_22.from_prompt import SAMPLE_DATA_A, SAMPLE_SOLUTION_A, SOLUTION_A


def test_solve():
    assert solve(SAMPLE_DATA_A) == SAMPLE_SOLUTION_A


def test_my_solution():
    assert get_solution() == SOLUTION_A