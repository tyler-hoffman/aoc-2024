import pytest
from aoc_2024.day_20.a import get_solution, solve
from aoc_2024.day_20.from_prompt import (
    SAMPLE_DATA,
    SAMPLE_SOLUTION_A_ABOVE_1,
    SAMPLE_SOLUTION_A_ABOVE_64,
    SOLUTION_A,
)


@pytest.mark.parametrize(
    ("min_seconds_to_save", "expected"),
    [
        (1, SAMPLE_SOLUTION_A_ABOVE_1),
        (64, SAMPLE_SOLUTION_A_ABOVE_64),
    ],
)
def test_solve(min_seconds_to_save: int, expected: int):
    assert solve(SAMPLE_DATA, min_seconds_to_save=min_seconds_to_save) == expected


def test_my_solution():
    assert get_solution() == SOLUTION_A
