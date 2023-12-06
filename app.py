from flask import Flask, render_template, request, redirect, url_for
from controllers.database import dbConnection as dbase
#from modules.product import Product
from modules.registro import Registro


db = dbase()

app = Flask(__name__)


# ---- Rutas ----- 
@app.route('/',methods=['GET','POST'])
def index():
    
    return render_template('index.html')



#--------Login ---------
@app.route('/index', methods=['GET','POST'])
def login():

  if request.method== 'POST' :

    user = request.form['user']
    password = request.form['password']
    # Consulta la base de datos para verificar las credenciales
    user_found = db.registros.find_one({'user': user, 'password': password})
    if user_found:
        #  redirigir a una página LLamado client.html
        return redirect(url_for('bienvenido'))#Nombre de la funcion @app.route('/client')
    else:
        # Credenciales no válidas, puedes mostrar un mensaje de error
        return 'Usuario o contraseña incorrectos'
    return render_template('client.html')
    

@app.route('/client')
def bienvenido():
    return render_template('client.html')


# ---- Registros envio de datos----

@app.route('/registros')
def regi():
    registros = db['registros']# Esta es la collection name de mi base de datos 
    registrosReceived = registros.find()
    return render_template('registro.html', registros=registrosReceived)


# Envio a registro de mi base de datos
@app.route('/registros', methods=['POST'])
def addRegistros():
    registros = db['registros']# Esta es la collection name de mi base de datos 
    correo = request.form['correo']
    user = request.form['user']
    password = request.form['password']

    if correo and user and password:
        registro = Registro(correo, user, password)
        registros.insert_one(registro.toDBCollection())
        return redirect(url_for('index'))
    else:
        return notFound()








# Este es para manejo de errores
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    return render_template('404.html', message=message), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
