import tracemalloc
import time
import random

def contarInversiones(arr):
    # caso base
    if len(arr) <= 1:
        return arr, 0

    # split
    mid = len(arr) // 2
    izquierda, inv_izq = contarInversiones(arr[:mid])
    derecha, inv_der = contarInversiones(arr[mid:])

    combinado, inv_cruz = merge_contando(izquierda, derecha)

    return combinado, inv_izq + inv_der + inv_cruz


def merge_contando(izq, der):
    i = j = inv = 0
    combinado = []

    #contar los elementos 
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            combinado.append(izq[i])
            i += 1
        else:
            combinado.append(der[j])
            j += 1
            
            inv += len(izq) - i

    #combinacion arreglos
    combinado += izq[i:]
    combinado += der[j:]


    return combinado, inv


sizeArr = int(input("Ingresa el tamaño del arreglo que deseas: ")) 

arr = [random.randint(0, 100) for _ in range(sizeArr)] 

print(arr)



tracemalloc.start()
start = time.time()



inversiones = contarInversiones(arr)
print(inversiones)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f" Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
memoria = (peak / 1024) - (current / 1024)
print(f"Consumo de memoria: {memoria} ")
print(f" Tiempo de ejecución: {end - start} segundos\n")