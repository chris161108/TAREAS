// Ejercicio 7: Palabra Más Larga
function palabraMasLarga(oracion) {
    let palabras = oracion.split(" ");
    let masLarga = "";

    for (let i = 0; i < palabras.length; i++) {
        if (palabras[i].length > masLarga.length) {
            masLarga = palabras[i];
        }
    }
    return masLarga;
}

const texto = "Aprender JavaScript es realmente fascinante";
console.log(palabraMasLarga(texto));