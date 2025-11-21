/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package practica5algoritmosvoraces;

import java.util.Scanner;
/**
 *
 * @author angel
 */
public class ProblemaDelCambio {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Monedas disponibles (ordenadas de mayor a menor)
        int[] monedas = {10, 5, 2, 1};

        System.out.print("Ingresa la cantidad N: ");
        int N = sc.nextInt();

        int cantidad = N;

        System.out.println("Cambio para " + N + ":");
        for (int m : monedas) {
            // Cuántas monedas de este tipo se usan
            int num = cantidad / m;
            if (num > 0) {
                System.out.println(num + " moneda(s) de " + m);
            }
            cantidad = cantidad % m;
        }
        sc.close();
    }
}
