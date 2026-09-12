import numpy as np

# Ejemplo 1: Array 2D + Array 1D
a = np.array([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
b = np.array([10, 20, 30])            # Shape (3,)

# b se "estira" para coincidir con a
resultado = a + b
print(resultado)

# Ejemplo 2: Array 2D + Escalar
escalar = 5
print(a * escalar)
