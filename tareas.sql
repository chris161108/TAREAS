-- Parte 1 Creacion de Tabla Principal
-- Creando la tabla de empleados con su llave primaria automatica
CREATE TABLE Empleados (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    salario DECIMAL(10, 2),
    fecha_contratacion DATE
);

-- Parte2 Insercion de Registros
-- Metiendo los primeros registros de prueba para trabajar
INSERT INTO Empleados (nombre, salario, fecha_contratacion) 
VALUES 
('christopher', 3500.00, '2021-03-15'),
('el negro', 2800.00, '2019-07-22'),
('anuel', 4200.00, '2022-01-10');

-- parte3 Consulta Basica y Filtrado
-- Buscando empleados con sueldo alto mayor a 3000
SELECT nombre, salario 
FROM Empleados 
WHERE salario > 3000;

-- parte4 Actualizacion Salarial
-- Subiendo el sueldo un 10 por ciento usando el id
UPDATE Empleados 
SET salario = salario * 1.10 
WHERE id_empleado = 2;

-- parte5 Eliminacion de Registros
-- Borrando los registros de empleados contratados antes de 2020
DELETE FROM Empleados 
WHERE fecha_contratacion < '2020-01-01';

-- parte6 Top 5 Mejores Pagados
-- Ordenando de mayor a menor sueldo con un limite de 5
SELECT * FROM Empleados 
ORDER BY salario DESC 
LIMIT 5;

-- Parte7 Integridad Referencial
-- Creamos la tabla de departamentos con la sintaxis del compilador
CREATE TABLE Departamentos (
    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_departamento VARCHAR(50)
);

INSERT INTO Departamentos (nombre_departamento) VALUES ('Ventas'), ('Sistemas'), ('Gerencia');


ALTER TABLE Empleados 
ADD COLUMN id_departamento INT REFERENCES Departamentos(id_departamento);

UPDATE Empleados SET id_departamento = 1 WHERE id_empleado = 2; 
UPDATE Empleados SET id_departamento = 2 WHERE id_empleado = 1; 
UPDATE Empleados SET id_departamento = 3 WHERE id_empleado = 3;


-- Parte8 Consultas Multitabla
-- Juntamos las dos tablas con un INNER JOIN para ver que empleado pertenece a cada area
SELECT Empleados.nombre, Departamentos.nombre_departamento
FROM Empleados
INNER JOIN Departamentos 
ON Empleados.id_departamento = Departamentos.id_departamento;


-- Parte9 Totales por Departamento
-- Agrupamos para contar los empleados y sumar los salarios de cada departamento
SELECT id_departamento, SUM(salario) AS total_salarios, COUNT(*) AS total_empleados
FROM Empleados
GROUP BY id_departamento;


-- Parte10 Filtrado de Grupos
-- Filtramos los grupos usando HAVING para mostrar solo donde el promedio pase de 2500
SELECT id_departamento, AVG(salario) AS promedio_salario
FROM Empleados
GROUP BY id_departamento
HAVING AVG(salario) > 2500;