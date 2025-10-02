#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void burbuja(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int n;
    printf("Ingrese el tamaño del arreglo: ");
    scanf("%d", &n);

    int *arr = (int*)malloc(n * sizeof(int));
    if (arr == NULL) return 1;

    // Llenamos el arreglo en orden inverso (peor caso)
    for (int i = 0; i < n; i++) arr[i] = n - i;

    clock_t inicio = clock();
    burbuja(arr, n);
    clock_t fin = clock();

    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;
    size_t memoria = n * sizeof(int);

    printf("Ordenamiento completo.\n");
    printf("Tiempo: %f segundos\n", tiempo);
    printf("Memoria usada: %zu bytes\n", memoria);

    free(arr);
    return 0;
}