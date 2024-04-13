from copy import deepcopy
from random import shuffle, sample, randint

# Constants for the size of the sudoku table and the smaller 3x3 boxes.
TABLE_SIZE = 9
BOX_SIZE = 3


class SingleSolution:
    """
    This class represents a single solution for a Sudoku puzzle.
    It includes methods for generating a solution, mutating a solution,
    calculating the solution's fitness, and finding candidates for each cell.
    """

    def __init__(
        self, table: list[list[int]], original: list[list[int]]
    ) -> list[list[int]]:
        """
        Initializes a new instance of the SingleSolution class.

        Args:
            table (list of list of int): The current state of the Sudoku puzzle.
            original (list of list of int): The original Sudoku puzzle with some cells filled and others empty.
        """
        self.table = deepcopy(
            table
        )  # The current state of the puzzle, which can be mutated.
        self.original_table = original  # The original puzzle state, used to check which cells should not be changed.

    def generate_solution(self) -> None:
        """
        Fills empty cells in each 3x3 box of the Sudoku puzzle with random numbers that follow Sudoku rules.
        This method modifies the puzzle state in place.
        """
        for row_index in range(0, TABLE_SIZE, BOX_SIZE):
            for col_index in range(0, TABLE_SIZE, BOX_SIZE):

                # Calculate the starting row and column for the current box.
                row_offset = (row_index // BOX_SIZE) * BOX_SIZE
                col_offset = (col_index // BOX_SIZE) * BOX_SIZE

                nums = [n for n in range(1, TABLE_SIZE + 1)]

                # Remove numbers already present in the current box from the list.
                for i in range(BOX_SIZE):
                    for j in range(BOX_SIZE):
                        if self.original_table[row_offset + i][col_offset + j] != 0:
                            nums.remove(
                                self.original_table[row_offset + i][col_offset + j]
                            )

                shuffle(nums)  # Shuffle the remaining numbers to randomize their order.

                # Fill empty cells in the box with the shuffled numbers.
                for i in range(BOX_SIZE):
                    for j in range(BOX_SIZE):
                        if self.original_table[row_offset + i][col_offset + j] == 0:
                            self.table[row_offset + i][col_offset + j] = nums.pop()

    def mutate(self) -> None:
        """
        Mutates the solution by swapping two numbers within a single 3x3 box.
        This method modifies the puzzle state in place.
        """
        # Randomly select a 3x3 box.
        row_offset = (randint(0, TABLE_SIZE - 1) // BOX_SIZE) * BOX_SIZE
        col_offset = (randint(0, TABLE_SIZE - 1) // BOX_SIZE) * BOX_SIZE

        indexes = (
            []
        )  # List to hold the positions of mutable (non-original) cells within the box.

        # Identify mutable cells within the selected box.
        for i in range(BOX_SIZE):
            for j in range(BOX_SIZE):
                if self.original_table[row_offset + i][col_offset + j] == 0:
                    indexes.append([row_offset + i, col_offset + j])

        # Randomly select two cells to swap.
        pair1, pair2 = sample(indexes, 2)

        # Perform the swap.
        self.table[pair1[0]][pair1[1]], self.table[pair2[0]][pair2[1]] = (
            self.table[pair2[0]][pair2[1]],
            self.table[pair1[0]][pair1[1]],
        )

    def fitness(self) -> int:
        """
        Calculates the fitness of the solution based on the number of duplicate numbers in each row and column.

        Returns:
            int: The fitness of the solution, with lower numbers indicating a better fit (less conflict).
        """
        penalty = 0

        # Calculate row conflicts.
        for row_index in range(TABLE_SIZE):
            penalty += len(self.table[row_index]) - len(set(self.table[row_index]))

        # Calculate column conflicts.
        transposed_table = list(zip(*self.table))
        for row_index in range(TABLE_SIZE):
            penalty += len(transposed_table[row_index]) - len(
                set(transposed_table[row_index])
            )

        return penalty

    def find_candidates(self) -> list[list[set]]:
        """
        Finds candidate numbers for each empty cell in the puzzle based on Sudoku rules.

        Returns:
            list of list of set: A matrix where each cell contains a set of possible numbers that could fit based on the current state of the puzzle.
        """
        candidates = [
            [set(range(1, TABLE_SIZE + 1)) for _ in range(TABLE_SIZE)]
            for _ in range(TABLE_SIZE)
        ]
        for i in range(TABLE_SIZE):
            for j in range(TABLE_SIZE):
                if self.table[i][j] != 0:
                    candidates[i][
                        j
                    ] = set()  # Empty the set if the cell is already filled.
                    continue
                # Remove numbers that are already present in the same row, column, and box.
                for k in range(TABLE_SIZE):
                    candidates[i][j].discard(self.table[i][k])
                    candidates[i][j].discard(self.table[k][j])
                    candidates[i][j].discard(
                        self.table[3 * (i // 3) + k // 3][3 * (j // 3) + k % 3]
                    )
        return candidates

    def __str__(self) -> str:
        """
        Provides a string representation of the current state of the Sudoku puzzle.

        Returns:
            str: The current state of the puzzle formatted as a grid.
        """
        return "\n".join(["\t".join([str(cell) for cell in row]) for row in self.table])
