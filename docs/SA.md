# Simulated Annealing for Sudoku

This document provides details about the `SimulatedAnnealing` class used for solving Sudoku puzzles using the Simulated Annealing optimization algorithm.

## Overview

Simulated Annealing is a probabilistic technique for approximating the global optimum of a given function. Specifically, it mimics the physical process of heating a material and then slowly lowering the temperature to decrease defects, thus minimizing the system's energy. For Sudoku, the "energy" is analogous to the number of conflicting numbers (violations of Sudoku rules).

## Class: SimulatedAnnealing

Implements the Simulated Annealing algorithm tailored for Sudoku puzzle solving, aiming to minimize the number of conflicts.

### Attributes

- `table (list[list[int]])`: The initial state of the Sudoku puzzle.
- `original (list[list[int]])`: The original state of the Sudoku puzzle to maintain fixed numbers.
- `min_temp (float)`: The minimum temperature at which the annealing process will stop.
- `max_temp (float)`: The maximum temperature from which the annealing process starts.
- `cooling_rate (float)`: The rate at which the temperature decreases per iteration.
- `actual_state (SingleSolution)`: The current Sudoku puzzle state as a `SingleSolution` instance.
- `best_state (SingleSolution)`: The best solution encountered during the process.
- `next_state (SingleSolution)`: A placeholder for generating new states.

### Methods

#### `__init__(self, table: list[list[int]], min_temp: float, max_temp: float, cooling_rate: float = 0.999)`
Initializes the SimulatedAnnealing instance with the specified parameters.
- `table`: Current Sudoku puzzle state.
- `min_temp`: Lower bound of temperature for stopping the algorithm.
- `max_temp`: Starting temperature for the annealing process.
- `cooling_rate`: Multiplier to decrease the temperature after each iteration.

#### `run(self, process_id: int) -> tuple`
Executes the Simulated Annealing algorithm.
- `process_id`: Identifier for the process, useful for debugging or logging.
- Returns a tuple containing the best solution found, its fitness, and additional data for analysis (iterations, temperature, best fitness over time).

#### `generate_nxt_state(self, actual_state: SingleSolution) -> SingleSolution`
Generates a new Sudoku state by mutating the given state.
- `actual_state`: The current solution state to be mutated.
- Returns a new mutated state.

#### `accept_prob(actual_energy: float, next_energy: float, temp: float) -> float`
Calculates the probability of accepting a new state.
- `actual_energy`: Energy (number of conflicts) of the current state.
- `next_energy`: Energy of the new state.
- `temp`: Current temperature.
- Returns the probability of accepting the new state, favoring states with lower energy.

## Example Usage

Here's how to use the `SimulatedAnnealing` class to solve a Sudoku puzzle:

```python
initial_table = [[0]*9 for _ in range(9)]  
solver = SimulatedAnnealing(table=initial_table, min_temp=1.0, max_temp=100.0, cooling_rate=0.99)
best_solution, best_fitness, run_info = solver.run(process_id=1)
print("Best solution:", best_solution)
print("Best fitness:", best_fitness)
