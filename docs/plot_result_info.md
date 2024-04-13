# Documentation for Generating and Saving Plots from CSV Data

This document describes the functionality of a Python script that generates and saves plots for series data contained in CSV files. The script is designed to automate the visualization process for a series of data points, facilitating the analysis of trends such as "Best Fitness" and "Temperature" over "Iterations".

## Modules Required

- `pandas`: Used to read data from CSV files and manipulate it efficiently.
- `matplotlib.pyplot`: Utilized for creating and saving plots.
- `os`: For handling directory paths and operations.

## Function Description

### `generate_and_save_plots(file_pattern, output_dir, start_index, end_index)`

Generates and saves line plots from data in CSV files, specified by a range of indices.

#### Parameters

- `file_pattern (str)`: The pattern of the file path with a placeholder for the index, used to generate file paths dynamically.
- `output_dir (str)`: The directory where the generated plots will be saved.
- `start_index (int)`: The starting index for the files to be processed.
- `end_index (int)`: The ending index for the files to be processed.

#### Process

1. **Directory Validation**: Ensures the specified output directory exists; creates it if not.
2. **Loop Through Files**: Iterates through a range of indices to process each specified CSV file:
   - Reads data into a DataFrame using `pandas`.
   - Generates a plot with a consistent gray background and contrasting line colors.
   - Plots multiple variables ("Best Fitness" and "Temperature") on dual axes against "Iterations".
   - Saves each plot as a PNG file in the specified directory.
3. **Visual Customization**:
   - Sets axes and label colors for clarity and aesthetic appeal.
   - Includes a grid and a legend to enhance readability.
   - Uses twin axes to display two different scales on the same plot for comparison.

#### Styling Details

- **Background Color**: Light gray for both the plot and the figure to maintain visual consistency and reduce strain.
- **Line Styles**: Solid and dashed lines are used to differentiate the series, with distinct colors for each variable.
- **File Naming**: Plots are saved with names formatted as `additional_info_plot_{index}.png`, where `{index}` corresponds to the file index.

## Example Usage

The function is designed to be run within a script or a larger application. Here's an example call:

```python
generate_and_save_plots(
    "../SOLVER/additional_info/additional_info_{index}.csv",  # File pattern
    "../plots",  # Output directory
    0,  # Start index
    100  # End index
)
