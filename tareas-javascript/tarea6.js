// Ejercicio 6: Sanitización de Datos
function limpiarDatos(datos) {
    let arrayLimpio = [];
    
    for (let i = 0; i < datos.length; i++) {
        if (typeof datos[i] === 'string' || typeof datos[i] === 'number') {
            arrayLimpio.push(datos[i]);
        }
    }
    
    return arrayLimpio;
}

const listaMixta = ["Hola", 25, true, null, "Mundo", 42, undefined, { id: 1 }];
const resultado = limpiarDatos(listaMixta);
console.log(resultado);