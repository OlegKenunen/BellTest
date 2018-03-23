from ComputeDistances import compute_distances_from_start
from FindShortPath import find_path
from InitializeGraph import initialize_vertices
from InitializeGraph import initialize_connections

number_of_vertices = 12

start_vertex = 0
finish_vertex = 10
# structure of edges: [[from_vertex_index, to_vertex_index, distance], [...], ...]
edges = [[0, 1, 20.0],
         [0, 2, 10.0],
         [0, 3, 30.0],
         [1, 4, 10.0],
         [1, 2, 10.0],
         [1, 3, 10.0],
         [2, 4, 30.0],
         [3, 4, 40.0],
         [3, 7, 60.0],
         [4, 6, 10.0],
         [4, 5, 30.0],
         [5, 9, 20.0],
         [6, 7, 50.0],
         [7, 8, 10.0],
         [6, 8, 10.0],
         [6, 9, 10.0],
         [7, 10, 50.0],
         [8, 11, 50.0],
         [8, 9, 20.0],
         [9, 11, 10.0],
         [11, 10, 20.0]]

vertices = initialize_vertices(number_of_vertices, start_vertex)
vertices = initialize_connections(vertices, edges)
vertices = compute_distances_from_start(vertices)

# for vertex in range(len(vertices)):
#     print(vertices[vertex])

path = find_path(vertices, start_vertex, finish_vertex)

print("Path :", path)
