import unittest

from ComputeDistances import compute_distances_from_start
from FindShortPath import find_path
from InitializeGraph import initialize_vertices, initialize_connections


class UnitTestGraphPath(unittest.TestCase):

    def test_zero_distance_to_start(self):
        number_of_vertices = 4
        start_vertex = 0
        finish_vertex = 3
        edges = [[0, 1, 10.0],
                 [1, 2, 20.0],
                 [2, 3, 30.0]]

        vertices = initialize_vertices(number_of_vertices, start_vertex)
        vertices = initialize_connections(vertices, edges)
        vertices = compute_distances_from_start(vertices)

        self.assertEqual(vertices[start_vertex][1], 0)

    def test_obvious_path(self):
        number_of_vertices = 4
        start_vertex = 0
        finish_vertex = 3
        edges = [[0, 1, 10.0],
                 [1, 2, 20.0],
                 [2, 3, 30.0]]

        vertices = initialize_vertices(number_of_vertices, start_vertex)
        vertices = initialize_connections(vertices, edges)
        vertices = compute_distances_from_start(vertices)
        path = find_path(vertices, start_vertex, finish_vertex)

        self.assertEqual(path, [0, 1, 2, 3])

    def test_no_path(self):
        number_of_vertices = 4
        start_vertex = 0
        finish_vertex = 3
        edges = [[0, 1, 10.0],
                 [2, 3, 30.0]]

        vertices = initialize_vertices(number_of_vertices, start_vertex)
        vertices = initialize_connections(vertices, edges)
        vertices = compute_distances_from_start(vertices)
        path = find_path(vertices, start_vertex, finish_vertex)

        self.assertEqual(path, [])

    def test_not_too_long_path(self):
        number_of_vertices = 4
        start_vertex = 0
        finish_vertex = 3
        edges = [[0, 1, 10.0],
                 [1, 2, 20.0],
                 [2, 3, 30.0]]

        vertices = initialize_vertices(number_of_vertices, start_vertex)
        vertices = initialize_connections(vertices, edges)
        vertices = compute_distances_from_start(vertices)
        path = find_path(vertices, start_vertex, finish_vertex)

        self.assertLessEqual(len(path), number_of_vertices)
