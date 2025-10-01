import tracemalloc
import time


sizeArr = int(input("Ingresa el tamaño del arreglo que deseas: ")) + 1

import random

arr = [random.randint(1, 100) for _ in range(sizeArr)]


start = time.time()
tracemalloc.start()


def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    return arr



print(bubblesort(arr))

current, peak = tracemalloc.get_traced_memory()
print(f"Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
tracemalloc.stop()
end = time.time()
print(f"Tiempo de ejecución: {end - start} segundos")