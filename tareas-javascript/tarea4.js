// Ejercicio 4: Tabla de Multiplicar Segura
function generarTabla(numero) {
    if (numero < 1 || numero > 20) {
        return "Error: El número debe estar entre 1 y 20.";
    }

    let tabla = [];
    for (let i = 1; i <= 10; i++) {
        tabla.push(numero + " * " + i + " = " + (numero * i));
    }
    
    return tabla;
}

const resultado = generarTabla(5);
console.log(resultado);