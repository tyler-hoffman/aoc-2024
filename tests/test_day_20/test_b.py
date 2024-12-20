import pytest
from aoc_2024.day_20.b import get_solution, solve
from aoc_2024.day_20.from_prompt import (
    SAMPLE_DATA,
    SAMPLE_SOLUTION_B_ABOVE_50,
    SAMPLE_SOLUTION_B_ABOVE_76,
    SOLUTION_B,
)


@pytest.mark.parametrize(
    ("min_seconds_to_save", "expected"),
    [
        (50, SAMPLE_SOLUTION_B_ABOVE_50),
        (76, SAMPLE_SOLUTION_B_ABOVE_76),
    ],
)
def test_solve(min_seconds_to_save: int, expected: int):
    assert solve(SAMPLE_DATA, min_seconds_to_save=min_seconds_to_save) == expected


def test_my_solution():
    assert get_solution() == SOLUTION_B
