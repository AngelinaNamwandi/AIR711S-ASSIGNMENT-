import random
import matplotlib.pyplot as plt

# PROBLEM REPRESENTATION
places = ['Dorado Park', 'Khomasdal', 'Katutura', 'Eros', 'Klein Windhoek']
distances_in_km = {
    ('Dorado Park', 'Dorado Park'): 0,
    ('Dorado Park', 'Khomasdal'): 7,
    ('Dorado Park', 'Katutura'): 20,
    ('Dorado Park', 'Eros'): 15,
    ('Dorado Park', 'Klein Windhoek'): 12,
    ('Khomasdal', 'Khomasdal'): 0,
    ('Khomasdal', 'Dorado Park'): 10,
    ('Khomasdal', 'Katutura'): 6,
    ('Khomasdal', 'Eros'): 14,
    ('Khomasdal', 'Klein Windhoek'): 18,
    ('Katutura', 'Katutura'): 0,
    ('Katutura', 'Dorado Park'): 20,
    ('Katutura', 'Khomasdal'): 6,
    ('Katutura', 'Eros'): 25,
    ('Katutura', 'Klein Windhoek'): 30,
    ('Eros', 'Eros'): 0,
    ('Eros', 'Dorado Park'): 15,
    ('Eros', 'Khomasdal'): 14,
    ('Eros', 'Katutura'): 25,
    ('Eros', 'Klein Windhoek'): 2,
    ('Klein Windhoek', 'Klein Windhoek'): 0,
    ('Klein Windhoek', 'Dorado Park'): 12,
    ('Klein Windhoek', 'Khomasdal'): 18,
    ('Klein Windhoek', 'Katutura'): 30,
    ('Klein Windhoek', 'Eros'): 2
}

# Function to calculate total distance of a path
def calculate_distance(path, distances_in_km):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances_in_km[(path[i], path[i + 1])]
    return total_distance

# Function to generate an initial random path
def TSP_hillclimb(places):
    path = places.copy()
    random.shuffle(path)
    return path

# Function to explore neighboring paths by swapping two random cities
def explore_neighbors(path):
    new_path = path.copy()
    i, j = random.sample(range(len(new_path)), 2)
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path

# The hill climb algorithm
def hill_climbing(places, distances_in_km):
    # Generate initial random path
    current_path = TSP_hillclimb(places)
    current_distance = calculate_distance(current_path, distances_in_km)

    while True:
        # Explore neighboring path
        neighbor_path = explore_neighbors(current_path)
        neighbor_distance = calculate_distance(neighbor_path, distances_in_km)

        # If neighbor is better, move to that path
        if neighbor_distance < current_distance:
            current_path = neighbor_path
            current_distance = neighbor_distance
        else:
            # No better neighbor found, return current solution
            return current_path, current_distance

# Function to plot the cities and routes
def plot_route(cities, path, title):
    # Extract x and y coordinates of each city
    x_coords = [city[0] for city in cities.values()]
    y_coords = [city[1] for city in cities.values()]

    # Plot cities
    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords, color='blue')
    for i, city in enumerate(cities.keys()):
        plt.text(x_coords[i], y_coords[i], city)

    # Plot routes
    for i in range(len(path) - 1):
        city1 = path[i]
        city2 = path[i + 1]
        plt.plot([cities[city1][0], cities[city2][0]], [cities[city1][1], cities[city2][1]], 'k-')

    # Connect last city with the first city to complete the loop
    city1 = path[-1]
    city2 = path[0]
    plt.plot([cities[city1][0], cities[city2][0]], [cities[city1][1], cities[city2][1]], 'k-')

    plt.title(title)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.show()

# Define city coordinates
cities_coordinates = {
    'Dorado Park': (0, 0),
    'Khomasdal': (2, 1),
    'Katutura': (3, 3),
    'Eros': (1, 2),
    'Klein Windhoek': (4, 0)
}

# Run hill climbing algorithm to find the routes and distances
initial_route, initial_distance = hill_climbing(places, distances_in_km)
intermediate_route, intermediate_distance = hill_climbing(places, distances_in_km)
final_route, final_distance = hill_climbing(places, distances_in_km)

# Output the routes and distances
print("Initial Route:", initial_route)
print("Initial Distance:", initial_distance, "km")

print("Intermediate Route:", intermediate_route)
print("Intermediate Distance:", intermediate_distance, "km")

print("Final Route:", final_route)
print("Final Distance:", final_distance, "km")

# Visualize the routes
plot_route(cities_coordinates, initial_route, 'Initial Route')
plot_route(cities_coordinates, intermediate_route, 'Intermediate Route')
plot_route(cities_coordinates, final_route, 'Final Route')
