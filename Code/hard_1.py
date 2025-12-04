import numpy as np


def f(r, x):
    return r * x * (1 - x)


def period(r, sample_size, iterations_number=5000, precision=1e-8, x0=0.5):
    x = x0
    for _ in range(iterations_number):
        x = f(r, x)
    x_list = [x]
    for _ in range(sample_size):
        x = f(r, x)
        x_list.append(x)
    x_list = np.array(x_list)
    for m in range(1, sample_size // 2):
        if np.all(np.abs(x_list[:-m] - x_list[m:]) < precision):
            return m
    return None


sample_size = 2000
r_inf = 3.5699456
r_values = np.linspace(3.0, r_inf, sample_size)
periods = [period(r, sample_size) for r in r_values if period(r, sample_size)]
result = sorted(set(periods))
print(result)
