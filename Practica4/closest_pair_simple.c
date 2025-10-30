#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

typedef struct { double x, y; } Point;

static int cmpX(const void *a, const void *b) {
    const Point *p = (const Point*)a, *q = (const Point*)b;
    return (p->x < q->x) ? -1 : (p->x > q->x);
}
static int cmpY(const void *a, const void *b) {
    const Point *p = (const Point*)a, *q = (const Point*)b;
    return (p->y < q->y) ? -1 : (p->y > q->y);
}
static inline double dist2(Point a, Point b) {
    double dx = a.x - b.x, dy = a.y - b.y;
    return dx*dx + dy*dy;
}

static double brute_best2(Point *p, int n) {
    double best2 = INFINITY;
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j) {
            double d2 = dist2(p[i], p[j]);
            if (d2 < best2) best2 = d2;
        }
    return best2;
}


static double closest_rec(Point *px, Point *py, int n) {
    if (n <= 3) return brute_best2(px, n);

    int mid = n / 2;
    double midx = px[mid].x;

    Point *pxL = px;            
    Point *pxR = px + mid;      
    int nL = mid, nR = n - mid;

    Point *yL = (Point*)malloc(n * sizeof(Point));
    Point *yR = (Point*)malloc(n * sizeof(Point));
    int ln = 0, rn = 0;
    for (int i = 0; i < n; ++i) {
        if (py[i].x < midx || (py[i].x == midx && ln < nL)) yL[ln++] = py[i];
        else yR[rn++] = py[i];
    }

    double dL = closest_rec(pxL, yL, nL);
    double dR = closest_rec(pxR, yR, nR);
    double d2min = (dL < dR ? dL : dR); 

    double delta = sqrt(d2min);
    Point *strip = (Point*)malloc(n * sizeof(Point));
    int s = 0;
    for (int i = 0; i < n; ++i)
        if (fabs(py[i].x - midx) < delta) strip[s++] = py[i];

    for (int i = 0; i < s; ++i) {
        for (int j = i + 1; j < s && (strip[j].y - strip[i].y) < delta; ++j) {
            double d2 = dist2(strip[i], strip[j]);
            if (d2 < d2min) {
                d2min = d2;
                delta = sqrt(d2min);
            }
        }
    }

    free(yL); free(yR); free(strip);
    return d2min;
}

static double closest_pair(Point *p, int n) {
    Point *px = (Point*)malloc(n * sizeof(Point));
    Point *py = (Point*)malloc(n * sizeof(Point));
    if (!px || !py) { fprintf(stderr, "Sin memoria\n"); exit(1); }

    for (int i = 0; i < n; ++i) { px[i] = p[i]; py[i] = p[i]; }
    qsort(px, n, sizeof(Point), cmpX);
    qsort(py, n, sizeof(Point), cmpY);

    double best2 = closest_rec(px, py, n);
    free(px); free(py);
    return sqrt(best2);
}

static void fill_points(Point *p, int n, unsigned seed) {
    srand(seed);
    for (int i = 0; i < n; ++i) {
        p[i].x = (double)(rand() % 1000000);
        p[i].y = (double)(rand() % 1000000);
    }
}

int main(void) {
    int sizes[] = {10, 100, 1000, 100000};
    for (int s = 0; s < 4; ++s) {
        int n = sizes[s];
        Point *pts = (Point*)malloc(n * sizeof(Point));
        if (!pts) { fprintf(stderr, "Sin memoria\n"); return 1; }
        fill_points(pts, n, 12345u);

        clock_t t0 = clock();
        double dmin = closest_pair(pts, n);
        clock_t t1 = clock();

        double ms = 1000.0 * (t1 - t0) / CLOCKS_PER_SEC;
        printf("n=%d -> distancia_min=%.6f, tiempo=%.3f ms\n", n, dmin, ms);

        free(pts);
    }
    return 0;
}
