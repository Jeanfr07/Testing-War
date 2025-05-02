DELIMITER $$

CREATE PROCEDURE EliminarCurso(
    IN codigoCurso CHAR(3)
)
BEGIN
    -- Verificar si el curso existe
    IF NOT EXISTS (SELECT 1 FROM Curso WHERE codigo = codigoCurso) THEN
        SELECT CONCAT('El curso con código ', codigoCurso, ' no existe.') AS Resultado;
    ELSE
        -- Verificar si hay alumnos inscritos en el curso
        IF EXISTS (SELECT 1 FROM Inscripcion WHERE codigoCurso = codigoCurso) THEN
            -- Eliminar a los alumnos inscritos en el curso (Inscripciones)
            DELETE FROM Inscripcion WHERE codigoCurso = codigoCurso;

            -- Confirmación de la eliminación de inscripción y actualización de alumnos
            SELECT CONCAT('El curso con código ', codigoCurso, ' tiene alumnos inscritos. Las inscripciones han sido eliminadas y los alumnos desvinculados del curso.') AS Resultado;
        END IF;

        -- Eliminar el curso de la tabla Curso
        DELETE FROM Curso WHERE codigo = codigoCurso;

        -- Confirmación de eliminación del curso
        SELECT CONCAT('Curso con código ', codigoCurso, ' eliminado correctamente.') AS Resultado;
    END IF;
END$$

DELIMITER ;

