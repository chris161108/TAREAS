// Ejercicio 10: Clasificador de Inventario
function clasificarInventario(productos) {
    let inventario = { agotados: [], premium: [], estandar: [] };

    for (let i = 0; i < productos.length; i++) {
        let p = productos[i];
        if (p.stock === 0) {
            inventario.agotados.push(p);
        } else if (p.stock > 0 && p.precio > 1000) {
            inventario.premium.push(p);
        } else {
            inventario.estandar.push(p);
        }
    }
    return inventario;
}

const lista = [{nombre: 'TV', precio: 1500, stock: 5}, {nombre: 'Mouse', precio: 20, stock: 0}];
console.log(clasificarInventario(lista));