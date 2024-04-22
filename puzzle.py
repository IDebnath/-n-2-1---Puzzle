import heapq
import time
import random

class Node:
    def __init__(self, state, parent, move, depth, cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth  # This is f(x)
        self.cost = cost    # This is C(x)

    def __lt__(self, other):
        return self.cost < other.cost

def calculate_heuristic(state, goal):
    count = 0
    n = len(state)
    for i in range(n):
        for j in range(n):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

# state expansion function
def get_neighbors(node):
    directions = [(-1, 0, 'up'), (1, 0, 'down'), (0, -1, 'left'), (0, 1, 'right')]
    neighbors = []
    state = node.state
    n = len(state)
    row, col = next((r, c) for r in range(n) for c in range(n) if state[r][c] == 0)

    for dr, dc, move in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < n and 0 <= new_col < n:
            new_state = [row[:] for row in state]  # create a copy of the state
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]  # swap
            neighbors.append((new_state, move))
    return neighbors

def least_cost_search(initial_state, goal_state):
    n = len(initial_state)
    initial_cost = calculate_heuristic(initial_state, goal_state)
    root = Node(state=initial_state, parent=None, move=None, depth=0, cost=initial_cost)
    frontier = []
    heapq.heappush(frontier, root)
    visited = set()

    while frontier:
        current_node = heapq.heappop(frontier)
        current_state = current_node.state

        if current_state == goal_state:
            return current_node  # Found the solution

        visited.add(tuple(tuple(row) for row in current_state))  # Track visited states

        for new_state, move in get_neighbors(current_node):
            if tuple(tuple(row) for row in new_state) not in visited:
                new_cost = calculate_heuristic(new_state, goal_state)
                new_node = Node(state=new_state, parent=current_node, move=move, depth=current_node.depth + 1, cost=current_node.depth + 1 + new_cost)
                heapq.heappush(frontier, new_node)

    return None  # If no solution is found

# Function to generate random initial states
# def generate_random_initial_states(num_states, n):
#     initial_states = []
#     base_list = list(range(1, n*n)) + [0]  # 1 to n*n-1 and 0 for the blank space

#     for _ in range(num_states):
#         random.shuffle(base_list)  # Randomly shuffle the numbers
#         # Split the list into n lists of n elements each to create an n x n grid
#         state = [base_list[i:i+n] for i in range(0, n*n, n)]
#         initial_states.append(state)
    
#     return initial_states

def print_solution(node):
    path = []
    while node:
        path.append((node.move, node.state))
        node = node.parent
    path.reverse()
    for move, state in path:
        print(f"Move: {move}")
        for row in state:
            print(row)
        print('-------')

# Define goal state and test
n = 4
goal_state = [list(range(1 + i * n, 1 + (i + 1) * n)) for i in range(n)]
goal_state[-1][-1] = 0  # set the last element as the blank

# Testing
# Example of initial configuration
initial_states = [
    [
    [1, 2, 3, 4], 
    [5, 6, 0, 8], 
    [9, 10, 7, 12], 
    [13, 14, 11, 15]
    ],  
    [
    [5, 2, 3, 4], 
    [1, 6, 0, 8], 
    [9, 10, 7, 11], 
    [13, 14, 15, 12]
    ],
    [
    [1, 6, 2, 4], 
    [5, 10, 3, 8], 
    [9, 13, 7, 11], 
    [14, 0, 15, 12]
    ],
    [
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 0], 
    [13, 14, 15, 12]
    ],
    [
    [1, 6, 2, 3], 
    [9, 5, 7, 4], 
    [13, 10, 11, 8], 
    [0, 14, 15, 12]
    ]
]


# Loop through each initial configuration to find the solution
for index, initial_state in enumerate(initial_states):
    try:
        start_time = time.time()
        solution_node = least_cost_search(initial_state, goal_state)
        end_time = time.time()

        if solution_node:
            print(f"Solution found for initial state {index} in {end_time - start_time:.2f} seconds")
            print_solution(solution_node)
        else:
            print(f"No solution found for initial state {index}.")
    except Exception as e:
        print(f"An error occurred with initial state {index}: {str(e)}")
