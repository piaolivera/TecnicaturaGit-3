miFuncion(6,4) // Esto se le conoce como hosting

function miFuncion(a, b){
    //console.log("Sumamos: "+ (a+b));
    return a+b;
}
//Llamamos la funcion
miFuncion (4,5);

let resultado = miFuncion(6,7);
console.log(resultado);

//DEclaramos una función de tipo expreción
let x =function(a,b){  return a+b }; //Necesita cierre con punto y coma
resultado = x(5, 6); // al llamar se pone la variable y parentesis
console.log(resultado);
// Funciones de tipo self y invoking
(function(a,b){
    console.log('Ejecutando la función: '+ (a + b));
})(9, 6);

console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments.length); 
}
miFuncionDos(5,7);

//toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

//Funciones flecha
const sumarFuncionFlecha = (a, b)=> a + b;
resultado = sumarFuncionFlecha(3, 7);
console.log(resultado);

//Función tipo expresión
let sumar = function(a, b){
    console.log(arguments[0]);// muestra el parametro de : a
    console.log(arguments[1]);
    console.log(arguments[3])
    return a + b;
}
resultado = sumar(3, 5);
console.log(resultado)

// Sumar todos los argumentos
let respuesta = SumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function SumarTodo(){
    let suma =0;
    for(let i = 0; i< arguments.length; i++){
        suma+= arguments[i]; // arguments es para arreglos
    }
    return suma;
}

//Tipos primitivos 
let k = 10;
function cambiarValor(a){ //Paso por valor
    a= 20;
}
cambiarValor(k);
console.log(k);


// Paso por referencia
const persona = {
    nombre: 'Juan',
    apellido: 'Lepez'
}
console.log(persona);
function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez';
}
cambiarValorObjeto(persona);
console.log(persona);