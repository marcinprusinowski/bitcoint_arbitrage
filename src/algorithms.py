import heapq


def bellman_ford_arbitrage(graph, source):
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node

    negative_cycle = []
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                current = neighbor
                while current not in negative_cycle:
                    negative_cycle.insert(0, current)
                    current = predecessors[current]
                negative_cycle.insert(0, current)
                return negative_cycle


def dijkstra_arbitrage(graph, source):
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0

    priority_queue = [(0, source)]

    while priority_queue:
        distance, node = heapq.heappop(priority_queue)

        if distance > distances[node]:
            continue

        for neighbor, weight in graph[node].items():
            new_distance = distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = node
                heapq.heappush(priority_queue, (new_distance, neighbor))

                if neighbor == source:
                    cycle = [source]
                    current = source
                    while predecessors[current] != source:
                        cycle.insert(0, predecessors[current])
                        current = predecessors[current]
                    cycle.insert(0, source)
                    return cycle


def floyd_warshall_negative_cycle(graph):
    nodes = list(graph.keys())
    distances = {node: {node: 0 for node in nodes} for node in nodes}
    predecessors = {node: {} for node in nodes}

    for node in nodes:
        for neighbor, weight in graph.get(node, {}).items():
            distances[node][neighbor] = weight
            predecessors[node][neighbor] = node

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    predecessors[i][j] = predecessors[k][j]

                    if i == j and distances[i][i] < 0:
                        cycle = [i]
                        current = predecessors[i][i]
                        while current not in cycle:
                            cycle.append(current)
                            current = predecessors[i][current]
                        cycle.append(current)
                        cycle = cycle[cycle.index(current):]
                        cycle.reverse()
                        return cycle
