
import heapq

text = """Omar
Andrés
Barrón
Rivera
"""
size = len(text)

print(text)
print(size)

frecuencias = {}
for caracter in text:
    if caracter in frecuencias:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1

# print(frecuencias)

frecuencias = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

# print(frecuencias)
print("frecuencias usadas")
for frecuencia in frecuencias:
    print(frecuencia)

nodos = []

for elemento in frecuencias:
    nodo = {
        "caracter": elemento[0],
        "frecuencia": elemento[1],
        "izq": None,
        "der": None
    }
    nodos.append(nodo)

for nodo in nodos:
    print(nodo)

heap = []
contador = 0

for nodo in nodos:
    heap.append((nodo['frecuencia'], contador, nodo))
    contador += 1

heapq.heapify(heap)

print("Heap")

for elemento in heap:
    print(elemento)

print("algoritmo")

while(len(heap) > 1):
    freq1, _, nodoA = heapq.heappop(heap)
    freq2, _, nodoB = heapq.heappop(heap)

    # print(f"nodoA {nodoA} ")
    # print(f"nodoB {nodoB}")

    
    freqTotal = freq1 + freq2

    nuevo = {
        'caracter': None,
        'frecuencia': freqTotal,
        'izq': nodoA,
        'der': nodoB
    }
    
    heapq.heappush(heap,(freqTotal, contador, nuevo))
    contador+=1


print(heap)
arbol = heap[0][2]
print("arbol")

print(arbol)

def mostrarArbol(nodo, nivel=0):
    if nodo is None:
        return

    # sangría según profundidad
    indent = "    " * nivel

    if nodo['caracter'] is None:
        print(f"{indent}Nodo interno ({nodo['frecuencia']})")
    else:
        print(f"{indent}'{nodo['caracter']}' ({nodo['frecuencia']})")

    mostrarArbol(nodo['izq'], nivel + 1)
    mostrarArbol(nodo['der'], nivel + 1)


mostrarArbol(arbol)
    




