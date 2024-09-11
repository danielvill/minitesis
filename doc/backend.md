

# Lógica de la aplicación de cobranzas


## Tablas que tengo en mi base de datos

1.	Clientes
2.	Admin
3.	Cobranza
4.	Pedidos
5.	Productos
6.	Reporte_p
7.	Deudas_Yanbal
8.	Pagos_codigos
9.	Reporte_c


## Tabla Clientes
En esta tabla lo que se requiere es que agregue todo lo relacionado del cliente como se puede visualizar en el siguiente ejemplo

- Nombre	
- Telefono	
- Ciudad	
- Referencia	
- Enlace (No es obligatorio)


## Tabla Admin

Todo lo relacionado con la tabla admin y lo que se necesita ingresar de los que van a manejar el sistema en este caso solo usuario y contraseña

## Tabla Cobranza

Todo lo relacionado a cobranzas de las personas no es igual a tabla pedidos esto no es asi es más bien se recopila lo que son los datos 

-	Nombre
-   Fecha de Pedido
-	Fecha de Cobranzas
-	Valor de Cobrar
-	Abono
-	Fecha Resultado
-	Estado

## Con la tabla Pedidos

En esta tabla agregare todo lo que pida la señora para que pueda enviarse a pedidos en este caso la tabla contendrá lo siguiente 

- Id_unico
- Nombre
- Fecha de pedido
- Fecha de Cobranza
- Campaña
- Semana
- Codigo
- N_Producto
- Precio
- Cantidad
- Resultado
- Comentario

En esta tabla tiene que contener todo lo relacionado con los productos y debo continuar con la lógica que hice con el sistema de Inventario para cada uno de los productos 

**_ Recuerda: Algo que no he probado que un registro contenga tantos subregistros eso es necesario que vaya a probar _**


## Tabla Productos

- Código
- Nombre
- IC
- Veintecinco
- Treinta
- Treintacinco

Esta tabla será algo que se convierte de cvc a json para los productos que contiene ya convertidos del pdf

## Tabla Reporte_p

Esta tabla debe contener todas las cobranzas pero que se pago todo esto debe registrar 

- Nombre 
- Total
- Fecha de pedido
- Fecha de cobranza
- Abono
- Fecha Abono
- Saldo
- Estado

## Tabla Deuda Yanbal

- Código 
- Valor de Deuda
- Deuda
- Fecha Limite

Esto es lo mismo que la página de Yanbal para poder tener registrado los datos que se deben pagar esa es la idea para tener un orden para lo que se debe pagar.


## Tabla Pagos_codigos

Esta tabla es para agregar todos los depósitos que se hacen para guardarlos y registrarlos

1.	Codigo_depositante
2.	Valor
3.	Fecha
4.	Descripciones


## Tabla Reporte_c

- Nombre 
- Total
- Fecha de pedido
- Fecha de cobranza
- Abono
- Fecha Abono
- Saldo
- Estado

Esta debe contener todo lo relacionado a los movimientos de la tabla cobranzas debe contener los abonos
