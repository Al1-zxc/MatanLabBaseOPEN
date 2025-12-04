import matplotlib.pyplot as plt


def f(x, r):
    return r * x * (1 - x)


plt.figure(figsize=(8, 8))
r_list = [i / 10 for i in range(11)]
x0 = 0.3

for r in r_list:
    x_list = [x0]
    for _ in range(100):
        x_list.append(f(x_list[-1], r))
    plt.plot(x_list, label=f'r = {r}')

plt.title("Монотонное убывание и стремление к" + "\n" +
          "единственному пределу (нулю) при различных r", fontsize=16)
plt.xlabel("n", fontsize=16)
plt.ylabel("x_n", fontsize=16)
plt.legend(fontsize=10, loc='upper right')
plt.grid(True)
plt.show()
