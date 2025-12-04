import matplotlib.pyplot as plt

def g(x, r):
    return r * x * ((1 - x) ** 2)


plt.figure(figsize=(8, 8))
iterations_number = 75
x0 = 0.2

r = 0.5
x_list = [x0]
x_now = x0
for _ in range(iterations_number):
    x_now = g(x_now, r)
    x_list.append(x_now)
plt.plot(x_list, "o-", label=f"r = {r} $-$> 0")

r = 3
static_x = 1 - 1 / r ** 0.5
x_list = [x0]
x_now = x0
for _ in range(iterations_number):
    x_now = g(x_now, r)
    x_list.append(x_now)
plt.plot(x_list, "o-", label=f"r = {r} $-$> {static_x:.3f}")
plt.axhline(static_x, color="black", linestyle="--",
            label=f"Неподвижная точка $x^*$ = {static_x:.3f}")

r = 27 / 4
x_list = [x0]
x_now = x0
for _ in range(iterations_number):
    x_now = g(x_now, r)
    x_list.append(x_now)
plt.plot(x_list, "o-", label=f"r = {r}")

plt.title(f"График зависимости $x_{{n+1}}$ от n" + "\n" +
          "при различных r", fontsize=16)
plt.xlabel("n", fontsize=16)
plt.ylabel("$x_n$", fontsize=16)
plt.legend(fontsize=10, loc='upper left')
plt.grid()
plt.show()
