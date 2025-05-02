DELIMITER $$

CREATE TRIGGER ControlMaxAlumnosAntesDeInsertar
BEFORE INSERT ON Inscripcion
FOR EACH ROW
BEGIN
    DECLARE cantidadAlumnos INT;

    -- Contar el número de alumnos ya inscritos en el curso
    SELECT COUNT(*) INTO cantidadAlumnos
    FROM Alumno
    WHERE codigoCurso = NEW.codigoCurso;

    -- Verificar si el curso ha alcanzado el máximo de alumnos
    IF cantidadAlumnos >= (SELECT maxAlumnos FROM Curso WHERE codigo = NEW.codigoCurso) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El curso ha alcanzado el límite máximo de alumnos.';
    END IF;
END$$

DELIMITER ;

-- Trigger para auto-incrementar el código en la tabla Transaccion
DELIMITER //
CREATE TRIGGER AutoIncrementCodigoTransaccion
BEFORE INSERT ON Transaccion
FOR EACH ROW
BEGIN
    DECLARE max_codigo CHAR(8);
    SET max_codigo = (SELECT MAX(codigo) FROM Transaccion);
    IF max_codigo IS NOT NULL THEN
        SET NEW.codigo = LPAD(CAST(CAST(max_codigo AS UNSIGNED) + 1 AS CHAR), 8, '0');
    ELSE
        SET NEW.codigo = '00000001';
    END IF;
END;
//
DELIMITER ;

-- Trigger para auto-incrementar el número de recibo en la tabla ReciboPago
DELIMITER //
CREATE TRIGGER AutoIncrementNumRecibo
BEFORE INSERT ON ReciboPago
FOR EACH ROW
BEGIN
    DECLARE max_recibo CHAR(6);
    SET max_recibo = (SELECT MAX(numRecibo) FROM ReciboPago);
    IF max_recibo IS NOT NULL THEN
        SET NEW.numRecibo = LPAD(CAST(CAST(max_recibo AS UNSIGNED) + 1 AS CHAR), 6, '0');
    ELSE
        SET NEW.numRecibo = '000001';
    END IF;
END;
//
DELIMITER ;