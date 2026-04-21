# 4.2 Algoritmo de Strassen para Multiplicación de Matrices

La multiplicación de matrices es una operación absolutamente fundamental en el mundo de los gráficos 3D, el álgebra lineal y el Machine Learning moderno (Redes Neuronales).
Dado el producto de dos matrices cuadradas $n \times n$ (A y B) para producir la matriz C:

## La Fuerza Bruta: $\Theta(n^3)$
El método matemático que todos aprendemos en la escuela involucra 3 bucles for anidados: calcular el elemento $c_{ij}$ tomando el producto punto de la fila $i$ de A y la columna $j$ de B.
Como hay $n \times n$ elementos calculados, y cada uno toma $n$ multiplicaciones-sumas, esto produce indudablemente un $\Theta(n^3)$.

## Divide and Conquer Simple (Naive): $\Theta(n^3)$
Si fragmentamos las matrices $A$, $B$ y $C$ en 4 submatrices cada una (tamaño $n/2 \times n/2$), el cálculo de una submatriz en C se define como:
$C_{11} = A_{11} \cdot B_{11} + A_{12} \cdot B_{21}$

Es decir, la recursión de "Divide and Conquer" necesitará **8 multiplicaciones dispersas** de matrices $n/2 \times n/2$. 
Aplicando la recurrencia:
$T(n) = 8T(n/2) + \Theta(n^2)$
Usando el Teorema Maestro, descubrimos tristemente que esto equivale a $\Theta(n^{\log_2 8}) = \Theta(n^3)$. ¡Decepcionante! Matemáticamente "Divide y Vencerás" sin aplicar ingenio no mejoró en absoluto a los rudimentarios 3 bucles de fuerza bruta.

## El Algoritmo de Strassen: $\Theta(n^{\lg 7})$
En 1969, Volker Strassen descubrió que el mundo de las matemáticas estaba equivocado: no necesitábamos 8 multiplicaciones para unir los bloques. Jugando algebráicamente y haciendo 10 sumas/restas previas entre las submatrices, determinó que se podía calcular $C$ realizando **solo 7 multiplicaciones recursivas**.

La nueva ecuación de recurrencia es:
$T(n) = 7T(n/2) + \Theta(n^2)$

Por Teorema Maestro: $\Theta(n^{\log_2 7}) \approx \Theta(n^{2.81})$.
¡Para $n$ suficientemente grandes, $n^{2.81}$ aplastará sin piedad a $n^3$!

---

> [!TIP]
> **Staff L7 Insight (El Engaño Académico):**
> En la universidad, Strassen te lo exigen. En tu puesto de Arquitecto L7 (Google, NVIDIA), prohibirás Strassen para el 99.9% de los casos. ¿El motivo?
> 1. **La constante oculta**: Strassen requiere tantas adiciones esparcidas e inicialización de matrices sub-temporales, que su factor "constante" arrastra de forma brutal a su ganancia asintótica. Comercialmente, hasta matrices mayores a `N=2000`, la fuerza bruta optimizada suele ir en cabeza.
> 2. **Caches y Hardware**: Strassen destroza por completo la localidad de caché contigua. En cambio, variantes súper-optimizadas en C++/Fortran (librerías BLAS o CuBLAS) con $\Theta(n^3)$ usan **Tile/Block Matrix Multiplication**, logrando un control simétrico y maximizando los aciertos del cache de CPU L1.
> 3. **Precisión Numérica**: Multiplicar flotantes con tantas adiciones y sustracciones a nivel Strassen degrada la precisión (*Floating Point Instability*).
> 4. **Hardware dedicado**: En IA, usamos TPUs (Tensor Processing Units). Las TPUs tienen circuiterías *Systolic Arrays* que resuelven $\Theta(n^3)$ de un golpe en nanosegundos (en hardware).
> *Lección Staff:* ¡Siempre cuestiona el $\Theta(n)$ teórico a nivel físico antes de ir a Producción!
