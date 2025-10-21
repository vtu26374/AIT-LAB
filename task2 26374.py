from sys import maxsize
from itertools import permutations

V = 4  # Number of vertices

def travellingSalesmanProblem(graph, s):
    vertex = []
    
    # Store all vertices except the start vertex
    for i in range(V):
        if i != s:
            vertex.append(i)

    # Store minimum weight of a Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_pathweight = 0
        k = s

        # Compute cost of the current path
        for j in i:
            current_pathweight += graph[k][j]
            k = j

        # Add cost to return to starting point
        current_pathweight += graph[k][s]

        # Update minimum path cost
        min_path = min(min_path, current_pathweight)

    return min_path

if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    s = 0
    print("Minimum cost of TSP path:", travellingSalesmanProblem(graph, s))
