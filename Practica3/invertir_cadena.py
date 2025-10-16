import time
import tracemalloc

def invertir(s: str) -> str:
    res = []
    for i in range(len(s) - 1, -1, -1):
        res.append(s[i])
    return "".join(res)

def invertirCadenaRecursiva(cadena):
    size = len(cadena)
    if( size == 0):
        return ""
    return cadena[size-1] + (invertirCadenaRecursiva(cadena[:size-1]))

if __name__ == "__main__":
    texto = input("Cadena a invertir: ")

    tracemalloc.start()
    t0 = time.perf_counter()

    invertida = invertir(texto)

    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Invertida:", invertida)
    print(f"Tiempo de ejecución: {elapsed_ms:.3f} ms")
    print(f"Memoria pico: {peak/1024:.1f} KB")


    invertidaRecursiva = invertirCadenaRecursiva(texto)

    print(f"Cadena invertida recursivamente: {invertidaRecursiva}")



