import heapq

graph = {
    'A': {'B': 10, 'C': 15},
    'B': {'D': 12, 'E': 15},
    'C': {'E': 10},
    'D': {'F': 2},
    'E': {'F': 5},
    'F': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(
                    pq,
                    (distance, neighbor)
                )

    return distances

hasil = dijkstra(graph, 'A')

for node, jarak in hasil.items():
    print(f"Jarak dari A ke {node} = {jarak} km")