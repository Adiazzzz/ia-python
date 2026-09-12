import numpy as np
import matplotlib.pyplot as plt

dias = np.arange(1, 11)
temperaturas = np.array([28, 30, 25, 27, 29, 31, 26, 24, 32, 28])

plt.figure(figsize=(8, 5))
plt.plot(dias, temperaturas, marker='o', linestyle='-', color='b', label='Temperatura')

plt.title('Temperaturas en Cartago (últimos 10 días)')
plt.xlabel('Día')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.legend()

plt.savefig('temperaturas.png', dpi=150, bbox_inches='tight')
print("Gráfica guardada como 'temperaturas.png'")

