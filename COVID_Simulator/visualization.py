import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


color_map = {
    "susceptible": "blue",
    "infected": "orange",
    "immune" : "purple",
    "dead": "black"
}


names = {
    "V": "Mobility",
    "p": "Infection Probability",
    "t1": "Incubation Time",
    "t2": "Recovery Time",
    "m": "Mortality"
}


def animate(simulation):
    fig, ax = plt.subplots()

    ax.set_aspect("equal")

    ax.set_xlim(0, simulation.width)
    ax.set_ylim(0, simulation.height)
    ax.set_title("Disease Spread Simulation")

    scatter = ax.scatter([], [], s = 10)

    def update(frame_index):
        snapshot = simulation.position_history[frame_index]
        x_vals, y_vals, colors = [], [], []

        for x, y, state in snapshot:
            x_vals.append(x)
            y_vals.append(y)
            colors.append(color_map[state])
        
        scatter.set_offsets(list(zip(x_vals, y_vals)))
        scatter.set_color(colors)
        ax.set_title(f"Step: {frame_index}")

        return scatter,

    anim = FuncAnimation(
        fig,
        update,
        len(simulation.position_history),
        interval = 50,
        repeat = False
    )

    plt.show()

    return anim


def plot_history(simulation):
    plt.figure()

    for state, values in simulation.history.items():
        plt.plot(values, label = state)
    
    plt.xlabel("Time [frames]")
    plt.ylabel("Number of agents")
    plt.title("COVID-19")
    plt.legend()
    plt.grid()
    plt.show()


def plot_multi_experiments(results, parameter_values):
    fig, axes = plt.subplots(2, 3, figsize = (14, 8))
    parameters = ["V", "p", "t1", "t2", "m"]

    for idx, param in enumerate(parameters):
        row = idx // 3
        col = idx % 3
        ax = axes[row][col]

        experiments = results[param]
        x_values = parameter_values[param]

        for exp_index, y_values in enumerate(experiments):
            if len(x_values) != len(y_values):
                continue
            ax.plot(x_values, y_values, label = f"Experiment {exp_index + 1}")
        
        ax.set_title(f"{names[param]} vs R0")
        ax.set_xlabel(param)
        ax.set_ylabel("R0")
        ax.grid()
        ax.legend()
    
    axes[1][2].axis("off")
    fig.suptitle("R0 Sensitivity Analysis", fontsize = 14)

    plt.tight_layout()   # Plots will not overlap with each other
    plt.show()
