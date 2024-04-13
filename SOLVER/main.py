from SA import SimulatedAnnealing
import csv
import os
from multiprocessing import Pool


def run_simulated_annealing(params: tuple):
    """
    Executes the Simulated Annealing algorithm on a single Sudoku puzzle.

    Args:
        params (tuple): A tuple containing the Sudoku puzzle, the minimum and maximum temperatures,
                        the cooling rate, and a process ID for file naming.

    Returns:
        A tuple with paths to the final solution and additional information files.
    """
    sudoku_table, min_temp, max_temp, cooling_rate, process_id = params
    algorithm = SimulatedAnnealing(sudoku_table, min_temp, max_temp, cooling_rate)
    best_state, fitness, additional_info_data = algorithm.run(process_id)

    # Ensure output directories exist
    final_solution_path = os.path.join("final_solutions", f"solution_{process_id}.csv")
    additional_info_path = os.path.join(
        "additional_info", f"additional_info_{process_id}.csv"
    )

    # Save the best solution for each puzzle to a CSV file
    with open(final_solution_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in best_state:
            writer.writerow(row)

    # Save additional information about the process for each puzzle
    with open(additional_info_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Iteration", "Temperature", "Best Fitness"])
        for data in additional_info_data:
            writer.writerow(data)

    return final_solution_path, additional_info_path


def read_sudoku_csv(file_path: str) -> list:
    """
    Reads Sudoku puzzles from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing Sudoku puzzles.

    Returns:
        A list of Sudoku puzzles, each represented as a list of lists of integers.
    """
    sudokus = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        sudoku = []
        for row in reader:
            if row:  # Non-empty row indicates part of a puzzle
                sudoku.append([int(num) for num in row])
            else:  # Empty row indicates separation between puzzles
                if sudoku:  # If a puzzle is accumulated, add it to the list
                    sudokus.append(sudoku)
                    sudoku = []
        if sudoku:  # Add the last puzzle if the file doesn't end with an empty row
            sudokus.append(sudoku)
    return sudokus


if __name__ == "__main__":
    print("Reading Sudoku puzzles from CSV file...")
    file_path = "../quiz/sudoku_quiz.csv"  # Path to the CSV file with puzzles
    sudoku_grids = read_sudoku_csv(file_path)
    print(f"Found {len(sudoku_grids)} puzzles.")

    # Prepare output directories
    os.makedirs("final_solutions", exist_ok=True)
    os.makedirs("additional_info", exist_ok=True)

    # Prepare parameters for each process in multiprocessing
    processes_parameters = [
        (sudoku, 1e-7, 1e8, 0.999, i) for i, sudoku in enumerate(sudoku_grids)
    ]

    print("Starting simulated annealing process on all puzzles...")
    with Pool(processes=8) as pool:  # Use 8 parallel processes
        pool.map(run_simulated_annealing, processes_parameters)

    print("All solutions and additional information have been successfully saved.")
