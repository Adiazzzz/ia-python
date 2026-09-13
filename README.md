## Propuesta de Proyecto

### Nombre del proyecto
Chatbot de Consulta de Material Bibliográfico - Biblioteca COTECNOVA

### Problemática

La Biblioteca COTECNOVA gestiona un acervo de 7.869 libros, de los cuales solo una parte está correctamente procesada en el aplicativo institucional, mientras que otro grupo importante se controla mediante un archivo paralelo en Excel. Actualmente, cuando un usuario (estudiante o docente) tiene una duda puntual sobre disponibilidad, ubicación, autor o categoría de un libro, debe:

- Consultar directamente en físico en la biblioteca, o
- Depender de que el sistema web actual tenga la búsqueda avanzada funcionando correctamente (lo cual presenta fallas conocidas).

Esto genera demoras, desplazamientos innecesarios y una experiencia de consulta poco eficiente para los usuarios, especialmente considerando el crecimiento institucional y la oferta de nuevos programas académicos que aumentan la demanda del servicio.

### Datos

**¿Qué información se necesita?**
- Base de datos de material bibliográfico: título, autor, categoría, disponibilidad (prestado/disponible), ubicación física.
- Historial de preguntas frecuentes de los usuarios (para entrenar o afinar las respuestas del chatbot).

**¿Dónde se va a obtener?**
- Base de datos MySQL del sistema de gestión de préstamos ya construida como parte del proyecto integrador.
- Complementado con el archivo Excel de la anterior bibliotecaria, una vez migrado/unificado a la base de datos oficial.

### Objetivo

Desarrollar un módulo de chatbot que se conecte directamente a la base de datos de la biblioteca y permita a los usuarios resolver, mediante lenguaje natural, preguntas sobre disponibilidad, ubicación y características del material bibliográfico, sin necesidad de desplazarse físicamente o depender del buscador web actual.

### Tecnologías

- Python
- Librerías sugeridas: Pandas, NumPy y NLP básico. 
- MySQL.
- Docker.
## Análisis Exploratorio de Datos

### ¿Qué variables analizamos?

Para este análisis se cruzaron dos variables del catálogo de la biblioteca:

- **Stock**: cuántos ejemplares físicos tiene cada libro (de `libro.csv`).
- **Préstamos**: cuántas veces se ha prestado cada libro (calculado a partir de `prestamo_ejemplar.csv` y `ejemplar.csv`).

La idea era responder una pregunta simple: **¿Los libros que más se prestan son también los que tienen más ejemplares disponibles?**

### ¿Qué estadísticas encontramos?

| Variable | Media | Mediana | Desv. estándar | Mínimo | Máximo |
|---|---|---|---|---|---|
| Stock | 2.20 | 2.00 | 1.19 | 1 | 5 |
| Préstamos | 1.05 | 1.00 | 1.16 | 0 | 7 |

En promedio cada libro tiene unos 2 ejemplares y se ha prestado apenas 1 vez. Esto ya nos da una pista: La demanda general no es muy alta y muy pocos libros concentran varios préstamos.

### Gráfico 1: Distribución de préstamos por libro (histograma)

![Distribución de préstamos](/ia-python/src/clase4/Act-Indep4/distribucion_prestamos.png)

**¿Qué muestra?** Cuántos libros caen en cada "cantidad de préstamos". El eje X es el número de préstamos (0, 1, 2...) y el eje Y es cuántos libros tuvieron esa cantidad.

**¿Cómo leerlo?** La barra más alta está en 0-1 préstamos, con casi 480 libros. A medida que se avanza hacia la derecha, las barras bajan rápidamente: muy pocos libros llegan a 6 u 8 préstamos.

**¿Qué significa?** La mayoría del catálogo casi no rota, muchos libros nunca se han prestado o se han prestado solo una vez. Mientras que un grupo pequeño concentra la mayor demanda. Es un patrón típico de "pocos libros populares, muchos libros de baja rotación".

### Gráfico 2: Relación entre stock y préstamos (dispersión)

![Stock vs préstamos](/ia-python/src/clase4/Act-Indep4/stock_vs_prestamos.png)

**¿Qué muestra?** Cada punto verde es un libro. Su posición horizontal (eje X) indica cuántos ejemplares tiene, y su posición vertical (eje Y) indica cuántas veces se prestó.

**¿Por qué se ve como una cuadrícula?** Porque el stock solo toma 5 valores posibles (1 a 5) y los préstamos van de 0 a 7. Al ser números enteros con rangos pequeños muchos libros comparten exactamente la misma combinación de valores y sus puntos quedan superpuestos (los círculos más oscuros son en realidad decenas de libros apilados en el mismo punto).

**¿Qué significa?** No se observa una relación clara entre tener más ejemplares y ser más prestado: los puntos están repartidos de forma pareja en todas las columnas sin una tendencia dispersa. Esto sugiere que con los datos actuales el número de copias disponibles no está explicando por sí solo la demanda del libro.

### ¿Cómo influyen estos hallazgos en el proyecto?
- Confirman que existe un grupo identificable de libros de "alta demanda" que se pueden priorizar para decisiones de compra (se debe la lista de libros con pocos ejemplares y varios préstamos generada en eda_proyecto.py).
- La falta de relación entre stock y préstamos indica que si se quisiera predecir qué tan prestado será un libro el stock por sí solo no sería una variable suficiente, habría que considerar otras (género, editorial, año de edición, carrera asociada).
- Refuerza la importancia de seguir recolectando datos reales de uso de la biblioteca, ya que, patrones más claros probablemente aparecerían con información real en lugar de datos simulados.