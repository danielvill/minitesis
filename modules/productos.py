class Productos:
    def __init__(self, codigo ,nombre, veinticinco,treinta,treintaicinco):
        self.codigo = codigo
        self.nombre = nombre
        self.veinticinco = veinticinco
        self.treinta = treinta
        self.treintaicinco = treintaicinco
        
    def productosDBCollection(self):
        return{
            'codigo': self.codigo,
            'nombre': self.nombre,
            'veinticinco': self.veinticinco,
            'treinta': self.treinta,
            'treintaicinco': self.treintaicinco,
        }