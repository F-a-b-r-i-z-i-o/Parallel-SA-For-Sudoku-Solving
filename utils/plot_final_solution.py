import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np


def generate_and_save_matrix_images(file_pattern, output_dir, start_index, end_index):
    """
    Generates and saves images of matrices for each CSV file specified by a range of indices.

    Parameters:
    - file_pattern (str): The pattern of the file path with a placeholder for the index.
    - output_dir (str): Directory to save the generated images.
    - start_index (int): Starting index of the files.
    - end_index (int): Ending index of the files.
    """
    # Ensure the directory for images exists
    os.makedirs(output_dir, exist_ok=True)

    # Define the background and text colors
    background_color = "#f5f5f5"  # Soft gray
    text_color = "#000000"  # Black for good contrast

    for i in range(start_index, end_index):
        file_path = file_pattern.format(i)
        matrix = pd.read_csv(file_path, header=None).values

        # Create a figure with specific background color
        fig, ax = plt.subplots(figsize=(8, 8))
        fig.patch.set_facecolor(
            background_color
        )  # Set the background color for the entire figure

        # Set the axes' background color
        ax.set_facecolor(background_color)

        # Annotate the matrix with the numerical values
        for (j, k), value in np.ndenumerate(matrix):
            ax.text(
                k,
                j,
                int(value),
                ha="center",
                va="center",
                color=text_color,
                fontsize=12,
            )

        # Set the limits and remove the axes
        ax.set_xlim(-0.5, len(matrix[0]) - 0.5)
        ax.set_ylim(-0.5, len(matrix) - 0.5)
        plt.axis("off")

        # Invert the y-axis to have the origin at the top left corner as in a matrix
        ax.invert_yaxis()

        # Save the matrix as an image ensuring background color is saved
        image_filename = f"{output_dir}/matrix_image_{i}.png"
        plt.savefig(
            image_filename,
            bbox_inches="tight",
            pad_inches=0.1,
            facecolor=fig.get_facecolor(),
        )
        plt.close(fig)

        print(f"Matrix image saved as {image_filename}")


# Usage example
generate_and_save_matrix_images(
    "../SOLVER/final_solutions/solution_{}.csv", "../matrix_images", 0, 100
)
