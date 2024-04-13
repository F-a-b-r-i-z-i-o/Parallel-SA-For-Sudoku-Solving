# Documentation for Generating and Saving Matrix Images

This document outlines the functionality of a Python script designed to generate and save images of matrices, which are read from CSV files. The script uses the `pandas` library to handle data manipulation, `matplotlib` for generating the images, and `numpy` for numerical operations.

## Modules Required

- `pandas`: Used for reading CSV files and handling data.
- `matplotlib.pyplot`: Utilized for creating and manipulating figures and plots.
- `os`: For handling directory paths and operations.
- `numpy`: For handling numerical data and operations within the matrix.

## Function Description

### `generate_and_save_matrix_images(file_pattern, output_dir, start_index, end_index)`

Generates and saves images of matrices for each CSV file specified by a range of indices.

#### Parameters

- `file_pattern (str)`: The pattern of the file path with a placeholder for the index. This pattern is used to construct file paths dynamically.
- `output_dir (str)`: The directory where the generated images will be saved.
- `start_index (int)`: The starting index for the files to be processed.
- `end_index (int)`: The ending index for the files to be processed.

#### Process

1. **Directory Creation**: Checks and creates the output directory if it does not exist.
2. **File Processing Loop**: Iterates through a range of indices, constructs file paths based on the `file_pattern`, and reads each corresponding CSV file into a matrix.
3. **Image Generation**:
   - Sets up a figure with a specified background color.
   - Populates the figure with the matrix data, annotating each cell with its respective value.
   - Configures the visual aspects of the figure, such as text color, font size, and axis visibility.
   - Saves the figure as a PNG image in the specified output directory.

#### Visualization Details

- **Background Color**: A soft gray (`#f5f5f5`) is used for the figure's background to ensure visual comfort.
- **Text Color**: Black (`#000000`) is used for text to provide high contrast against the background.
- **Image Format**: Images are saved as PNG files with names formatted as `matrix_image_{index}.png`.

## Example Usage

Here is an example of how to use this function to generate images for matrices stored in CSV files ranging from index 0 to 99:

```python
generate_and_save_matrix_images(
    "../SOLVER/final_solutions/solution_{index}.csv",  # File pattern
    "../matrix_images",  # Output directory
    0,  # Start index
    100  # End index
)
