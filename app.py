from flask import flash, Flask, session,render_template, request,Response ,jsonify, redirect, url_for
from controllers.database import dbConnection as dbase
from modules.client import Client
from modules.registro import Registro
from modules.product import Product
from modules.cobranza import Cobranza
from modules.stadist import Estadistica


db = dbase()

app = Flask(__name__)
app.secret_key = 'daniel123' # Es necesario tener una clave secreta para esto y el manejo de errores



# ---- Rutas ----- 
@app.route('/',methods=['GET','POST'])
def index():
    
    return render_template('index.html')


@app.route('/logout')
def logout():
    # Elimina el usuario de la sesión si está presente
    session.pop('username', None)
    return redirect(url_for('index'))

#--------Login ---------
@app.route('/index', methods=['GET','POST'])
def login():
  # Verifica si el usuario está en la sesión
  # Redirige al usuario al inicio si no está en la sesión
  if request.method== 'POST' :

    user = request.form['user']
    password = request.form['password']
    

    user_found = db.registros.find_one({'user': user, 'password': password})
    usuario_found = db.admin.find_one({'user': user, 'password': password})
    if usuario_found:
        session["username"]= user
        return redirect(url_for('client'))
    elif user_found:
        session["username"]= user
        return redirect(url_for('user_client'))
    else:
        # Credenciales no válidas, puedes mostrar un mensaje de error
        flash('Usuario o contraseña incorrectos')
        return redirect(url_for('index'))
    

# * ---- Registros envio de datos----

@app.route('/admin/registro')
def regi():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    registros = db['registros']# Esta es la collection name de mi base de datos 
    registrosReceived = registros.find()
    return render_template('admin/registro.html', registros=registrosReceived)


# * Envio a registro de mi base de datos
@app.route('/admin/registro', methods=['POST'])
def addRegistros():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    
    registros = db['registros']# Esta es la collection name de mi base de datos 
    cedula = request.form["cedula"]
    rol = request.form['rol']
    correo = request.form['correo']
    user = request.form['user']
    password = request.form['password']

    existing_cedula = registros.find_one({'cedula': cedula})
    existing_user = registros.find_one({'user': user})

    if existing_cedula:
        flash("Ya existe un usuario con esa cedula")
        return render_template('admin/registro.html')
    elif existing_user:
        flash("Ya existe un usuario con ese nombre de usuario")
        return render_template('admin/registro.html')
    else:
        registro = Registro(cedula, rol, correo, user, password)
        registros.insert_one(registro.toDBCollection())
        flash("Guardado en la base de datos")
        return redirect(url_for('regi'))
    

#* Muestra de los usuarios registrados
@app.route('/admin/v_user')
def v_user():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    usuarios =db['registros'].find()
    return render_template('admin/v_user.html', registros=usuarios)

#* Eliminar usuarios
@app.route('/delete_user/<string:client_user>')
def del_user(client_user):#Pasa la funcion al form osea al boton
    user = db['registros']
    user.delete_one({'cedula' : client_user})
    return redirect(url_for('v_user'))

# * Editar usuarios
@app.route('/edit_us/<string:client_user>', methods=['GET', 'POST'])#
def edit_user(client_user):
    userer = db['registros']
    cedula = request.form['cedula']
    rol = request.form['rol']
    correo = request.form['correo']
    user = request.form['user']
    password = request.form['password']
    
    if cedula and rol and correo and user and password:
        userer.update_one({'cedula' : client_user}, {'$set' : {'cedula' : cedula, 'rol' : rol, 'correo' : correo, 'user' : user, 'password' :password}})
        return redirect(url_for('v_user'))
    else:
        return notFound()




#Ruta de cliente e ingresado de los mismo
@app.route('/admin/client', methods=['GET','POST'])
def client():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    if request.method == 'POST':
        # Aquí va tu código para manejar el POST
        clientes = db['clientes']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        provincia = request.form['provincia']
        canton = request.form['canton']
        direccion = request.form['direccion']
        mapa=request.form['mapa']
        referencia = request.form['referencia']
        comentario = request.form['comentario']
        
        existing_nombre = clientes.find_one({'nombre':nombre})
        existing_telefono = clientes.find_one({'telefono':telefono})
        
        if existing_nombre:
            flash("Ya existe ese nombre")
            return render_template('admin/client.html')
            
        elif existing_telefono:
            flash("Ya existe ese telefono")
            return render_template('admin/client.html')

        else :
            client = Client(nombre, telefono, provincia,canton,direccion,referencia,mapa,comentario)
            clientes.insert_one(client.cliDBCollection())
            flash("Se envio a la base de datos")
            return redirect(url_for('client'))#Este es para que se quede en la misma pagina
        
    else:
        # Aquí va tu código para manejar el GET
        return render_template('admin/client.html')
    

