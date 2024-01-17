class Registro:
    def __init__(self, cedula , rol,correo, user,password):
        self.cedula = cedula
        self.rol = rol
        self.correo = correo
        self.user = user
        self.password = password

    def toDBCollection(self):
        return{
            'cedula': self.cedula,
            'rol': self.rol,
            'correo': self.correo,
            'user': self.user,
            'password':self.password,
            
        }
    