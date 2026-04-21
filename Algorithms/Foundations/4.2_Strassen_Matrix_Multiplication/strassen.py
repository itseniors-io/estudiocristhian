# Para ejecutar este código usando el entorno virtual de la raíz del proyecto, usa:
# source ../../../.venv/bin/activate && python3 strassen.py
# O alternativamente:
# ../../../.venv/bin/python3 strassen.py

import time
import numpy as np

def brute_force_multiply(A, B):
    """
    Simulación teórica de un O(n^3) clásico usando pura sumatoria en Python nativo para 
    evidenciar su debilidad (nota: jamás lo usarías así en prod).
    """
    n = len(A)
    # Por simplicidad en Python, alocamos con Numpy la matrix resultado pero operamos bruto
    C = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def strassen_recursive(A, B):
    """
    Algoritmo de Strassen. Reduce el O(n^3) a O(n^{lg 7}) ~ O(n^2.81).
    Sólo se ha programado para soportar tamaños de matrices de n = 2^k.
    """
    n = len(A)
    # Caso Base (Fallback). En implementaciones reales, no llegaríamos a n=1 sino
    # que retornaríamos a fuerza bruta cuando n < 64 para evitar constante alta.
    if n == 1:
        return A * B

    # Paso de DIVIDE
    mid = n // 2
    A11, A12 = A[:mid, :mid], A[:mid, mid:]
    A21, A22 = A[mid:, :mid], A[mid:, mid:]
    
    B11, B12 = B[:mid, :mid], B[:mid, mid:]
    B21, B22 = B[mid:, :mid], B[mid:, mid:]

    # Paso de CONQUER: Las 7 míticas multiplicaciones de Strassen
    M1 = strassen_recursive(A11 + A22, B11 + B22)
    M2 = strassen_recursive(A21 + A22, B11)
    M3 = strassen_recursive(A11, B12 - B22)
    M4 = strassen_recursive(A22, B21 - B11)
    M5 = strassen_recursive(A11 + A12, B22)
    M6 = strassen_recursive(A21 - A11, B11 + B12)
    M7 = strassen_recursive(A12 - A22, B21 + B22)

    # Paso COMBINE
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Ensamblamos la matriz
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

if __name__ == "__main__":
    # Generar matrices aleatorias de tamaño n = 64 (potencia de 2)
    # Aumentar este número evidenciaría la ganancia de Strassen, pero
    # la implementación en bucles puros para el Naive puede tardar mucho.
    n = 64
    A = np.random.randint(1, 10, size=(n, n))
    B = np.random.randint(1, 10, size=(n, n))

    print("="*70)
    print(f"MULTIPLICACIÓN DE MATRICES (N={n}) - DECONSTRUYENDO A STRASSEN")
    print("="*70)

    # 1. FUERZA BRUTA DE LIBRO (O(n^3))
    t0 = time.perf_counter()
    res_brute = brute_force_multiply(A, B)
    t_brute = time.perf_counter() - t0

    # 2. ALGORITMO DE STRASSEN (O(n^2.81))
    t0 = time.perf_counter()
    res_strassen = strassen_recursive(A, B)
    t_strassen = time.perf_counter() - t0

    # 3. L7 REALITY CHECK: EL CAMINO DEL SENIOR/STAFF (Optimizado C en Numpy, BLAS)
    t0 = time.perf_counter()
    res_numpy = np.dot(A, B)  # Usa Hardware y Cache Tiling (en el engine de C)
    t_numpy = time.perf_counter() - t0

    # Validación de sanidad
    assert np.array_equal(res_brute, res_strassen) and np.array_equal(res_brute, res_numpy), "Los resultados no coinciden!"

    print("\n[RESULTADOS]")
    print(f"1. Fuerza Bruta (Triple Bucle FOR): {t_brute * 1000:.2f} ms")
    print(f"2. Algoritmo de Strassen (Recursión): {t_strassen * 1000:.2f} ms")
    print(f"3. Algoritmo BLAS Interno (np.dot):   {t_numpy * 1000:.4f} ms")

    print("\n-> Apreciación L7:")
    print("Aunque matemáticamente Strassen (2.81) vence al (3.0),")
    print("¡la sobrecarga de memoria del Python recursivo lo hace sumamente lento en la práctica!")
    print("Mientras tanto, la función integrada es literalmente inmedible (por Tiling cache y C).")
