import numpy as np
import matplotlib.pyplot as plt


def g(x, r):
    return r * x * (1 - x) ** 2


def find_cycle_length(x0, r, iterations_number=1000, precision=1e-6):
    x = x0
    history = []
    for _ in range(iterations_number):
        x = g(x, r)
        history.append(x)
        for period in range(1, len(history) // 2):
            if np.allclose(history[-period:], history[-2 * period:-period],
                           atol=precision):
                return period
    return 0


plt.figure(figsize=(8, 8))
r_list = np.linspace(0, 27 / 4, 100)
x0 = 0.5
cycle_lengths = []

for r in r_list:
    period = find_cycle_length(x0, r)
    cycle_lengths.append(period)

plt.plot(r_list, cycle_lengths, '.', markersize=2)
plt.xlabel("r")
plt.ylabel("Длина цикла")
plt.title("Длина цикла g(x,r) в зависимости от r")
plt.show()
