/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package practica5algoritmosvoraces;

import java.util.*;
/**
 *
 * @author angel
 */

class Item {
    double valor, peso;

    Item(double v, double p) {
        valor = v;
        peso = p;
    }
}

public class MochilaFraccionaria {
     public static double resolver(List<Item> items, double capacidad) {
        // Ordenar por valor/peso descendente
        items.sort((a, b) -> Double.compare(b.valor / b.peso, a.valor / a.peso));

        double valorTotal = 0;

        for (Item x : items) {
            if (capacidad == 0) break;

            if (x.peso <= capacidad) {
                valorTotal += x.valor;
                capacidad -= x.peso;
            } else {
                double fraccion = capacidad / x.peso;
                valorTotal += x.valor * fraccion;
                capacidad = 0;
            }
        }
        return valorTotal;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Numero de articulos: ");
        int n = sc.nextInt();

        List<Item> items = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            System.out.print("Valor del articulo " + (i+1) + ": ");
            double v = sc.nextDouble();
            System.out.print("Peso del articulo " + (i+1) + ": ");
            double p = sc.nextDouble();
            items.add(new Item(v, p));
        }

        System.out.print("Capacidad de la mochila: ");
        double capacidad = sc.nextDouble();

        double resultado = resolver(items, capacidad);

        System.out.println("Valor maximo obtenido: " + resultado);

        sc.close();
    }
}
