import math

def distancia(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def par_mas_cercano(puntos):
    n = len(puntos)
    
    # Caso base directo dentro del divide and conquer
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

    #  Dividir por la mitad
    mid = n // 2
    mitad_x = puntos[mid][0]
    izq = puntos[:mid]
    der = puntos[mid:]

    #  Resolver recursivamente
    p1_izq, p2_izq, d_izq = par_mas_cercano(izq)
    p1_der, p2_der, d_der = par_mas_cercano(der)

    #  Obtener el mínimo actual
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


# Ejemplo de uso
puntos = [(2,3), (12,30), (40,50), (5,1), (12,10), (3,4)]
puntos.sort(key=lambda p: p[0])  # importante: ordenar por coordenada X

p1, p2, dist = par_mas_cercano(puntos)
print(f"Los puntos más cercanos son {p1} y {p2} con distancia {dist:.3f}")
