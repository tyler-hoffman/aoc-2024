import pytest

from aoc_2024.day_04.b import get_solution, solve
from aoc_2024.day_04.from_prompt import SAMPLE_DATA, SAMPLE_SOLUTION_B, SOLUTION_B


def test_solve():
    assert solve(SAMPLE_DATA) == SAMPLE_SOLUTION_B


@pytest.mark.skip
def test_my_solution():
    assert get_solution() == SOLUTION_B
