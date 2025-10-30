import math
import tracemalloc
import time
import random

def distancia(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def par_mas_cercano(puntos):
    n = len(puntos)
    
    #Caso base 
    if n <= 3:
        min_d = float('inf')
        par = (None, None)
        for i in range(n):
            for j in range(i+1, n):
                d = distancia(puntos[i], puntos[j])
                if d < min_d:
                    min_d = d
                    par = (puntos[i], puntos[j])
        return par[0], par[1], min_d

    #split
    mid = n // 2
    mitad_x = puntos[mid][0]
    izq = puntos[:mid]
    der = puntos[mid:]

   
    p1_izq, p2_izq, d_izq = par_mas_cercano(izq)
    p1_der, p2_der, d_der = par_mas_cercano(der)


    if d_izq < d_der:
        d_min = d_izq
        par_min = (p1_izq, p2_izq)
    else:
        d_min = d_der
        par_min = (p1_der, p2_der)

    # Combinar: revisar el “strip” (zona entre mitades)
    strip = [p for p in puntos if abs(p[0] - mitad_x) < d_min]
    strip.sort(key=lambda p: p[1])

    # Comparar solo puntos cercanos en Y
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= d_min:
                break
            d = distancia(strip[i], strip[j])
            if d < d_min:
                d_min = d
                par_min = (strip[i], strip[j])

    # Devolver el mejor par encontrado
    return par_min[0], par_min[1], d_min



cantPuntos = int(input("Ingresa el numero de puntos que deseas: ")) 

tracemalloc.start()
start = time.time()

puntos = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(cantPuntos)]

print(puntos)

puntos.sort(key=lambda p: p[0])  




p1, p2, dist = par_mas_cercano(puntos)
print(f"Los puntos más cercanos son {p1} y {p2} con distancia {dist:.3f}")


end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f" Memoria actual: {current / 1024} KB; Pico: {peak / 1024} KB")
memoria = (peak / 1024) - (current / 1024)
print(f"Consumo de memoria: {memoria} ")
print(f" Tiempo de ejecución: {end - start} segundos\n")