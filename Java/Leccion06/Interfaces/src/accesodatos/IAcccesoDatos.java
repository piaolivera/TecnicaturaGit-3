
package accesodatos;

/**
 *
 * @author Pia Olivera
 */
public interface IAcccesoDatos {
    int MAX_REGISTRO = 10;
    
    //METODO INSERTAR ES ABSTRACTO Y SIN CUERPO
    void insertar ();
    
    void listar();
   
    void actualizay ();
    
    void eliminar();
}
