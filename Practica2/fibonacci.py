import tracemalloc
import time

numero = int(input("Ingrese un numero para obtener fibonacci: "))

start = time.time()
tracemalloc.start()


def fibonacci(n):
    
    if( n <= 1 ):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(numero))

current, peak = tracemalloc.get_traced_memory()
print(f"Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
tracemalloc.stop()
end = time.time()
print(f"Tiempo de ejecución: {end - start} segundos")