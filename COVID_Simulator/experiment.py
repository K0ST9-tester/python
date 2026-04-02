from simulation import Simulation


def run_experiment(parameter_name, parameter_values, defaults):
    R0_results = []

    for value in parameter_values:
        params = defaults.copy()
        params[parameter_name] = value

        sim = Simulation(
            width = params["width"],
            height = params["height"],
            num_agents = params["num_agents"],
            mobility = params["V"],
            infection_radius = params["infection_radius"],
            infection_probability = params["p"],
            incubation_time = params["t1"],
            recovery_time = params["t2"],
            mortality_probability = params["m"]
        )

        for _ in range(params["steps"]):
            sim.step()
        
        R0 = sim.compute_R0()
        R0_results.append(R0)

    return R0_results
