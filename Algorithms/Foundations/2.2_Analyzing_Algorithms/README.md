# Téma 2.2: Analizando Algoritmos

Analizar un algoritmo significa predecir los recursos que el algoritmo requiere. Ocasionalmente, recursos como memoria, ancho de banda de comunicación o hardware de computadora son de interés principal, pero más a menudo es el **tiempo computacional** lo que queremos medir.

## El Modelo RAM (Random-Access Machine)
Para analizar algoritmos de una manera independiente de la máquina concreta, utilizamos el modelo RAM de computación.
- **Instrucciones simples**: Las instrucciones se ejecutan una tras otra (sin concurrencia).
- **Tipos de instrucciones**: Aritmética (suma, resta, multiplicación, división), movimiento de datos (cargar, guardar, copiar), y control (bifurcación, llamada a subrutina).
- **Costo constante**: Asumimos que cada instrucción toma una cantidad de tiempo constante.

## Tamaño de la Entrada ($n$)
La mejor noción de tamaño de entrada depende del problema que se estudia.
- Para ordenar (sorting): El número de items en la entrada ($n$).
- Para multiplicar enteros: El número total de bits requeridos.
- Para grafos: Número de vértices y aristas.

## Tiempo de Ejecución
El tiempo de ejecución de un algoritmo en una entrada particular es el número de pasos primitivos u operaciones ejecutadas.
A menudo expresamos el tiempo de ejecución como una función del tamaño de la entrada: $T(n)$.

### Tipos de Análisis
1.  **Peor caso (Worst-case analysis)**: Es el tiempo máximo de ejecución en cualquier entrada de tamaño $n$. Nos da una garantía de que el algoritmo nunca tardará más que esto. Es el análisis más común.
2.  **Caso promedio (Average-case analysis)**: Es el tiempo esperado de ejecución sobre todas las entradas posibles de tamaño $n$. Requiere suposiciones sobre la distribución estadística de las entradas.
3.  **Mejor caso (Best-case analysis)**: El tiempo mínimo. Suele ser poco útil para garantizar rendimiento real ("el algoritmo es muy rápido si la lista ya está ordenada").

## Orden de Crecimiento (Rate of Growth)
Nos interesa la **tasa de crecimiento** del tiempo de ejecución a medida que $n$ crece.
- Ignoramos constantes y términos de orden inferior.
- Un algoritmo con tiempo de ejecución $\Theta(n^2)$ (cuadrático) será eventualmente más lento que uno con $\Theta(n)$ (lineal) para un $n$ suficientemente grande.
- Por ejemplo, **Insertion Sort** es $\Theta(n^2)$, mientras que **Merge Sort** es $\Theta(n \lg n)$.
