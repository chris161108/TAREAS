// decimal a binario

let decimal = 25;
let binario = "";

while (decimal > 0) {

    let bit = decimal % 2;
    binario = bit + binario;
    decimal = match.floor(decimal / 2);
}

console.log(binario);
