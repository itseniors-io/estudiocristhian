import matplotlib.pyplot as plt
import numpy as np
import os

# Establecer el estilo del gráfico (fondo oscuro/transparente u otro bonito)
plt.style.use('ggplot')

# Definir el rango de valores de x (tamaño de entrada n)
n = np.linspace(1, 15, 400)

# Definir las funciones para la demostración
# Nuestra función principal f(n) = 3n^2 - 2n + 5
f_n = 3 * n**2 - 2 * n + 5

# Cota superior: c1 * g(n) -> Notación Big-O
# Supongamos g(n) = n^2, c1 = 4
c1_g_n = 4 * n**2

# Cota inferior: c2 * g(n) -> Notación Big-Omega
# Supongamos g(n) = n^2, c2 = 2
c2_g_n = 2 * n**2

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(n, f_n, label=r'$f(n)$', color='blue', linewidth=2)
ax.plot(n, c1_g_n, label=r'$c_1 g(n)$ (Cota Superior)', color='red', linestyle='--')
ax.plot(n, c2_g_n, label=r'$c_2 g(n)$ (Cota Inferior)', color='green', linestyle='--')

# Rellenar la zona entre las cotas para mostrar la región Theta
ax.fill_between(n, c2_g_n, c1_g_n, color='gray', alpha=0.2, label=r'Región $\Theta(g(n))$')

# Resaltar el punto n0 a partir del cual se cumplen las condiciones
n0 = 5
ax.axvline(x=n0, color='black', linestyle=':', label=r'$n_0$')

# Anotaciones de la gráfica
ax.set_title("Notación Asintótica (Θ, O, Ω)")
ax.set_xlabel(r'Tamaño de entrada $n$')
ax.set_ylabel(r'Tiempo / Operaciones')
ax.set_xlim([1, 15])
ax.set_ylim([0, 1000])
ax.legend()

ax.text(n0 + 0.2, 50, r'Para todo $n \geq n_0$', fontsize=10, color='black')

# Guardar la imagen generada en la misma carpeta
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'asymptotic_bounds.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Gráfica guardada en {output_path}")
