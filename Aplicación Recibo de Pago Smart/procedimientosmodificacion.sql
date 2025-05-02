USE smartdb;

-- Actualizar datos de un curso
DELIMITER //
CREATE PROCEDURE ActualizarCurso(
    IN p_codigo CHAR(3),
    IN p_nombre VARCHAR(20),
    IN p_idioma VARCHAR(20),
    IN p_precio REAL,
    IN p_docenteEncargado VARCHAR(120),
    IN p_nivel VARCHAR(20),
    IN p_maxAlumnos INT
)
BEGIN
    UPDATE Curso
    SET nombre = p_nombre,
        idioma = p_idioma,
        precio = p_precio,
        docenteEncargado = p_docenteEncargado,
        nivel = p_nivel,
        maxAlumnos = p_maxAlumnos
    WHERE codigo = p_codigo;
END //
DELIMITER ;

-- Actualizar datos de alumno --
DELIMITER //
CREATE PROCEDURE ActualizarAlumno(
    IN p_dni CHAR(8),
    IN p_primerNombre VARCHAR(25),
    IN p_segundoNombre VARCHAR(25),
    IN p_apellidoPaterno VARCHAR(25),
    IN p_apellidoMaterno VARCHAR(25),
    IN p_genero CHAR(1),
    IN p_fechaNacimiento DATE,
    IN p_lugarProcedencia VARCHAR(30),
    IN p_codigoCurso CHAR(3)
)
BEGIN
    UPDATE Alumno
    SET primerNombre = p_primerNombre,
        segundoNombre = p_segundoNombre,
        apellidoPaterno = p_apellidoPaterno,
        apellidoMaterno = p_apellidoMaterno,
        genero = p_genero,
        fechaNacimiento = p_fechaNacimiento,
        lugarProcedencia = p_lugarProcedencia,
        codigoCurso = p_codigoCurso
    WHERE dni = p_dni;
END //
DELIMITER ;

-- Actualizar informacion de contacto de alumno --
DELIMITER //
CREATE PROCEDURE ActualizarNumeroCelular(
    IN p_dniAlumno CHAR(8),
    IN p_numeroActual CHAR(9),
    IN p_numeroNuevo CHAR(9)
)
BEGIN
    UPDATE NumeroCelular
    SET numeroCelular = p_numeroNuevo
    WHERE dniAlumno = p_dniAlumno AND numeroCelular = p_numeroActual;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ActualizarCorreo(
    IN p_dniAlumno CHAR(8),
    IN p_correoActual VARCHAR(50),
    IN p_correoNuevo VARCHAR(50)
)
BEGIN
    UPDATE Correo
    SET correo = p_correoNuevo
    WHERE dniAlumno = p_dniAlumno AND correo = p_correoActual;
END //
DELIMITER ;

-- Actualizar coordinacion -- 
DELIMITER //
CREATE PROCEDURE ActualizarCoordinador(
    IN p_dni CHAR(8),
    IN p_nombres VARCHAR(50),
    IN p_apellidos VARCHAR(50),
    IN p_correo VARCHAR(50)
)
BEGIN
    UPDATE CoordinacionAcademica
    SET nombres = p_nombres,
        apellidos = p_apellidos,
        correo = p_correo
    WHERE dni = p_dni;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ActualizarTelefonoCoordinador(
    IN p_dniCoordinador CHAR(8),
    IN p_telefonoActual CHAR(9),
    IN p_telefonoNuevo CHAR(9)
)
BEGIN
    UPDATE Telefono
    SET telefono = p_telefonoNuevo
    WHERE dniCoordinacion = p_dniCoordinador AND telefono = p_telefonoActual;
END //
DELIMITER ;