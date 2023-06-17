package paquete2;

import paquete1.Clase1;

/**
 *
 * @author Pia Olivera
 */
public class Clase3 extends Clase1{
    public Clase3(){
        super("protected");
        this.protectedAtributo = "Accedemos desde la clase hija";
        System.out.println("protectedAtributo = " + this.protectedAtributo);
        this.AtributPublic = "Es totalmente publico";
    }
}
