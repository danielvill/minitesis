class Comprobantes:
    def __init__(self, codigo_deposito , valor,fecha,descripciones):
        self.codigo_deposito = codigo_deposito
        self.valor = valor
        self.fecha = fecha
        self.descripciones = descripciones
        
    def comprobanteDBCollection(self):
        return{
            'codigo_deposito': self.codigo_deposito,
            'valor': self.valor, 
        }