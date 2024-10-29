import networkx as nx
import matplotlib.pyplot as plt
import heapq

district = nx.Graph()
district.add_nodes_from([
    'Home', 'School', 'Park', 'Library', 'Store', 'Gym', 'Restaurant',
    'Work', 'Bank', 'Pharmacy', 'Cinema', 'Hospital'
])

district.add_edges_from([
    ('Home', 'School', {'weight': 2}),
    ('Home', 'Bank', {'weight': 4}),
    ('Home', 'Work', {'weight': 5}),
    ('Home', 'Gym', {'weight': 3}),
    ('Home', 'Store', {'weight': 1}),
    ('Home', 'Hospital', {'weight': 8}),
    ('Home', 'Cinema', {'weight': 10}),
    ('Home', 'Restaurant', {'weight': 6}),
    ('Home', 'Library', {'weight': 5}),
    ('School', 'Library', {'weight': 2}),
    ('School', 'Park', {'weight': 3}),
    ('School', 'Store', {'weight': 4}),
    ('Park', 'Cinema', {'weight': 8}),
    ('Cinema', 'Library', {'weight': 6}),
    ('Store', 'Bank', {'weight': 3}),
    ('Store', 'Pharmacy', {'weight': 2}),
    ('Pharmacy', 'Bank', {'weight': 4}),
    ('Pharmacy', 'Hospital', {'weight': 2}),
    ('Bank', 'Gym', {'weight': 6}),
    ('Library', 'Work', {'weight': 3}),
])


def dijkstra(graph, start):
    shortest_path = {vertex: float('infinity') for vertex in graph}
    shortest_path[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > shortest_path[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

        return shortest_path


print(f'Shortest path: {dijkstra(district, 'Home')}')

pos = nx.spring_layout(district)
nx.draw(district, pos, with_labels=True, node_color='skyblue', font_size=8,
        font_color='black', edge_color='gray', node_size=700)
plt.gca().set_aspect('equal', adjustable='datalim')
plt.gca().set_xlim(-1.5, 1.5)
plt.gca().set_ylim(-1.5, 1.5)
edge_labels = nx.get_edge_attributes(district, 'weight')
nx.draw_networkx_edge_labels(district, pos, edge_labels=edge_labels)
plt.show()
