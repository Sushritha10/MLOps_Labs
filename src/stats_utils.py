def mean(values):
    if len(values) == 0:
        raise ValueError("List cannot be empty")
    return sum(values) / len(values)


def variance(values):
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)


def std_dev(values):
    return variance(values) ** 0.5


def summary_stats(values):
    return {
        "mean": mean(values),
        "variance": variance(values),
        "std_dev": std_dev(values),
    }
