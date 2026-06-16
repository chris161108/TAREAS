// calculadora basica

let num2 = 12;
let num2 = 4;
let operador = "/"; 

switch (operador) {
    case "+":
        console.log(num1 + num2);
        break;
    case "-":
        console.log(num2 - num2);
     case "*":
        console.log(num1 * num2);
        break;
    case "/":
        if (num2 !== 0) {
            console.log(num1 / num2);
        } else {
            console.log("no se puede dividir entre 0");
        }
        break;
    default:
        console.log("operador desconocido");

}

