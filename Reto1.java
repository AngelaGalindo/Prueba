package reto1;

import java.util.Scanner;

/**
 *
 * @author ANGELA
 */
public class Reto1 {
 
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // imprimir el numero en letra con la suma
        Scanner sc = new Scanner (System.in);
        System.out.println("Programa que da resultado de dos dados ");
        boolean contad = true;
        while (contad){  
        System.out.print("Escriba el número del primer dado: ");
        int d1 = sc.nextInt();
        System.out.print("Escriba el número del segundo dado: ");
        int d2 = sc.nextInt();
        if (d1 > 6 || d2 > 6){  
            System.out.println("Alguno de los numeros no es valido");
        }
        else{ 
        switch (d1){
            case 1:
                System.out.println("Primer dado: uno");
                break;
            case 2:
                System.out.println("Primer dado: dos");
                break;
            case 3:
                System.out.println("Primer dado: tres");
                break;
            case 4:
                System.out.println("Primer dado: cuatro");
                break;
            case 5:
                System.out.println("Primer dado: cinco");
                break;
            case 6:
                System.out.println("Primer dado: seis");
                break;
            default :
                System.out.println("El número no es valido");
                break;
        }
        switch (d2){
            case 1:
                System.out.println("Segundo dado: uno");
                break;
            case 2:
                System.out.println("Segundo dado: dos");
                break;
            case 3:
                System.out.println("Segundo dado: tres");
                break;
            case 4:
                System.out.println("Segundo dado: cuatro");
                break;
            case 5:
                System.out.println("Segundo dado: cinco");
                break;
            case 6:
                System.out.println("Segundo dado: seis");
                break;
        }    
        int resultado = d1 + d2;        
        switch (resultado){
            case 2:
                System.out.println("Total:dos");
                break;
            case 3:
                System.out.println("Total:tres");
                break;
            case 4:
                System.out.println("Total:cuatro");
                break;
            case 5:
                System.out.println("Total:cinco");
                break;
            case 6:
                System.out.println("Total:seis");
                break;
            case 7:
                System.out.println("Total:siete");
                break;
            case 8:
                System.out.println("Total:ocho");
                break;
            case 9:
                System.out.println("Total:nueve");
                break;
            case 10:
                System.out.println("Total:diez");
                break;
            case 11:
                System.out.println("Total:once");
                break;
            case 12:
                System.out.println("Total:doce");
                break;
        } 
        }
        
        System.out.print("Desea volver a ingresar nuevos números(si/no): ");
        String resp = sc.next();
        switch (resp){
            case "Si":
            case "si":
            case "S":
            case "s":
                contad = true;
                break;
            default:
                contad = false;
                break;
                
        } 
        }
    }
    
}
