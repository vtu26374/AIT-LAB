import numpy as np

# Distance matrix
d = np.array([
    [0, 10, 12, 11, 14],
    [10, 0, 13, 15, 8],
    [12, 13, 0, 9, 14],
    [11, 15, 9, 0, 16],
    [14, 8, 14, 16, 0]
])

n_ants = 5
n_citys = 5
iterations = 100

alpha = 1      # pheromone importance
beta = 2       # visibility importance
evaporation = 0.5

n = n_citys
m = n_ants

# Visibility matrix
visibility = 1 / (d + np.diag([np.inf] * n))  # Avoid division by zero

# Pheromone matrix
pheromone = 0.1 * np.ones((n, n))

# Best path and cost
best_cost = np.inf
best_route = None

for ite in range(iterations):
    routes = np.ones((m, n + 1), dtype=int)

    for ant in range(m):
        visited = [0]  # start from city 0 (indexing from 0)

        for step in range(1, n):
            current = visited[-1]

            # Compute probabilities
            probs = np.zeros(n)
            for j in range(n):
                if j not in visited:
                    probs[j] = (pheromone[current][j] ** alpha) * (visibility[current][j] ** beta)

            if probs.sum() == 0:
                break  # dead end, should rarely happen

            probs = probs / probs.sum()
            next_city = np.random.choice(np.arange(n), p=probs)
            visited.append(next_city)

        visited.append(0)  # return to start city
        routes[ant] = np.array(visited)

    # Calculate cost of each route
    route_costs = np.zeros(m)
    for ant in range(m):
        cost = 0
        for i in range(n):
            cost += d[routes[ant][i]][routes[ant][i + 1]]
        route_costs[ant] = cost

        if cost < best_cost:
            best_cost = cost
            best_route = routes[ant].copy()

    # Pheromone evaporation
    pheromone = (1 - evaporation) * pheromone

    # Update pheromone based on routes
    for ant in range(m):
        for i in range(n):
            from_city = routes[ant][i]
            to_city = routes[ant][i + 1]
            pheromone[from_city][to_city] += 1 / route_costs[ant]
            pheromone[to_city][from_city] += 1 / route_costs[ant]  # symmetric TSP

# Final output
print("Best route found:")
print(best_route + 1)  # convert to 1-based index
print("Cost of the best route:", int(best_cost))
