import csv
import os

# Paths for the input CSV file, quiz, and solutions directories
file_to_read = "../sudoku.csv"
quiz_folder = "../quiz"
solutions_folder = "../solutions"

# Constructing file paths for the output sudoku quiz and solutions CSV files
sudoku_file = os.path.join(quiz_folder, "sudoku_quiz.csv")
solutions_file = os.path.join(solutions_folder, "sudoku_solutions.csv")

# Define the size of the Sudoku table
TABLE_SIZE = 9

# Create quiz and solutions folders if they don't already exist
if not os.path.exists(quiz_folder):
    os.makedirs(quiz_folder)
if not os.path.exists(solutions_folder):
    os.makedirs(solutions_folder)


def read_and_process_csv(
    file_to_read: str, sudoku_file: str, solutions_file: str
) -> None:
    """
    Reads the input CSV file containing Sudoku puzzles and their solutions,
    and writes them to separate CSV files in a formatted manner.

    Args:
    file_to_read (str): Path to the input CSV file.
    sudoku_file (str): Path to the output CSV file for Sudoku puzzles.
    solutions_file (str): Path to the output CSV file for Sudoku solutions.
    """
    with open(file_to_read) as csv_file, open(
        sudoku_file, "w", newline=""
    ) as sudoku_csv, open(solutions_file, "w", newline="") as solutions_csv:
        csv_reader = csv.reader(csv_file, delimiter=",")
        sudoku_writer = csv.writer(sudoku_csv)
        solutions_writer = csv.writer(solutions_csv)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # Process each row for sudoku puzzles and solutions
                process_row(row[0], sudoku_writer)
                process_row(row[1], solutions_writer)
                line_count += 1
        print(f"Processed {line_count - 1} lines.")


def process_row(sudoku_string: str, writer: str) -> None:
    """
    Processes a single row of Sudoku string, converting it into a grid format
    and writing it to the specified CSV writer.

    Args:
    sudoku_string (str): A string representation of a Sudoku puzzle or solution.
    writer (csv.writer): The CSV writer object to write the grid to.
    """
    # Split the Sudoku string into a grid format
    grid = [
        sudoku_string[i : i + TABLE_SIZE]
        for i in range(0, len(sudoku_string), TABLE_SIZE)
    ]

    # Write each row of the grid to the CSV file
    for row in grid:
        writer.writerow(list(row))
    writer.writerow([])  # Add an empty row for separation between puzzles/solutions


if __name__ == "__main__":
    read_and_process_csv(file_to_read, sudoku_file, solutions_file)
