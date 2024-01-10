class Estadistica:
    def __init__(self, nombre, fecha_co,fecha_ab):
        self.nombre = nombre
        self.fecha_co =fecha_co
        self.fecha_ab = fecha_ab

    def estadBCollection(self):
        return{
            'nombre': self.nombre,
            'fecha_co': self.fecha_co,
            'fecha_ab':self.fecha_ab
            
        }