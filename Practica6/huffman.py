
import heapq

with open("texto.txt", "r", encoding="utf8") as f:
    text = f.read()

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

def generarCodigos(nodo, codigoActual="", tabla=None):
    if tabla is None:
        tabla = {}

    
    if nodo['caracter'] is not None:
        tabla[nodo['caracter']] = codigoActual
        return tabla
    
    if nodo['izq'] is not None:
        generarCodigos(nodo['izq'], codigoActual + "0", tabla)

    if nodo['der'] is not None:
        generarCodigos(nodo['der'], codigoActual + "1", tabla)

    return tabla


codigos = generarCodigos(arbol)
print(codigos)

for c, cod in codigos.items():
    print(f"{repr(c)} : {cod}")

comprimido = ""

for caracter in text:
    clave = codigos[caracter]
    comprimido += clave

print("Texto comprimido:")
print(comprimido)

def crearComprimido(comprimido: str, nombre_archivo: str):
    with open(nombre_archivo, "wb") as f:
        byte = 0
        bits_acumulados = 0

        for bit in comprimido:
            byte = (byte << 1) | int(bit)
            bits_acumulados += 1

            
            if bits_acumulados == 8:
                f.write(bytes([byte]))
                byte = 0
                bits_acumulados = 0

        
        if bits_acumulados > 0:
            byte = byte << (8 - bits_acumulados)
            f.write(bytes([byte]))

    print(f"Archivo comprimido guardado como {nombre_archivo}")

crearComprimido(comprimido, "respaldo.bin")

