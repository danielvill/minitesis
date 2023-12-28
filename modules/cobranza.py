class Cobranza:
    def __init__(self,nombre,total,fecha_p,fecha_co,abono,fecha_ab,resultado,pagado):
        self.nombre = nombre
        self.total = total
        self.fecha_p = fecha_p
        self.fecha_co = fecha_co
        self.abono=abono
        self.fecha_ab=fecha_ab
        self.resultado=resultado
        self.pagado=pagado
    def cobDBCollection(self):
        return{
            'nombre': self.nombre,
            'total': self.total,
            'fecha_p': self.fecha_p,
            'fecha_co': self.fecha_co,
            'abono':self.abono,
            'fecha_ab':self.fecha_ab,
            'resultado':self.resultado,
            'pagado':self.pagado    
        }