# Este es para Editar a todos los clientes de mi base de datos    
@app.route('/admin/v_client')
def editarclient():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    cliente = db['clientes'].find()
    return render_template('admin/v_client.html', clientes=cliente)
    

# Metodo Eliminar CLientes
@app.route('/delete_cl/<string:client_name>')
def delete_client(client_name):#Pasa la funcion al form osea al boton
    cliente = db['clientes']
    cliente.delete_one({'nombre' : client_name})
    return redirect(url_for('editarclient'))

# Metodo Para editar el cliente
# Method Put
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
# Agregar un select para el html 
@app.route('/admin/products')
def products():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    select = db['clientes']
    nombres = select.find({}, {'nombre': 1})
    return render_template('admin/products.html', nombres=nombres)


# Modificación en addProduct
@app.route('/admin/products', methods=['POST', 'GET'])
def addProduct():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    
    products = db['products']
    nombre_cliente = request.form.get('nombre')
    codigos = request.form.getlist('codigo[]')
    nombre_p = request.form.getlist('nombre_p[]')
    cantidades = request.form.getlist('cantidad[]')
    precios = request.form.getlist('precio[]')
    resultados = request.form.getlist('resultado[]')
    total = request.form.get('total')
    fecha_p = request.form.get('fecha_p')
    fecha_co =request.form.get('fecha_co')

    
    # Validar que se proporcionen datos
    if nombre_cliente and codigos and nombre_p and cantidades and precios and resultados and total and fecha_p and fecha_co:
        # Crear una lista de productos para el cliente
        productos_cliente = []

        for codigo, nombre_p,cantidad, precio, resultado in zip(codigos, nombre_p, cantidades, precios, resultados):
            if codigo and nombre_p and cantidad and precio and resultado:
                producto = Product(nombre_cliente, codigo, nombre_p,precio, cantidad, resultado, total,fecha_p,fecha_co)
                productos_cliente.append(producto.proDBCollection())

        # Insertar todos los productos del cliente en la base de datos
        products.insert_many(productos_cliente)

        return redirect(url_for('products'))

    return notFound()

# Ruta de Pay

@app.route('/admin/pay')
def pago():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    products = db['products'].find()
    return render_template('admin/pay.html', products=products)

# * Vista de las deudas -----------------------

#* Metodo Eliminar Pay
#@app.route('/delete/<string:product_nombre>')
#def delete(product_nombre):
#    products = db['products']
#    products.delete_one({'nombre': product_nombre})
#    return redirect(url_for('pago'))
#
# Metodo Editar Pay

@app.route('/edit/<string:product_nombre>', methods=['GET','POST'])
def edit(product_nombre):
    products = db['products']
    nombre_cliente = request.form.get('nombre')
    codigos = request.form.get('codigo')
    cantidades = request.form.get('cantidad')
    precios = request.form.get('precio')
    resultados = request.form.get('resultado')
    total = request.form.get('total')
    fecha_p = request.form.get('fecha_p')
    fecha_co = request.form.get('fecha_co')
    print("hola amigo")

    if nombre_cliente and codigos and cantidades and resultados and precios and total and fecha_p and fecha_co:
        products.update_one({'nombre': product_nombre}, {'$set': {'nombre': nombre_cliente, 'codigo': codigos, 'cantidad': cantidades ,'precio':precios,'resultado':resultados, 'total':total ,'fecha_p':fecha_p, 'fecha_co':fecha_co  }})
        return redirect(url_for('pago'))
    else:
        return 'No se muestra nada'

# * Modulo de cobranza y muestra del form 
@app.route('/admin/cobranza')
def cobranza():
    # * Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # *Redirige al usuario al inicio si no está en la sesión
    products =db.products.find() 
    return render_template('admin/cobranza.html', products=products)


# * Ingresado Para el modulo Cobranza

@app.route('/admin/cobranza', methods=['GET','POST'])
def r_reporte():
    # * Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # * Redirige al usuario al inicio si no está en la sesión

    if request.method =='POST':
        report=db['cobranza']
        nombre=request.form['nombre']
        total=request.form['total']
        fecha_p=request.form['fecha_p']
        fecha_co=request.form['fecha_co']
        abono=request.form['abono']
        fecha_ab=request.form['fecha_ab']
        resultado=request.form['resultado']
        pagado=request.form['pagado']
        
        if nombre and total and fecha_p and fecha_co and abono and fecha_ab and resultado and pagado:
            r_reporte = Cobranza(nombre,total,fecha_p,fecha_co,abono,fecha_ab,resultado,pagado)
            report.insert_one(r_reporte.cobDBCollection())
            return redirect(url_for('reporte'))
        else:
            return notFound()
    else:
        return render_template('admin/reporte.html') 


