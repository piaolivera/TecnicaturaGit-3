let x = 10; // variable de tipo primitiva
console.log(x.length);


console.log('Tipo primitivo');
//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30,
    nombreCompleto: function(){// método o función en JavaScript
        return this.nombre+ ' '+ this.apellido;
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



