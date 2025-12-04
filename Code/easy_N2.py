from numpy import linspace
import matplotlib.pyplot as plt


def g(x, r):
    return r * x * ((1 - x) ** 2)


plt.figure(figsize=(8, 8))
x = linspace(0, 1, 1000)
r_list = [27 / 4, 27 / 8, 1, 0]

for r in r_list:
    y = g(x, r)
    plt.plot(x, y, label=f"r = {r}")

plt.plot([0, 1], [0, 1], alpha=0.5, label="y = x", color="black")

plt.title(f"$x_n = r x_{{n-1}} (1 - x_{{n-1}})^2$", fontsize=16)
plt.xlabel("$x_{n-1}$", fontsize=16)
plt.ylabel("$x_n$", fontsize=16)
plt.legend(fontsize=10, loc='upper left')
plt.grid(True)
plt.show()
