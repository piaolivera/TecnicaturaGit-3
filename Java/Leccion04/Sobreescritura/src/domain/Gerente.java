package domain;

/**
 *
 * @author Pia Olivera
 */
public class Gerente extends Empleado{
    private String departamento;
    
    public Gerente(String nombre, double sueldo, String departamento){
        super (nombre, sueldo);
        this.departamento = departamento;
    }
    
}
