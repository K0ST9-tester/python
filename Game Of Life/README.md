# Game of Life

This project is an implementation of **Conway's Game of Life**, this project is a zero-player simulation in which a 2D grid of "living" or "dead" cells evolves based on simple rules.

The simulation is written using **Matplotlib** for visualization.


## RULES

Each cell in the grid can be either **alive** or **dead**, and its state in the next generation depends on its neighbors:

For **Survival**:
    • A live cell with 2 or 3 live neighbors survives to the next generation

For **Death**:
    • A live cell with fewer than 2 neighbors dies (Underpopulation)
    • A live cell with more than 3 neighbors dies (Overcrowding)

For **Birth**:
    • A dead cell with exactly 3 live neighbors becomes a live cell


## REQUIREMENTS

- Python 3.x
- numpy
- matplotlib