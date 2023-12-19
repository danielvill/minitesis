class Product:
    def __init__(self, nombre ,codigo, precio,cantidad,resultado,total,fecha_p,fecha_co):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.cantidad = cantidad
        self.resultado = resultado
        self.total = total
        self.fecha_p=fecha_p
        self.fecha_co=fecha_co
        

    def proDBCollection(self):
        return{
            'nombre': self.nombre,
            'codigo': self.codigo,
            'precio': self.precio,
            'cantidad':self.cantidad,
            'resultado':self.resultado,
            'total':self.total,
            'fecha_p':self.fecha_p,
            'fecha_co':self.fecha_co
            
            
        }