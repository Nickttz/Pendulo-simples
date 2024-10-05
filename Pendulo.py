import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Definindo a equação diferencial
def equation(x, y, a, q):
    return [y[1], -(a - 2*q*np.cos(2*x)) * y[0]]

# Condições iniciais
y0 = [1, 0]  # y(0) = 1, y'(0) = 0

# Intervalo de x para a solução
x_span = (0, 10)

# Valores diferentes de a e q
params = [(1, 0.5), (2, 0.3), (0.5, 0.8), (1.5, 0.4), (0.8, 0.6)]

# Plotando as soluções
plt.figure(figsize=(10, 8))

for a, q in params:
    # Resolvendo a equação diferencial usando solve_ivp
    sol = solve_ivp(equation, x_span, y0, args=(a, q), method='RK45', dense_output=True)

    # Avaliando a solução em um conjunto de pontos
    x_vals = np.linspace(x_span[0], x_span[1], 1000)
    y_vals = sol.sol(x_vals)

    # Plotando a solução
    plt.plot(x_vals, y_vals[0], label=f'a={a}, q={q}')

plt.title('Soluções da Equação Diferencial com Diferentes Valores de a e q')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid(True)
plt.show()