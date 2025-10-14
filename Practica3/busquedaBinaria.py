import tracemalloc
import time

def busquedaBinariaRec( arreglo ,numeroBuscar, inicio, final):

    if (inicio > final):
        return -1
    
    mid = (inicio + final) // 2

    if( numeroBuscar  == arreglo[mid]):
        return mid
    if( numeroBuscar < arreglo[mid]):
        return busquedaBinariaRec(arreglo, numeroBuscar, inicio, mid - 1 )
    if (numeroBuscar > arreglo[mid]):
        return busquedaBinariaRec(arreglo, numeroBuscar, mid + 1, final )
    

def busquedaBinariaIt( arreglo, numeroBuscar):
    inicio = 0
    fin = len(arreglo) -1
    while inicio <= fin :
        mid = (inicio+fin) // 2
        if(numeroBuscar == arreglo[mid]):
            return mid
        if(numeroBuscar < arreglo[mid]):
            fin = mid - 1
        if(numeroBuscar > arreglo[mid]):
            inicio = mid + 1
            
    return -1


sizeArr = int(input("Ingresa el tamaño del arreglo que deseas: ")) + 1
numeroBuscar = int(input("Ingresa el numero que deseas buscar: "))

arr = list(range(1, sizeArr))
size = len(arr) -1
print(arr)

tracemalloc.start()
start = time.time()

print("Solucion recursiva:")
indiceRec = busquedaBinariaRec(arr, numeroBuscar, 0, size)
print(f"Elemento {numeroBuscar} encontrado en posicion {indiceRec}")

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f" Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
memoriaRecursiva = (peak / 1024) - (current / 1024)
print(f"Consumo de memoria: {memoriaRecursiva} ")
print(f" Tiempo de ejecución: {end - start} segundos\n")

tracemalloc.start()
start = time.time()

indiceIt = busquedaBinariaIt(arr, numeroBuscar)
print(f"Elemento {numeroBuscar} encontrado en posicion {indiceIt}")

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Solucion recursiva:")
print(f" Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
memoriaIterativa = (peak / 1024) - (current / 1024)
print(f"Consumo de memoria: {memoriaIterativa} ")
print(f" Tiempo de ejecución: {end - start} segundos\n")