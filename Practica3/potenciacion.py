import time
import tracemalloc

# Versión Iterativa

def potencia_iterativa(base, exponente):
    """
    Calcula la potencia de un numero usando un bucle (metodo iterativo).
    """
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

# Versión Recursiva

def potencia_recursiva(base, exponente):
    """
    Calcula la potencia de un numero usando recursividad.
    """
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

# Representación de la Pila de Llamadas Recursivas

def potencia_recursiva_visual(base, exponente, nivel=0):
    """
    Calcula la potencia de forma recursiva y muestra la pila de llamadas.
    'nivel' ayuda a indentar la salida para visualizar la profundidad.
    """
    indentacion = "  " * nivel
    print(f"{indentacion}Entrando -> potencia({base}, {exponente})")

    if exponente == 0:
        print(f"{indentacion}Caso base alcanzado. Retornando 1.")
        return 1
    else:
        # Llamada recursiva
        resultado_parcial = potencia_recursiva_visual(base, exponente - 1, nivel + 1)
        resultado_final = base * resultado_parcial
        print(f"{indentacion}<- Retornando {resultado_final} de potencia({base}, {exponente})")
        return resultado_final


# Funcion principal

def main():
    try:
        base = int(input("Introduce el numero base: "))
        exponente = int(input("Introduce el exponente (entero no negativo): "))
        if exponente < 0:
            print("El exponente debe ser un numero entero no negativo.")
            return
    except ValueError:
        print("Por favor, introduce numeros enteros validos.")
        return

    print("\n" + "="*40)
    print(" ANALISIS DEL METODO ITERATIVO")
    print("="*40)

    # Medicion del tiempo de ejecución (Iterativo)
    inicio_tiempo = time.perf_counter()
    resultado_it = potencia_iterativa(base, exponente)
    fin_tiempo = time.perf_counter()
    tiempo_ejecucion_it = (fin_tiempo - inicio_tiempo) * 1e6 # a microsegundos

    # Medicion del consumo de memoria (Iterativo)

    tracemalloc.start()
    potencia_iterativa(base, exponente)
    memoria_actual_it, memoria_pico_it = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Resultado: {base}^{exponente} = {resultado_it}")
    print(f"Tiempo de ejecucion: {tiempo_ejecucion_it:.4f} microsegundos")
    print(f"Consumo de memoria (pico): {memoria_pico_it / 1024:.4f} KiB")


    print("\n" + "="*40)
    print(" ANALISIS DEL METODO RECURSIVO")
    print("="*40)

    # Medicion del tiempo de ejecución (Recursivo)

    inicio_tiempo = time.perf_counter()
    resultado_rec = potencia_recursiva(base, exponente)
    fin_tiempo = time.perf_counter()
    tiempo_ejecucion_rec = (fin_tiempo - inicio_tiempo) * 1e6 # a microsegundos

    # Medicion del consumo de memoria (Recursivo)

    tracemalloc.start()
    potencia_recursiva(base, exponente)
    memoria_actual_rec, memoria_pico_rec = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Resultado: {base}^{exponente} = {resultado_rec}")
    print(f"Tiempo de ejecucion: {tiempo_ejecucion_rec:.4f} microsegundos")
    print(f"Consumo de memoria (pico): {memoria_pico_rec / 1024:.4f} KiB")
    print("\n--- Pila de Llamadas Recursivas ---")
    potencia_recursiva_visual(base, exponente)
    print("-" * 35)


if __name__ == "__main__":
    main()