// Ejercicio 8: Cifrador de Mensajes
function cifrarPalabra(palabra) {
    let alfabeto = "abcdefghijklmnopqrstuvwxyz";
    let cifrado = "";

    for (let i = 0; i < palabra.length; i++) {
        let letra = palabra[i].toLowerCase();
        let indice = alfabeto.indexOf(letra);

        if (indice === -1) {
            cifrado += letra;
        } else if (letra === 'z') {
            cifrado += 'a';
        } else {
            cifrado += alfabeto[indice + 1];
        }
    }
    return cifrado;
}

console.log(cifrarPalabra("hola"));