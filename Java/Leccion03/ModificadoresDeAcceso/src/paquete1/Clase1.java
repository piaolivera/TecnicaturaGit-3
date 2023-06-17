package paquete1;

/**
 *
 * @author Pia Olivera
 */
public class Clase1 {
    public String AtributPublic = "Valor atributo public";
    protected String protectedAtributo = "Valor atributo protected";
    
    public Clase1(){
        System.out.println("Constructor public");
    }
    
    protected Clase1 (String atributoPublic){
        System.out.println("Constructor protected");
    }
    public void metodoPublico(){
        System.out.println("Metodo public");
    }
    
    protected void metodoProtected(){
        System.out.println("Método protected");
    }
}
