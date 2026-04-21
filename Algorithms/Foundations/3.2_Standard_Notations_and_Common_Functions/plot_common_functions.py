# Para ejecutar este código usando el entorno virtual de la raíz del proyecto, usa:
# source ../../../.venv/bin/activate && python3 plot_common_functions.py
# O alternativamente:
# ../../../.venv/bin/python3 plot_common_functions.py

import matplotlib.pyplot as plt
import numpy as np
import math
import os

# Establecer estilo visual bonito
plt.style.use('ggplot')

# Configurar valores n en varios rangos
n_small = np.linspace(1, 10, 400)
n_large = np.linspace(1, 100, 400)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ---- Gráfico 1: Comparación en entradas pequeñas (Comportamiento Inicial) ----
ax1 = axes[0]

# Logarítmica
ax1.plot(n_small, np.log2(n_small), label=r'$\lg n$', color='green')

# Lineal y polilogarítmica
ax1.plot(n_small, n_small, label=r'$n$', color='c')
ax1.plot(n_small, n_small * np.log2(n_small), label=r'$n \lg n$', color='orange')

# Polinómicas
ax1.plot(n_small, n_small**2, label=r'$n^2$', color='blue')
ax1.plot(n_small, n_small**3, label=r'$n^3$', color='purple')

# Exponencial
ax1.plot(n_small, 2**n_small, label=r'$2^n$', color='red')

# Factorial (Usamos math.gamma(n+1) para extender el factorial mapeado a array)
fact_vals = [math.gamma(x + 1) for x in n_small]
ax1.plot(n_small, fact_vals, label=r'$n!$', color='brown')

ax1.set_ylim(0, 50)
ax1.set_xlim(1, 10)
ax1.set_title("Crecimiento de Funciones Comunes (En entradas pequeñas, limite y=50)")
ax1.set_xlabel('Tamaño de entrada $n$')
ax1.set_ylabel('Tiempo o Complejidad f(n)')
ax1.legend()

# ---- Gráfico 2: La Batalla Asintótica (Crecimiento inmenso limitando polinomios vs exponenciales) ----
ax2 = axes[1]
n_mid = np.linspace(1, 20, 400)

# El orden asintótico es clave en entradas más grandes. 
ax2.plot(n_mid, n_mid**3, label=r'Polinomio: $n^3$', color='purple', linewidth=2)
ax2.plot(n_mid, 2**n_mid, label=r'Exponencial: $2^n$', color='red', linewidth=2)

ax2.set_yscale('log') # Eje y logarítmico para notar las absurdas diferencias de escala
ax2.set_xlim(1, 20)
ax2.set_title("Batalla Asintótica en Escala Logarítmica\n¡La Exponencial siempre domina al polinomio!")
ax2.set_xlabel('Tamaño de entrada $n$')
ax2.set_ylabel('Escala Logarítmica de f(n)')
ax2.legend()

plt.tight_layout()

# Guardar la imagen generada en la misma carpeta
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'common_functions_growth.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Gráfica guardada exitosamente en: {output_path}")
