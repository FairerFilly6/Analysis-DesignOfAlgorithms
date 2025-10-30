#include <stdio.h>
#include <stdlib.h> 
#include <time.h>   
#include <string.h>

// --- 1. Funciones Auxiliares ---
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Funcion de comparacion para qsort (usada en la verificacion)
int compare(const void * a, const void * b) {
   return (*(int*)a - *(int*)b);
}

// --- 2. Funcion de Particion (Divide) ---
int partition(int arr[], int left, int right) {
    int i;
    // Elegir un pivote aleatorio entre left y right
    int pivotIndex = left + rand() % (right - left + 1);
    int pivotValue = arr[pivotIndex];

    // Mover el pivote al final (right) para facilitar
    swap(&arr[pivotIndex], &arr[right]);

    int storeIndex = left;
    
    // Iterar y mover elementos menores que el pivote
    for (i = left; i < right; i++) {
        if (arr[i] < pivotValue) {
            swap(&arr[storeIndex], &arr[i]);
            storeIndex++;
        }
    }

    // Mover el pivote a su posicion final
    swap(&arr[storeIndex], &arr[right]);
    
    return storeIndex; // Devolver el indice final del pivote
}

// --- 3. Quick Select (Conquer) ---
int quickSelectDaC(int arr[], int left, int right, int k_index) {
    
    while (left <= right) {
        // DIVIDIR: Particionar el arreglo
        int pivot_index = partition(arr, left, right);

        // VENCER: Comprobar donde cayo el pivote
        if (pivot_index == k_index) {
            // Caso A: Encontrado
            return arr[pivot_index];
        } 
        else if (k_index < pivot_index) {
            // Caso B: Esta en la izquierda. Ajustamos el limite 'right'.
            right = pivot_index - 1;
        } 
        else {
            // Caso C: Esta en la derecha. Ajustamos el limite 'left'.
            left = pivot_index + 1;
        }
    }
    // No deberia llegar aqui si k es valido
    return -1; 
}

// --- 4. Funcion Envoltura (Wrapper) ---

int findKthSmallest(int original_arr[], int n, int k) {
    if (k < 1 || k > n) {
        printf("Error: k esta fuera de rango.\n");
        return -1;
    }

    // 1. Crear una copia del arreglo
    int* arr_copy = (int*)malloc(n * sizeof(int));
    if (arr_copy == NULL) {
        printf("Error: No se pudo asignar memoria para la copia.\n");
        exit(1); // Salir si falla la memoria
    }
    memcpy(arr_copy, original_arr, n * sizeof(int));

    // 2. Llamar a Quick Select sobre la copia

    int result = quickSelectDaC(arr_copy, 0, n - 1, k - 1);

    // 3. Liberar la memoria de la copia
    free(arr_copy);

    return result;
}

// --- 5. Banco de Pruebas ---
int main() {
    int i, j;
    // Generador de numeros aleatorios
    srand(time(NULL));

    int sizes[] = {100, 1000, 100000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("Algoritmo Quick Select (Encontrar k-esimo elemento) usando DaC en C\n");

    for (i = 0; i < num_sizes; i++) {
        int n = sizes[i];
        
        printf("\n========================================\n");
        printf("PRUEBA: Arreglo de %d elementos.\n", n);

        // Asignar memoria para el arreglo de prueba
        int* test_array = (int*)malloc(n * sizeof(int));
        if (test_array == NULL) {
            printf("Error: No se pudo asignar memoria para el arreglo de prueba.\n");
            continue; // Saltar a la siguiente iteracion
        }

        // Poblar el arreglo con numeros aleatorios
        for (j = 0; j < n; j++) {
            test_array[j] = rand() % (n * 10) + 1; // Rango de 1 a n*10
        }

        // Elegir un k-esimo elemento aleatorio (1-based)
        int k_to_find = (rand() % n) + 1;
        printf("Buscando el k-esimo elemento mas pequeno (k = %d)\n", k_to_find);

        // --- Medir Tiempo de Quick Select (DaC) ---
        clock_t start = clock();
        int kth_element = findKthSmallest(test_array, n, k_to_find);
        clock_t end = clock();
        
        double time_taken_dac = ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("\nResultado (Quick Select): %d\n", kth_element);
        printf("Tiempo de ejecucion (DaC): %f segundos.\n", time_taken_dac);

        // --- Verificacion (usando qsort) ---
        // Usamos el 'test_array' original (que no fue modificado)
        start = clock();
        qsort(test_array, n, sizeof(int), compare);
        int correct_element = test_array[k_to_find - 1]; // k-1 por indice 0-based
        end = clock();
        
        double time_taken_sort = ((double)(end - start)) / CLOCKS_PER_SEC;
        
        printf("Verificacion (con qsort): %d\n", correct_element);
        printf("(Tiempo de verificacion con qsort: %f s)\n", time_taken_sort);

        if (kth_element == correct_element) {
            printf("Estado: CORRECTO \n");
        } else {
            printf("Estado: INCORRECTO \n");
        }

        // Liberar la memoria del arreglo de prueba
        free(test_array);
    }
    printf("========================================\n");

    return 0;
}