// numero perfecto

let numero = 20; 
let sumaDivisores = 0;

for (let i = 1; i < numero; i++) {
    if (numero % i === 0) {
        sumaDivisores += i;
    }
}

if (sumaDivisores === numero) {
    console.log(numero + "es un numero perfecto");
} else {
    console.log(numero + "no es un numero perfecto")
}