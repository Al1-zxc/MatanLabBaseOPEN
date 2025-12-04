import matplotlib.pyplot as plt


def f(x, r):
    return r * x * (1 - x)


plt.figure(figsize=(8, 8))
r = 2.8
x0 = 0.6
iterations_number = 75
static_x = 1 - 1 / r

x_list = [x0]
x_now = x0
for _ in range(iterations_number):
    x_now = f(x_now, r)
    x_list.append(x_now)

even_x_list = x_list[0::2]
n_even = list(range(0, iterations_number + 1, 2))

odd_x_list = x_list[1::2]
n_odd = list(range(1, iterations_number + 1, 2))

plt.axhline(static_x, color="black", linestyle="--",
            label=f"Неподвижная точка $x^*$ = {static_x:.3f}")
plt.plot(n_even, even_x_list, "o-", label="$x_{2n}$ - Монотонно убывают")
plt.plot(n_odd, odd_x_list, "o-", label="$x_{2n+1}$ - Монотонно возрастают")

plt.title(f"Монотонность подпоследовательностей при r = {r}", fontsize=16)
plt.xlabel("n", fontsize=16)
plt.ylabel("$x_n$", fontsize=16)
plt.legend(fontsize=10, loc='upper right')
plt.grid(True)
plt.show()
