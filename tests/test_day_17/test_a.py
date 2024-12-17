from aoc_2024.day_17.a import Machine, get_solution, solve
from aoc_2024.day_17.from_prompt import (
    MINI_EXAMPLE_1,
    MINI_EXAMPLE_2,
    MINI_EXAMPLE_3,
    MINI_EXAMPLE_4,
    MINI_EXAMPLE_5,
    MINI_EXAMPLE_1_B,
    MINI_EXAMPLE_2_OUTPUT,
    MINI_EXAMPLE_3_OUTPUT,
    MINI_EXAMPLE_3_A,
    MINI_EXAMPLE_4_B,
    MINI_EXAMPLE_5_B,
    SAMPLE_DATA_A,
    SAMPLE_SOLUTION_A,
    SOLUTION_A,
)
from aoc_2024.day_17.parser import Parser


def test_mini_example_1():
    machine = Machine(*Parser.parse(MINI_EXAMPLE_1))
    machine.get_output()
    assert machine.registers["B"] == MINI_EXAMPLE_1_B


def test_mini_example_2():
    machine = Machine(*Parser.parse(MINI_EXAMPLE_2))
    output = machine.get_output()
    assert output == MINI_EXAMPLE_2_OUTPUT


def test_mini_example_3():
    machine = Machine(*Parser.parse(MINI_EXAMPLE_3))
    output = machine.get_output()
    assert machine.registers["A"] == MINI_EXAMPLE_3_A
    assert output == MINI_EXAMPLE_3_OUTPUT


def test_mini_example_4():
    machine = Machine(*Parser.parse(MINI_EXAMPLE_4))
    machine.get_output()
    assert machine.registers["B"] == MINI_EXAMPLE_4_B


def test_mini_example_5():
    machine = Machine(*Parser.parse(MINI_EXAMPLE_5))
    machine.get_output()
    assert machine.registers["B"] == MINI_EXAMPLE_5_B


def test_solve():
    assert solve(SAMPLE_DATA_A) == SAMPLE_SOLUTION_A


def test_my_solution():
    assert get_solution() == SOLUTION_A
    assert get_solution() != "7,7,7,7,7,7,7,7,7"
