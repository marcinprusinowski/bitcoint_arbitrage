import requests

from src.algorithms import bellman_ford_arbitrage
from src.utils import build_graph

url = "https://api.swissborg.io/v1/challenge/rates"
response = requests.get(url)
data = response.json()

graph = build_graph(data['rates'])
print(bellman_ford_arbitrage(graph, 'BTC'))
