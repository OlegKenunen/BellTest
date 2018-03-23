import math

def find_path(vertices, start_vertex, finish_vertex):
    path = []
    if (vertices[finish_vertex][1] == math.inf):
        print("No path from start to finish")
        return path
    else:
        path = [vertices[finish_vertex][0]]

    for _ in range(len(vertices)):
        current_vertex = path[0]
        if vertices[current_vertex][0] == start_vertex:
            break
        next_best_vertex = None
        distance_through_next = math.inf
        for neighbor in range(len(vertices[current_vertex][2])):
            neighbor_index = vertices[current_vertex][2][neighbor][0]
            distance_to_neighbor = vertices[current_vertex][2][neighbor][1]
            distance_from_neighbor_to_start = vertices[neighbor_index][1]
            if distance_through_next > distance_to_neighbor + distance_from_neighbor_to_start:
                distance_through_next = distance_to_neighbor + distance_from_neighbor_to_start
                next_best_vertex = neighbor_index

        path.insert(0, next_best_vertex)

    return path