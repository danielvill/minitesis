CREATE DATABASE cobryan;

CREATE TABLE cliente(
    id_cliente int ,
    nombre  varchar(50)PRIMARY KEY,
    telefono varchar(50),
    ciudad varchar(50),
    referencia varchar(50),
    enlace varchar(50)
);

create table admin(
    user varchar(50) not null,
    contraseña varchar(50) not null
);

create table cobranza(
    id_cobranza int not null PRIMARY KEY,
    nombre varchar(50),
    fecha_de_pedido date,
    fecha_de_cobranzas date,
    abono int,
    fecha date,
    resultado int,
    estado varchar(50),
    FOREIGN KEY (nombre) REFERENCES cliente(nombre)
);
create table pedidos(
    id_unico int not null,
    nombre varchar(50),
    fecha_de_pedido date,
    fecha_de_cobranzas date,
    campaña varchar(50),
    semana varchar(50),
    codigo int() primary key,
    n_produtos varchar(50),
    precio float ,
    cantidad float ,
    resultado float,
    comentario varchar(50),
    FOREIGN KEY (id_unico) REFERENCES cobranza(id_cobranza)
);

create table productos(
    codigo int(10) primary key,
    campaña varchar(50),
    nombre varchar(50),
    ic float,
    veinticinco float,
    treinta float,
    treintacinco float,
    FOREIGN key (codigo) references pedidos (codigo)

);

create table reporte (
    nombre varchar(50) not null,
    total float (10),
    fecha_de_pedido date,
    fecha_de_cobranzas date,
    abono  float (10),
    fecha_abono date,
    saldo float (10),
    estado varchar (50)
);

create table deudas(
    codigo int (10) not null,
    valor_deuda float (10) ,
    deuda float,
    fecha_limite date
);

create table comprobantes(
    codigo_depositante int(10) not null,
    valor float (10),
    fecha date,
    descripciones varchar
)

