import unittest
from src.stats_utils import mean


class TestStatsUtils(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([4, 6, 8]), 6)


if __name__ == "__main__":
    unittest.main()
