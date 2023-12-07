from flask import flash, Flask, render_template, request,jsonify, redirect, url_for
from controllers.database import dbConnection as dbase
from modules.client import Client
from modules.registro import Registro


db = dbase()

app = Flask(__name__)
app.secret_key = 'daniel123' # Es necesario tener una clave secreta para esto y el manejo de errores

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
        #return redirect('/client')
        return redirect(url_for('client'))#Nombre de la funcion @app.route('/client')
    else:
        # Credenciales no válidas, puedes mostrar un mensaje de error
        flash('Usuario o contraseña incorrectos')
        return redirect(url_for('index'))
  # return render_template('client.html')
    

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

#Ruta de cliente e ingresado de los mismo



@app.route('/client', methods=['GET','POST'])
def client():
    if request.method == 'POST':
        # Aquí va tu código para manejar el POST
        clientes = db['clientes']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        provincia = request.form['provincia']
        canton = request.form['canton']
        mapa=request.form['mapa']
        referencia = request.form['referencia']
        comentario = request.form['comentario']
        direccion = request.form['direccion']

        # Imprime los valores en la consola esto es para comprobar los errores
        print('Nombre:', nombre)
        print('Teléfono:', telefono)
        print('Provincia:', provincia)
        print('Cantón:', canton)
        print('Mapa:', mapa)
        print('Referencia:', referencia)
        print('Comentario:', comentario)
        print('Dirección:', direccion)

        if nombre and telefono and provincia and canton and referencia and mapa and comentario and direccion:
            client = Client(nombre, telefono, provincia,canton,referencia,mapa,comentario,direccion)
            clientes.insert_one(client.cliDBCollection())
            return redirect(url_for('client'))#Este es para que se quede en la misma pagina
        else:
            return notFound()
    else:
        # Aquí va tu código para manejar el GET
        return render_template('client.html')
    

#Ruta de Products
@app.route('/products')
def prod():
    return render_template('products.html')


#Ruta de Pay

@app.route('/pay')
def pago():
    return render_template('pay.html')

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
