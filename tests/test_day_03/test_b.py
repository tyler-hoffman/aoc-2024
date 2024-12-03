from aoc_2024.day_03.b import get_solution, solve
from aoc_2024.day_03.from_prompt import SAMPLE_DATA_B, SAMPLE_SOLUTION_B, SOLUTION_B


def test_solve():
    assert solve(SAMPLE_DATA_B) == SAMPLE_SOLUTION_B


def test_my_solution():
    assert get_solution() == SOLUTION_B
