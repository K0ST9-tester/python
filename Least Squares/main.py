import matplotlib.pyplot as plt
import numpy as np


def load_data(file):
    with open(file, "rt") as f:
        x, y = [], []

        lines = f.readlines()

        for line in lines[2:]:
            curr_line = line.split()
            x.append(float(curr_line[1]))
            y.append(float(curr_line[2]))
        
        return x, y


def compute_coefficients(x, y):
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    num_of_points = len(x)
    denominator = num_of_points * sum_x2 - (sum_x) ** 2

    a = (num_of_points * sum_xy - sum_x * sum_y) / denominator
    b = (sum_y - a * sum_x) / num_of_points

    sum_r2 = sum((yi - (a*xi + b))**2 for xi, yi in zip(x, y))

    sigma2 = sum_r2 / (num_of_points - 2)
    error_a = ((num_of_points * sigma2) / denominator) ** 0.5
    error_b = ((sigma2 * sum_x2) / denominator) ** 0.5


    return a, b, error_a, error_b


def plot_results(x, y, a, b, x_line, y_line, error_a, error_b):
    plt.scatter(x, y, color = "blue", label = "Data")
    plt.plot(x_line, y_line, "r", label = "Fit")

    plt.text(
        0.05, 0.95,
        f"a = {a:.3f} ± {error_a:.3f}\nb = {b:.3f} ± {error_b:.3f}",
        transform = plt.gca().transAxes,
        verticalalignment = 'top',
        bbox = dict(facecolor = "white", alpha = 0.8, edgecolor = "gray")
    )

    plt.xlabel("Mass [g]")
    plt.ylabel("Deflection [mm]")
    plt.title("Least Squares Fit")
    plt.legend()
    plt.grid()

    plt.show()


def main():
    initial_file = "data_RMS.txt"
    x, y = load_data(initial_file)
    a, b, error_a, error_b = compute_coefficients(x, y)
    x_line = np.linspace(min(x), max(x), 100)
    y_line = a * x_line + b
    plot_results(x, y, a, b, x_line, y_line, error_a, error_b)


if __name__ == "__main__":
    main()