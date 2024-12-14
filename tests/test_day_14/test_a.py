from aoc_2024.day_14.a import get_solution, solve
from aoc_2024.day_14.from_prompt import SAMPLE_DATA, SAMPLE_SOLUTION_A, SOLUTION_A


def test_solve():
    assert solve(SAMPLE_DATA, width=11, height=7) == SAMPLE_SOLUTION_A


def test_my_solution():
    assert get_solution() == SOLUTION_A
