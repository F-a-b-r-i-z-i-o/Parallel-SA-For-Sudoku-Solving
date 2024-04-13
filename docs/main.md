# Parallel Sudoku Solver using Simulated Annealing

This documentation details the functions and modules used for solving multiple Sudoku puzzles in parallel via Simulated Annealing.

## Modules Required

- `SA`: Contains the `SimulatedAnnealing` class which implements the Simulated Annealing algorithm tailored for Sudoku.
- `csv`: For reading and writing CSV files which contain the Sudoku puzzles and the solutions.
- `os`: For directory and path manipulations.
- `multiprocessing`: Utilized to execute multiple instances of the algorithm in parallel to leverage multi-core processors.

## Functions

### `run_simulated_annealing(params: tuple)`

Executes the Simulated Annealing algorithm on a single Sudoku puzzle.

#### Parameters

- `params (tuple)`: A tuple containing the Sudoku puzzle, the minimum and maximum temperatures, the cooling rate, and a process ID for file naming.

#### Returns

- Returns a tuple with paths to the final solution and additional information files.

#### Description

This function initializes the `SimulatedAnnealing` class with the provided parameters, runs the algorithm, and then saves the final state of the Sudoku solution along with additional runtime information to CSV files. Each run is identified by a unique process ID to facilitate parallel processing without file conflicts.

### `read_sudoku_csv(file_path: str) -> list`

Reads Sudoku puzzles from a CSV file.

#### Parameters

- `file_path (str)`: The path to the CSV file containing Sudoku puzzles.

#### Returns

- A list of Sudoku puzzles, each represented as a list of lists of integers.

#### Description

This function reads a CSV file where each row represents a line in a Sudoku puzzle and empty lines indicate separations between puzzles. It returns a list of puzzles that can be fed into the Simulated Annealing algorithm.

## Main Execution Block

In the main block, the following steps are performed:

1. **Reading Puzzles**: Sudoku puzzles are read from a specified CSV file.
2. **Directory Preparation**: Directories for storing the final solutions and additional runtime data are prepared.
3. **Parameter Preparation**: Parameters for each Simulated Annealing process are prepared, including specific configurations for temperature and cooling.
4. **Parallel Execution**: The `multiprocessing.Pool` is used to run multiple instances of the `run_simulated_annealing` function in parallel, one for each puzzle.
5. **Completion**: After all processes complete, a message is printed to indicate that all solutions and data have been successfully saved.

## Example Usage

This setup is ideal for solving a large number of Sudoku puzzles in scenarios where individual puzzle solving is computationally intensive, and the solution speed is a priority. By utilizing multiple cores, the overall time to solve all puzzles can be significantly reduced.

```python
if __name__ == "__main__":
    file_path = 'path_to_sudoku_puzzles.csv'
    sudoku_grids = read_sudoku_csv(file_path)
    with Pool(processes=4) as pool:
        pool.map(run_simulated_annealing, [(grid, 1e-7, 1e5, 0.995, idx) for idx, grid in enumerate(sudoku_grids)])
