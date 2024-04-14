import random

# PROBLEM REPRESENTATION (20%)
places = ['Dorado Park', 'Khomasdal', 'Katutura', 'Eros', 'Klein Windhoek']
distances_in_km = {
    ('Dorado Park', 'Dorado Park'):0,
    ('Dorado Park', 'Khomasdal'): 7,
    ('Dorado Park', 'Katutura'): 20,
    ('Dorado Park', 'Eros'): 15,
    ('Dorado Park', 'Klein Windhoek'): 12,
    ('Khomasdal', 'Khomasdal'):0,
    ('Khomasdal', 'Dorado Park'): 10,
    ('Khomasdal', 'Katutura'): 6,
    ('Khomasdal', 'Eros'): 14,
    ('Khomasdal', 'Klein Windhoek'): 18,
    ('Katutura', 'Katutura'):0,
    ('Katutura', 'Dorado Park'): 20,
    ('Katutura', 'Khomasdal'): 6,
    ('Katutura', 'Eros'): 25,
    ('Katutura', 'Klein Windhoek'): 30,
    ('Eros', 'Eros'):0,
    ('Eros', 'Dorado Park'): 15,
    ('Eros', 'Khomasdal'): 14,
    ('Eros', 'Katutura'): 25,
    ('Eros', 'Klein Windhoek'): 2,
    ('Klein Windhoek', 'Klein Windhoek'):0,
    ('Klein Windhoek', 'Dorado Park'): 12,
    ('Klein Windhoek', 'Khomasdal'): 18,
    ('Klein Windhoek', 'Katutura'): 30,
    ('Klein Windhoek', 'Eros'): 2
}

# Function to calculate total distance of a path
def calculate_distance(path, distances_in_km):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances_in_km[(path[i], path[i+1])]
    return total_distance

#HILL CLIMBING ALGORITHM(50%)


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

# output of  the graph 
optimal_path, optimal_distance = hill_climbing(places, distances_in_km)
print("Optimal route", optimal_path)
print(f"Optimal distance: {optimal_distance} km")


#ANALYSIS AND COMPARISON(50%)

#1.TIME COMPLEXITY 
"""

In our code, we explore the neighbors which involves shuffling
the list, so that would have the time complexity OF O(N); n
being the number of places, thus, O(5).

The size of the search space is a 5*5 grid; which is 25. So we
have (5! =120) possible paths to explore.

"""
#2. TEST CASES
# Test case 1: 3 places
places_test_1 = ['Dorado Park', 'Khomasdal', 'Katutura']
distances_test_1 = {
    ('Dorado Park', 'Khomasdal'): 7,
    ('Dorado Park', 'Katutura'): 20,
    ('Khomasdal', 'Dorado Park'): 10,
    ('Khomasdal', 'Katutura'): 6,
    ('Katutura', 'Dorado Park'): 20,
    ('Katutura', 'Khomasdal'): 6
}
optimal_path_1, optimal_distance_1 = hill_climbing(places_test_1, distances_test_1)
print("Test Case 1:")
print(f"Optimal route: {optimal_path_1}")
print(f"Optimal distance: {optimal_distance_1} km")

# Test case 2: 4 places
places_test_2 = ['Dorado Park', 'Khomasdal', 'Katutura', 'Eros']
distances_test_2 = {
    ('Dorado Park', 'Khomasdal'): 7,
    ('Dorado Park', 'Katutura'): 20,
    ('Dorado Park', 'Eros'): 15,
    ('Khomasdal', 'Dorado Park'): 10,
    ('Khomasdal', 'Katutura'): 6,
    ('Khomasdal', 'Eros'): 14,
    ('Katutura', 'Dorado Park'): 20,
    ('Katutura', 'Khomasdal'): 6,
    ('Katutura', 'Eros'): 25,
    ('Eros', 'Dorado Park'): 15,
    ('Eros', 'Khomasdal'): 14,
    ('Eros', 'Katutura'): 25
}
optimal_path_2, optimal_distance_2 = hill_climbing(places_test_2, distances_test_2)
print("\nTest Case 2:")
print(f"Optimal route: {optimal_path_2}")
print(f"Optimal distance: {optimal_distance_2} km")

# Test case 3: 5 places
places_test_3 = ['Dorado Park', 'Khomasdal', 'Katutura', 'Eros', 'Klein Windhoek']
distances_test_3 = {
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
optimal_path_3, optimal_distance_3 = hill_climbing(places_test_3, distances_test_3)
print("\nTest Case 3:")
print(f"Optimal route: {optimal_path_3}")
print(f"Optimal distance: {optimal_distance_3} km")



