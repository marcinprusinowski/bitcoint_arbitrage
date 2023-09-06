import unittest
from src.algorithms import dijkstra_arbitrage, floyd_warshall_negative_cycle, bellman_ford_arbitrage
from src.utils import build_graph


class TestArbitrageAlgorithm(unittest.TestCase):
    def test_dijkstra_arbitrage_exists(self):
        # Given
        graph = build_graph(
            {
                "USD-USD": "1.00000000",
                "USD-EUR": "0.85",
                "USD-JPY": "100.00",
                "EUR-USD": "1.17647059",
                "EUR-EUR": "1.00000000",
                "EUR-JPY": "120.00",
                "JPY-USD": "0.01000000",
                "JPY-EUR": "0.00833333",
                "JPY-JPY": "1.00000000"
            }
        )
        expected_cycle = ['USD', 'JPY', 'USD']
        source_currency = "USD"

        # When
        arbitrage_cycle = dijkstra_arbitrage(graph, source_currency)

        # Then
        self.assertEqual(arbitrage_cycle, expected_cycle)

    def test_dijkstra_no_arbitrage_cycle(self):
        # Given
        graph = build_graph(
            {
                "USD-USD": "1.00000000",
                "USD-EUR": "1.00000000",
                "USD-JPY": "1.00000000",
                "EUR-USD": "1.00000000",
                "EUR-EUR": "1.00000000",
                "EUR-JPY": "1.00000000",
                "JPY-USD": "1.00000000",
                "JPY-EUR": "1.00000000",
                "JPY-JPY": "1.00000000"
            }
        )
        source_currency = "USD"

        # When
        arbitrage_cycle = dijkstra_arbitrage(graph, source_currency)

        # Then
        self.assertIsNone(arbitrage_cycle)

    def test_bellman_ford_arbitrage_cycle_exists(self):
        # Given
        graph = build_graph(
            {
                "USD-USD": "1.00000000",
                "USD-EUR": "0.85",
                "USD-JPY": "100.00",
                "EUR-USD": "1.17647059",
                "EUR-EUR": "1.00000000",
                "EUR-JPY": "120.00",
                "JPY-USD": "0.01000000",
                "JPY-EUR": "0.00833333",
                "JPY-JPY": "1.00000000"
            }
        )
        expected_cycle = ['EUR', 'JPY', 'USD', 'EUR']
        source_currency = "USD"

        # When
        arbitrage_cycle = bellman_ford_arbitrage(
            graph,
            source_currency
        )

        # Then
        self.assertEqual(arbitrage_cycle, expected_cycle)

    def test_bellman_ford_no_arbitrage_cycle(self):
        # Given
        graph = build_graph(
            {
                "USD-USD": "1.00000000",
                "USD-EUR": "1.00000000",
                "USD-JPY": "1.00000000",
                "EUR-USD": "1.00000000",
                "EUR-EUR": "1.00000000",
                "EUR-JPY": "1.00000000",
                "JPY-USD": "1.00000000",
                "JPY-EUR": "1.00000000",
                "JPY-JPY": "1.00000000"
            }
        )
        source_currency = "USD"

        # When
        arbitrage_cycle = bellman_ford_arbitrage(graph, source_currency)

        # Then
        self.assertIsNone(arbitrage_cycle)

    def test_floyd_warshall_negative_cycle_exists(self):
        # Given
        graph = build_graph(
            {
                "USD-EUR": "0.9",
                "EUR-USD": "1.2",
                "EUR-GBP": "0.8",
                "GBP-EUR": "1.4",
                "GBP-USD": "1.5",
                "USD-GBP": "0.7"
            }
        )
        expected_cycle = ['EUR', 'USD', 'EUR']

        # When
        arbitrage_cycle = floyd_warshall_negative_cycle(graph)

        # Then
        self.assertEqual(arbitrage_cycle, expected_cycle)

    def test_floyd_warshall_no_arbitrage_cycle(self):
        # Given
        graph = build_graph(
            {
                "USD-USD": "1.00000000",
                "USD-EUR": "1.00000000",
                "USD-JPY": "1.00000000",
                "EUR-USD": "1.00000000",
                "EUR-EUR": "1.00000000",
                "EUR-JPY": "1.00000000",
                "JPY-USD": "1.00000000",
                "JPY-EUR": "1.00000000",
                "JPY-JPY": "1.00000000"
            }
        )

        # When
        arbitrage_cycle = floyd_warshall_negative_cycle(graph)

        # Then
        self.assertIsNone(arbitrage_cycle)

if __name__ == '__main__':
    unittest.main()