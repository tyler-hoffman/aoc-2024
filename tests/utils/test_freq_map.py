from aoc_2024.utils.freq_map import freq_map


def test_empty() -> None:
    assert freq_map([]) == {}


def test_ints() -> None:
    assert freq_map([1, 2, 3, 2, 2, 2]) == {1: 1, 2: 4, 3: 1}


def test_strings() -> None:
    assert freq_map(["foo", "foo", "bar"]) == {"foo": 2, "bar": 1}
