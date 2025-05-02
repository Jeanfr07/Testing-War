USE SmartDB;
INSERT INTO Curso (codigo, nombre, idioma, precio, docenteEncargado, nivel, maxAlumnos)
VALUES
('IB1', 'Inglés Básico 1', 'Inglés', 200.00, 'Katherine Lazo', 'Básico', 30),
('IB2', 'Inglés Básico 2', 'Inglés', 250.00, 'Hayde Sandoval', 'Básico', 30),
('IB3', 'Inglés Básico 3', 'Inglés', 300.00, 'Daniel Murillo', 'Básico', 30);
INSERT INTO CoordinacionAcademica (dni, nombres, apellidos, correo)
VALUES ('70244842', 'Flor Marilia', 'Velasquez Ordoñez', 'flor.mevelasquezo@gmail.com');
INSERT INTO Alumno (dni, primerNombre, segundoNombre, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, lugarProcedencia)
VALUES
('74233730', 'Yaneli', 'Margoth', 'Tipo', 'Churata', 'F', '2004-09-07', 'Puno'),
('01342387', 'Sandra', 'Suzette', 'Apaza', 'Quispe', 'F', '1977-12-16', 'Puno'),
('60850516', 'Flor', 'Andrea', 'Escarcena', 'Iberos', 'F', '1996-02-19', 'Puno'),
('70977117', 'Carolina', 'Raquel', 'Velasquez', 'Mamani', 'F', '2002-12-16', 'Puno'),
('60980364', 'Nicole', 'Gabriela', 'Miranda', 'Cruz', 'F', '2004-09-28', 'Puno'),
('74205947', 'Kiara', 'Mollehuanca', 'Mollehuanca', 'Castillo', 'F', '2000-09-22', 'Puno'),
('71378923', 'BRADDY', 'GABRIEL', 'ABARCA', 'ARANIBAR', 'M', '1993-09-26', 'Puno'),
('75347227', 'Jimena', 'Nayhely', 'Roque', 'Quispe', 'F', '2002-07-15', 'Puno'),
('40661862', 'Leoncio', 'Miriam', 'Flores', 'Suricallo', 'M', '1980-03-20', 'Puno'),
('62074117', 'Yanet', 'Antonio', 'Martinez', 'Coila', 'F', '1998-09-05', 'Santa Lucía'),
('72357011', 'Greis', 'Rose', 'Zapana', 'Yahua', 'F', '2009-11-25', 'Puno'),
('75521474', 'Maribel', 'Melina', 'Choquecota', 'Illacutipa', 'F', '2002-11-11', 'Puno'),
('61803131', 'YUREMI', 'SAHILY', 'CHOQUEQUETINO', 'QUISPE', 'F', '2008-04-20', 'Juliaca'),
('70000924', 'Jean', 'Ronet', 'Mamami', 'Cara', 'M', '1998-06-11', 'Cusco'),
('74350315', 'Danedy', 'Yoseling', 'Parillo', 'Coaquira', 'F', '2006-05-06', 'Juliaca'),
('61323166', 'Miguel', 'Carlos', 'Pilco', 'Pilino', 'M', '1974-04-10', 'Arequipa'),
('77014380', 'Cristel', 'Alejandra', 'Jove', 'Pacompia', 'F', '2010-04-16', 'Juliaca'),
('60029514', 'Astrid', 'Alexandra', 'Poma', 'Pari', 'F', '2008-07-22', 'Puno');
INSERT INTO Inscripcion (dniAlumno, codigoCurso, dniCoordinacion)
VALUES
('74233730', 'IB1', '70244842'),
('01342387', 'IB1', '70244842'),
('60850516', 'IB1', '70244842'),
('70977117', 'IB1', '70244842'),
('60980364', 'IB1', '70244842'),
('74205947', 'IB1', '70244842'),
('71378923', 'IB1', '70244842'),
('75347227', 'IB1', '70244842'),
('40661862', 'IB1', '70244842'),
('62074117', 'IB1', '70244842'),
('72357011', 'IB1', '70244842'),
('75521474', 'IB1', '70244842'),
('61803131', 'IB2', '70244842'),
('70000924', 'IB2', '70244842'),
('74350315', 'IB3', '70244842'),
('61323166', 'IB1', '70244842'),
('77014380', 'IB3', '70244842'),
('60029514', 'IB2', '70244842');
INSERT INTO Transaccion (codigo, montoTransaccion, tipoTransaccion, nombreRemitente, dniAlumno, dniCoordinacion)
VALUES
-- BECA COMPLETA
('TRX001', 0, 'BECA COMPLETA', 'Yaneli Margoth Tipo Churata', '74233730', '70244842'),
('TRX002', 0, 'BECA COMPLETA', 'Sandra Suzette Apaza Quispe', '01342387', '70244842'),
('TRX003', 0, 'BECA COMPLETA', 'Flor Andrea Escarcena Iberos', '60850516', '70244842'),
('TRX004', 0, 'BECA COMPLETA', 'Marco Antonio Cruz Coila', '70000924', '70244842'),
('TRX005', 0, 'BECA COMPLETA', 'Kiara Mollehuanca Castillo', '74205947', '70244842'),
('TRX006', 0, 'BECA COMPLETA', 'BRADDY GABRIEL ABARCA ARANIBAR', '71378923', '70244842'),
-- PAGOS EFECTUADOS
('TRX007', 200.00, 'EN EFECTIVO', 'Carolina Raquel Velasquez Mamani', '70977117', '70244842'),
('TRX008', 200.00, 'EN EFECTIVO', 'Nicole Gabriela Miranda Chamba', '60980364', '70244842'),
('TRX009', 200.00, 'PAGO EN EFECTIVO', 'Shantall Michelle Carrasco Flores', '61803131', '70244842'),
('TRX010', 200.00, 'PAGO EN EFECTIVO', 'Jimena Nayhely Roque Quispe', '75347227', '70244842'),
('TRX011', 250.00, 'EFECTIVO', 'Maribel Melina Choquecota Illacutipa', '75521474', '70244842'),
('TRX012', 250.00, 'EFECTIVO', 'Rayza Melina Choquecota Illacutipa', '76871660', '70244842'),
('TRX013', 250.00, 'EFECTIVO', 'Greis Rose Zapana Yahua', '62074117', '70244842'),
('TRX014', 300.00, 'EFECTIVO', 'Danedy Yoseling Parillo Coaquira', '74350315', '70244842'),
('TRX015', 300.00, 'PAGO POR YAPE', 'Danedy Yoseling Parillo Coaquira', '73540100', '70244842'),
('TRX016', 300.00, 'EN EFECTIVO', 'Jean Ronet Mamani Mamani', '70000924', '70244842'),
('TRX017', 329.00, 'EN EFECTIVO', 'Jean Ronet Mamani Mamani', '70000924', '70244842'),
('TRX018', 148.00, 'PAGO LIBROS', 'Shantall Michelle Carrasco Flores', '61803131', '70244842'),
('TRX019', 119356.00, 'EN EFECTIVO', 'Zenaida Maria Mamani Huayta', '45532041', '70244842'),
('TRX020', 120303.00, 'EN EFECTIVO', 'Homero Ticona Garayar', '77463860', '70244842'),
('TRX021', 120302.00, 'EN EFECTIVO', 'Danedy Yoseling Parillo Coaquira', '74350315', '70244842');
INSERT INTO NumeroCelular (dniAlumno, numeroCelular)
VALUES
('74233730', '950533774'),
('01342387', '968780095'),
('60850516', '914368122'),
('70977117', '997058062'),
('60980364', '918565927'),
('74205947', '952152089'),
('71378923', '915161005'),
('75347227', '913882106'),
('61803131', '985360710'),
('40661862', '971533332'),
('62074117', '975455292'),
('72357011', '929252521'),
('71571616', '921582529'),
('75521474', '943989086'),
('73740817', '974358104'),
('76871606', '923573958'),
('70000924', '952420857'),
('74350315', '931034714'),
('61323166', '995429806'),
('77014380', '951741362'),
('60029514', '932873919'),
('61750147', '950015053'),
('74107731', '967663132'),
('74363680', '930133397'),
('72055315', '951655215'),
('71756116', '990505336');
INSERT INTO Correo (dniAlumno, correo)
VALUES
('74233730', 'yanelitapitopchurata@gmail.com'),
('01342387', 'zsapazaza@gmail.com'),
('60850516', 'flor@gmail.com'),
('70977117', 'carolinaraquele@gmail.com'),
('60980364', 'mirandachamba@gmail.com'),
('74205947', 'mollehuancacas@gmail.com'),
('71378923', 'braddygabriel@gmail.com'),
('75347227', 'jimenaorquequisp@gmail.com'),
('61803131', 'shantallflor2@gmail.com'),
('40661862', 'leosur80@gmail.com'),
('62074117', 'miriamartinezs@gmail.com'),
('72357011', 'zapanaabraham@gmail.com'),
('71571616', 'anyela10.15w@gmail.com'),
('75521474', 'marily7722@gmail.com'),
('61803131', 'yuremic0993@gmail.com'),
('73740817', 'joserichardpt1@gmail.com'),
('76871606', 'edbusdan@gmail.com'),
('70000924', 'mamanimamanim@gmail.com'),
('74350315', 'danedyoelling@gmail.com'),
('61323166', 'miguelpilino@gmail.com'),
('77014380', 'crisalejandrajove@gmail.com'),
('60029514', 'astridpomapari@gmail.com'),
('61750147', 'jhimysalas60@gmail.com'),
('74107731', 'zmamanihuayta@gmail.com'),
('74363680', 'claudiamrub@gmail.com'),
('72055315', 'luzmilarc0223@gmail.com'),
('71756116', 'gracekurmysosa@gmail.com'),
('74205947', 'hebermamani@gmail.com');
INSERT INTO Telefono (dniCoordinacion, telefono)
VALUES ('70244842', '985199644');
INSERT INTO ReciboPago (numRecibo, fechaEmision, razonPago, dniAlumno, codTransaccion, dniCoordinacion)
VALUES
-- RECIBOS PARA ESTUDIANTES CON BECA COMPLETA (RAZÓN: EXONERACIÓN DE PAGO)
('RCP001', '2023-05-04', 'Exoneración de Pago - Beca Completa', '74233730', 'TRX001', '70244842'),
('RCP002', '2023-05-05', 'Exoneración de Pago - Beca Completa', '01342387', 'TRX002', '70244842'),
('RCP003', '2023-05-09', 'Exoneración de Pago - Beca Completa', '60850516', 'TRX003', '70244842'),
('RCP004', '2023-06-13', 'Exoneración de Pago - Beca Completa', '70000924', 'TRX004', '70244842'),
('RCP005', '2023-06-13', 'Exoneración de Pago - Beca Completa', '74205947', 'TRX005', '70244842'),
('RCP006', '2023-06-13', 'Exoneración de Pago - Beca Completa', '71378923', 'TRX006', '70244842'),
-- RECIBOS PARA PAGOS EN EFECTIVO (RAZÓN: INSCRIPCIÓN AL CURSO)
('RCP007', '2023-06-06', 'Pago de Inscripción - Inglés Básico 1', '70977117', 'TRX007', '70244842'),
('RCP008', '2023-06-09', 'Pago de Inscripción - Inglés Básico 1', '60980364', 'TRX008', '70244842'),
('RCP009', '2023-07-07', 'Pago de Inscripción - Inglés Básico 1', '61803131', 'TRX009', '70244842'),
('RCP010', '2023-07-07', 'Pago de Inscripción - Inglés Básico 1', '75347227', 'TRX010', '70244842'),
('RCP011', '2023-08-06', 'Pago de Inscripción - Inglés Básico 1', '75521474', 'TRX011', '70244842'),
('RCP012', '2023-08-06', 'Pago de Inscripción - Inglés Básico 1', '76871660', 'TRX012', '70244842'),
-- RECIBOS PARA PAGOS EN EFECTIVO (RAZÓN: INSCRIPCIÓN A NIVELES SUPERIORES)
('RCP013', '2023-08-07', 'Pago de Inscripción - Inglés Básico 2', '61803131', 'TRX013', '70244842'),
('RCP014', '2023-08-08', 'Pago de Inscripción - Inglés Básico 2', '70000924', 'TRX014', '70244842'),
('RCP015', '2023-09-06', 'Pago de Inscripción - Inglés Básico 2', '72357011', 'TRX015', '70244842'),
('RCP016', '2023-10-09', 'Pago de Inscripción - Inglés Básico 3', '77463860', 'TRX016', '70244842'),
('RCP017', '2023-10-09', 'Pago de Inscripción - Inglés Básico 3', '74350315', 'TRX017', '70244842'),
('RCP018', '2023-12-04', 'Pago de Inscripción - Inglés Básico 4', '70000924', 'TRX018', '70244842'),
('RCP019', '2023-12-05', 'Pago de Inscripción - Inglés Básico 4', '60295164', 'TRX019', '70244842'),
('RCP020', '2023-12-05', 'Pago de Inscripción - Inglés Básico 4', '72357011', 'TRX020', '70244842'),
-- RECIBOS PARA PAGO DE LIBROS
('RCP021', '2023-10-09', 'Pago de Libros de Idiomas', '71378923', 'TRX021', '70244842');