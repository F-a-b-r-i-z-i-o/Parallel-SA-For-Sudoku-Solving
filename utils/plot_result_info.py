import pandas as pd
import matplotlib.pyplot as plt
import os


def generate_and_save_plots(file_pattern, output_dir, start_index, end_index):
    """
    Generates and saves plots with a consistent gray background for each CSV file
    specified by a range of indices

    Parameters:
    - file_pattern (str): The pattern of the file path with a placeholder for the index.
    - output_dir (str): Directory to save the generated plots.
    - start_index (int): Starting index of the files.
    - end_index (int): Ending index of the files.
    """
    # Ensure the directory for plots exists
    os.makedirs(output_dir, exist_ok=True)

    plt.rcParams["axes.facecolor"] = "lightgray"
    plt.rcParams["figure.facecolor"] = "lightgray"

    for i in range(start_index, end_index + 1):
        file_path = file_pattern.format(i)
        df = pd.read_csv(file_path)

        fig, ax1 = plt.subplots(figsize=(10, 6))

        # Plot Best Fitness with a slightly thicker line
        (line1,) = ax1.plot(
            df["Best Fitness"],
            df["Iteration"],
            label="Best Fitness",
            color="C1",
            linewidth=1.5,
        )
        ax1.set_xlabel("Best Fitness", color="black")
        ax1.set_ylabel("Iteration", color="black")
        ax1.tick_params(axis="x", colors="black")
        ax1.tick_params(axis="y", colors="black")

        # Create a twin Axes sharing the y-axis for Temperature
        ax2 = ax1.twiny()
        (line2,) = ax2.plot(
            df["Temperature"],
            df["Iteration"],
            label="Temperature",
            color="C0",
            linestyle="--",
            linewidth=1.5,
        )
        ax2.set_xlabel("Temperature", color="black")
        ax2.tick_params(axis="x", colors="black")

        # Set all axis labels and title colors to black
        ax1.xaxis.label.set_color("black")
        ax1.yaxis.label.set_color("black")
        ax2.xaxis.label.set_color("black")
        ax1.title.set_color("black")

        # Improve layout and title to enhance clarity
        ax1.set_title(f"File {i} - Best Fitness and Temperature over Iterations")
        ax1.grid(True)
        ax1.figure.tight_layout()

        # Set the legend inside the plot
        ax1.legend(
            loc="upper right", frameon=True, facecolor="white", edgecolor="black"
        )
        ax2.legend(
            loc="upper right",
            frameon=True,
            facecolor="white",
            edgecolor="black",
            bbox_to_anchor=(1, 0.9),
        )

        plot_filename = f"{output_dir}/additional_info_plot_{i}.png"
        plt.savefig(plot_filename)
        plt.close(fig)

        print(f"Plot saved as {plot_filename}")


if __name__ == "__main__":
    generate_and_save_plots(
        "../SOLVER/additional_info/additional_info_{}.csv", "../plots", 0, 100
    )
