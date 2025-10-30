#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long long merge_count(int *a, int *tmp, int l, int m, int r) {
    int i = l, j = m + 1, k = l;
    long long inv = 0;
    while (i <= m && j <= r) {
        if (a[i] <= a[j]) tmp[k++] = a[i++];
        else { tmp[k++] = a[j++]; inv += (m - i + 1); }
    }
    while (i <= m) tmp[k++] = a[i++];
    while (j <= r) tmp[k++] = a[j++];
    for (i = l; i <= r; ++i) a[i] = tmp[i];
    return inv;
}

long long sort_count(int *a, int *tmp, int l, int r) {
    if (l >= r) return 0;
    int m = (l + r) / 2;
    long long inv = 0;
    inv += sort_count(a, tmp, l, m);
    inv += sort_count(a, tmp, m + 1, r);
    inv += merge_count(a, tmp, l, m, r);
    return inv;
}

long long count_inversions(int *a, int n) {
    int *tmp = (int*)malloc(n * sizeof(int));
    if (!tmp) { fprintf(stderr, "Sin memoria\n"); exit(1); }
    long long inv = sort_count(a, tmp, 0, n - 1);
    free(tmp);
    return inv;
}

void fill_random(int *a, int n, unsigned seed) {
    srand(seed);
    for (int i = 0; i < n; ++i) a[i] = rand();  
}

int main(void) {
    int sizes[] = {100, 1000, 100000};
    for (int s = 0; s < 3; ++s) {
        int n = sizes[s];
        int *a = (int*)malloc(n * sizeof(int));
        if (!a) { fprintf(stderr, "Sin memoria\n"); return 1; }
        fill_random(a, n, 12345u);

        clock_t t0 = clock();
        long long inv = count_inversions(a, n);
        clock_t t1 = clock();

        double ms = 1000.0 * (t1 - t0) / CLOCKS_PER_SEC;
        printf("n=%d -> inversiones=%lld, tiempo=%.3f ms\n", n, inv, ms);

        free(a);
    }
    return 0;
}