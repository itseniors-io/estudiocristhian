# Tema 2.3: Diseñando Algoritmos

Existen muchas formas de diseñar algoritmos. En el tema anterior (Insertion Sort) vimos un enfoque llamado **incremental**: ir insertando un elemento en su lugar adecuado iterando sobre los elementos que ya están ordenados.

En esta sección, se introduce un enfoque de diseño muy poderoso conocido como **Divide y Vencerás (Divide and Conquer)**. 

## El enfoque "Divide y Vencerás"

Muchos algoritmos útiles son **recursivos** en estructura: para resolver un problema dado, se llaman a sí mismos recursivamente una o más veces para tratar problemas estrechamente relacionados. 
Estos algoritmos suelen seguir el paradigma de "Divide y Vencerás", el cual involucra tres pasos en cada nivel de la recursión:

1. **Divide (Dividir)**: Divide el problema original en varios subproblemas que son instancias más pequeñas del mismo problema.
2. **Conquer (Vencer)**: Resuelve los subproblemas de forma recursiva. Si el tamaño de los subproblemas es suficientemente pequeño, resuélvelos de manera directa (caso base).
3. **Combine (Combinar)**: Combina las soluciones de los subproblemas en la solución del problema original.

> [!TIP]
> **Staff L7 Insight:** Entender matemáticamente el patrón recursivo de Divide y Vencerás es dominar el pilar madre histórico del diseño de Sistemas Distribuidos masivos at-scale: El **Modelo MapReduce** concebido originariamente en Google para domar Exabytes de datos webs dispersos. La fase de Divide es una paralelizacion feroz sobre miles de workers que mapean (*Mappers*); mientras que el bloque de "Combine" consolida los resultados fragmentados reduciendolos (*Reducers*) a tu salida final. Entender por qué el paradigma de un CPU funciona, modela exactamente cómo funciona la constelación de servidores de Datacenters interconectados.

## Ejemplo Central: Merge Sort (Ordenamiento por Mezcla)

El algoritmo **Merge Sort** sigue fielmente el paradigma de Divide y Vencerás:

1. **Dividir**: Divide la secuencia de $n$ elementos a ordenar en dos subsecuencias de tamaño aproximado $n/2$.
2. **Vencer**: Ordena las dos subsecuencias de forma recursiva invocando nuevamente a Merge Sort.
3. **Combinar**: "Mezcla" (merge) las dos subsecuencias ordenadas para producir la secuencia original ya ordenada.

La recursión "toca fondo" cuando la secuencia a ordenar tiene longitud de 0 o 1, en cuyo caso simplemente se considera ordenada, ya que no hay elementos desordenados.

## Análisis de Algoritmos de "Divide y Vencerás"

Cuando un algoritmo contiene llamadas recursivas a sí mismo, a menudo podemos describir su tiempo de ejecución mediante una **ecuación de recurrencia** o **recurrencia**, que describe el tiempo total en problemas de tamaño $n$ en términos del tiempo en las llamadas a los subproblemas más pequeños.

Para el caso de Merge Sort:
- **Dividir**: Toma tiempo constante $\Theta(1)$ porque solo es calcular el punto medio del arreglo.
- **Vencer**: Resolvemos dos subproblemas de tamaño $n/2$, lo que contribuye con $2T(n/2)$ al tiempo general de ejecución.
- **Combinar**: El procedimiento de mezclar $n$ elementos toma un tiempo lineal de $\Theta(n)$.

Por lo tanto, la ecuación de recurrencia para Merge Sort tomando los tiempos limitantes es:
$T(n) = 2T(n/2) + \Theta(n)$

Al resolver esta recurrencia, descubrimos que el tiempo de ejecución de Merge Sort en el peor caso, es de **$\Theta(n \lg n)$**. Esto representa una mejora muy grande comparado al $\Theta(n^2)$ de Insertion Sort cuando $n$ empieza a ser grande.
