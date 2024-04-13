# Sudoku Solution

This document provides details about the classes and methods used in the Python program for generating and manipulating Sudoku puzzle solutions.

## Modules Required

- `copy`: Used to create deep copies of data structures.
- `random`: Used for shuffling and randomly selecting elements.

## Constants

- `TABLE_SIZE`: The size of the Sudoku puzzle, typically 9x9.
- `BOX_SIZE`: The size of each smaller 3x3 box within the Sudoku puzzle, typically 3x3.

## Class: SingleSolution

Represents a single solution for a Sudoku puzzle. Includes methods for generating, mutating, and evaluating a Sudoku solution, as well as finding candidates for each cell.

### Attributes

- `table (list[list[int]])`: Represents the current state of the Sudoku puzzle, which can be mutated.
- `original_table (list[list[int]])`: Represents the original state of the Sudoku puzzle, indicating which cells are pre-filled and should not be altered.

### Methods

#### `__init__(self, table: list[list[int]], original: list[list[int]])`
Initializes a new instance of the SingleSolution class.
- `table`: The current state of the Sudoku puzzle.
- `original`: The original Sudoku puzzle with some cells filled and others empty.

#### `generate_solution(self)`
Fills empty cells in each 3x3 box of the Sudoku puzzle with random numbers that follow Sudoku rules. This method modifies the puzzle state in place.

#### `mutate(self)`
Mutates the solution by swapping two numbers within a single 3x3 box. This method is used to explore neighboring solutions in a genetic algorithm or similar optimization approach.

#### `fitness(self) -> int`
Calculates the fitness of the solution based on the number of duplicate numbers in each row and column. A lower score indicates a better fit (less conflict).

#### `find_candidates(self) -> list[list[set]]`
Finds candidate numbers for each empty cell in the puzzle based on Sudoku rules. Each cell contains a set of possible numbers that could fit based on the current state of the puzzle.

#### `__str__(self) -> str`
Provides a string representation of the current state of the Sudoku puzzle, formatted as a grid.

## Example Usage

Here's a simple example of how to use the `SingleSolution` class to generate and mutate a Sudoku solution:

```python

initial_table = [[0]*9 for _ in range(9)]
original_puzzle = [[...]]  

solution = SingleSolution(table=initial_table, original=original_puzzle)

solution.generate_solution()
print(solution)

solution.mutate()
print(solution)

print("Fitness:", solution.fitness())

candidates = solution.find_candidates()
print(candidates)
