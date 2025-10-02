import tracemalloc
import time
import random

sizeArr = int(input("Ingresa el tamaño del arreglo que deseas: ")) + 1

arr = [random.randint(1, 100) for _ in range(sizeArr)]


start = time.time()
tracemalloc.start()

def merge_sort(lista):
    
    if len(lista) <= 1:
        return lista

    
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    
    return merge(izquierda, derecha)


def merge(izquierda, derecha):
    resultado = []
    i = j = 0

   
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

print(merge_sort(arr))

current, peak = tracemalloc.get_traced_memory()
print(f"Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
total = (peak / 1024) - (current /1024)
print(f"total: {total} ")
tracemalloc.stop()
end = time.time()
print(f"Tiempo de ejecución: {end - start} segundos")