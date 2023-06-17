package paquete2;

/**
 *
 * @author Pia Olivera
 */
public class Clase4 {
    private String atributoPrivado = "atributo Privado";
    
    private Clase4(){
        System.out.println("Constructor privado");
    }

    //Creamos un constructor public para poder crear objetos
    public Clase4 (String argumento){ // Aquí se puede llamar al constructor vacio
        this();
        System.out.println("Constructor público");
    }
    
    //Método privado
    private void metodoPrivado(){
        System.out.println("Método privado");
    } 

    public String getAtributoPrivado() {
        return atributoPrivado;
    }

    public void setAtributoPrivado(String atributoPrivado) {
        this.atributoPrivado = atributoPrivado;
    }
    
}
