# Tema 1.1: ¿Qué es un Algoritmo? (Visión Staff L7)

> **Nota para el Staff Engineer:** A nuestro nivel, un algoritmo no es solo código; es una decisión de negocio sobre cómo gastamos recursos (CPU, RAM, Tiempo) para obtener un resultado.

## 1. Definición L7: El Contrato de Recursos

Para un Junior, un algoritmo es una receta: "Haz A, luego B, obtén C".
Para un **Staff Engineer**, un algoritmo es un **contrato de gestión de recursos**.

Es una caja negra donde metemos datos (Input) y sacamos resultados (Output), pero lo crítico es **el costo** de esa transformación.
*   **Tiempo**: Latencia de usuario (¿El cliente espera 10ms o 10s?).
*   **Espacio**: Costo de infraestructura en GCP (¿Necesitamos 128MB de RAM o 64GB?).
*   **Complejidad**: Deuda técnica (¿Puede un dev junior mantener esto sin romper producción?).

> **La mentalidad L7:** Un algoritmo es la decisión consciente de *cómo* pagamos por una respuesta. ¿Pagamos esperando (tiempo) o pagamos con hardware (espacio)?

## 2. Los Tres Pilares de Evaluación

Al diseñar sistemas distribuidos o servicios en GCP, evaluamos los algoritmos bajo tres lentes:

### A. Corrección (Correctness)
¿Funciona *siempre*?
*   En sistemas distribuidos, lo difícil son los **Edge Cases** (casos borde) y los fallos parciales.
*   *Ejemplo*: Un algoritmo de reintento (retry) sin "Exponential Backoff" es técnicamente "correcto" (reintenta), pero en la práctica es un ataque DDoS a tu propio servicio.

### B. Eficiencia (Big O sin academicismos)
No buscamos la fórmula matemática exacta, sino el **comportamiento a escala**. ¿Cómo se degrada el sistema cuando pasamos de 100 usuarios a 10 millones?

| Notación | Nombre | Comportamiento en Producción | Ejemplo GCP |
| :--- | :--- | :--- | :--- |
| **$O(1)$** | Constante | **Oro puro**. Tarda lo mismo con 1 usuario que con 1 billón. | Acceso a Redis por Key. |
| **$O(\log n)$** | Logarítmico | **Excelente**. Si los datos se duplican, el tiempo solo crece un "pasito". | Índices en Cloud Spanner, Búsqueda Binaria. |
| **$O(n)$** | Lineal | **Cuidado**. Pagas por cada dato. Si los datos se duplican, tu factura/latencia se duplica. | Full Table Scan en BigQuery, iterar una lista. |
| **$O(n^2)$** | Cuadrático | **Incendio**. Peligro mortal en sistemas grandes. | Bucles anidados comparando todo contra todo. |

### C. Trade-offs (Compromisos)
Rara vez existe el algoritmo perfecto. Nuestro trabajo es negociar.
*   **Escenario**: Necesitamos búsquedas ultra-rápidas ($O(1)$).
*   **Solución**: Usar un Hash Map (Diccionario) en memoria.
*   **Costo (Trade-off)**: Consumo masivo de RAM.
*   **Decisión Staff**: "¿Tenemos presupuesto en los pods de Kubernetes para esta RAM? Si sí, compramos velocidad con dinero (memoria)."

---

## 3. Ejemplo Práctico: La Biblioteca vs. El GPS

Imagina buscar un libro específico en una biblioteca de 1 millón de libros.

### Algoritmo 1: Búsqueda Lineal ($O(n)$)
*   **Método**: Empiezas en el primer libro. ¿Es este? No. Siguiente.
*   **Peor caso**: El libro está al final o no existe. Revisas 1,000,000 de libros.
*   **Staff View**: Inviable para sistemas en tiempo real. Equivalente a escanear logs sin filtros.

### Algoritmo 2: Búsqueda Binaria ($O(\log n)$)
*   **Requisito**: Los libros deben estar **ordenados**.
*   **Método**: Vas a la mitad. ¿Tu libro es "M"? La mitad es "L". Sabes que está a la derecha. Descartas 500,000 libros de golpe.
*   **Peor caso**: Encuentras el libro en **~20 pasos**.
*   **Staff View**: Esto es lo que hace escalable a una base de datos. Pasamos de 1 millón de operaciones a 20.
