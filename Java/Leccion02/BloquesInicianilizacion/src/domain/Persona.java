package domain;

/**
 *
 * @author Pia Olivera
 */
public class Persona {
    private final int IdPersona;
    private static int contadorPersona;
    
    static{ //Bloque de inicialización estático
        System.out.println("Ejecución bloque estático");
        ++Persona.contadorPersona;
        //idPersona = 10; No es estático por esto tenemos un error
    }
    { //Bloque de inicialización NO estático (contexto dinámico)
        System.out.println("Ejecución de bloque de inicialización NO estatico");
        this.IdPersona = Persona.contadorPersona++; //Incrementamos el atributo
      }
    // Los bloques de inicialización se ejcutan antes del constructor
    
    public Persona(){
        System.out.println("Ejecución del constuctor");
    }
    
    public int getidPersona(){
        return this.IdPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "IdPersona=" + IdPersona + '}';
    }
    
}
