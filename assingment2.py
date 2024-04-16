import random

# PROBLEM REPRESENTATION
places = ['Dorado Park', 'Khomasdal', 'Katutura', 'Eros', 'Klein Windhoek']
distances = {
    ('Dorado Park', 'Khomasdal'): 7,
    ('Dorado Park', 'Katutura'): 20,
    ('Dorado Park', 'Eros'): 15,
    ('Dorado Park', 'Klein Windhoek'): 12,
    ('Khomasdal', 'Dorado Park'): 10,
    ('Khomasdal', 'Katutura'): 6,
    ('Khomasdal', 'Eros'): 14,
    ('Khomasdal', 'Klein Windhoek'): 18,
    ('Katutura', 'Dorado Park'): 20,
    ('Katutura', 'Khomasdal'): 6,
    ('Katutura', 'Eros'): 25,
    ('Katutura', 'Klein Windhoek'): 30,
    ('Eros', 'Dorado Park'): 15,
    ('Eros', 'Khomasdal'): 14,
    ('Eros', 'Katutura'): 25,
    ('Eros', 'Klein Windhoek'): 2,
    ('Klein Windhoek', 'Dorado Park'): 12,
    ('Klein Windhoek', 'Khomasdal'): 18,
    ('Klein Windhoek', 'Katutura'): 30,
    ('Klein Windhoek', 'Eros'): 2
}

# PROBLEM REPRESENTATION
def get_places():
    places = input("Enter the place names separated by commas: ").split(",")
    return [place.strip() for place in places]

def get_distances(places):
    distances = {}
    for i in range(len(places)):
        for j in range(i + 1, len(places)):
            distance = int(input(f"Enter the distance between {places[i]} and {places[j]}: "))
            distances[(places[i], places[j])] = distance
            distances[(places[j], places[i])] = distance
    return distances

def calculate_total_distance(route, distances):
    return sum(distances[(route[i], route[i+1])] for i in range(len(route)-1)) + distances[(route[-1], route[0])]

def TSP_hillclimb(places):
    path = places.copy()
    random.shuffle(path)
    return path

def explore_neighbors(path):
    new_path = path.copy()
    i, j = random.sample(range(len(new_path)), 2)
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path

def calculate_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[(path[i], path[i+1])]
    return total_distance

def hill_climbing(places, distances, max_iterations=1000):
    current_path = TSP_hillclimb(places)
    current_distance = calculate_distance(current_path, distances)
    best_path = current_path
    best_distance = current_distance

    for _ in range(max_iterations):
        neighbor_path = explore_neighbors(current_path)
        neighbor_distance = calculate_distance(neighbor_path, distances)

        if neighbor_distance < best_distance:
            current_path = neighbor_path
            current_distance = neighbor_distance
            best_path = current_path
            best_distance = current_distance
        elif neighbor_distance >= current_distance:
            break  # No better neighbor found, so we've reached the optimum

    return best_path, best_distance

def display_route(places, route):
    max_name_length = max(len(place) for place in places)
    route_string = " → ".join(place.ljust(max_name_length + 2) for place in route + [route[0]])
    return route_string

# Example usage
places = get_places()
print("\nPlaces:")
print(", ".join(places))

distances = get_distances(places)
print("\nTotal Distances:")
for place1, place2 in distances:
    print(f"{place1} → {place2}: {distances[(place1, place2)]} km")

print("\nInitial Random Route:")
initial_path = TSP_hillclimb(places)
print(display_route(places, initial_path))
initial_distance = calculate_distance(initial_path, distances)
print(f"Initial distance: {initial_distance} km")

print("\nExploring Neighbors:")
neighbor_path = explore_neighbors(initial_path)
neighbor_distance = calculate_distance(neighbor_path, distances)
print(display_route(places, neighbor_path))
print(f"Neighbor distance: {neighbor_distance} km")

print("\nRunning Hill Climbing:")
optimal_path, optimal_distance = hill_climbing(places, distances)
print(f"Optimal Route:\n{display_route(places, optimal_path)}")
print(f"Optimal Distance: {optimal_distance} km")