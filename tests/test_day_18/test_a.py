from aoc_2024.day_18.a import get_solution, solve
from aoc_2024.day_18.from_prompt import (
    SAMPLE_BYTES_CORRUPTED,
    SAMPLE_DATA,
    SAMPLE_SOLUTION_A,
    SOLUTION_A,
)


def test_solve():
    assert (
        solve(SAMPLE_DATA, grid_size=7, bytes_fallen=SAMPLE_BYTES_CORRUPTED)
        == SAMPLE_SOLUTION_A
    )


def test_my_solution():
    assert get_solution() == SOLUTION_A
