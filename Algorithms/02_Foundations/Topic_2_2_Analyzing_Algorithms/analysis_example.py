import time
import random

def insertion_sort(arr):
    """
    Ordenamiento por inserción.
    Tiempo esperado (peor caso): O(n^2).
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def measure_time(sort_function, data):
    """Mide el tiempo de ejecución de una función de ordenamiento."""
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time

def run_analysis():
    """
    Ejecuta el análisis comparando el tiempo de ejecución
    con diferentes tamaños de entrada (n).
    """
    input_sizes = [100, 500, 1000, 2000, 3000]
    times = []

    print(f"{'Input Size (n)':<15} | {'Time (seconds)':<15}")
    print("-" * 35)

    for n in input_sizes:
        # Generar una lista aleatoria de tamaño n
        data = [random.randint(0, 10000) for _ in range(n)]
        
        # Medir tiempo (usamos una copia para no afectar mediciones futuras si hubieran más)
        exec_time = measure_time(insertion_sort, data.copy())
        times.append(exec_time)
        
        print(f"{n:<15} | {exec_time:.6f}")

    print("\nAnálisis:")
    print("Observa cómo el tiempo aumenta a medida que crece n.")
    print("Para Insertion Sort, si duplicamos n, el tiempo se cuadruplica aproximadamente (O(n^2)).")

if __name__ == "__main__":
    run_analysis()
