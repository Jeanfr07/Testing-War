drop database if exists SmartDB;

create database SmartDB;

use SmartDB;

create table Curso(
	codigo char(3) primary key,
    nombre varchar(20) not null,
    idioma varchar(20) not null,
    precio real not null,
    docenteEncargado varchar(120) not null,
    nivel varchar(20) not null,
    maxAlumnos integer not null,
    
    index idx_idioma(idioma)
) engine = InnoDB;

create table CoordinacionAcademica(
	dni char(8) primary key,
    nombres varchar(50) not null,
    apellidos varchar(50) not null,
    correo varchar(50) not null
) engine = InnoDB;

create table Telefono(
	dniCoordinacion char(8),
    telefono char(9) unique not null,
    
    primary key (dniCoordinacion, telefono),
    
    constraint fk_dniCoordinacion foreign key(dniCoordinacion) references CoordinacionAcademica(dni) on delete cascade
) engine = MyISAM;

create table Alumno(
	dni char(8) primary key not null,
    primerNombre varchar(25) not null,
    segundoNombre varchar(25) not null,
    apellidoPaterno varchar(25) not null,
    apellidoMaterno varchar(25) not null,
    genero char(1),
    fechaNacimiento date not null,
    lugarProcedencia varchar(30), 

    index idx_primerNombre(primerNombre),
    index idx_apellidoPaterno(apellidoPaterno)
) engine = InnoDB;

create table NumeroCelular(
	dniAlumno char(8),
    numeroCelular char(9) unique not null,
    
    primary key (dniAlumno, numeroCelular),
    
    constraint fk_dniAlumno foreign key(dniAlumno) references Alumno(dni) on delete cascade
) engine = MyISAM;

create table Correo(
	dniAlumno char(8),
    correo varchar(50) unique not null,
    
    primary key (dniAlumno, correo),
    
    constraint fk_correoAlumno foreign key(dniAlumno) references Alumno(dni) on delete cascade
) engine = MyISAM;

create table Transaccion(
	codigo char(8) primary key,
    montoTransaccion real not null,
    tipoTransaccion varchar(25) not null,
    nombreRemitente varchar(120) not null,
    dniAlumno char(8) not null,
    dniCoordinacion char(8) not null,
    
	index idx_tipoTransaccion(tipoTransaccion),
    
    constraint fk_dniAlumnoT foreign key(dniAlumno) references Alumno(dni),
    constraint fk_dniCoordinacionT foreign key(dniCoordinacion) references CoordinacionAcademica(dni)
) engine = InnoDB;

create table Inscripcion(
    dniAlumno char(8) primary key,
    codigoCurso char(3) not null,
    dniCoordinacion char(8) not null,
    constraint fk_dniAlumnoI foreign key(dniAlumno) references Alumno(dni),
    constraint fk_codigoCursoI foreign key(codigoCurso) references Curso(codigo),
    constraint fk_dniCoordinacionI foreign key(dniCoordinacion) references CoordinacionAcademica(dni)
) engine = InnoDB;

create table ReciboPago(
	numRecibo char(6) primary key,
    fechaEmision date not null,
    razonPago varchar(40) not null,
    dniAlumno char(8) not null,
    codTransaccion char(6) not null,
    dniCoordinacion char(8) not null,
    
    index idx_fechaEmision(fechaEmision),
    
	constraint fk_dniAlumnoR foreign key(dniAlumno) references Alumno(dni),
    constraint fk_codTransaccion foreign key(codTransaccion) references Transaccion(codigo),
    constraint fk_dniCoordinacionR foreign key(dniCoordinacion) references CoordinacionAcademica(dni)
) engine = InnoDB;

