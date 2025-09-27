import tracemalloc
import time


sizeArr = int(input("Ingresa el tamaño del arreglo que deseas: ")) + 1
numeroBuscar = int(input("Ingresa el numero que deseas buscar: "))

arr = list(range(1, sizeArr))

start = time.time()
tracemalloc.start()

arr.sort()

def busquedaBinaria(arr,numeroBuscar,inicio,final): 
    
    if (inicio > final):
        return -1
    # size = final - 1
    # print(size)
    mid = (inicio + final) // 2
    
    # print(f"idx {mid} value {arr[mid]}")
    # print(f"Inicio {inicio} Final {final} Mid {mid}")

    if(arr[mid] == numeroBuscar):
        return arr[mid]
    if(numeroBuscar < arr[mid]):
        return busquedaBinaria(arr,numeroBuscar,inicio,mid-1)
    if(numeroBuscar > arr[mid]):
        return busquedaBinaria(arr,numeroBuscar,mid+1,final)
    if(numeroBuscar > final or numeroBuscar < inicio):
        return -1
 

# def busquedaBinaria(arr,numeroBuscar):
size = len(arr)
    

posicion = busquedaBinaria(arr, numeroBuscar,0, size)
    
if(posicion != -1):
    print(f"Numero encontrado en la posicion {posicion}")
else:
    print(f"Numero no encontrado")



current, peak = tracemalloc.get_traced_memory()
print(f"Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
tracemalloc.stop()
end = time.time()
print(f"Tiempo de ejecución: {end - start} segundos")

