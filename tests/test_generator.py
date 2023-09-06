import unittest

from src.generator import generate_currencies, generate_rates


class TestGenerator(unittest.TestCase):

    def test_generate_currencies(self):
        # Given
        currencies_to_be_generated = 2

        # When
        currencies = generate_currencies(currencies_to_be_generated)

        # Then
        assert len(currencies) == currencies_to_be_generated
        assert currencies == ["CUR1", "CUR2"]

    def test_generate_rates(self):
        # Given
        currencies = ["CUR1", "CUR2"]

        # When
        rates = generate_rates(currencies)

        # Then
        assert len(rates) == len(currencies) * len(currencies)
        for k, v in rates.items():
            assert 0.01 <= float(v) <= 100


if __name__ == '__main__':
    unittest.main()
