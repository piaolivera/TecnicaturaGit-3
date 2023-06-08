package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;

/**
 *
 * @author Pia Olivera
 */
public class testEnumeraciones {
    public static void main(String[] args) {
       // System.out.println("Día 1: "+Dias.DOMINGO);
        //indicarDiaSemana(Dias.DOMINGO);
        
        System.out.println("Continente No 4:"+Continentes.AMERICA);
        System.out.println("No. de paises en el 4to. continente: "
                +Continentes.AMERICA.getPaises());
                System.out.println("No. de Habitantes en el 4to. continente: "
                +Continentes.AMERICA.getHabitantes());
    }
    
    private static void indicarDiaSemana(Dias dias){
        switch(dias){
            case LUNES:
                System.out.println("Primer dá de la semana.");
                break;
            case MARTES:
                System.out.println("Segundo dá de la semana.");
                break;
            case MIÉRCOLES:
                System.out.println("Tercer dá de la semana.");
                break; 
            case JUEVES:
                System.out.println("Cuarto dá de la semana.");
                break;
            case VIERNES:
                System.out.println("Quinto dá de la semana.");
                break;
            case SÁBADO:
                System.out.println("Sexto dá de la semana.");
                break;
            case DOMINGO:
                System.out.println("Último dá de la semana.");
                break;
            default:
                System.out.println("Ese día no existe.");

        }
    }
    
}
