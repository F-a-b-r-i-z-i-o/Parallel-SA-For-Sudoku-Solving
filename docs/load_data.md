# Sudoku CSV Processor Documentation

This documentation provides details on a Python script designed to read Sudoku puzzles and their solutions from a CSV file and write them to separate, formatted CSV files.

## Modules Required

- `csv`: Used for reading from and writing to CSV files.
- `os`: Used for file path manipulations and directory operations.

## File Paths and Constants

- `file_to_read`: Path to the input CSV file containing Sudoku puzzles and their solutions.
- `quiz_folder`: Directory path where the Sudoku puzzles will be saved.
- `solutions_folder`: Directory path where the Sudoku solutions will be saved.
- `sudoku_file`: File path for the output CSV file that will store the Sudoku puzzles.
- `solutions_file`: File path for the output CSV file that will store the Sudoku solutions.
- `TABLE_SIZE`: The size of each side of the Sudoku grid, usually 9x9.

## Functionality

### Directory Setup

The script checks for the existence of the specified `quiz_folder` and `solutions_folder` directories. If these do not exist, they are created. This ensures that the output files have a place to be stored without errors.

### Main Functions

#### `read_and_process_csv(file_to_read: str, sudoku_file: str, solutions_file: str) -> None`

Reads the input CSV file containing rows of Sudoku puzzles and their solutions, writes them to separate formatted CSV files.

##### Parameters

- `file_to_read (str)`: The file path of the CSV file containing the Sudoku data.
- `sudoku_file (str)`: The file path where the Sudoku puzzles will be written.
- `solutions_file (str)`: The file path where the Sudoku solutions will be written.

##### Description

This function opens the specified input CSV file and two output CSV files for puzzles and solutions. It reads through the input file, processes each row using `process_row()`, and writes the formatted output to the respective files.

#### `process_row(sudoku_string: str, writer: csv.writer) -> None`

Processes a single string of Sudoku data into a grid format and writes it to the specified CSV writer.

##### Parameters

- `sudoku_string (str)`: A string representation of a Sudoku grid, where each character represents a cell in the puzzle.
- `writer (csv.writer)`: The CSV writer object used to write the formatted grid to a file.

##### Description

The function converts a single string of Sudoku numbers into a 9x9 grid format by slicing the string into rows. Each row of the grid is then written to the CSV file, with an empty row added between grids for clear separation.

## Example Usage

This script is executed from the command line, where it reads an input CSV file, processes the contained Sudoku puzzles and solutions, and writes the results to separate output files:

```python
if __name__ == "__main__":
    file_path = "path/to/sudoku.csv"
    read_and_process_csv(file_to_read, sudoku_file, solutions_file)
