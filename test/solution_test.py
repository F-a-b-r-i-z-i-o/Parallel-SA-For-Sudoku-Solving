import pytest
from copy import deepcopy
import sys
import os

# Fix import
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "SOLVER"))
)

from solution import SingleSolution, TABLE_SIZE, BOX_SIZE


@pytest.fixture
def sudoku_puzzle():
    # Creates a Sudoku puzzle filled with zeros (an empty puzzle)
    return [[0 for _ in range(TABLE_SIZE)] for _ in range(TABLE_SIZE)]


@pytest.fixture
def single_solution_instance(sudoku_puzzle):
    # Creates an instance of SingleSolution with the empty puzzle and its deepcopy as the original state
    return SingleSolution(sudoku_puzzle, deepcopy(sudoku_puzzle))


def test_generate_solution(single_solution_instance):
    # Generates a solution for the puzzle and then checks each 3x3 box to ensure it contains numbers 1 to 9 without repeats
    single_solution_instance.generate_solution()
    for row_index in range(0, TABLE_SIZE, BOX_SIZE):
        for col_index in range(0, TABLE_SIZE, BOX_SIZE):
            box = {
                single_solution_instance.table[row_index + i][col_index + j]
                for i in range(BOX_SIZE)
                for j in range(BOX_SIZE)
            }
            assert box == set(
                range(1, TABLE_SIZE + 1)
            ), "Each box should contain unique numbers from 1 to 9"


def test_mutate(single_solution_instance):
    # Generates a solution, makes a deepcopy, mutates the solution, and checks that the table has changed post-mutation
    single_solution_instance.generate_solution()
    original_table = deepcopy(single_solution_instance.table)
    single_solution_instance.mutate()
    assert (
        original_table != single_solution_instance.table
    ), "The table should be different after mutation."


def test_fitness(single_solution_instance):
    # Generates a solution and calculates its fitness. For a valid solution, fitness should be 0, but can be higher for partial or mutated solutions
    single_solution_instance.generate_solution()
    fitness = single_solution_instance.fitness()
    assert isinstance(fitness, int), "Fitness should be an integer"
    assert fitness >= 0, "Fitness should be non-negative."


def test_find_candidates(single_solution_instance):
    # Finds candidate numbers for each cell and checks that each cell contains a set of candidates, which should be all numbers 1 to 9 for empty cells
    candidates = single_solution_instance.find_candidates()
    assert isinstance(candidates, list), "Candidates should be stored in a list"
    assert all(
        isinstance(candidates[row][col], set)
        for row in range(TABLE_SIZE)
        for col in range(TABLE_SIZE)
    ), "All cells should contain a set of candidates."
    expected_candidates = set(range(1, TABLE_SIZE + 1))
    assert (
        candidates[0][0] == expected_candidates
    ), "Empty cells should have all numbers as candidates."
