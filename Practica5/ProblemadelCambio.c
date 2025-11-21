#include <stdio.h>

int main() {
    int monedas[] = {10, 5, 2, 1};
    int N;
    int i;

    printf("Ingresa la cantidad N: ");
    scanf("%d", &N);

    int cantidad = N;

    printf("Cambio para %d:\n", N);
    for (i = 0; i < 4; i++) {
        int num = cantidad / monedas[i];
        if (num > 0) {
            printf("%d moneda(s) de %d\n", num, monedas[i]);
        }
        cantidad %= monedas[i];
    }

    return 0;
}

