import pytest
from aoc_2024.day_12.b import get_solution, solve
from aoc_2024.day_12.from_prompt import (
    SAMPLE_DATA_1,
    SAMPLE_DATA_2,
    SAMPLE_DATA_3,
    SAMPLE_DATA_4,
    SAMPLE_DATA_5,
    SAMPLE_SOLUTION_B1,
    SAMPLE_SOLUTION_B2,
    SAMPLE_SOLUTION_B3,
    SAMPLE_SOLUTION_B4,
    SAMPLE_SOLUTION_B5,
    SOLUTION_B,
)


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (SAMPLE_DATA_1, SAMPLE_SOLUTION_B1),
        (SAMPLE_DATA_2, SAMPLE_SOLUTION_B2),
        (SAMPLE_DATA_3, SAMPLE_SOLUTION_B3),
        (SAMPLE_DATA_4, SAMPLE_SOLUTION_B4),
        (SAMPLE_DATA_5, SAMPLE_SOLUTION_B5),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == SOLUTION_B
