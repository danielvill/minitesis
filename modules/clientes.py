class Clientes:
    # Estos datos son importantes pero no todos los datos seran necesarios
    def __init__(self,id_cliente, nombre, telefono, provincia,canton,direccion,referencia,mapa,comentario):
        self.id_client = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.provincia = provincia
        self.canton = canton
        self.direccion = direccion
        self.referencia = referencia
        self.mapa = mapa
        self.comentario = comentario

    def clientesDBCollection(self):
        return{
            "id_cliente":self.id_cliente,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'provincia': self.provincia,
            'canton': self.canton,
            'direccion':self.direccion,
            'referencia': self.referencia,
            'mapa': self.mapa,
            'comentario': self.comentario
        }