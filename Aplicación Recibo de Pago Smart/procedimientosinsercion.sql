use smartdb;

DELIMITER $$

CREATE PROCEDURE InsertarAlumno(
    IN alumnoDNI CHAR(8),
    IN primerNombre VARCHAR(25),
    IN segundoNombre VARCHAR(25),
    IN apellidoPaterno VARCHAR(25),
    IN apellidoMaterno VARCHAR(25),
    IN genero CHAR(1),
    IN fechaNacimiento DATE,
    IN lugarProcedencia VARCHAR(30),
    IN codigoCurso CHAR(3),
    IN correoAlumno VARCHAR(50),        -- Correo del alumno
    IN numeroCelularAlumno CHAR(9),     -- Número de celular del alumno
    IN dniCoordinacion CHAR(8)         -- DNI de la coordinación académica
)
BEGIN
    -- Verificar si el alumno ya existe
    IF EXISTS (SELECT 1 FROM Alumno WHERE dni = alumnoDNI) THEN
        SELECT CONCAT('El alumno con DNI ', alumnoDNI, ' ya existe.') AS Resultado;
    ELSE
        -- Insertar el nuevo alumno en la tabla Alumno
        INSERT INTO Alumno (
            dni, primerNombre, segundoNombre, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, lugarProcedencia
        ) VALUES (
            alumnoDNI, primerNombre, segundoNombre, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, lugarProcedencia
        );

        -- Insertar el correo del alumno en la tabla Correo
        INSERT INTO Correo (
            dniAlumno, correo
        ) VALUES (
            alumnoDNI, correoAlumno
        );

        -- Insertar el número de celular del alumno en la tabla NumeroCelular
        INSERT INTO NumeroCelular (
            dniAlumno, numeroCelular
        ) VALUES (
            alumnoDNI, numeroCelularAlumno
        );

        -- Insertar el nuevo registro de inscripción en la tabla Inscripcion
        INSERT INTO Inscripcion (
            dniAlumno, codigoCurso, dniCoordinacion
        ) VALUES (
            alumnoDNI, codigoCurso, dniCoordinacion
        );

        -- Mensaje de confirmación
        SELECT CONCAT('Alumno con DNI ', alumnoDNI, ' insertado correctamente con correo, número de celular e inscripción al curso.') AS Resultado;
    END IF;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE AgregarCurso(
    IN codigoCurso CHAR(3),
    IN nombreCurso VARCHAR(20),
    IN idiomaCurso VARCHAR(20),
    IN precioCurso REAL,
    IN docenteCurso VARCHAR(120),
    IN nivelCurso VARCHAR(20),
    IN maxAlumnosCurso INTEGER
)
BEGIN
    -- Verificar si el código del curso ya existe
    IF EXISTS (SELECT 1 FROM Curso WHERE codigo = codigoCurso) THEN
        SELECT CONCAT('El curso con código ', codigoCurso, ' ya existe.') AS Resultado;
    ELSE
        -- Insertar el nuevo curso en la tabla Curso
        INSERT INTO Curso (
            codigo, nombre, idioma, precio, docenteEncargado, nivel, maxAlumnos
        ) VALUES (
            codigoCurso, nombreCurso, idiomaCurso, precioCurso, docenteCurso, nivelCurso, maxAlumnosCurso
        );
        
        -- Mensaje de confirmación
        SELECT CONCAT('Curso con código ', codigoCurso, ' insertado correctamente.') AS Resultado;
    END IF;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE AgregarCoordinacionAcademica(
    IN dniCoordinacion CHAR(8),
    IN nombresCoordinacion VARCHAR(50),
    IN apellidosCoordinacion VARCHAR(50),
    IN correoCoordinacion VARCHAR(50),
    IN telefonoCoordinacion CHAR(9) 
)
BEGIN
    -- Verificar si la coordinación académica ya existe
    IF EXISTS (SELECT 1 FROM CoordinacionAcademica WHERE dni = dniCoordinacion) THEN
        SELECT CONCAT('La coordinación académica con DNI ', dniCoordinacion, ' ya existe.') AS Resultado;
    ELSE
        -- Insertar la nueva coordinación académica en la tabla CoordinacionAcademica
        INSERT INTO CoordinacionAcademica (
            dni, nombres, apellidos, correo
        ) VALUES (
            dniCoordinacion, nombresCoordinacion, apellidosCoordinacion, correoCoordinacion
        );
        
        -- Mensaje de confirmación
        SELECT CONCAT('Coordinación académica con DNI ', dniCoordinacion, ' insertada correctamente.') AS Resultado;
        
        -- Si se proporciona un teléfono, insertarlo en la tabla Telefono
        IF telefonoCoordinacion IS NOT NULL THEN
            INSERT INTO Telefono (
                dniCoordinacion, telefono
            ) VALUES (
                dniCoordinacion, telefonoCoordinacion
            );
            SELECT CONCAT('Teléfono ', telefonoCoordinacion, ' agregado a la coordinación académica con DNI ', dniCoordinacion) AS ResultadoTelefono;
        END IF;
    END IF;
END$$

DELIMITER ;

DELIMITER //

CREATE PROCEDURE InsertarTransaccion(
    IN p_montoTransaccion REAL,
    IN p_tipoTransaccion VARCHAR(25),
    IN p_nombreRemitente VARCHAR(120),
    IN p_dniAlumno CHAR(8),
    IN p_dniCoordinacion CHAR(8)
)
BEGIN
    -- Insertar la nueva transacción
    INSERT INTO Transaccion (
        montoTransaccion,
        tipoTransaccion,
        nombreRemitente,
        dniAlumno,
        dniCoordinacion
    ) VALUES (
        p_montoTransaccion,
        p_tipoTransaccion,
        p_nombreRemitente,
        p_dniAlumno,
        p_dniCoordinacion
    );
END;
//

DELIMITER ;


DELIMITER //

CREATE PROCEDURE InsertarReciboPago(
    IN p_fechaEmision DATE,
    IN p_razonPago VARCHAR(40),
    IN p_dniAlumno CHAR(8),
    IN p_codTransaccion CHAR(8), 
    IN p_dniCoordinacion CHAR(8)
)
BEGIN
    -- Verificar si el código de transacción existe en la base de datos
    IF EXISTS (SELECT 1 FROM Transaccion WHERE codigo = p_codTransaccion) THEN
        -- Insertar el nuevo recibo de pago
        INSERT INTO ReciboPago (
            fechaEmision,
            razonPago,
            dniAlumno,
            codTransaccion,
            dniCoordinacion
        ) VALUES (
            p_fechaEmision,
            p_razonPago,
            p_dniAlumno,
            p_codTransaccion, 
            p_dniCoordinacion
        );
    ELSE
        SELECT CONCAT('No existe ese código de transacción.') AS Resultado;
    END IF;
END;
//

DELIMITER ;