
package test;

/**
 *
 * @author Pia Olivera
 */

import accesodatos.*; 

public class Testinterfaces {
    public static void main(String[] args) {
        IAcccesoDatos datos = new ImplementacionMysql();
      //  datos.listar();
       // imprimir(datos);
        datos = new ImplementacionOracle();
       //  datos.listar();
       imprimir(datos);
    }
    
    public static void imprimir(IAcccesoDatos datos){
        datos.listar();
    }
}
