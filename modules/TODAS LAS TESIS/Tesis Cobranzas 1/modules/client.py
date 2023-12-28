class Client:
    def __init__(self, nombre, telefono, direccion,provincia,canton ,referencia,mapa,comentario):
        self.nombre = nombre
        self.telefono = telefono
        self.provincia = provincia
        self.canton = canton
        self.referencia = referencia
        self.mapa = mapa
        self.comentario = comentario
        self.direccion = direccion

    def cliDBCollection(self):
        return{
            'nombre': self.nombre,
            'telefono': self.telefono,
            'provincia': self.provincia,
            'canton': self.canton,
            'referencia': self.referencia,
            'mapa': self.mapa,
            'comentario': self.comentario,
            'direccion':self.direccion

        }