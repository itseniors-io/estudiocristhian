import time
import random

def merge_sort(arr):
    """
    Algoritmo Merge Sort usando el paradigma Divide y Vencerás.
    Tiempo de ejecución (todos los casos): O(n log n).
    """
    if len(arr) > 1:
        # 1. DIVIDIR: en dos mitades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 2. VENCER: ordenamos recursivamente cada mitad
        merge_sort(left_half)
        merge_sort(right_half)

        # 3. COMBINAR: mezclamos (merge) las dos mitades ordenadas
        i = j = k = 0

        # Comparamos y colocamos el menor elemento
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Si quedaron elementos en left_half, los agregamos
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Si quedaron elementos en right_half, los agregamos
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def insertion_sort(arr):
    """
    Algoritmo de inserción para poder comparar.
    Tiempo esperado (peor caso o promedio): O(n^2).
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def measure_time(sort_function, data):
    """Mide el tiempo exacto de ejecución de la función sobre un arreglo."""
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time


def run_comparison():
    """
    Compara empíricamente el tiempo de ejecución en arreglos aleatorios
    usando Insertion Sort (O(n^2)) vs Merge Sort (O(n log n)).
    """
    # Aumentamos los tamaños para ver la clara diferencia exponencial/linealítmica
    input_sizes = [1000, 2000, 4000, 8000]
    
    print("--- COMPARACION DE ALGORITMOS DE ORDENAMIENTO ---")
    print(f"{'Tamaño (n)':<12} | {'Insertion (O(n^2))':<20} | {'Merge Sort (O(n log n))':<22}")
    print("-" * 62)

    for n in input_sizes:
        # Base de datos aleatoria
        data = [random.randint(0, 100000) for _ in range(n)]
        
        # Copiamos la lista para enviar los mismos datos desordenados a ambos
        time_insertion = measure_time(insertion_sort, data.copy())
        time_merge = measure_time(merge_sort, data.copy())
        
        print(f"{n:<12} | {time_insertion:<20.6f} | {time_merge:<22.6f}")

    print("\n--- ANALISIS ---")
    print("Presta atención a cómo escala el tiempo (tiempo extra cada que N se duplica).")
    print("En Insertion Sort (O(n^2)), cuando 'n' se duplica (por ejemplo de 2000 a 4000),")
    print("el tiempo se multiplica aprox. por 4.")
    print("En Merge Sort (O(n log n)), el aumento de tiempo crece de forma muy leve y lineal logarítmica,")
    print("volviéndolo increíblemente más rápido a futuro para datasets muy grandes.")

if __name__ == "__main__":
    run_comparison()
