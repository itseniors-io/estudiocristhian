# Para ejecutar este código usando el entorno virtual de la raíz del proyecto, usa:
# source ../../../.venv/bin/activate && python3 maximum_subarray.py
# O alternativamente:
# ../../../.venv/bin/python3 maximum_subarray.py

import time
import sys

def find_max_crossing_subarray(A, low, mid, high):
    """
    Rutina auxiliar (Combine) para D&C. 
    Encuentra el máximo subarreglo que deba cruzar el 'mid' inexcusablemente.
    """
    left_sum = -float('inf')
    total = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        total += A[i]
        if total > left_sum:
            left_sum = total
            max_left = i
            
    right_sum = -float('inf')
    total = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        total += A[j]
        if total > right_sum:
            right_sum = total
            max_right = j
            
    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray_dnq(A, low, high):
    """
    Desarrollo puro: Divide and Conquer. Tiempo asintótico Theta(n lg n).
    """
    # Base Case (Array de tamaño 1)
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        
        # Divide / Conquer
        left_low, left_high, left_sum = find_maximum_subarray_dnq(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray_dnq(A, mid + 1, high)
        
        # Combine Checkers
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


def kadane_algorithm(A):
    """
    Aproximación Staff/Senior puramente iterativa usando Programación Dinámica plana. 
    Tiempo T(n) = Theta(n).  Limpio, elegante y sin stack overhead.
    """
    max_so_far = -float('inf')
    current_max = 0
    start = end = s = 0
    
    for i in range(len(A)):
        current_max += A[i]
        
        if current_max > max_so_far:
            max_so_far = current_max
            start = s
            end = i
            
        # Si un segmento cae por debajo de cero, descartarlo no contribuye al futuro.
        if current_max < 0:
            current_max = 0
            s = i + 1
            
    return (start, end, max_so_far)


if __name__ == "__main__":
    sys.setrecursionlimit(10**6) # Protección a Stack Overflows tontos

    # Arreglo de cambios de valor histórico del CLRS / Stocks
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    
    # 1. DIVIDE AND CONQUER
    start_time = time.perf_counter()
    dc_res = find_maximum_subarray_dnq(A, 0, len(A) - 1)
    t_dc = time.perf_counter() - start_time
    
    # 2. KADANE'S ALGORITHM
    start_time = time.perf_counter()
    kadane_res = kadane_algorithm(A)
    t_kadane = time.perf_counter() - start_time
    
    print("="*60)
    print("THE MAXIMUM-SUBARRAY PROBLEM (Array size = {})".format(len(A)))
    print("="*60)
    
    print("\n[RESULTADOS DEL MODELO DIVIDE AND CONQUER | O(n log n)]")
    print(f"Subarreglo máximo: indices [{dc_res[0]} a {dc_res[1]}] -> Suma Máxima: {dc_res[2]}")
    print(f"Tiempo de cómputo (ns): {t_dc * 1e9:.0f}")
    
    print("\n[RESULTADOS DEL MODELO KADANE DP | O(n)]")
    print(f"Subarreglo máximo: indices [{kadane_res[0]} a {kadane_res[1]}] -> Suma Máxima: {kadane_res[2]}")
    print(f"Tiempo de cómputo (ns): {t_kadane * 1e9:.0f}")
    
    print("\n-> Apreciación Staff: Ambas arrojarán matemáticamente los mismos extremos, sin ")
    print("   embargo Kadane vence estructuralmente a todo dar por carencia de operaciones de \n   subruteo en la memoria del Call Stack y su asintótica ultra lineal bruta.")
