import csv
import os
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

CARPETA_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/app/data")


def cargar_datos(carpeta_datos):
    """
    Carga los archivos CSV necesarios (libro.csv, ejemplar.csv y
    prestamo_ejemplar.csv) usando csv.DictReader.

    Parámetros:
        carpeta_datos (str): ruta a la carpeta con los archivos CSV.

    Retorna:
        tuple: (libros, ejemplares, prestamos_ejemplar) como listas de diccionarios,
        o (None, None, None) si ocurre un error.
    """
    try:
        with open(os.path.join(carpeta_datos, "libro.csv"), encoding="utf-8", newline="") as f:
            libros = list(csv.DictReader(f))
        with open(os.path.join(carpeta_datos, "ejemplar.csv"), encoding="utf-8", newline="") as f:
            ejemplares = list(csv.DictReader(f))
        with open(os.path.join(carpeta_datos, "prestamo_ejemplar.csv"), encoding="utf-8", newline="") as f:
            prestamos_ejemplar = list(csv.DictReader(f))
    except FileNotFoundError as e:
        print(f"Error: no se encontró el archivo. {e}")
        return None, None, None
    except Exception as e:
        print(f"Error al leer los archivos: {e}")
        return None, None, None

    print(f"Datos cargados correctamente: {len(libros)} libros, "
          f"{len(ejemplares)} ejemplares, {len(prestamos_ejemplar)} préstamos.")
    return libros, ejemplares, prestamos_ejemplar


def construir_array_stock_prestamos(libros, ejemplares, prestamos_ejemplar):
    """
    Construye un array de NumPy con el stock y la cantidad de préstamos
    de cada libro.

    Parámetros:
        libros (list[dict]): datos de libro.csv.
        ejemplares (list[dict]): datos de ejemplar.csv.
        prestamos_ejemplar (list[dict]): datos de prestamo_ejemplar.csv.

    Retorna:
        tuple: (array de NumPy con shape (n, 2) [stock, prestamos], lista de títulos)
    """
    ejemplar_a_libro = {e["id_ejemplar"]: e["id_libro"] for e in ejemplares}

    conteo_prestamos = Counter()
    for p in prestamos_ejemplar:
        id_libro = ejemplar_a_libro.get(p["id_ejemplar"])
        if id_libro is not None:
            conteo_prestamos[id_libro] += 1

    filas = []
    titulos = []
    for libro in libros:
        try:
            stock = float(libro["stock"])
        except (KeyError, TypeError, ValueError):
            continue
        prestamos = float(conteo_prestamos.get(libro["id_libro"], 0))
        filas.append([stock, prestamos])
        titulos.append(libro["titulo"])

    datos_numericos = np.array(filas, dtype=float)
    return datos_numericos, titulos


def calcular_estadisticas(datos_numericos):
    """
    Calcula media, mediana, desviación estándar, mínimo y máximo
    para 'stock' y 'prestamos'.

    Parámetros:
        datos_numericos (np.ndarray): array con columnas [stock, prestamos].

    Retorna:
        dict: estadísticas por variable.
    """
    if datos_numericos is None or len(datos_numericos) == 0:
        return None

    stock = datos_numericos[:, 0]
    prestamos = datos_numericos[:, 1]

    estadisticas = {
        "stock": {
            "media": np.mean(stock),
            "mediana": np.median(stock),
            "desviacion": np.std(stock),
            "minimo": np.min(stock),
            "maximo": np.max(stock),
        },
        "prestamos": {
            "media": np.mean(prestamos),
            "mediana": np.median(prestamos),
            "desviacion": np.std(prestamos),
            "minimo": np.min(prestamos),
            "maximo": np.max(prestamos),
        },
    }
    return estadisticas


def generar_visualizaciones(datos_numericos):
    """
    Genera un histograma de préstamos por libro y un gráfico de dispersión
    entre stock y préstamos, guardándolos como archivos PNG.

    Parámetros:
        datos_numericos (np.ndarray): array con columnas [stock, prestamos].
    """
    if datos_numericos is None or len(datos_numericos) == 0:
        return

    stock = datos_numericos[:, 0]
    prestamos = datos_numericos[:, 1]

    plt.figure(figsize=(8, 5))
    plt.hist(prestamos, bins=range(0, int(prestamos.max()) + 2), color="orange", edgecolor="black")
    plt.title("Distribución de préstamos por libro")
    plt.xlabel("Cantidad de préstamos")
    plt.ylabel("Cantidad de libros")
    plt.grid(True, axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("distribucion_prestamos.png", dpi=150, bbox_inches="tight")
    plt.close()

    plt.figure(figsize=(8, 6))
    plt.scatter(stock, prestamos, color="green", alpha=0.5)
    plt.title("Relación entre stock y préstamos por libro")
    plt.xlabel("Stock (ejemplares disponibles)")
    plt.ylabel("Cantidad de préstamos")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("stock_vs_prestamos.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("Gráficas guardadas: 'distribucion_prestamos.png' y 'stock_vs_prestamos.png'")


def libros_alta_demanda_bajo_stock(datos_numericos, titulos, umbral_prestamos=3, umbral_stock=3):
    """
    Identifica libros con muchos préstamos pero poco stock: candidatos
    a comprar más ejemplares.

    Parámetros:
        datos_numericos (np.ndarray): array con columnas [stock, prestamos].
        titulos (list[str]): títulos correspondientes a cada fila.
        umbral_prestamos (float): mínimo de préstamos para considerarse "alta demanda".
        umbral_stock (float): máximo de stock para considerarse "bajo stock".

    Retorna:
        list[tuple]: (titulo, stock, prestamos) de los libros que cumplen la condición.
    """
    stock = datos_numericos[:, 0]
    prestamos = datos_numericos[:, 1]

    mascara = (prestamos >= umbral_prestamos) & (stock <= umbral_stock)
    indices = np.where(mascara)[0]

    resultado = [(titulos[i], stock[i], prestamos[i]) for i in indices]
    resultado.sort(key=lambda x: x[2], reverse=True)
    return resultado


def main():
    libros, ejemplares, prestamos_ejemplar = cargar_datos(CARPETA_DATOS)
    if libros is None:
        return

    datos_numericos, titulos = construir_array_stock_prestamos(libros, ejemplares, prestamos_ejemplar)

    estadisticas = calcular_estadisticas(datos_numericos)
    if estadisticas:
        print("\nESTADÍSTICAS DESCRIPTIVAS:")
        for variable, valores in estadisticas.items():
            print(f"\n{variable.upper()}:")
            for key, value in valores.items():
                print(f"  {key.capitalize()}: {value:.2f}")

    generar_visualizaciones(datos_numericos)

    candidatos = libros_alta_demanda_bajo_stock(datos_numericos, titulos)
    print(f"\nLibros con alta demanda y bajo stock (candidatos a comprar más ejemplares): {len(candidatos)}")
    for titulo, stock, prestamos in candidatos[:10]:
        print(f"  - {titulo} | stock: {int(stock)} | préstamos: {int(prestamos)}")

    print("\nAnálisis completado exitosamente.")


if __name__ == "__main__":
    main()
