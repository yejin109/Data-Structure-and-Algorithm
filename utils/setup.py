import numpy as np


def load_data(size=1000, dtype=int, high=10000, low=0):
    if dtype == int:
        return np.random.randint(low, high, size, dtype)
    elif dtype == float:
        return np.random.random(size)

