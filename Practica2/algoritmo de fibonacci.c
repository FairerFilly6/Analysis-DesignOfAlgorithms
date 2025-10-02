#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Función recursiva para calcular Fibonacci
long long fibonacci(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main() {
    int n, size;

    // Medir el tiempo de ejecución
    clock_t start_time, end_time;
    double time_taken;

    // Solicitar al usuario el tamaño del arreglo
    printf("Introduce el tamaño del arreglo: ");
    scanf("%d", &size);

    // Solicitar al usuario el número de Fibonacci a calcular
    printf("Introduce un número para calcular Fibonacci (1-20): ");
    scanf("%d", &n);

    // Asegurarse de que el número está entre 1 y 45
    if (n < 1 || n > 50) {
        printf("El valor de n debe estar entre 1 y 20.\n");
        return 1;
    }

    // Crear el arreglo de tamaño especificado
    long long *arr = (long long *)malloc(size * sizeof(long long));

    if (arr == NULL) {
        printf("Error al asignar memoria para el arreglo.\n");
        return 1;
    }

    // Iniciar el temporizador
    start_time = clock();

    // Llamada recursiva a Fibonacci
    long long result = fibonacci(n);

    // Detener el temporizador
    end_time = clock();

    // Calcular el tiempo de ejecución
    time_taken = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    // Mostrar el resultado
    printf("Fibonacci(%d) = %lld\n", n, result);

    // Mostrar el tiempo de ejecución
    printf("Tiempo de ejecución: %f segundos\n", time_taken);

    // Mostrar el consumo de memoria
    printf("Tamaño del arreglo solicitado: %d elementos\n", size);
    printf("Consumo de memoria del arreglo: %lu bytes\n", size * sizeof(long long));

    // Liberar la memoria del arreglo
    free(arr);

    return 0;
}