// Ejercicio 1: Filtrado de Pares
function filtrarPares(numeros) {
    let resultado = [];
    for (let i = 0; i < numeros.length; i++) {
        if (numeros[i] % 2 === 0) {
            resultado.push(numeros[i]);
        }
    }
    return resultado;
}

const miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const soloPares = filtrarPares(miLista);

console.log(soloPares);