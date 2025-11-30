#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int inicio;
    int fin;
} Actividad;

int cmp(const void *a, const void *b) {
    Actividad *x = (Actividad*)a;
    Actividad *y = (Actividad*)b;
    return x->fin - y->fin;
}

int main() {
    int n;
    int i;

    printf("Numero de actividades: ");
    scanf("%d", &n);

    Actividad acts[n];

    for (i = 0; i < n; i++) {
        printf("Inicio de actividad %d: ", i+1);
        scanf("%d", &acts[i].inicio);
        printf("Fin de actividad %d: ", i+1);
        scanf("%d", &acts[i].fin);
    }

    // Ordenar por tiempo de fin
    qsort(acts, n, sizeof(Actividad), cmp);

    printf("\nActividades seleccionadas:\n");
    int ultimaFin = -1;

    for (i = 0; i < n; i++) {
        if (acts[i].inicio >= ultimaFin) {
            printf("Inicio: %d  Fin: %d\n", acts[i].inicio, acts[i].fin);
            ultimaFin = acts[i].fin;
        }
    }

    return 0;
}

