class Client:
    def __init__(self, nombre, telefono, provincia,canton,direccion,referencia,mapa,comentario):
        self.nombre = nombre
        self.telefono = telefono
        self.provincia = provincia
        self.canton = canton
        self.direccion = direccion
        self.referencia = referencia
        self.mapa = mapa
        self.comentario = comentario

    def cliDBCollection(self):
        return{
            'nombre': self.nombre,
            'telefono': self.telefono,
            'provincia': self.provincia,
            'canton': self.canton,
            'direccion':self.direccion,
            'referencia': self.referencia,
            'mapa': self.mapa,
            'comentario': self.comentario
            

        }