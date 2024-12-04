def create_part_test_stub(day_string: str, part: str) -> str:
    src = "aoc_2024"
    return _TEST_PART_TEMPLATE.format(
        day_string=day_string,
        part=part,
        part_upper=part.upper(),
        src=src,
    )


_TEST_PART_TEMPLATE = """
from {src}.day_{day_string}.{part} import get_solution, solve
from {src}.day_{day_string}.from_prompt import SAMPLE_DATA, SAMPLE_SOLUTION_{part_upper}, SOLUTION_{part_upper}


def test_solve():
    assert solve(SAMPLE_DATA) == SAMPLE_SOLUTION_{part_upper}

def test_my_solution():
    assert get_solution() == SOLUTION_{part_upper}

"""
