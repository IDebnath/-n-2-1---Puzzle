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

# Manhattan Distance
def calculate_manhattan_distance(state, goal):
    n = len(state)
    distance = 0
    goal_positions = {}
    # Create a dictionary for goal positions for quick lookup
    for i in range(n):
        for j in range(n):
            goal_positions[goal[i][j]] = (i, j)
    
    for i in range(n):
        for j in range(n):
            if state[i][j] != 0:
                goal_i, goal_j = goal_positions[state[i][j]]
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance


# manhattan implementation function
def least_cost_search(initial_state, goal_state):
    n = len(initial_state)
    initial_cost = calculate_manhattan_distance(initial_state, goal_state)
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
                new_cost = calculate_manhattan_distance(new_state, goal_state)
                new_node = Node(state=new_state, parent=current_node, move=move, depth=current_node.depth + 1, cost=current_node.depth + 1 + new_cost)
                heapq.heappush(frontier, new_node)       
    return None  # If no solution is found


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


# Function to generate random initial states
def generate_random_initial_states(num_states, n):
    initial_states = []
    base_list = list(range(1, n*n)) + [0]  # 1 to n*n-1 and 0 for the blank space

    for _ in range(num_states):
        random.shuffle(base_list)  # Randomly shuffle the numbers
        # Split the list into n lists of n elements each to create an n x n grid
        state = [base_list[i:i+n] for i in range(0, n*n, n)]
        initial_states.append(state)
    return initial_states

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

initial_states = generate_random_initial_states(5, n)  
print(f"Generated {len(initial_states)} initial states.")



"""Solvability check for randomly generated initial states"""
def count_inversions(state):
    """Count the number of inversions in a given state."""
    # Flatten the list excluding the blank (0)
    flat_list = [num for row in state for num in row if num != 0]
    num_inversions = 0
    for i in range(len(flat_list)):
        for j in range(i + 1, len(flat_list)):
            if flat_list[i] > flat_list[j]:
                num_inversions += 1
    return num_inversions

def find_blank_row(state):
    """Find the row index of the blank (0), counting from the bottom of the grid."""
    n = len(state)
    for i in range(n):
        if 0 in state[i]:
            # Row counting from the bottom
            return n - i

def is_solvable(state):
    """Determine if a given n x n puzzle configuration is solvable."""
    n = len(state)
    num_inversions = count_inversions(state)
    if n % 2 != 0:
        # Odd grid size
        return num_inversions % 2 == 0
    else:
        # Even grid size
        blank_row = find_blank_row(state)
        if blank_row % 2 == 0:
            return num_inversions % 2 != 0
        else:
            return num_inversions % 2 == 0

solvable_states = [state for state in initial_states if is_solvable(state)]
print(f"{len(solvable_states)} states are solvable and will be tested.")



# Testing loop for solvable states
for index, initial_state in enumerate(solvable_states):
    print(f"Testing state {index + 1}")
    start_time = time.time()
    solution_node = least_cost_search(initial_state, goal_state)
    end_time = time.time()

    if solution_node:
        print(f"Solution found for initial state {index + 1} in {end_time - start_time:.2f} seconds")
        print_solution(solution_node)
    else:
        print(f"No solution found for initial state {index + 1}.")
