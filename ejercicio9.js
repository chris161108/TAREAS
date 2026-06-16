// verificador de primos

let numero = 13;
let esPrimo = true;

if (numero <= 1) {
    esPrimo = false;
} else {
    for (let i = 2;  i <= numero / 2; i++) {
        if (numero % i === 0) {
            esPrimo = false;
            break;
        }
    }
}

console.log("es primo?: " + esPrimo);
