from copy import deepcopy
from solution import SingleSolution
import numpy as np
import random


class SimulatedAnnealing:
    """
    This class implements the Simulated Annealing optimization algorithm to solve Sudoku puzzles.
    It simulates the physical process of heating a material and then slowly lowering the temperature to decrease defects,
    thus minimizing the energy (number of conflicts) of the system (Sudoku puzzle). The algorithm iterates through possible solutions,
    probabilistically accepting solutions based on the difference in energy and the current temperature,
    in search of the solution with the minimum number of conflicts.
    """

    def __init__(
        self,
        table: list[list[int]],
        min_temp: float,
        max_temp: float,
        cooling_rate: float = 0.999,
    ) -> None:
        """
        Initializes the SimulatedAnnealing instance with a Sudoku puzzle and parameters for the algorithm.

        Args:
            table (list[list[int]]): The initial state of the Sudoku puzzle, represented as a 2D list of integers.
            min_temp (float): The minimum temperature at which the algorithm will stop running.
            max_temp (float): The initial (maximum) temperature at which the algorithm starts.
            cooling_rate (float): The rate at which the temperature decreases after each iteration.
        """
        self.table = table  # The current state of the Sudoku puzzle.
        self.original = deepcopy(
            table
        )  # A copy of the original state to keep track of fixed numbers.
        self.min_temp = min_temp  # Minimum temperature for the annealing process.
        self.max_temp = max_temp  # Starting (maximum) temperature.
        self.cooling_rate = cooling_rate  # Rate at which the temperature decreases.
        self.actual_state = SingleSolution(
            table, original=self.original
        )  # The current solution state.
        self.best_state = self.actual_state  # The best solution state found so far.
        self.next_state = None  # Placeholder for the next state, used in the generation of new states.

    def run(self, process_id: int) -> tuple:
        """
        Executes the Simulated Annealing algorithm to find a solution for the Sudoku puzzle.

        Args:
            process_id (int): An identifier for the process, useful for debugging or logging.

        Returns:
            tuple: Contains the best solution found, its fitness, and additional data about the run (for analysis purposes).
        """
        self.actual_state.generate_solution()  # Initializes the actual state with a generated solution.
        temp = self.max_temp
        best_fitness = self.best_state.fitness()

        additional_info_data = (
            []
        )  # To store data for analysis, like temperature and fitness over iterations.

        iterations = 0
        while temp > self.min_temp:
            iterations += 1
            new_state = self.generate_nxt_state(self.actual_state)

            actual_energy = self.actual_state.fitness()
            new_energy = new_state.fitness()

            if random.random() < self.accept_prob(actual_energy, new_energy, temp):
                self.actual_state = new_state
                if new_energy < best_fitness:
                    best_fitness = new_energy
                    self.best_state = new_state

            additional_info_data.append((iterations, temp, best_fitness))

            if best_fitness == 0:
                print(f"Optimal solution found at iteration {iterations}.")
                break

            temp *= self.cooling_rate

        return self.best_state.table, best_fitness, additional_info_data

    def generate_nxt_state(self, actual_state: SingleSolution) -> SingleSolution:
        """
        Generates a new state by mutating the current solution.

        Args:
            actual_state (SingleSolution): The current solution state.

        Returns:
            SingleSolution: A new solution state after mutation.
        """
        new_state = SingleSolution(actual_state.table, self.original)
        new_state.mutate()
        return new_state

    @staticmethod
    def accept_prob(actual_energy: float, next_energy: float, temp: float) -> float:
        """
        Calculates the probability of accepting a new state, based on the energies of the current and new states and the current temperature.

        Args:
            actual_energy (float): The energy (number of conflicts) of the current state.
            next_energy (float): The energy of the new state.
            temp (float): The current temperature.

        Returns:
            float: The probability of accepting the new state. Higher probabilities are returned for better states.
        """
        if next_energy < actual_energy:
            return 1.0  # Always accept a better solution.
        # Accept worse solutions with a probability that decreases with the temperature and the solution's fitness difference.
        return np.exp((actual_energy - next_energy) / temp)
