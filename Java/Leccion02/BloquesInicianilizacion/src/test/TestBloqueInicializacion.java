package test;

import domain.Persona;

/**
 *
 * @author Pia Olivera
 */
public class TestBloqueInicializacion {
    public static void main(String[] args) {
           Persona persona1 = new Persona();
           System.out.println("Persona1" +persona1);
           
           Persona persona2 = new Persona ();
           System.out.println("persona2 = " + persona2);
    }
 
}
