class Product:
    def __init__(self, nombre ,codigo, nombre_p,precio,cantidad,resultado,total,fecha_p,fecha_co):
        self.nombre = nombre
        self.codigo = codigo
        self.nombre_p = nombre_p
        self.precio = precio
        self.cantidad = cantidad
        self.resultado = resultado
        self.total = total
        self.fecha_p = fecha_p
        self.fecha_co = fecha_co
        
    def proDBCollection(self):
        return{
            'nombre': self.nombre,
            'codigo': self.codigo,
            'nombre_p': self.nombre_p,
            'precio': self.precio,
            'cantidad':self.cantidad,
            'resultado':self.resultado,
            'total':self.total,
            'fecha_p':self.fecha_p,
            'fecha_co':self.fecha_co
            
            
        }