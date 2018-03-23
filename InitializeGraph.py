import math


def initialize_vertices(number_of_vertices, start_vertex):
    vertices = []
    for vertex in range(number_of_vertices):
        if vertex == start_vertex:
            vertices.append([vertex, 0, []])
            # first value - vertex,
            # second value - distance to start,
            # third value - list of neighbors [[vertex, distance], ...]
        else:
            vertices.append([vertex, math.inf, []])
    return vertices


def initialize_connections(vertices, edges):
    print("Initialize connections:")
    for edge in range(len(edges)):
        print("Vertex", edges[edge][0], "connected with", edges[edge][1], "distance =", edges[edge][2])
        vertices[edges[edge][0]][2].append([edges[edge][1], edges[edge][2]])
        vertices[edges[edge][1]][2].append([edges[edge][0], edges[edge][2]])
    return vertices
