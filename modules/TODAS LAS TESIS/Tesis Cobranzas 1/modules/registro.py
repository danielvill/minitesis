class Registro:
    def __init__(self, correo, user,password):
        self.correo = correo
        self.user = user
        self.password = password

    def toDBCollection(self):
        return{
            'correo': self.correo,
            'user': self.user,
            'password':self.password,
            
        }