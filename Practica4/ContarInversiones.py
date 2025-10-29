import tracemalloc
import time


def contarInversiones(arr):
    # Si el arreglo tiene 0 o 1 elementos, no hay inversiones
    if len(arr) <= 1:
        return arr, 0

    # Dividir el arreglo a la mitad
    mid = len(arr) // 2
    izquierda, inv_izq = contarInversiones(arr[:mid])
    derecha, inv_der = contarInversiones(arr[mid:])

    # Combinar ambas mitades y contar las inversiones cruzadas
    combinado, inv_cruz = merge_contando(izquierda, derecha)

    # Retornar el arreglo ordenado y el total de inversiones
    return combinado, inv_izq + inv_der + inv_cruz


def merge_contando(izq, der):
    i = j = inv = 0
    combinado = []

    # Mientras haya elementos en ambas mitades
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            combinado.append(izq[i])
            i += 1
        else:
            combinado.append(der[j])
            j += 1
            # Todos los elementos restantes en izq[i:] son mayores que der[j-1]
            inv += len(izq) - i

    # Agregar los elementos restantes
    combinado += izq[i:]
    combinado += der[j:]

    return combinado, inv


# Ejemplo de uso
arr = [2, 4, 1, 3, 5]
_, total = contarInversiones(arr)
print(f"El número total de inversiones es: {total}")




# tracemalloc.start()
# start = time.time()


arreglo = [3,4,1,0]

inversiones = contarInversiones(arreglo)
print(inversiones)

# end = time.time()
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f" Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
# memoria = (peak / 1024) - (current / 1024)
# print(f"Consumo de memoria: {memoria} ")
# print(f" Tiempo de ejecución: {end - start} segundos\n")