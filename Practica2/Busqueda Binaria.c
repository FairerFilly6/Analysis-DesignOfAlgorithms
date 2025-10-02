#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int busquedaBinaria(int arr[], int n, int x) {
    int inicio = 0, fin = n - 1;
    while (inicio <= fin) {
        int medio = (inicio + fin) / 2;
        if (arr[medio] == x) return medio;
        else if (arr[medio] < x) inicio = medio + 1;
        else fin = medio - 1;
    }
    return -1;
}

int main() {
    int n, x;
    printf("Ingrese el tamaño del arreglo: ");
    scanf("%d", &n);

    int *arr = (int*)malloc(n * sizeof(int));
    if (arr == NULL) return 1;

    for (int i = 0; i < n; i++) arr[i] = i + 1;

    printf("Ingrese el valor a buscar: ");
    scanf("%d", &x);

    clock_t inicio = clock();
    int resultado = busquedaBinaria(arr, n, x);
    clock_t fin = clock();

    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;
    size_t memoria = n * sizeof(int);

    if (resultado == -1)
        printf("No encontrado\n");
    else
        printf("Encontrado en la posición %d\n", resultado);

    printf("Tiempo: %f segundos\n", tiempo);
    printf("Memoria usada: %zu bytes\n", memoria);

    free(arr);
    return 0;
}