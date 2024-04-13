# Sudoku Solver Using Parallel Simulated Annealing 🧊🔥

This project implements a Sudoku solver using the Simulated Annealing optimization algorithm 🔄. The solver mimics the physical process of heating a material and then slowly lowering the temperature 🌡️ to decrease defects, thus minimizing the energy (number of conflicts) of the Sudoku puzzle.

## Features 🌟

- **Simulated Annealing Algorithm** 🔥: Utilizes simulated annealing to solve Sudoku puzzles by minimizing the number of conflicts.
- **Dynamic State Generation** 🔄: Generates new potential solutions by mutating the current state, respecting immutable cells.
- **Optimization Over Iterations** ⏳: Gradually decreases the temperature to reduce the likelihood of accepting worse solutions, honing in on the optimal solution.

## Structure 🏗️

The project is structured into several key components:

1. **SingleSolution Class** 🧩: Manages individual solutions of the Sudoku puzzle, providing methods to generate, mutate, and evaluate the fitness of solutions.
2. **SimulatedAnnealing Class** 🌡️: Oversees the simulated annealing process, including temperature management, state transitions, and probability calculations for accepting new states.
3. **Utils Folder** 📁: Contains scripts for data handling and visualization:
   - **Sudoku CSV Processor**: Manages reading and formatting Sudoku puzzles and solutions from CSV files.
   - **Matrix Image Generator**: Generates and saves images of Sudoku solution matrices for visualization.
   - **Plot Generator**: Produces plots to visually represent the evolution of solution metrics over iterations.

## Documentation 📖

For more detailed information and usage instructions, check out our [documentation](/Parallel-SA-For-Sudoku-Solving/docs/).

## Installation and Dependencies 🔧

Ensure Python is installed along with the following packages:
- `numpy`
- `multiprocessing`
- `pandas`
- `matplotlib`
- `csv`
- `pytest`

### Steps for Installation:

1. **Clone the Repository** 📥: 
   - Use the command `git clone https://github.com/F-a-b-r-i-z-i-o/Parallel-SA-For-Sudoku-Solving.git` to clone the repository to your local machine.
2. **Create and Activate Virtual Environment** 🌐:
   - Navigate to the repository directory:
     ```bash
     cd Parallel-SA-For-Sudoku-Solving
     ```
   - Create a virtual environment named `env` within this directory:
     ```bash
     python3 -m venv env
     ```
   - Activate the virtual environment using the `script.sh` script:
     ```bash
     . ./active_env.sh
     ```
3. **Install Dependencies** 📦:
   - Install required dependencies by executing:
     ```bash
     pip3 install -r requirements.txt
     ```

## Running Tests 🧪

To ensure the functionality and stability of the Sudoku solver, tests have been implemented using `pytest`. Here’s how you can run these tests:

1. **Activate the Virtual Environment**
2. **Run Tests**:
   - With the virtual environment active, simply execute the following command in the project root directory:
     ```bash
     pytest
     ```
   - This will discover and run all tests written for the Sudoku solver, reporting any failures and their respective reasons.

This setup enables easy testing and debugging, ensuring that enhancements or changes do not introduce regressions or new issues.

## Data Source 📊
 
### Sudoku Puzzles 🧩

The Sudoku puzzles used in this project were sourced from the following Kaggle dataset: [Sudoku Dataset](https://www.kaggle.com/datasets/bryanpark/sudoku).

### Limitations on Data Upload 📈

While all Sudoku puzzles have been solved using the algorithm, due to size limitations, only the first 100 solutions are uploaded to GitHub. The complete set of solutions remains available upon request or can be generated using the provided scripts.

## Results 🏆

The simulated annealing algorithm has been effectively applied to solve numerous Sudoku puzzles. The method's adaptability and efficiency in finding solutions within acceptable time frames have been thoroughly documented through various metrics plotted during the solving process.

### Example of a Solved Sudoku 🖼️

<p align="center">
  <img src="/matrix_images/matrix_image_0.png">
</p>

### Graph on Temperature and Fitness 📉

<p align="center">
  <img src="/plots/additional_info_plot_0.png">
</p>

## Contributing 🤝

Contributions to enhance the project are welcome. Please feel free to fork the repository, make improvements, and submit pull requests.

## License 📄

This project is released under the [MIT License](/LICENSE).

---

*Enjoy 2F_*
