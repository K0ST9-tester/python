'''
    Author: Kostiantyn Halanets
    Date: 2026-03-30
'''


from experiment import run_experiment
from simulation import Simulation
from visualization import animate, plot_history, plot_multi_experiments


defaults = {
    "width": 1500,
    "height": 1500,
    "num_agents": 500,
    "V": 40,
    "infection_radius": 20,
    "p": 70,
    "t1": 35,
    "t2": 80,
    "m": 30,
    "steps": 250
}


def validation_data(number_of_exp = None, data = None, min_val = None, max_val = None, type_func = None):
    validated_data = []

    while True:
        try:
            if number_of_exp is None:
                validated_data = type_func(input(data))

                if min_val is not None and validated_data < min_val:
                    raise ValueError(f"Please write value greater than or equal to {min_val}")
                elif max_val is not None and validated_data > max_val:
                    raise ValueError(f"Please write value less than or equal to {max_val}")
            else:
                validated_data = [type_func(value.strip()) for value in input(data).split(",")]

                if len(validated_data) != number_of_exp:
                    raise ValueError("Number of elements should be equal to number of experiments")

                for element in validated_data:
                    if min_val is not None and element < min_val:
                        raise ValueError(f"Please write value greater than or equal to {min_val}")
                    elif max_val is not None and element > max_val:
                        raise ValueError(f"Please write value less than or equal to {max_val}")
            break
    
        except ValueError as e:
            print(e)
            continue

    return validated_data


def run_single_simulation(defaults):
    sim = Simulation(
        width = defaults["width"],
        height = defaults["height"],
        num_agents = defaults["num_agents"],
        mobility = defaults["V"],
        infection_radius = defaults["infection_radius"],
        infection_probability = defaults["p"],
        incubation_time = defaults["t1"],
        recovery_time = defaults["t2"],
        mortality_probability = defaults["m"]
    )

    for _ in range(defaults["steps"]):
        sim.step()
    
    animate(sim)
    plot_history(sim)


def run_multiple_experiments(defaults):
    num_of_exp = validation_data(None, "Enter number of experiments from 1 to 9: ", 1, 9, int)
    V_base = validation_data(num_of_exp, f"Enter {num_of_exp} mobility values separated by comma (e.g. 10,20,30): ", 0, None, float)
    p_base = validation_data(num_of_exp, f"Enter {num_of_exp} infection_probability values from 0-100 (comma separated): ", 0, 100, float)
    t1_base = validation_data(num_of_exp, f"Enter {num_of_exp} incubation_time values (comma separated): ", 0, None, int)
    t2_base = validation_data(num_of_exp, f"Enter {num_of_exp} recovery_time values (comma separated): ", 0, None, int)
    m_base = validation_data(num_of_exp, f"Enter {num_of_exp} mortality_probability values from 0-100 (comma separated): ", 0, 100, float)


    results = {
        "V": [],
        "p": [],
        "t1": [],
        "t2": [],
        "m": []
    }

    parameter_values = {
        "V": V_base,
        "p": p_base,
        "t1": t1_base,
        "t2": t2_base,
        "m": m_base
    }

    results["V"].append(run_experiment("V", V_base, defaults))
    results["p"].append(run_experiment("p", p_base, defaults))
    results["t1"].append(run_experiment("t1", t1_base, defaults))
    results["t2"].append(run_experiment("t2", t2_base, defaults))
    results["m"].append(run_experiment("m", m_base, defaults))

    plot_multi_experiments(results, parameter_values)


def main():
    mode = input("Choose mode: (1) single simulation, (2) experiments: ")

    while mode != "1" and mode != "2":
        print("Invalid choice... For real? You're given two options. It's not a rocket science...")
        mode = input("Choose mode: (1) single simulation, (2) experiments: ")

    if mode == "1":
        run_single_simulation(defaults)
    else:
        run_multiple_experiments(defaults)


if __name__ == "__main__":
    main()