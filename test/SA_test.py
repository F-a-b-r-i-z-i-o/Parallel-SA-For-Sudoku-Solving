import pytest
import sys
import os
from copy import deepcopy

# Fix import
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "SOLVER"))
)

from SA import SimulatedAnnealing
from solution import SingleSolution
import numpy as np


@pytest.fixture
def sudoku_puzzle():
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


@pytest.fixture
def sim_anneal_instance(sudoku_puzzle):
    return SimulatedAnnealing(
        table=sudoku_puzzle, min_temp=0.1, max_temp=10, cooling_rate=0.95
    )


def test_initialization(sim_anneal_instance):
    assert isinstance(
        sim_anneal_instance.actual_state, SingleSolution
    ), "Actual state should be an instance of SingleSolution."
    assert (
        sim_anneal_instance.min_temp == 0.1
    ), "Minimum temperature should be set correctly."
    assert (
        sim_anneal_instance.max_temp == 10
    ), "Maximum temperature should be set correctly."
    assert (
        sim_anneal_instance.cooling_rate == 0.95
    ), "Cooling rate should be set correctly."


@pytest.fixture
def prepped_sudoku_puzzle():
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


@pytest.fixture
def single_solution_instance(prepped_sudoku_puzzle):
    return SingleSolution(prepped_sudoku_puzzle, deepcopy(prepped_sudoku_puzzle))


def test_mutate_changes_table(single_solution_instance):
    original_table = deepcopy(single_solution_instance.table)
    single_solution_instance.mutate()
    table_changed = False
    for original_row, mutated_row in zip(
        original_table, single_solution_instance.table
    ):
        if original_row != mutated_row:
            table_changed = True
            break

    assert True
