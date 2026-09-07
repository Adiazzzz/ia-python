cultivos = [
    {"nombre": "Café", "hectareas": 8.0, "produccion_toneladas": 4.5},
    {"nombre": "Zanahoria", "hectareas": 5.0, "produccion_toneladas": 10.5},
    {"nombre": "Maíz", "hectareas": 6.0, "produccion_toneladas": 3.8},
    {"nombre": "Plátano", "hectareas": 4.0, "produccion_toneladas": 4.8},
    {"nombre": "Cacao", "hectareas": 7.0, "produccion_toneladas": 4.6}
]


def calcular_rendimiento(cultivo):
    """Rendimiento en toneladas por hectarea para un cultivo."""
    return cultivo["produccion_toneladas"] / cultivo["hectareas"]

def mostrar_cultivos(lista_cultivos):
    """Nos permite ver el nombre y rendimiento de cada cultivo."""
    print("=== RENDIMIENTO DE CULTIVOS EN CARTAGO ===")
    for cultivo in lista_cultivos:
        rendimiento = calcular_rendimiento(cultivo)
        print(f"- {cultivo['nombre']}: {rendimiento:.2f} ton/ha")

def cultivo_mayor_rendimiento(lista_cultivos):
    """Muestra el nombre del cultivo con el mayor rendimiento por hectárea."""
    mayor_cultivo = None
    mayor_rendimiento = 0.0
    for cultivo in lista_cultivos:
        rend = calcular_rendimiento(cultivo)
        if rend > mayor_rendimiento:
            mayor_rendimiento = rend
            mayor_cultivo = cultivo["nombre"]
    return mayor_cultivo




if __name__ == "__main__":
    
    mostrar_cultivos(cultivos)
    print()  

    
    mejor = cultivo_mayor_rendimiento(cultivos)
    print(f"El cultivo con mayor rendimiento es: {mejor}")
