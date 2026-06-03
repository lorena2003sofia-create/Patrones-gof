import unittest

from patterns.strategy.kpi_strategy import (
    AHTStrategy,
    ACWStrategy
)


class TestStrategy(unittest.TestCase):

    def test_aht_strategy(self):

        strategy = AHTStrategy()

        self.assertEqual(
            strategy.calculate(100, 10),
            10
        )

    def test_acw_strategy(self):

        strategy = ACWStrategy()

        self.assertEqual(
            strategy.calculate(50, 10),
            5
        )


if __name__ == "__main__":
    unittest.main()