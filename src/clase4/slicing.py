
import numpy as np

# Array 1D
arr = np.array([10, 20, 30, 40, 50, 60, 70])

print(arr[0])      # primer elemento
print(arr[-1])     # último elemento
print(arr[1:4])    # del índice 1 al 3
print(arr[:3])     # primeros 3
print(arr[3:])     # desde el índice 3
print(arr[::2])    # de 2 en 2

# Array 2D (matriz)
matriz = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])

print(matriz[1, 2])      # fila 1, columna 2
print(matriz[:2, 1:3])   # primeras 2 filas, columnas 1 y 2
