// Ejercicio 5: Procesador de Notas
function procesarNotas(estudiantes) {
    for (let i = 0; i < estudiantes.length; i++) {
        if (estudiantes[i].nota >= 60) {
            estudiantes[i].estado = 'Aprobado';
        } else {
            estudiantes[i].estado = 'Reprobado';
        }
    }
    return estudiantes;
}

const listaEstudiantes = [
    { nombre: 'Ana', nota: 85 },
    { nombre: 'Juan', nota: 45 },
    { nombre: 'Luis', nota: 60 }
];

const resultado = procesarNotas(listaEstudiantes);
console.log(resultado);