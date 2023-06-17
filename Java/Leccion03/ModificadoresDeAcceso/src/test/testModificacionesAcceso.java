/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package test;

import paquete1.Clase1;
import paquete2.Clase3;

/**
 *
 * @author Pia Olivera
 */
public class testModificacionesAcceso {
     public static void main(String[] args) {
         Clase1 clase1 = new Clase1();
         System.out.println("clase1 = " + clase1.AtributPublic);
         clase1.metodoPublico();
         Clase3 clasehija = new Clase3();
         System.out.println("clasehija = " + clasehija);
    }
    
    
}
