import math


def build_graph(exchange_rates):
    graph = {}
    for pair, rate in exchange_rates.items():
        source, destination = pair.split('-')

        if source == destination:
            continue

        rate = float(rate)

        if source not in graph:
            graph[source] = {}
        graph[source][destination] = -1 * math.log(rate)

    return graph
