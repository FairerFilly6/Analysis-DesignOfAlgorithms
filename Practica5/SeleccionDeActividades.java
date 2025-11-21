/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package practica5algoritmosvoraces;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

/**
 *
 * @author angel
 */

class Actividad {
    int inicio, fin;

    Actividad(int i, int f) {
        inicio = i;
        fin = f;
    }
}

public class SeleccionDeActividades {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Número de actividades: ");
        int n = sc.nextInt();

        List<Actividad> acts = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            System.out.print("Inicio de actividad " + (i+1) + ": ");
            int ini = sc.nextInt();
            System.out.print("Fin de actividad " + (i+1) + ": ");
            int fin = sc.nextInt();
            acts.add(new Actividad(ini, fin));
        }

        // Ordenar por tiempo de fin
        acts.sort(Comparator.comparingInt(a -> a.fin));

        System.out.println("\nActividades seleccionadas:");
        int ultimaFin = -1;

        for (Actividad a : acts) {
            if (a.inicio >= ultimaFin) {
                System.out.println("Inicio: " + a.inicio + "  Fin: " + a.fin);
                ultimaFin = a.fin;
            }
        }

        sc.close();
    }
}
