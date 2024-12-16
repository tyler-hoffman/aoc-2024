import pytest
from aoc_2024.day_16.a import get_solution, solve
from aoc_2024.day_16.from_prompt import (
    SAMPLE_DATA_1,
    SAMPLE_DATA_2,
    SAMPLE_SOLUTION_A1,
    SAMPLE_SOLUTION_A2,
    SOLUTION_A,
)


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (SAMPLE_DATA_1, SAMPLE_SOLUTION_A1),
        (SAMPLE_DATA_2, SAMPLE_SOLUTION_A2),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == SOLUTION_A
