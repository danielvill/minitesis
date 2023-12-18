from flask import flash, Flask, render_template, request,Response ,jsonify, redirect, url_for
from controllers.database import dbConnection as dbase
from modules.client import Client
from modules.registro import Registro
from modules.product import Product

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

        if nombre and telefono and provincia and canton and referencia and mapa and comentario and direccion:
            client = Client(nombre, telefono, provincia,canton,referencia,mapa,comentario,direccion)
            clientes.insert_one(client.cliDBCollection())
            return redirect(url_for('client'))#Este es para que se quede en la misma pagina
        else:
            return notFound()
    else:
        # Aquí va tu código para manejar el GET
        return render_template('client.html')
    

#Este es para Editar a todos los clientes de mi base de datos    
@app.route('/v_client')
def editarclient():
    cliente = db['clientes'].find()
    return render_template('v_client.html', clientes=cliente)
    

#Metodo Eliminar CLientes
@app.route('/delete_cl/<string:client_name>')
def delete_client(client_name):#Pasa la funcion al form osea al boton
    cliente = db['clientes']
    cliente.delete_one({'nombre' : client_name})
    print("No se muestrra los resultrados")
    return redirect(url_for('editarclient'))

# Metodo Para editar el cliente
#Method Put
@app.route('/edit_cl/<string:client_name>', methods=['GET', 'POST'])#Para editar debes colocar edit_cl en la misma ruta
def edit_c(client_name):
    cliente = db['clientes']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    provincia = request.form['provincia']
    canton = request.form['canton']
    referencia = request.form['referencia']
    mapa = request.form['mapa']
    comentario = request.form['comentario']
    direccion = request.form['direccion']

    if nombre and telefono and provincia and canton and referencia and mapa and comentario and direccion: 
        cliente.update_one({'nombre' : client_name}, {'$set' : {'nombre' : nombre, 'telefono' : telefono, 'provincia' : provincia ,'canton':canton,'referencia':referencia,'mapa':mapa,'comentario':comentario,'direccion':direccion}})
        response = jsonify({'message' : 'Clientes ' + client_name + ' actualizado correctamente'})
        return redirect(url_for('editarclient'))
    else:
        return notFound()
    



# Ruta Productos
#Agregar un select para el html 
@app.route('/products')
def products():
    select = db['clientes']
    nombres = select.find({}, {'nombre': 1})
    return render_template('products.html', nombres=nombres)


# Modificación en addProduct
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    nombre_cliente = request.form.get('nombre')
    codigos = request.form.getlist('codigo[]')
    cantidades = request.form.getlist('cantidad[]')
    precios = request.form.getlist('precio[]')
    resultados = request.form.getlist('resultado[]')
    total = request.form.get('total')
    fecha_p = request.form.get('fecha_p')
    fecha_co =request.form.get('fecha_co')

    
    # Validar que se proporcionen datos
    if nombre_cliente and codigos and cantidades and precios and resultados and total and fecha_p and fecha_co:
        # Crear una lista de productos para el cliente
        productos_cliente = []

        for codigo, cantidad, precio, resultado in zip(codigos, cantidades, precios, resultados):
            if codigo and cantidad and precio and resultado:
                producto = Product(nombre_cliente, codigo, precio, cantidad, resultado, total,fecha_p,fecha_co)
                productos_cliente.append(producto.proDBCollection())

        # Insertar todos los productos del cliente en la base de datos
        products.insert_many(productos_cliente)

        return redirect(url_for('products'))

    return notFound()




#Ruta de Pay

@app.route('/pay')
def pago():
    products = db['products'].find()
    return render_template('pay.html', products=products)

#Vista de las deudas -----------------------

#Metodo Eliminar Pay
@app.route('/delete/<string:product_nombre>')
def delete(product_nombre):
    products = db['products']
    products.delete_one({'nombre': product_nombre})
    return redirect(url_for('pago'))

#Metodo Editar Pay

@app.route('/edit/<string:product_nombre>', methods=['GET','POST'])
def edit(product_nombre):
    products = db['products']
    nombre_cliente = request.form['nombre']
    codigos = request.form['codigo']
    cantidades = request.form['cantidad']
    precios = request.form['precio']
    resultados = request.form['resultado']
    total = request.form['total']
    fecha_p = request.form['fecha_p']
    fecha_co =request.form['fecha_co']

    if nombre_cliente and codigos and cantidades and resultados and precios and total and fecha_p and fecha_co:
        products.update_one({'nombre': product_nombre}, {'$set': {'nombre': nombre_cliente, 'codigo': codigos, 'cantidad': cantidades ,'precio':precios,'resultado':resultados, 'total':total ,'fecha_p':fecha_p, 'fecha_co':fecha_co  }})
        return redirect(url_for('pago'))
    else:
        return print('No se muestra nada')





# Este es para manejo de errores
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    return render_template('404.html', message=message), 404


if __name__ == '__main__':
    app.run(debug=True, port=3000)
