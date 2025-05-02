-- Consulta para obtener los detalles del recibo de pago de un alumno específico:
SELECT ReciboPago.numRecibo, ReciboPago.fechaEmision, ReciboPago.razonpago, Alumno.primerNombre, Alumno.apellidoPaterno
FROM ReciboPago
JOIN Alumno ON ReciboPago.dniAlumno = Alumno.dni
WHERE Alumno.dni = '24374901';

-- Consulta para obtener todas las transacciones realizadas por un alumno:
SELECT Transaccion.codigo, Transaccion.montoTransaccion, Transaccion.tipoTransaccion
FROM Transaccion
JOIN Alumno ON Transaccion.dniAlumno = Alumno.dni
WHERE Alumno.dni = '24374901';

-- Consulta para listar todos los cursos en los que un alumno está inscrito:
SELECT Curso.nombre, Curso.nivel, Curso.precio
FROM Inscripcion
JOIN Curso ON Inscripcion.codigoCurso = Curso.codigo
WHERE Inscripcion.dniAlumno = '24374901';

-- Consulta para verificar si el pago de un recibo ya ha sido procesado:
SELECT ReciboPago.numRecibo, Transaccion.montoTransaccion, Transaccion.tipoTransaccion
FROM ReciboPago
JOIN Transaccion ON ReciboPago.codTransaccion = Transaccion.codigo
WHERE ReciboPago.numRecibo = '3453';

-- Consulta para listar todas las transacciones de un tipo específico (por ejemplo, transferencias):
SELECT Transaccion.codigo, Transaccion.montoTransaccion, Transaccion.tipoTransaccion
FROM Transaccion
WHERE Transaccion.tipoTransaccion = 'Transferencia';

-- Consulta para obtener los recibos emitidos por un coordinador académico específico:
SELECT ReciboPago.numRecibo, ReciboPago.fechaEmision, CoordinacionAcademica.nombres
FROM ReciboPago
JOIN CoordinacionAcademica ON ReciboPago.dniCoordinacion = CoordinacionAcademica.dni
WHERE CoordinacionAcademica.dni = '70946723';

-- Consulta para obtener el total de pagos recibidos en un mes específico:
SELECT SUM(Transaccion.montoTransaccion) AS totalPagos
FROM ReciboPago
JOIN Transaccion ON ReciboPago.codTransaccion = Transaccion.codigo
WHERE MONTH(ReciboPago.fechaEmision) = 02
AND YEAR(ReciboPago.fechaEmision) = 2024;

-- Consulta para obtener los alumnos que han realizado pagos superiores a un monto determinado:
SELECT Alumno.primerNombre, Alumno.apellidoPaterno, Transaccion.montoTransaccion
FROM ReciboPago
JOIN Alumno ON ReciboPago.dniAlumno = Alumno.dni
JOIN Transaccion ON ReciboPago.codTransaccion = Transaccion.codigo
WHERE Transaccion.montoTransaccion > 140.00;

-- Consulta para obtener la información acerca de los cursos de cierto idioma 
SELECT Curso.codigo, Curso.nombre, Curso.nivel, Curso.precio, Curso.docenteEncargado
FROM Curso
WHERE Curso.idioma = 'Inglés';

-- Consulta para obtener los números de celular de un alumno en caso tuviera más de un número de celular a su nombre
SELECT a.primerNombre, a.segundoNombre, a.apellidoPaterno, a.apellidoMaterno, nc.numeroCelular
FROM NumeroCelular nc
JOIN Alumno a ON nc.dniAlumno = a.dni
WHERE nc.dniAlumno IN (
    SELECT dniAlumno
    FROM NumeroCelular
    GROUP BY dniAlumno
    HAVING COUNT(*) > 1
);
