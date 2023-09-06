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

    def test_build_graph(self):
        # Given
        exchange_rates = {
            "BTC-BTC": "1.00000000",
            "BTC-CHSB": "0.00000499",
            "BTC-DAI": "0.00003830",
            "BTC-EUR": "0.00004109",
            "CHSB-BTC": "199126.80682993",
            "CHSB-CHSB": "1.00000000",
            "CHSB-DAI": "7.92796971",
            "CHSB-EUR": "8.30466748",
            "DAI-BTC": "25329.62752750",
            "DAI-CHSB": "0.12531293",
            "DAI-DAI": "1.00000000",
            "DAI-EUR": "1.08182069",
            "EUR-BTC": "24185.01694493",
            "EUR-CHSB": "0.11682889",
            "EUR-DAI": "0.91827610",
            "EUR-EUR": "1.00000000"
        }

        # When
        graph = build_graph(exchange_rates)

        print(graph)



if __name__ == '__main__':
    unittest.main()
