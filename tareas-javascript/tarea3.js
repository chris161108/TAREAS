// Ejercicio 3: Sumatoria Positiva
function sumarPositivos(numeros) {
    let acumulador = 0;
    
    for (let i = 0; i < numeros.length; i++) {
        if (numeros[i] > 0) {
            acumulador += numeros[i];
        }
    }
    
    return acumulador;
}

const listaMixta = [-5, 10, -2, 3, 0, 7];
const resultado = sumarPositivos(listaMixta);
console.log(resultado);