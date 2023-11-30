import pytest

from aoc.day04.day04 import Solver
from aoc.util import Solution


#############################
# ======= solutons =========#
#############################
EXAMPLE_PART_ONE = 4512
EXAMPLE_PART_TWO = 1924
PART_ONE = 35711
PART_TWO = 5586


#############################
# ========= setup ==========#
#############################
@pytest.fixture
def example_input() -> str:
    with open("inputs/day04_example.txt", "r") as f:
        return f.read()


@pytest.fixture
def real_input() -> str:
    with open("inputs/day04.txt", "r") as f:
        return f.read()


@pytest.fixture
def example_solver(example_input: str) -> Solver:
    return Solver(example_input)


@pytest.fixture
def real_solver(real_input: str) -> Solver:
    return Solver(real_input)


#############################
# === tests for part one ===#
#############################
@pytest.mark.example
def test_example_part_one(example_solver: Solver):
    assert example_solver.part_one() == EXAMPLE_PART_ONE


@pytest.mark.real
def test_real_part_one(real_solver: Solver):
    assert real_solver.part_one() == PART_ONE


#
#############################
# === tests for part two ===#
#############################
@pytest.mark.example
def test_example_part_two(example_solver: Solver):
    assert example_solver.part_two() == EXAMPLE_PART_TWO


@pytest.mark.real
def test_real_part_two(real_solver: Solver):
    assert real_solver.part_two() == PART_TWO


#############################
# ======= benchmarks =======#
#############################
@pytest.mark.bench
def test_day04(benchmark, real_input: str):
    expected = Solution(part_one=PART_ONE, part_two=PART_TWO)
    result = benchmark(Solver.solve, real_input)

    # let's just leverage the diffs pytest will provide for better output
    assert result.__dict__ == expected.__dict__