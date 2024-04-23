# Sliding Puzzle Solver
## This project presents a Python implementation of the sliding puzzle solver, specifically designed for solving the n x n sliding puzzle (also known as the n^2-1 puzzle, such as the 15-puzzle). The solver utilizes the Manhattan Distance heuristic to efficiently find the solution by minimizing the number of moves required to reach the goal state.

## Features
* Manhattan Distance Heuristic: Uses the sum of the absolute values of the horizontal and vertical distances of each tile from its goal position to prioritize moves.
* Priority Queue (Min-Heap): Ensures that the state with the lowest heuristic cost is expanded first, improving the efficiency of the search.
* Solvability Check: Ensures that only solvable puzzles are processed, preventing unnecessary computation.

## Installation
No installation is necessary, as the script runs in a Python environment. Ensure you have Python installed on your machine. Python 3.8 or higher is recommended.

## Usage
To run the puzzle solver, simply execute the script from the command line:

## bash
Copy code
`python sliding_puzzle_solver.py`
Ensure that the script puzzle_solver.py is in your current directory.

## Configuration
The script uses a default puzzle size of 4x4 (15-puzzle), but this can be adjusted within the code to accommodate different puzzle sizes. Modify the n variable in the generate_random_initial_states function to change the puzzle size.

## Contributing
Contributions to the project are welcome. Please fork the repository and submit a pull request with your enhancements.
