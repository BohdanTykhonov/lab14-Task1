import numpy as np
import matplotlib.pyplot as plt

# Функція для побудови графіка
def Y(x):
    return 10 * np.cos(x**2) / x**2

# Створення масиву значень x
x = np.linspace(0.1, 5, 400)  # Уникаємо x = 0, щоб не було ділення на нуль

# Створення графіка
plt.figure(figsize=(8, 6))
plt.plot(x, Y(x), color='blue', linewidth=2, linestyle='-', label=r'$Y(x) = \frac{10 \cdot cos(x^2)}{x^2}$')

# Додавання підписів осей
plt.xlabel('x')
plt.ylabel('Y(x)')

# Додавання заголовка
plt.title('Графік функції Y(x) = 10*cos(x^2)/x^2')

# Додавання легенди
plt.legend()

# Відображення графіка
plt.grid(True)
plt.show()
