
package accesodatos;

/**
 *
 * @author Pia Olivera
 */
public class ImplementacionMysql implements IAcccesoDatos{

    @Override
    public void insertar() {
        System.out.println("Insertar desde Mysql");
    }

    @Override
    public void listar() {
         System.out.println("Listar desde Mysql");
    }

    @Override
    public void actualizay() {
        System.out.println("Actualizar desde Mysql");
    }

    @Override
    public void eliminar() {
        System.out.println("Eliminar desde Mysql");
    }
    
}
