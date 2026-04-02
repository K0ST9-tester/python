import random

from agent import Agent
from math import pi, cos, sin, sqrt


class Simulation:
    def __init__(self, width, height, num_agents, mobility, infection_radius, infection_probability, incubation_time, recovery_time, mortality_probability):
        self.width = width
        self.height = height
        self.num_agents = num_agents
        self.infection_radius = infection_radius
        self.infection_probability = infection_probability
        self.incubation_time = incubation_time
        self.recovery_time = recovery_time
        self.mortality_probability = mortality_probability
        self.mobility = mobility
        self.current_step = 0
        self.death_count = 0
        self.states = ["susceptible", "infected", "immune", "dead"]
        self.history = {state: [] for state in self.states}
        self.position_history = []
        self.agents = self.generate_agents()
        self.update_history()
        self.save_positions()
    

    def update_history(self):
        """
            Record the number of agents in each state at the current step.

            Used for plotting simulation statistics over time.
        """

        state_counts = {state: 0 for state in self.states}
        for agent in self.agents:
            state_counts[agent.state] += 1
        for state in self.states:
            self.history[state].append(state_counts[state])

    
    def save_positions(self):
        """
            Save current positions and states of all agents.

            Stores a snapshot of:
                - x coordinate
                - y coordinate
                - agent state

            This data is used for animation and visualization.
        """

        snapshot = []
        for agent in self.agents:
            snapshot.append((agent.x, agent.y, agent.state))
        self.position_history.append(snapshot)


    def generate_agents(self):
        """
            Create and initialize agents in the simulation.

            - Agents are placed at random positions within the simulation area.
            - Each agent is assigned a random mobility value.
            - A small fraction (~1%) of agents is initially infected.

            Returns:
                list: List of initialized Agent objects.
        """

        agents = []
        for i in range(self.num_agents):
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            mobility = random.uniform(0, 2 * self.mobility)
            agent = Agent(x, y, mobility)
            agents.append(agent)

        used_indices = set()
        maximum_infected = max(1, int(self.num_agents * 0.01))   # Ensures at least one infected agent
        for i in range(maximum_infected):
            number = random.randint(0, self.num_agents - 1)
            while number in used_indices:
                number = random.randint(0, self.num_agents - 1)
            used_indices.add(number)
            agents[number].state = "infected"
            agents[number].time_since_infection = 0
            agents[number].infected_by = None

        return agents


    def move_agents(self):
        """
            Move all agents randomly within the simulation space.

            - Dead agents do not move.
            - Infected agents stop moving after incubation period.
            - Positions are constrained within simulation boundaries.
        """

        for agent in self.agents:
            if agent.state == "dead":
                continue

            if agent.state == "infected":
                if agent.time_since_infection >= self.incubation_time:
                    continue
                else:
                    agent.time_since_infection += 1


            r = random.uniform(0, 2 * self.mobility)
            theta = random.uniform(0, 2 * pi)
            dx = r * cos(theta)
            dy = r * sin(theta)

            agent.x = max(0, min(agent.x + dx, self.width))
            agent.y = max(0, min(agent.y + dy, self.height))
    

    def handle_infections(self):
        """
            Process infection spread between agents.

            For each infected agent:
                - Check nearby susceptible agents.
                - Calculate distance-based infection probability.
                - Infect agents probabilistically.

            Uses delayed update to avoid modifying state during iteration.
        """ 

        agents_to_infect = set()

        for infected_agent in self.agents:
            if infected_agent.state == "infected" and infected_agent.time_since_infection < self.incubation_time:

                for other_agent in self.agents:
                    if other_agent.state == "susceptible" and other_agent != infected_agent:
                        dx = other_agent.x - infected_agent.x
                        dy = other_agent.y - infected_agent.y
                        distance_sq = dx ** 2 + dy ** 2

                        if distance_sq < self.infection_radius ** 2:
                            probability_effective = self.infection_probability / 100
                            probability_effective = max(0, probability_effective)
                            if random.random() <= probability_effective:
                                agents_to_infect.add((other_agent, infected_agent))
        
        for agent, source in agents_to_infect:
            agent.state = "infected"
            agent.time_since_infection = 0
            agent.infected_by = source


    def update_states(self):
        """
            Update health states of infected agents.

            - Increase infection time.
            - After recovery_time:
                → agent becomes immune OR dies (based on probability).
        """

        for agent in self.agents:
            if agent.state == "infected":
                agent.time_since_infection += 1

                if agent.time_since_infection >= self.recovery_time:
                    if random.random() <= (self.mortality_probability / 100):
                        agent.state = "dead"
                        self.death_count += 1
                    else:
                        agent.state = "immune"
    

    def compute_R0(self):
        """
            Compute the basic reproduction number (R0).

            R0 is defined as the average number of secondary infections
            caused by each infected agent.

            Returns:
                float: Estimated R0 value.
        """

        infection_counts = {}
        infected_states = ["infected", "immune", "dead"]

        for agent in self.agents:
            if agent.infected_by is not None:
                infector = agent.infected_by
                infection_counts[infector] = infection_counts.get(infector, 0) + 1
            if agent.state in infected_states:
                if agent not in infection_counts:
                    infection_counts[agent] = 0
        

        if len(infection_counts) == 0:
            return 0

        R0 = sum(infection_counts.values()) / len(infection_counts)
    
        return R0
            

    def step(self):
        """
            Perform a single simulation step.

            Order of operations:
                1. Move agents
                2. Handle infections
                3. Update states
                4. Record statistics
        """

        self.current_step += 1
        self.move_agents()
        self.handle_infections()
        self.update_states()
        self.update_history()
        self.save_positions()
