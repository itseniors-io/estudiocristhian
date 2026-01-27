import time
import random

def busqueda_lineal(arr, objetivo):
    """
    Algoritmo O(n): Revisa cada elemento uno por uno.
    Simple de implementar, pero lento a gran escala.
    """
    for i, valor in enumerate(arr):
        if valor == objetivo:
            return i
    return -1

def busqueda_binaria(arr, objetivo):
    """
    Algoritmo O(log n): Divide el espacio de búsqueda a la mitad en cada paso.
    Requiere que la lista esté ORDENADA.
    """
    izquierda, derecha = 0, len(arr) - 1
    pasos = 0
    
    while izquierda <= derecha:
        pasos += 1
        medio = (izquierda + derecha) // 2
        # print(f"Paso {pasos}: Buscando entre índices {izquierda} y {derecha}") # Descomentar para debug
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
            
    return -1

def demostracion_staff():
    """
    Simulación de impacto a escala (Persona L7).
    Comparamos el rendimiento cuando el dataset crece.
    """
    # Escenario: 10 millones de usuarios (IDs ordenados)
    tamano_dataset = 10_000_000
    print(f"--- Generando dataset de {tamano_dataset:,} usuarios simulados ---")
    # Generamos una lista ordenada (range produce una secuencia ordenada)
    # Usamos range directo para no consumir toda la RAM generando la lista real si no es necesario para el ejemplo,
    # pero para medir la búsqueda necesitamos acceso por índice, así que convertimos a lista (costoso en RAM, tradeoff aceptado para demo).
    usuarios = list(range(tamano_dataset))
    
    objetivo = 9_999_999 # El peor caso: último elemento
    
    print("\n--- Escenario 1: Búsqueda Lineal (La forma ingenua) ---")
    inicio = time.time()
    idx = busqueda_lineal(usuarios, objetivo)
    fin = time.time()
    print(f"Encontrado en índice: {idx}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")
    print("Nota: Si duplicamos los usuarios, este tiempo se duplicará.")

    print("\n--- Escenario 2: Búsqueda Binaria (La forma optimizada) ---")
    inicio = time.time()
    idx = busqueda_binaria(usuarios, objetivo)
    fin = time.time()
    print(f"Encontrado en índice: {idx}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")
    print("Nota: Si duplicamos los usuarios, esto solo tomará 1 micro-paso más.")

if __name__ == "__main__":
    demostracion_staff()
