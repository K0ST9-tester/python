class Agent:
    def __init__(self, x, y, mobility, state = "susceptible", time_since_infection = 0, infected_by = None):
        self.x = x
        self.y = y
        self.mobility = mobility
        self.state = state
        self.time_since_infection = time_since_infection
        self.infected_by = infected_by