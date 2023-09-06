import unittest
import math
from src.utils import build_graph


class TestBuildGraphMethod(unittest.TestCase):
    def test_empty_exchange_rates(self):
        # Given
        exchange_rates = {}

        # When
        graph = build_graph(exchange_rates)

        # Then
        self.assertEqual(
            graph,
            {}
        )

    def test_same_currency_pair(self):
        # Given
        exchange_rates = {
            "USD-USD": 1.0
        }

        # When
        graph = build_graph(exchange_rates)

        # Then
        self.assertEqual(
            graph,
            {}
        )

    def test_multiple_currency_pairs(self):
        # Given
        exchange_rates = {
            "USD-EUR": 0.85,
            "USD-GBP": 0.75,
            "EUR-GBP": 0.88
        }

        # When
        graph = build_graph(exchange_rates)

        # Then
        expected_graph = {
            "USD": {"EUR": -math.log(0.85), "GBP": -math.log(0.75)},
            "EUR": {"GBP": -math.log(0.88)}
        }

        self.assertEqual(
            graph,
            expected_graph
        )

    def test_non_negative_edge_weights_multiple_pairs(self):
        # Given
        exchange_rates = {
            "USD-EUR": 0.85,
            "USD-GBP": 0.75,
            "EUR-GBP": 0.88
        }

        # When
        graph = build_graph(exchange_rates)

        # Then
        for src, weights in graph.items():
            for weight in weights.values():
                self.assertGreaterEqual(weight, 0)


if __name__ == '__main__':
    unittest.main()
