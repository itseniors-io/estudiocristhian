"""
Topic 1.2: Sorting Algorithms
Visión Staff L7: Implementación de referencia para entender los mecanismos internos.
En producción, SIEMPRE usa los built-ins del lenguaje (que suelen ser Timsort en Python),
a menos que tengas una restricción de hardware muy específica.
"""

from typing import List
import time
import random

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort: O(n^2)
    
    Staff View:
    - Eficiente para N pequeño (< 50 elementos).
    - Cache-friendly: Accede a memoria de forma contigua.
    - Úsalo cuando: Tienes un stream de datos 'casi' ordenado y recibes un dato nuevo tardío.
    """
    # Trabajamos "in-place" (O(1) memoria auxiliar)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Movemos los elementos mayores que 'key' una posición adelante
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort: O(n log n)
    
    Staff View:
    - Divide y vencerás.
    - Predecible: Su rendimiento no depende de si el input está ordenado o no.
    - Trade-off: Consumo de memoria O(n). Crea nuevas listas constantemente.
      En sistemas con memoria restringida, esto puede causar OOM (Out of Memory).
    """
    if len(arr) <= 1:
        return arr

    # 1. Divide
    mid = len(arr) // 2
    left_half = arr[:mid]  # Ojo: El slicing en Python crea copias (consumo RAM)
    right_half = arr[mid:]

    # 2. Recursión
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 3. Merge (Conquista)
    return _merge(left_sorted, right_sorted)

def _merge(left: List[int], right: List[int]) -> List[int]:
    sorted_list = []
    i = j = 0
    
    # Comparamos y unimos
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Agregamos los remanentes (si quedan)
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# --- Ejemplo de Uso y Benchmarking (Staff Utility) ---

if __name__ == "__main__":
    # Caso 1: Lista pequeña (Donde Insertion brilla o empata)
    small_data = [random.randint(0, 100) for _ in range(20)]
    print(f"Data pequeña original: {small_data}")
    print(f"Insertion Sort: {insertion_sort(small_data.copy())}")
    
    # Caso 2: Simulación de Performance
    large_n = 5000
    large_data = [random.randint(0, 10000) for _ in range(large_n)]
    
    print(f"\n--- Benchmark (N={large_n}) ---")
    
    start = time.time()
    insertion_sort(large_data.copy())
    print(f"Insertion Sort Tiempo: {time.time() - start:.4f}s (Lento en N grande)")
    
    start = time.time()
    merge_sort(large_data.copy())
    print(f"Merge Sort Tiempo:     {time.time() - start:.4f}s (Escalable)")
    
    # Staff Note: Nota la diferencia masiva en tiempo. 
    # Para N=10,000, Insertion Sort puede ser 100x más lento que Merge Sort.
