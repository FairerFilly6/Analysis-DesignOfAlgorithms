import tracemalloc
import time
import random

sizeArr = int(input("Ingresa el tamaño del arreglo que deseas: ")) + 1

arr = [random.randint(1, 100) for _ in range(sizeArr)]


start = time.time()
tracemalloc.start()

def merge_sort(lista):
    # Caso base: una lista de un solo elemento ya está ordenada
    if len(lista) <= 1:
        return lista

    # Dividimos la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    # Mezclamos ambas mitades ya ordenadas
    return merge(izquierda, derecha)


def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    # Mientras haya elementos en ambas listas
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar lo que quede en izquierda o derecha
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

print(merge_sort(arr))

current, peak = tracemalloc.get_traced_memory()
print(f"Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
tracemalloc.stop()
end = time.time()
print(f"Tiempo de ejecución: {end - start} segundos")