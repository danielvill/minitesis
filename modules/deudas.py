class Deudas:
    def __init__(self, codigo ,valor_deuda, deuda, fecha_limite):
        self.codigo = codigo
        self.valor_deuda = valor_deuda
        self.deuda = deuda
        self.fecha_limite = fecha_limite
        
    def deudaDBCollection(self):
        return{
            'codigo': self.codigo,
            'valor_deuda': self.valor_deuda,
            'deuda': self.deuda,
            'fecha_limite': self.fecha_limite, 
        }