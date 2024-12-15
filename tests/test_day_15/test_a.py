import pytest
from aoc_2024.day_15.a import get_solution, solve
from aoc_2024.day_15.from_prompt import (
    SAMPLE_DATA_SMALL,
    SAMPLE_DATA_LARGE,
    SAMPLE_SOLUTION_A_LARGE,
    SAMPLE_SOLUTION_A_SMALL,
    SOLUTION_A,
)


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (SAMPLE_DATA_LARGE, SAMPLE_SOLUTION_A_LARGE),
        (SAMPLE_DATA_SMALL, SAMPLE_SOLUTION_A_SMALL),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == SOLUTION_A
