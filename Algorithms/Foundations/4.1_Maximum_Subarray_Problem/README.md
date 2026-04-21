# 4.1 El Problema del Subarreglo Máximo (The Maximum-Subarray Problem)

Imagina que tienes una serie de cambios en el precio de una acción día a día. Tu objetivo es encontrar la porción contigua de días que te hubiera dado el mayor margen de ganancias. Cuidado: no puedes simplemente comprar en el pico histórico más bajo y vender en el más alto si ocurrieron en el "pasado vs futuro"; el orden temporal (la contigüidad) importa.
Esto se reduce al **Maximum-Subarray Problem**: encontrar el subarreglo contiguo no vacío cuyos valores sumen el peso máximo.

## La Fuerza Bruta: $O(n^2)$
El abordaje más primitivo evalúa cada subarreglo posible. Escoge una posición inicial y luego chequea todas las subsecuentes. Esto cuesta matemáticamente $Tiempo = \Theta(n^2)$ lo cual, como sabemos, penaliza terriblemente al escalar.

## Divide-and-Conquer: $O(n \log n)$
Para superar la fuerza bruta, aplicamos *Divide y Vencerás*.
Se rompe el arreglo original en 2 mitades. El subarreglo máximo entonces OBLIGATORIAMENTE debe radicar exactitamente en uno de los siguientes 3 sitios:
1. Absolutamente incrustado en el **lado izquierdo** (subarreglo izquierdo pleno).
2. Absolutamente incrustado en el **lado derecho** (subarreglo derecho pleno).
3. **Cruzando la partición media** (arrastrando cola desde el lado izquierdo pero metiéndose al interior del lado derecho).

### Implementando las Piezas
Para resolver los sitios `1` y `2` invocamos simplemente recursión (`maximum_subarray()` sobre mitades menores).
Para resolver el sitio `3` de cruce central (`crossing_subarray`), se evalúa linealmente la expansión hacia la izquierda e izquierda de dicho medio hasta coger el subhíbrido más alto costando $\Theta(n)$.
La ecuación del algoritmo termina viéndose familiarmente como Merge Sort:
$T(n) = 2T(n/2) + \Theta(n) \Rightarrow \Theta(n \log n)$.

---

> [!TIP]
> **Staff L7 Insight (El Techo Falso vs Techo Verdadero):**
> En Google o Stripe es una ley no escrita: *No apliques Divide and Conquer ciegamente a no ser que tu sistema esté físicamente quebrado y necesites clústers paralelos (Data Sharding/MapReduce).*
> El máximo subarreglo sí se rebaja a $O(n \log n)$ con recursión, ¡pero un arquitecto siempre buscará el legendario **Algoritmo de Kadane** (Programación Dinámica)!
> Kadane resuelve el máximo subarreglo barriendo con un ciclo `for` en $\Theta(n)$ **en una sola pasada** y de forma iterativa, reduciendo la penalidad temporal del $\lg n$ y con gasto de memoria exacto $O(1)$ sin sobrecargar el Stack Recursivo. Divide and Conquer en una sola máquina en este caso resulta innecesario ante Programación Dinámica In-Place, enseñándonos a nunca idolatrar ciegamente una categoría de diseño de algoritmos si un modelo iterativo vence sin costos.
