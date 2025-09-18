#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAXD 256

int convertir_a_digitos_invertidos(const char *t, int d[]) {
    int n = (int)strlen(t);
    for (int i = 0; i < n; i++) {
        if (!isdigit((unsigned char)t[i])) return -1;
    }
    int k = 0;
    for (int i = n - 1; i >= 0; i--) d[k++] = t[i] - '0';
    return k;
}

void imprimir_numero_invertido(const int a[], int n) {
    int i = n - 1;
    while (i > 0 && a[i] == 0) i--;
    for (; i >= 0; i--) printf("%d", a[i]);
}

int longitud_efectiva(const int v[], int max_len) {
    int l = max_len;
    while (l > 1 && v[l - 1] == 0) l--;
    return l;
}

int main(void) {
    char Atxt[MAXD + 1], Btxt[MAXD + 1];
    printf("Ingresa A: "); if (scanf("%256s", Atxt) != 1) return 1;
    printf("Ingresa B: "); if (scanf("%256s", Btxt) != 1) return 1;

    int A[MAXD], B[MAXD];
    int nA = convertir_a_digitos_invertidos(Atxt, A);
    int nB = convertir_a_digitos_invertidos(Btxt, B);
    if (nA < 0 || nB < 0) {
        printf("Error: solo dígitos 0-9 sin signos ni puntos.\n");
        return 1;
    }

    int maxLen = nA + nB + 2;
    static int parciales[MAXD][2 * MAXD + 2];

    printf("\n=== FASE 1: Multiplicaciones parciales ===\n");
    for (int j = 0; j < nB; j++) {
        int digitoB = B[j];
        int acarreoMultiplicacion = 0;
        printf("\nParcial %d (A × %d, desplazamiento %d):\n", j + 1, digitoB, j);

        for (int i = 0; i < nA; i++) {
            int producto = digitoB * A[i] + acarreoMultiplicacion;
            int digitoEscrito = producto % 10;
            acarreoMultiplicacion = producto / 10;
            int col = i + j;
            parciales[j][col] = digitoEscrito;

            printf("  %d x %d -> %d, escribo %d en col %d, llevo %d\n",
                   digitoB, A[i], producto, digitoEscrito, col, acarreoMultiplicacion);
        }

        int col = nA + j;
        while (acarreoMultiplicacion > 0) {
            int dig = acarreoMultiplicacion % 10;
            parciales[j][col++] = dig;
            printf("  Acarreo final -> escribo %d en col %d\n", dig, col - 1);
            acarreoMultiplicacion /= 10;
        }
    }

    int longitudes[MAXD];
    int ancho_max = 1;
    for (int j = 0; j < nB; j++) {
        longitudes[j] = longitud_efectiva(parciales[j], maxLen);
        if (longitudes[j] > ancho_max) ancho_max = longitudes[j];
    }

    printf("\n--- Parciales alineados (vista normal) ---\n");
    for (int j = 0; j < nB; j++) {
        int espacios = ancho_max - longitudes[j];
        for (int s = 0; s < espacios; s++) putchar(' ');
        imprimir_numero_invertido(parciales[j], longitudes[j]);
        putchar('\n');
    }

    printf("\n=== FASE 2: Suma de parciales columna por columna ===\n");
    int R[2 * MAXD + 2] = {0};
    int acarreoSuma = 0;

    for (int col = 0; col < maxLen; col++) {
        int sumaColumna = acarreoSuma;
        for (int j = 0; j < nB; j++) sumaColumna += parciales[j][col];

        R[col] = sumaColumna % 10;
        acarreoSuma = sumaColumna / 10;
        printf("Col %d: suma=%d -> escribo %d, llevo %d\n",
               col, sumaColumna, R[col], acarreoSuma);
    }

    int LR = maxLen;
    while (acarreoSuma > 0) {
        R[LR++] = acarreoSuma % 10;
        acarreoSuma /= 10;
    }

    while (LR > 1 && R[LR - 1] == 0) LR--;

    printf("\n=== Resultado final ===\nA = %s\nB = %s\nProducto = ", Atxt, Btxt);
    imprimir_numero_invertido(R, LR);
    printf("\n");

    return 0;
}