# Para ejecutar este código usando el entorno virtual de la raíz del proyecto, usa:
# source ../../../.venv/bin/activate && python3 visualize_recurrence.py
# O alternativamente:
# ../../../.venv/bin/python3 visualize_recurrence.py

import os

def display_recursion_tree(n, current_depth=0, max_n_trigger=0):
    """
    Función educacional que NO soluciona un problema de dividir y vencerás.
    En vez de eso, simula el 'Árbol de Recursión' que modela el algoritmo
    y lo imprime visualmente para poder razonar sobre el Master Theorem en consola.
    
    Esta variante simula una Ecuación de Recurrencia común tipo: T(n) = 2T(n/2) + O(n)
    """
    indent = "    " * current_depth
    prefix = "L" + str(current_depth) + " " + "├─ " if current_depth > 0 else "Raíz: "
    
    # Costo base o Combine, simulamos O(n)
    cost = f"+ Costo Combine O({n})" if n > 0 else ""
    
    print(f"{indent}{prefix}T({n}) {cost}")
    
    if n > max_n_trigger:
        # Aquí simula los 2 llamados T(n/2) recursivos a subproblemas
        display_recursion_tree(n // 2, current_depth + 1, max_n_trigger)
        display_recursion_tree(n // 2, current_depth + 1, max_n_trigger)

if __name__ == "__main__":
    print("="*60)
    print("SIMULACIÓN DE ÁRBOL DE RECURSIÓN")
    print("Para la Ecuación Matemática: T(n) = 2*T(n/2) + O(n)")
    print("="*60)
    
    # Inicia con una ejecución simulada de un listado de tamaño 16.
    # Tocará fondo ('base case') cuando n quede en 1.
    display_recursion_tree(16, max_n_trigger=1)
    
    print("\nVisualizando lo que sucede, se puede apreciar gráficamente la")
    print("naturaleza fractal y el costo del 'Combine' en cada etapa ramificada.")
    print("En niveles más bajos (L4), tenemos innumerables instancias super pequeñas.\n")
