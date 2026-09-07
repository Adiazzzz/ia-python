import csv
import os

CARPETA_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")


def leer_datos(ruta_archivo):
    """
    Lee un archivo CSV y lo convierte en una lista de diccionarios.

    Parámetros:
        ruta_archivo (str): ruta al archivo .csv a leer.

    Retorna:
        list[dict]: lista de diccionarios con los datos del archivo.
    """
    datos = []
    with open(ruta_archivo, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos


def mostrar_resumen(datos, nombre_archivo, columna_numerica=None):
    """
    Muestra la cantidad total de registros y, si se indica una columna
    numérica, calcula promedio, valor máximo y valor mínimo sobre ella.

    Parámetros:
        datos (list[dict]): datos ya leídos con leer_datos().
        nombre_archivo (str): nombre descriptivo del archivo.
        columna_numerica (str, opcional): columna numérica para las estadísticas.
    """
    total_registros = len(datos)
    print(f"\nArchivo: {nombre_archivo}")
    print(f"  - Cantidad total de registros: {total_registros}")

    if columna_numerica and total_registros > 0 and columna_numerica in datos[0]:
        valores = []
        for fila in datos:
            valor_texto = fila.get(columna_numerica, "")
            try:
                valores.append(float(valor_texto))
            except (TypeError, ValueError):
                continue

        if valores:
            promedio = sum(valores) / len(valores)
            valor_maximo = max(valores)
            valor_minimo = min(valores)
            print(f"  - Estadísticas de la columna '{columna_numerica}':")
            print(f"      Promedio: {promedio:.2f}")
            print(f"      Máximo:   {valor_maximo:.2f}")
            print(f"      Mínimo:   {valor_minimo:.2f}")
        else:
            print(f"  - No se encontraron valores numéricos válidos en '{columna_numerica}'.")


def main():
    archivos_csv = [
        "autor.csv",
        "autor_libro.csv",
        "editorial.csv",
        "ejemplar.csv",
        "genero.csv",
        "libro.csv",
        "libro_genero.csv",
        "prestamo.csv",
        "prestamo_ejemplar.csv",
        "ubicacion.csv",
        "usuario.csv",
    ]

    print("RESUMEN DE DATOS - BIBLIOTECA")

    for nombre_archivo in archivos_csv:
        ruta = os.path.join(CARPETA_DATOS, nombre_archivo)
        datos = leer_datos(ruta)

        if nombre_archivo == "ejemplar.csv":
            mostrar_resumen(datos, nombre_archivo, columna_numerica="valor")
        else:
            mostrar_resumen(datos, nombre_archivo)


if __name__ == "__main__":
    main()
