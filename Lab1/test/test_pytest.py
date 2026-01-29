from src.stats_utils import mean, variance, std_dev


def test_mean():
    assert mean([1, 2, 3]) == 2


def test_variance():
    assert round(variance([1, 2, 3]), 2) == 0.67


def test_std_dev():
    assert round(std_dev([1, 2, 3]), 2) == 0.82
