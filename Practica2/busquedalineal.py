import tracemalloc
import time


sizeArr = int(input("Ingresa el tamaño del arreglo que deseas: ")) + 1
numeroBuscar = int(input("Ingresa el numero que deseas buscar: "))

arr = list(range(1, sizeArr))

start = time.time()
tracemalloc.start()

def busquedaLineal(arr, numeroBuscar):
    posicionNumero = -1
    for idxb, numero in enumerate(arr):
        if(numero == numeroBuscar):
            posicionNumero = idxb
            return posicionNumero
    return posicionNumero


posicion = busquedaLineal(arr, numeroBuscar)
    
if(posicion != -1):
    print(f"Numero encontrado en la posicion {posicion}")
else:
    print(f"Numero no encontrado")



current, peak = tracemalloc.get_traced_memory()
print(f"Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
tracemalloc.stop()
end = time.time()
print(f"Tiempo de ejecución: {end - start} segundos")