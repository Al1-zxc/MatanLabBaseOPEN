import numpy as np
import matplotlib.pyplot as plt


def f(x, r):
    return r * x * (1 - x)


plt.figure(figsize=(8, 8))
r_list = [3.2, 3.56]
x0 = 0.1
iterations_number = 20
x = np.linspace(0, 1, 1000)

for r in r_list:
    y = f(x, r)
    plt.plot(x, y, label=f'f(x), r={r}')
plt.plot([0, 1], [0, 1], alpha=0.5, label="y = x", color="black")

colors = ['blue', 'orange']
for i in range(len(r_list)):
    x_n = x0
    if len(colors) != len(r_list):
        break
    for _ in range(iterations_number):
        y_n = f(x_n, r_list[i])
        plt.plot([x_n, x_n], [x_n, y_n], colors[i])
        plt.plot([x_n, y_n], [y_n, y_n], colors[i])
        x_n = y_n

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Лестница Ламерея r = {r_list[0]} и r = {r_list[1]}')
plt.legend()
plt.grid(True)
plt.show()
