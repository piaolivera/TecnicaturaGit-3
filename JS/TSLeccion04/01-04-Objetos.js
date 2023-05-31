let x = 10; // variable de tipo primitiva
console.log(x.length);


console.log('Tipo primitivo');
//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma : 'ES',
    get lang(){
        return this.idioma.toUpperCase();
    },
    set lang(lang){
        this.idioma =lang.toUpperCase(); //Convierte loas minúsculas a mayúsculas
    },
    nombreCompleto: function(){// método o función en JavaScript
        return this.nombre+ ' '+ this.apellido;
    },
    get nombreEdad(){ // Este es el método get
        return 'El nombre es'+ this.nombre+' edad: '+ this.edad;
    }
    
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto');

let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion= 'Salada 14';
persona2.telefono= ' 5568648';
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');
console.log(persona['apellido']);// Accedemos como si fuera un arreglo

console.log('Usamos el ciclo for in');
// for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

console.log('Cambiamos y eliminamos un error');
persona.apellido = 'Betancud'; //Cambiamos dinamicamente un valor del objeto
console.log(persona);

persona.apellida= 'Ruiz';
delete persona.apellida // de esta manera lo eliminamos 

//Distintas formas de imprimir un objeto
//Numero 1: la más sencilla: concatentando cada valor de la propiedad
console.log('Distintas formas de imprimir un objeto');
console.log('Numero 1: la más sencilla: concatentando cada valor de la propiedad')
console.log(persona.nombre+ ' ' +persona.apellido);


//Numero2 : A través del ciclo for in
console.log('Numero2 : A través del ciclo for in')
for (nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}


//Numero 3: La cunicon objet. values()
console.log('Numero 3: La cunicon objet. values()')
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero4: Utilizaremos el método JSON.stringfy
console.log('Numero4: Utilizaremos el método JSON.stringfy');
let personaString = JSON.stringify(persona);
console.log(personaString)

console.log('Comenzamos a utilizar el método get');
console.log(persona.nombreEdad);


console.log('Comenzamos con el método get y set para idioma');
persona.lang = 'en';
console.log(persona.lang);


function Persona3( nombre, apellido, email){ //constuctor
    this.nombre= nombre;
    this.apellido = apellido;
    this.email =email;
    this.nombrembreCompleto = function(){
        return this.nombre+ ' '+this.apellido;
    }
}
let padre = new Persona3('Leo', 'Lopez', 'lopezleo@gmail.com');
console.log(padre);
console.log(padre.nombrembreCompleto());

let madre= new Persona3('Laura', 'Contreras', 'laura@gmai.com');
console.log(madre);
console.log(madre.nombrembreCompleto());


//Diferentes formas de crear objetos
let miObjeto = new Object();
//Caso numero2
let miObjeto2 = {}; // Esta opcion es breve y recomendada

//caso String
let miCadena1 = new String ('Hola');
// caso String2 
let miCadena2 = 'Hola';

//uso de call
let persona4 ={
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
       return titulo+ this.nombre+ ' '+ this.apellido+' '+telefono;
        //  return this.nombre+ ' '+ this.apellido;
    }
}
let persona5= {
    nombre: 'Carlos',
    apellido: 'Lara'
}
console.log(persona4.nombreCompleto2('Lic.', '6562685'));
console.log(persona4.nombreCompleto2.call(persona5, 'ing.', '54874575'));

//Método Apply
let arreglo = ['Ing.', '662842855'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));
