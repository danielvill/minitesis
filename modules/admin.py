class Admin:
    # Solo va a tener lo que es un solo administrador con ese usuario y contraseña
    def __init__(self, usuario , contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
        
    def adminDBCollection(self):
        return{
            'usuario': self.usuario,
            'contraseña': self.contraseña, 
        }