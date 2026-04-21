# 3.2 Standard Notations and Common Functions

Este capítulo repasa la notación y el comportamiento asintótico de funciones matemáticas comunes que surgen constantemente a la hora de analizar algoritmos.

## 1. Monotonicidad
* Una función es **monótonamente creciente** si $m \leq n \implies f(m) \leq f(n)$.
* Una función es **estrictamente creciente** si $m < n \implies f(m) < f(n)$.
Las funciones de tiempo de ejecución de la mayoría de algoritmos suelen tener tiempos de ejecución monótonamente crecientes (a mayor entrada, más o igual complejidad, pero nunca menos).

> [!TIP]
> **Staff L7 Insight:** A nivel de sistemas de alto desempeño y micro-arquitectura (Kernels, Drivers de hardware), la monotoniciad garantiza éxito para los procesadores modernos. Cuando los patrones de acceso de memoria a granel crecen monotónicamente (como arreglos contiguos iterados hacia adelante), los **Hardware Prefetchers** lograrán casi un 100% de Tasa de Aciertos en Caché (Cache hit rate). Los saltos aleatorios no-monotónicos causan Cache Misses de nivel L3, los cuales cuestan más ciclos de CPU que el algoritmo matemático en sí.

## 2. Pisos (Floors) y Techos (Ceilings)
Para cualquier número real $x$:
* **Piso (Floor) $\lfloor x \rfloor$**: El número entero más grande menor o igual a $x$.
* **Techo (Ceiling) $\lceil x \rceil$**: El número entero más pequeño mayor o igual a $x$.
Son fundamentales porque el tamaño de la entrada e índices de estructuras de datos suelen ser enteros. 

## 3. Aritmética Modular
Para un entero $a$ y un entero positivo $n$:
* $a \pmod n$ es el remanente de la división de $a$ entre $n$.
* Si $(a \pmod n) = (b \pmod n)$, decimos que $a \equiv b \pmod n$.

## 4. Polinomios
Un polinomio de grado $d$ es $P(n) = \sum_{i=0}^d a_i n^i$, donde $a_d > 0$.
* Su límite asintótico es **$P(n) = \Theta(n^d)$**.
Cualquier función polinómica es acotada por su término dominante ignorando constantes y coeficientes menores.

> [!TIP]
> **Staff L7 Insight:** Teóricamente $\Theta(n \log n)$ vence siempre a $\Theta(n^2)$. Pero los expertos saben de la "Latencia vs Throughput". Un $\Theta(n^2)$ con constantes increíblemente minúsculas, arreglos de memoria contiguos y completamente empaquetables dentro de instrucciones **SIMD de vectorización**, con frecuencia aplasta con creces algoritmos $O(n \log n)$ como red-black trees tradicionales en la vida real que dependen de saltos inmensos entre punteros para tamaños de $n$ sub-10.000 (algo bastante común en chunks distribuidos).

## 5. Exponenciales
* Propiedades base: $a^{m+n} = a^m a^n$, $(a^m)^n = a^{mn}$.
* Para cualquier constante real constante positiva $a > 1$ y $b > 0$, siempre se cumple que:
  $\lim_{n \to \infty} \frac{n^b}{a^n} = 0$
* **Fundamental:** Cualquier exponencial con base mayor a 1 crece estrictamente más rápido que cualquier término polinómico. ($n^b = o(a^n)$).

## 6. Logaritmos
Suelen denotarse comúnmente con:
* $\lg n = \log_2 n$ (logaritmo binario).
* $\ln n = \log_e n$ (logaritmo natural).
* $\lg^k n = (\lg n)^k$ (polilogaritmo).
* $\lg \lg n = \lg(\lg n)$ (composición).

Reglas fundamentales:
* Cualquier polinomio de forma $n^a$ para $a > 0$ crece asintóticamente más rápido que cualquier función polilogarítmica $\lg^b n$. ($\lg^b n = o(n^a)$).
* Cambio de base es constante (no afecta asintóticamente el análisis Big-O).

## 7. Factoriales
$n! = 1 \cdot 2 \cdot 3 \cdots n = n(n-1)!$ para $n \geq 1$ ($0! = 1$).
Una cota para factoriales es provista por la aproximación de **Stirling**:
* $n! \approx \sqrt{2 \pi n} \left(\frac{n}{e}\right)^n$
Demostrando que un factorial crece más que una función exponencial pero menos que $n^n$.

## 8. Logaritmo Iterado ($\lg^* n$)
* El logaritmo iterado $\lg^* n$ es una de las funciones de crecimiento más extremadamente lentas. ¡A nivel práctico (físico/universo observable) $\lg^* n \leq 5$ siempre! 

> [!TIP]
> **Staff L7 Insight:** En Google el Logaritmo Iterado es famoso por el algoritmo _Union-Find con Path Compression_. Este es el secreto detrás de algoritmos de Big Data que corren sobre grafos billonarios, p. ej., para rastrear qué servidores están conectados con qué usuarios a nivel internacional. Union-Find garantiza un tiempo casi absolutamente lineal gracias al milagroso comportamiento microscópico del inverso de la función de Ackermann (y sus relacionados con el Logaritmo Iterado).

## 9. Números de Fibonacci
$F_0 = 0$, $F_1 = 1$, $F_i = F_{i-1} + F_{i-2}$ para todo $i \ge 2$.
Crecen exponencialmente basados en el Golden Ratio $\phi = \frac{1 + \sqrt{5}}{2}$.
* $F_i = \Theta(\phi^i)$
