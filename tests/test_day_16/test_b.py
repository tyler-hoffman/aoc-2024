import pytest
from aoc_2024.day_16.b import get_solution, solve
from aoc_2024.day_16.from_prompt import (
    SAMPLE_DATA_1,
    SAMPLE_DATA_2,
    SAMPLE_SOLUTION_B1,
    SAMPLE_SOLUTION_B2,
    SOLUTION_B,
)


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (SAMPLE_DATA_1, SAMPLE_SOLUTION_B1),
        (SAMPLE_DATA_2, SAMPLE_SOLUTION_B2),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == SOLUTION_B
