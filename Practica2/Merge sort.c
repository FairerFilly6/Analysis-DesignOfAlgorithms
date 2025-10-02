#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void merge(int arr[], int izq, int mid, int der) {
    int n1 = mid - izq + 1;
    int n2 = der - mid;
    int *L = (int*)malloc(n1 * sizeof(int));
    int *R = (int*)malloc(n2 * sizeof(int));
    for (int i = 0; i < n1; i++) L[i] = arr[izq + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];
    int i = 0, j = 0, k = izq;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
    free(L);
    free(R);
}

void mergeSort(int arr[], int izq, int der) {
    if (izq < der) {
        int mid = (izq + der) / 2;
        mergeSort(arr, izq, mid);
        mergeSort(arr, mid + 1, der);
        merge(arr, izq, mid, der);
    }
}

int main() {
    int n;
    printf("Ingrese el tamaño del arreglo: ");
    scanf("%d", &n);

    int *arr = (int*)malloc(n * sizeof(int));
    if (!arr) return 1;

    for (int i = 0; i < n; i++) arr[i] = n - i;

    clock_t inicio = clock();
    mergeSort(arr, 0, n - 1);
    clock_t fin = clock();

    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;
    size_t memoria = n * sizeof(int);

    printf("Ordenamiento Merge Sort completo.\n");
    printf("Tiempo: %f segundos\n", tiempo);
    printf("Memoria usada: %zu bytes\n", memoria);

    free(arr);
    return 0;
}