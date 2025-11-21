#include <stdio.h>
#include <stdlib.h>

//ESTRUCTURA DE DATOS
typedef struct {
    double valor; //valor del artículo
    double peso;  //peso del artículo
} Item;

//FUNCION DE COMPARACIÓN con qsort

int cmp(const void *a, const void *b) {
    //convertir los punteros genéricos a punteros de tipo Item
    Item *x = (Item*)a;
    Item *y = (Item*)b;

    //calcular el ratio de valor/peso para ambos ítems
    double r1 = x->valor / x->peso; //ratio del ítem A
    double r2 = y->valor / y->peso; //ratio del ítem B
    
    //Devolvemos el resultado para ordenar de forma descendente (r2 > r1)
    // - Si r2 > r1, r2 es mejor. Retorna positivo para que 'y' vaya antes que 'x'
    // - Si r1 > r2, r1 es mejor. Retorna negativo para que 'x' vaya antes que 'y'
    // - Si r1 == r2, retorna 0
    return (r2 > r1) - (r2 < r1); 
}

//FUNCION PRINCIPAL DEL ALGORITMO
double resolver(Item items[], int n, double capacidad) {
    int i;

    //ORDENAR: Ordenamos el array items utilizando la función cmp
    //Los items con mayor valor/peso quedaran al principio
    qsort(items, n, sizeof(Item), cmp);

    double valorTotal = 0; //acumulador del valor maximo obtenido

    //RELLENAR: Recorremos los items ya ordenados
    for (i = 0; i < n; i++) {
        //Si la mochila ya esta llena salimos del bucle
        if (capacidad == 0) break;

        //CASO A: El item cabe completamente en el espacio restante
        if (items[i].peso <= capacidad) {
            //Se toma el ítem completo
            valorTotal += items[i].valor;
            //Reducimos la capacidad restante de la mochila
            capacidad -= items[i].peso;
        } else {
            //CASO B: El item no cabe completamente (Tomamos una fraccion)
            //Calculamos que fraccion del item podemos tomar
            //Esto siempre sera < 1.0 (ejemplo: 0.3 o 0.5)
            double fraccion = capacidad / items[i].peso;
            
            //Sumamos el valor proporcional a la fraccion tomada
            valorTotal += items[i].valor * fraccion;
            
            //La capacidad se vuelve 0 porque hemos llenado el espacio restante
            capacidad = 0; 
        }
    }
    //Devolvemos el valor total maximo
    return valorTotal;
}

//FUNCIÓN PRINCIPAL DE EJECUCIÓN
int main() {
    int n; // Número de artículos
    int i;
    
    // Solicitar el número de artículos
    printf("Numero de articulos: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Entrada invalida para el numero de articulos.\n");
        return 1;
    }

    // Declaración de un Array de Longitud Variable (VLA) para almacenar los ítems.
    Item items[n]; 
    
    // Bucle para ingresar el valor y peso de cada artículo
    for (i = 0; i < n; i++) {
        printf("Valor del articulo %d: ", i+1);
        if (scanf("%lf", &items[i].valor) != 1) {
             printf("Entrada invalida.\n");
             return 1;
        }
        printf("Peso del articulo %d: ", i+1);
        if (scanf("%lf", &items[i].peso) != 1 || items[i].peso <= 0) {
             printf("Entrada invalida o peso cero/negativo.\n");
             return 1;
        }
    }

    double capacidad; // Capacidad máxima de la mochila
    printf("Capacidad de la mochila: ");
    if (scanf("%lf", &capacidad) != 1 || capacidad < 0) {
        printf("Entrada invalida para la capacidad.\n");
        return 1;
    }

    // Llamada a la función para resolver el problema
    double resultado = resolver(items, n, capacidad);
    
    // Imprimir el resultado
    printf("\nValor maximo obtenido: %.2f\n", resultado);

    return 0; // Salida exitosa del programa
}
