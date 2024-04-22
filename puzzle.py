import heapq
import time

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
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0 and state[i][j] != goal[i*len(state) + j]:
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

def least_cost_search(initial_state):
    initial_cost = calculate_heuristic(initial_state)
    root = Node(state=initial_state, parent=None, move=None, depth=0, cost=initial_cost)
    frontier = []
    heapq.heappush(frontier, root)
    visited = set()

    while frontier:
        current_node = heapq.heappop(frontier)
        current_state = current_node.state

        if current_state == sorted(current_state, key=lambda x: (x != 0, x)):
            return current_node  # Found the solution

        # Expand the node (implement moving the blank space)
        # Add new states to the frontier with updated costs

    return None  # If no solution is found



def print_solution(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    for state in path:
        for row in state:
            print(row)
        print('-------')


# Testing
# Example of initial configuration
initial_states = [
    [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 12], [13, 14, 11, 15]],
    # Add more test states here
]

for state in initial_states:
    start_time = time.time()
    solution_node = least_cost_search(state)
    end_time = time.time()
    # Output the path and time
    if solution_node:
        print("Solution found in {:.2f} seconds".format(end_time - start_time))
        # Backtrack and print path if required