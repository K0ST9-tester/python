# COVID Simulator

## Problem Description

An agent-based simulation of infectious disease spread in a 2D environment, inspired by the dynamics of COVID-19 transmission. The project visualizes how a disease propagates through a moving population and analyzes the impact of parameters such as mobility, infection probability, incubation time, mortality, and population density.

The simulation is written in Python using an object-oriented design and provides both:

* **Animated visualization** of the population over time

* **Statistical plots** showing epidemic dynamics


## Features

* Agent-based epidemic 
* simulation
* Random movement in 2D space
* Multiple agent states:
    * Susceptible
    * Ill
    * Immune
    * Dead
* Infection spread based on distance and probability
* Isolation after symptom development
* Recovery or death after illness duration
* Animated simulation using Matplotlib
* Epidemic statistics visualization:
    * Total cases
    * Active cases
    * Deaths
* Easily configurable simulation parameters
* Modular and extensible object-oriented architecture


## Simulation rules
Each agent represents a single human in a 2D environment.

### Movement
At every simulation step:
* Each agent moves randomly
* Movement distance is selected from the range:

    ```[0, 2 x V]```

where:
* ```V``` = mobility parameter of the agent


### Infection

A susceptible agent becomes infected when:

* It is within distance ```d``` of an ill agent
* Infection occurs with probability ```p```


### Disease Progression

After infection:

1. Incubation period (```t1```)
    * The infected agent becomes isolated
    * Mobility is reduced to 0
2. Illness duration (```t2```)
    * The agent either:
        * Recovers and becomes immune
        * Dies with probability ```m```


## Technologies Used

* Python
* ```matplotlib.pyplot```
* ```matplotlib.animation```
* ```random```
* ```math```


## Configurable Parameters

| Parameter | Description |
|-----------|-------------|
| `V` | Agent mobility |
| `p` | Infection probability |
| `d` | Infection distance |
| `t1` | Incubation time before isolation |
| `t2` | Disease duration before recovery/death |
| `m` | Mortality rate |
| `population_size` | Number of agents in the simulation |
| `density` | Average population density |


## Visualization
The simulator provides:

### Population Animation
Agents are displayed as moving points in 2D space.

Suggested color scheme:

Blue - susceptible
Yellow - infected
Green - immune
Red - dead


## R<sub>0<sub> Estimation
The project investigates the basic reproduction number:

R<sub>0<sub>

which represents the average number of susceptible individuals infected by one ill person.

The simulation allows studying how:

* Social distancing
* Mobility reduction
* Population density
* Infection probability

affect epidemic spread and the value of <code>R<sub>0<sub></code>


## Inspiration
This project was inspired by epidemic spread simulations and public visualizations such as the Washington Post COVID-19 simulation article. 