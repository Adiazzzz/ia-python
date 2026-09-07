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

