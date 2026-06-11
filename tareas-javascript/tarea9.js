// Ejercicio 9: Motor Bancario
function motorBancario(saldo, operaciones) {
    let errores = 0;
    for (let i = 0; i < operaciones.length; i++) {
        if (operaciones[i].tipo === 'deposito') {
            saldo += operaciones[i].monto;
        } else if (operaciones[i].tipo === 'retiro') {
            if (saldo >= operaciones[i].monto) {
                saldo -= operaciones[i].monto;
            } else {
                errores++;
            }
        }
    }
    return { saldoFinal: saldo, errores: errores };
}

const ops = [{tipo: 'deposito', monto: 500}, {tipo: 'retiro', monto: 1000}];
console.log(motorBancario(200, ops));