class Cobranza:
    def __init__(self,fecha_co,fecha_p,nombre,total,codigo,cantidad,precio):
        self.nombre = nombre
        self.fecha_co = fecha_co
        self.fecha_p = fecha_p
        self.codigo = codigo
        self.cantidad= cantidad
        self.precio = precio
        self.total = total
        

    def cobDBCollection(self):
        return{
            'nombre': self.nombre,
            'fecha_co': self.fecha_co,
            'fecha_p': self.fecha_p,
            'codigo': self.codigo,
            'cantidad': self.cantidad,
            'precio': self.precio,
            'total': self.total
            
        }
