from collections import deque
import matplotlib.pyplot as plt
import numpy as np

# Define the grid size
GRID_SIZE = (10, 10)  # (rows, columns)

# Initialize the grid
grid = np.zeros(GRID_SIZE, dtype=int)

# Ask the user to enter the obstacle positions
num_obstacles = int(input("Enter the number of obstacles: "))
for i in range(num_obstacles):
    row = int(input(f"Enter the row for obstacle {i+1}: "))
    col = int(input(f"Enter the column for obstacle {i+1}: "))
    grid[row, col] = 1

# Define the robot's starting position
start_row = int(input("Enter the starting row: "))
start_col = int(input("Enter the starting column: "))

# Define the target cell (e.g., charging station)
target_row = int(input("Enter the target row: "))
target_col = int(input("Enter the target column: "))

# Define possible actions
ACTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

# Cost function
def cost_function(action):
    return 1

def manhattan_distance(current, target, grid):
    curr_row, curr_col = current
    target_row, target_col = target
    return abs(curr_row - target_row) + abs(curr_col - target_col)

def obstacle_aware_heuristic(current, target, grid):
    curr_row, curr_col = current
    target_row, target_col = target
    penalty = 0

    # Check obstacles along the horizontal path
    for col in range(min(curr_col, target_col), max(curr_col, target_col) + 1):
        if grid[curr_row, col] == 1:
            penalty += 1

    # Check obstacles along the vertical path
    for row in range(min(curr_row, target_row), max(curr_row, target_row) + 1):
        if grid[row, curr_col] == 1:
            penalty += 1

    return manhattan_distance(current, target, grid) + penalty

def a_star_search(grid, start, target, heuristic):
    rows, cols = grid.shape
    visited = set()
    queue = deque([(start, 0, heuristic(start, target, grid), [start])])  # (position, cost, heuristic, path)

    while queue:
        current, cost, _, path = queue.popleft()

        if current == target:
            return cost, path  # Reached the target, return the cost and the path

        visited.add(current)

        for action in ACTIONS:
            new_row, new_col = current[0] + action[0], current[1] + action[1]

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and grid[new_row, new_col] == 0
                and (new_row, new_col) not in visited
            ):
                new_cost = cost + cost_function(action)
                new_heuristic = heuristic((new_row, new_col), target, grid)
                new_path = path + [(new_row, new_col)]
                queue.append(((new_row, new_col), new_cost, new_heuristic, new_path))

    return float('inf'), []  # No path found

# Test the implementation
start = (start_row, start_col)
target = (target_row, target_col)

# Test with Manhattan distance heuristic
manhattan_cost, manhattan_path = a_star_search(grid, start, target, manhattan_distance)
print(f"Cost with Manhattan distance heuristic: {manhattan_cost}")
print("Path with Manhattan distance heuristic:")
for step in manhattan_path:
    print(step)

# Test with obstacle-aware heuristic
obstacle_aware_cost, obstacle_aware_path = a_star_search(grid, start, target, obstacle_aware_heuristic)
print(f"Cost with obstacle-aware heuristic: {obstacle_aware_cost}")
print("Path with obstacle-aware heuristic:")
for step in obstacle_aware_path:
    print(step)

def visualize_path(grid, path):
    if not path:
        print("No path found.")
        return
    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap='binary')
    for row, col in path:
        plt.scatter(col, row, c='r', marker='o')
    plt.show()

# Visualize the optimal path
visualize_path(grid, obstacle_aware_path)