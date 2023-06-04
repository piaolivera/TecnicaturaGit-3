
package accesodatos;

/**
 *
 * @author Pia Olivera
 */
public class ImplementacionOracle implements IAcccesoDatos{

    @Override
    public void insertar() {
       System.out.println("Insertar desde Oracle");
    }

    @Override
    public void listar() {
        System.out.println("Listar desde Oracle");
    }

    @Override
    public void actualizay() {
       System.out.println("Actualizar desde Oracle");
    }

    @Override
    public void eliminar() {
        System.out.println("Eliminar desde Oracle");
    }
}