import matplotlib.pyplot as plt
from generator import generate_rates, generate_currencies
from algorithms import dijkstra_arbitrage, bellman_ford_arbitrage, floyd_warshall_negative_cycle
from utils import build_graph
from timeit import timeit

bellman_times = []
floyd_times = []
dijkstra_times = []

for size in range(100, 600, 100):
    currencies = generate_currencies(size)
    rates = generate_rates(currencies)
    rates_graph = build_graph(rates)

    bellman_time = timeit(lambda: bellman_ford_arbitrage(rates_graph, currencies[0]), number=1)
    floyd_time = timeit(lambda: floyd_warshall_negative_cycle(rates_graph), number=1)
    dijkstra_time = timeit(lambda: dijkstra_arbitrage(rates_graph, currencies[0]), number=1)

    bellman_times.append(bellman_time)
    floyd_times.append(floyd_time)
    dijkstra_times.append(dijkstra_time)

dijkstra_times_2 = []
floyd_times_2 = []

for size in range(10000, 15000, 1000):
    currencies = generate_currencies(size)
    rates = generate_rates(currencies)
    rates_graph = build_graph(rates)

    floyd_time = timeit(lambda: floyd_warshall_negative_cycle(rates_graph), number=1)
    dijkstra_time = timeit(lambda: dijkstra_arbitrage(rates_graph, currencies[0]), number=1)

    floyd_times_2.append(floyd_time)
    dijkstra_times_2.append(dijkstra_time)

plt.figure(figsize=(10, 6))

plt.plot(range(100, 600, 100), bellman_times, label='Bellman-Ford (Small)')
plt.plot(range(100, 600, 100), floyd_times, label='Floyd-Warshall (Small)')
plt.plot(range(100, 600, 100), dijkstra_times, label='Dijkstra (Small)')

plt.plot(range(3000, 6000, 1000), floyd_times_2, label='Floyd-Warshall (Large)')
plt.plot(range(10000, 15000, 1000), dijkstra_times_2, label='Dijkstra (Large)')

plt.xlabel('Graph Size')
plt.ylabel('Time (seconds)')
plt.title('Algorithm Comparison')
plt.legend()

plt.savefig('./15k.png')

plt.show()
