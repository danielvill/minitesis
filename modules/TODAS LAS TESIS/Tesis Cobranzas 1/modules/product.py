class Product:
    def __init__(self, nombre ,codigo, precio,cantidad,resultado,total):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.cantidad = cantidad
        self.resultado = resultado
        self.total = total
        

    def proDBCollection(self):
        return{
            'nombre': self.nombre,
            'codigo': self.codigo,
            'price': self.precio,
            'cantidad':self.cantidad,
            'resultado':self.resultado,
            'total':self.total
            
            
        }