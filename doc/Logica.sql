CREATE DATABASE cobryan;

CREATE TABLE cliente(
    id_cliente int PRIMARY KEY,
    nombre  varchar(50),
    telefono varchar(50),
    ciudad varchar(50),
    referencia varchar(50),
    enlace varchar(50)
);

create table admin(
    user varchar(50) not null,
    password varchar(50) not null
    
);

create table cobranza(
    nombre varchar(50),
    fecha_de_pedido date,
    fecha_de_cobranzas date,
    abono int,
    fecha date,
    resultado int,
    estado int
);

create table pedidos(
    id_unico int not null,
    nombre varchar(50),
    fecha_de_pedido date,
    fecha_de_cobranzas date,
    campaña varchar(50),
    semana varchar(50),
    codigo int(),
    n_produtos varchar(50),
    precio float ,
    cantidad float ,
    resultado float,
    comentario varchar(50)

);

create table productos(
    codigo int(10),
    nombre varchar(50),
    ic float,
    25% float,
    30% float,
    35% float,

);

