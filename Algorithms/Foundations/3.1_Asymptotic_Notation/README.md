# 3.1 Notación Asintótica (Asymptotic Notation)

La notación asintótica es una herramienta matemática utilizada en ciencias de la computación para describir el comportamiento límite del tiempo de ejecución (o complejidad espacial) de un algoritmo cuando el tamaño de la entrada $n$ tiende a infinito. Nos permite clasificar algoritmos según su rendimiento e ignorar las constantes y los términos de menor orden.

Típicamente utilizamos estas notaciones para analizar algoritmos de forma teórica, sin enfrascarnos en limitaciones exactas de hardware o conteos de ciclos.

---

## 1. Notación $\Theta$ (Theta) -> Cota Ajustada (Tight Bound)
La notación $\Theta$ delimita una función por **arriba y por abajo**. Si una función $f(n) = \Theta(g(n))$, significa que $f(n)$ crece exactamente a la misma tasa que $g(n)$ asintóticamente.

**Definición matemática:**
$f(n) = \Theta(g(n))$ si existen constantes positivas $c_1, c_2, n_0$ tales que:
$0 \leq c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$ para todo $n \geq n_0$.

**Ejemplo:**
Para $f(n) = 3n^2 - 2n + 5$:
- A medida que $n \to \infty$, el término $n^2$ domina al resto.
- Por lo tanto, $f(n) = \Theta(n^2)$.

> [!TIP]
> **Staff L7 Insight:** En Big Tech (Google, AWS, Meta), la notación $\Theta$ determina viabilidad en el **Capacity Planning**. A escala planetaria, los factores constantes de desempeño del servidor se vuelven minúsculos comparados al volumen de los datos. Si tu pipeline de procesamiento masivo o validación distribuida es fundamentalmente $\Theta(n^2)$, fallará y experimentará cuellos de botella con seguridad matemática a bajo millares de nodos, sin importar qué tan optimizado esté el código o si programas en C++ o Rust en lugar de Python. 

---

## 2. Notación $O$ (Big-O) -> Cota Superior (Upper Bound)
La notación $O$ proporciona una **cota superior asintótica**. Nos da la tasa máxima de crecimiento, lo que significa que en el peor de los casos, el algoritmo tomará *a lo sumo* esta cantidad de tiempo.

**Definición matemática:**
$f(n) = O(g(n))$ si existen constantes positivas $c, n_0$ tales que:
$0 \leq f(n) \leq c \cdot g(n)$ para todo $n \geq n_0$.

**Ejemplo:**
Si un algoritmo toma $f(n) = 3n^2 - 2n + 5$ pasos, está limitado superiormente por $n^2$, así que $f(n) = O(n^2)$. Técnicamente, también es correcto decir que $f(n) = O(n^3)$ porque $n^3$ crece más rápido que $n^2$.

> [!TIP]
> **Staff L7 Insight:** Los ingenieros de nivel Staff se obsesionan particularmente con la cota Worst-Case $O(g(n))$ para poder proveer fiabilidad sistémica y **Service Level Objectives (SLOs) del Tail-Latency** (p.ej, el percentil p99.9). Los algoritmos que son extremadamente veloces "en promedio" pero poseen un peor caso severo pueden experimentar caídas catastróficas transitorias ('outages'). Por esto mismo Google suele evitar estrategias de Hash-table que caigan en clustering lineal lento, reemplazándolos con árboles u otras estructuras para evitar que un retraso inesperado demuela servicios de alta densidad en servidores Frontend de RPC síncronos.

---

## 3. Notación $\Omega$ (Big-Omega) -> Cota Inferior (Lower Bound)
La notación $\Omega$ proporciona una **cota inferior asintótica**. Significa que el algoritmo tomará *por lo menos* esta cantidad de tiempo.

**Definición matemática:**
$f(n) = \Omega(g(n))$ si existen constantes positivas $c, n_0$ tales que:
$0 \leq c \cdot g(n) \leq f(n)$ para todo $n \geq n_0$.

**Ejemplo:**
Para el algoritmo de ordenamiento por inserción (insertion sort), el tiempo de ejecución en el mejor de los casos (cuando el arreglo ya está ordenado) es $\Omega(n)$.

> [!TIP]
> **Staff L7 Insight:** Manejar las cotas base $\Omega$ ahorra innumerables horas e inversiones erróneas de dinero en Google. Si entiendes que la arquitectura inter-continental de tu aplicación tiene una limitante $\Omega(n)$ física impuesta por la latencia del cable de fibra óptica y transferencia bruta de red, cierras cualquier debate engañoso de optimización en memoria RAM y de inmediato buscas rediseñar por completo la forma del negocio (procesan la data en el perímetro vía edge-computing, o aplican compresión delta superior), encriptandolo como "Límite Fundamental".

---

## 4. Notación $o$ (Little-o) -> Cota Superior Estricta
A diferencia de Big-O, que puede ser una cota ajustada, el little-o representa una cota superior que **no es asintóticamente ajustada**.

$f(n) = o(g(n))$ significa que $f(n)$ crece estrictamente de forma más lenta que $g(n)$.
Ejemplo: $2n = o(n^2)$, pero $2n^2 \neq o(n^2)$.

## 5. Notación $\omega$ (Little-omega) -> Cota Inferior Estricta
De manera similar al little-o, la little-omega representa una cota inferior que **no es asintóticamente ajustada**.

$f(n) = \omega(g(n))$ significa que $f(n)$ crece estrictamente más rápido que $g(n)$.
Ejemplo: $n^2 = \omega(n)$, pero $n^2 \neq \omega(n^2)$.

---

## Analogía con los Números Reales

Puedes imaginar las notaciones asintóticas como operadores relacionales que comparan el crecimiento de las funciones:

*   $f(n) = O(g(n)) \approx a \le b$
*   $f(n) = \Omega(g(n)) \approx a \ge b$
*   $f(n) = \Theta(g(n)) \approx a = b$
*   $f(n) = o(g(n)) \approx a < b$
*   $f(n) = \omega(g(n)) \approx a > b$

---

## Visualizando las Cotas Asintóticas

Hemos proporcionado un script de Python en esta carpeta llamado `plot_asymptotic.py`. 
Al ejecutarlo usando `python3 plot_asymptotic.py` (requiere tener instalado `matplotlib` y `numpy`), se generará la imagen `asymptotic_bounds.png`. Esta gráfica muestra de forma visual cómo $f(n)$ se encuentra atrapada entre los límites de $c_1 g(n)$ y $c_2 g(n)$, para demostrar la región $\Theta$.

![Asymptotic Bounds](asymptotic_bounds.png) *(Una vez que generes la gráfica corriendo el script, la imagen aparecerá aquí)*