#* Eliminado de Cobranza

@app.route('/delete/<string:product_nombre>')
def delete(product_nombre):
    products = db['products']
    products.delete_many({'nombre': product_nombre})
    return redirect(url_for('cobranza'))    


# *Modulo de reporte

@app.route('/admin/reporte')
def reporte():
    #* Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  #* Redirige al usuario al inicio si no está en la sesión
    report=db.cobranza.find()
    return render_template('admin/reporte.html',cobranza=report)
    

#* Enviar modulo reporte a estadistica

@app.route('/admin/reporte', methods=['GET','POST'])
def env_esta():
    #* Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  #* Redirige al usuario al inicio si no está en la sesión
    if request.method =='POST':
        enviar_est =db['estadistica']
        nombre = request.form ['nombre']
        fecha_co = request.form['fecha_co']
        fecha_ab = request.form['fecha_ab']
        
        if nombre and fecha_co and fecha_ab:
            env_esta = Estadistica (nombre,fecha_co,fecha_ab)
            enviar_est.insert_one(env_esta.estadBCollection())
            return redirect(url_for('estadistica'))
        else:
            return notFound()
    else:
        return render_template('admin/reporte.html')
    
# *Modulo de Estadistica
@app.route('/admin/stadist')
def estadistica():
    #* Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  #* Redirige al usuario al inicio si no está en la sesión
    report=db.estadistica.find()
    return render_template('admin/stadist.html',estadistica=report)


#*Modulo eliminacion de Estadistica

@app.route('/delest/<string:esta_nombre>')
def delest(esta_nombre):
    estadistica = db['estadistica']
    estadistica.delete_one({'nombre': esta_nombre})
    return redirect(url_for('estadistica'))



#* ---------------------- Usuarios ----------------------------------------------------------------

@app.route('/user/client' , methods=['GET','POST'])
def user_client():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    
    if request.method == 'POST':
        # * Aquí va tu código para manejar el POST
        clientes = db['clientes']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        provincia = request.form['provincia']
        canton = request.form['canton']
        direccion = request.form['direccion']
        mapa = request.form['mapa']
        referencia = request.form['referencia']
        comentario = request.form['comentario']

        existing_nombre = clientes.find_one({'nombre':nombre})
        existing_telefono = clientes.find_one({'telefono':telefono})
        
        if existing_nombre:
            flash("Ya existe ese nombre")
            return render_template('user/client.html')
            
        elif existing_telefono:
            flash("Ya existe ese telefono")
            return render_template('user/client.html')

        else :
            client = Client(nombre, telefono, provincia,canton,direccion,referencia,mapa,comentario)
            clientes.insert_one(client.cliDBCollection())
            flash("Se envio a la base de datos")
            return redirect(url_for('user_client'))
    else:
        # Aquí va tu código para manejar el GET
        return render_template('user/client.html')

@app.route('/user/pay', methods=['GET','POST'])
def user_pay():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    products = db['products'].find()
    return render_template('user/pay.html', products=products)


@app.route('/user/product' , methods=['GET','POST'])
def user_product():
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    products = db['products']
    select = db['clientes']
    nombres = select.find({}, {'nombre': 1})
    nombre_cliente = request.form.get('nombre')
    codigos = request.form.getlist('codigo[]')
    nombre_p = request.form.getlist('nombre_p[]')
    cantidades = request.form.getlist('cantidad[]')
    precios = request.form.getlist('precio[]')
    resultados = request.form.getlist('resultado[]')
    total = request.form.get('total')
    fecha_p = request.form.get('fecha_p')
    fecha_co =request.form.get('fecha_co')
    # Validar que se proporcionen datos
    if nombre_cliente and codigos and nombre_p and cantidades and precios and resultados and total and fecha_p and fecha_co:
        # Crear una lista de productos para el cliente
        productos_cliente = []

        for codigo, nombre_p,cantidad, precio, resultado in zip(codigos, nombre_p, cantidades, precios, resultados):
            if codigo and nombre_p and cantidad and precio and resultado:
                producto = Product(nombre_cliente, codigo, nombre_p,precio, cantidad, resultado, total,fecha_p,fecha_co)
                productos_cliente.append(producto.proDBCollection())

        # Insertar todos los productos del cliente en la base de datos
        products.insert_many(productos_cliente)
        return redirect(url_for('user_product'))

    return  render_template('user/product.html', nombres=nombres)



# *  Este es para manejo de errores
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    return render_template('404.html', message=message), 404


if __name__ == '__main__':
    app.run(debug=True, port=3000)
