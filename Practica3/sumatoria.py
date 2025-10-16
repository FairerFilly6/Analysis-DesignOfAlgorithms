import tracemalloc
import time

def sumatoriaRecursiva(numero):

    if numero == 0:
        return 0
    else:
        return numero % 10 + sumatoriaRecursiva(numero // 10)
    
def sumatoriaIterativa(numero):
    sumatoria = 0
    while numero > 0:
        sumatoria += numero % 10
        numero //= 10
    return sumatoria

numero = int(input("Ingrese el numero del que desea obtener la sumatoria: "))

tracemalloc.start()
start = time.time()
sumatoriaRecursivaA = sumatoriaRecursiva(numero)
end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("Solucion recursiva:")
print(f" Resultado: {sumatoriaRecursivaA}")
print(f" Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
memoriaRecursiva = (peak / 1024) - (current / 1024)
print(f"Consumo de memoria: {memoriaRecursiva} ")
print(f" Tiempo de ejecución: {end - start} segundos\n")

tracemalloc.start()
start = time.time()
sumatoriaIterativaB = sumatoriaIterativa(numero)
end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("Solucion iterativa:")
print(f"Resultado: {sumatoriaIterativaB}")
print(f"Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
memoriaIterativa = (peak / 1024) - (current / 1024)
print(f"Consumo de memoria: {memoriaIterativa} ")
print(f"Tiempo de ejecución: {end - start} segundos")