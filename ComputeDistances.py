def compute_distances_from_start(vertices):
    distance_changes = True
    while distance_changes:
        distance_changes = False
        for vertex in range(len(vertices)):
            # print(vertices[vertex])
            distance_to_start_init = vertices[vertex][1]
            # print("Initial distance_to_start =", distance_to_start_init)
            distance_to_start_current = vertices[vertex][1]

            for neighbor in range(len(vertices[vertex][2])):
                neighbor_index = vertices[vertex][2][neighbor][0]
                distance_to_neighbor = vertices[vertex][2][neighbor][1]
                distance_from_neighbor_to_start = vertices[neighbor_index][1]
                # print("neighbor:", neighbor_index, "distance =",
                #  distance_to_neighbor, "D2 =",
                #  distance_from_neighbor_to_start)
                distance_to_start_current = min(distance_to_start_current,
                                                distance_to_neighbor + distance_from_neighbor_to_start)
                # print("New distance to start =", distance_to_start_current)

            if (distance_to_start_current != distance_to_start_init):
                distance_changes = True
                vertices[vertex][1] = distance_to_start_current
    return vertices
