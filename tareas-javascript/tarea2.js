// Ejercicio 2: Analizador de Vocales
function contarVocales(texto) {
    let contador = 0;
    let vocales = "aeiouAEIOU";
    
    for (let i = 0; i < texto.length; i++) {
        if (vocales.includes(texto[i])) {
            contador++;
        }
    }
    
    return contador;
}

const resultado = contarVocales("Hola Mundo");
console.log(resultado);