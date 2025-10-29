import tracemalloc
import time


def quickSelect(arr, k, inicio, fin):
    #caso base
    if inicio == fin:
        return arr[inicio]

    pivote = arr[fin]
    p = inicio


    for i in range(inicio, fin):
        if arr[i] < pivote:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1

    #siempre que un ciclo se acaba se cambia el arreglo
    arr[p], arr[fin] = arr[fin], arr[p]

    #casos recursivos
    if p == k - 1:
        return arr[p]
    elif p > k - 1:
        return quickSelect(arr, k, inicio, p - 1)
    else:
        return quickSelect(arr, k, p + 1, fin)



sizeArr = int(input("Ingresa el tamaño del arreglo que deseas: ")) + 1
numeroBuscar = int(input("Ingresa el k-esimo elemento que deseas buscar: "))

arr = list(range(1, sizeArr))
size = len(arr) -1

tracemalloc.start()
start = time.time()

kesimoElemento = quickSelect(arr, numeroBuscar, 0, size)

print(f"El {numeroBuscar} elemento mas pequeño es {kesimoElemento}")

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f" Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
memoria = (peak / 1024) - (current / 1024)
print(f"Consumo de memoria: {memoria} ")
print(f" Tiempo de ejecución: {end - start} segundos\n")


    


