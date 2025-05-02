-- PROCEDIMIENTOS CONSULTA DE DATOS --
use smartdb;

-- PROCEDIMIENTO 1 --
DELIMITER $$

create procedure obtener_recibo_pago_alumno(in dni_alumno char(8))
begin
select ReciboPago.numRecibo, ReciboPago.fechaEmision, ReciboPago.razonpago, Alumno.primerNombre, Alumno.apellidoPaterno
from ReciboPago
join Alumno on ReciboPago.dniAlumno = Alumno.dni
where Alumno.dni = dni_alumno;
end$$

DELIMITER ;

-- PROCEDIMIENTO 2 --
DELIMITER $$

create procedure obtener_transacciones_alumno(in dni_alumno char(8))
begin
select Transaccion.codigo, Transaccion.montoTransaccion, Transaccion.tipoTransaccion
from Transaccion
join Alumno on Transaccion.dniAlumno = Alumno.dni
where Alumno.dni = dni_alumno;
end$$

DELIMITER ;

-- PROCEDIMIENTO 3 --
DELIMITER $$

create procedure listar_cursos_alumno(in dni_alumno char(8))
begin
select Curso.nombre, Curso.nivel, Curso.precio
from Inscripcion
join Curso on Inscripcion.codigoCurso = Curso.codigo
where Inscripcion.dniAlumno = dni_alumno;
end$$

DELIMITER ;

-- PROCEDIMIENTO 4 --
DELIMITER $$

create procedure verificar_pago_recibo(in numero_recibo char(6))
begin
select ReciboPago.numRecibo, Transaccion.montoTransaccion, Transaccion.tipoTransaccion
from ReciboPago
join Transaccion ON ReciboPago.codTransaccion = Transaccion.codigo
where ReciboPago.numRecibo = numero_recibo;
end$$

DELIMITER ;

-- PROCEDIMIENTO 5 --
DELIMITER $$

create procedure listado_transacciones(in tipo_transaccion varchar(25))
begin
select Transaccion.codigo, Transaccion.montoTransaccion, Transaccion.tipoTransaccion
from Transaccion
where Transaccion.tipoTransaccion = tipo_transaccion;
end$$

DELIMITER ;

-- PROCEDIMIENTO 6 --
DELIMITER $$

create procedure recibos_por_coordinador(in dni_coordinacion char(8))
begin
select ReciboPago.numRecibo, ReciboPago.fechaEmision, CoordinacionAcademica.nombres
from ReciboPago
join CoordinacionAcademica on ReciboPago.dniCoordinacion = CoordinacionAcademica.dni
where CoordinacionAcademica.dni = dni_coordinacion;
end$$

DELIMITER ;

-- PROCEDIMIENTO 7 --
DELIMITER $$

create procedure total_pagos_por_mes(in mes int, anio int)
begin
select sum(Transaccion.montoTransaccion) as totalPagos
from ReciboPago
join Transaccion on ReciboPago.codTransaccion = Transaccion.codigo
where month(ReciboPago.fechaEmision) = mes
and year(ReciboPago.fechaEmision) = anio;
end$$

DELIMITER ;

-- PROCEDIMIENTO 8 --
DELIMITER $$

create procedure pagos_mayores_a(in monto real)
begin
SELECT Alumno.primerNombre, Alumno.apellidoPaterno, Transaccion.montoTransaccion
FROM ReciboPago
JOIN Alumno ON ReciboPago.dniAlumno = Alumno.dni
JOIN Transaccion ON ReciboPago.codTransaccion = Transaccion.codigo
WHERE Transaccion.montoTransaccion > monto;
end$$

DELIMITER ;

-- PROCEDIMIENTO 9 --
DELIMITER $$

create procedure informacion_cursos(in idioma_curso varchar(20))
begin
SELECT Curso.codigo, Curso.nombre, Curso.nivel, Curso.precio, Curso.docenteEncargado
FROM Curso
WHERE Curso.idioma = idioma_curso;
end$$

DELIMITER ;

-- PROCEDIMIENTO 10 --
DELIMITER $$

create procedure obtener_celular_multiples()
begin
SELECT a.primerNombre, a.segundoNombre, a.apellidoPaterno, a.apellidoMaterno, nc.numeroCelular
FROM NumeroCelular nc
JOIN Alumno a ON nc.dniAlumno = a.dni
WHERE nc.dniAlumno IN (
    SELECT dniAlumno
    FROM NumeroCelular
    GROUP BY dniAlumno
    HAVING COUNT(*) > 1
);
end$$

DELIMITER ;