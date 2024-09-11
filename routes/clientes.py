from flask import Blueprint, render_template, request, flash, session, jsonify, redirect, url_for 
from controllers.database import Conexion as dbase
from modules.clientes import Clientes
from pymongo import MongoClient
db = dbase()
clientes = Blueprint("clietes",__name__)

# Este apartado es para agregar lo que es a los clientes 
# No te olvides que es necesario que las validaciones para clientes algunos no son importantes
# Como lo son provincia, canton, mapa ,comentaio
# Esos puntos no son necesarios 

@clientes.route('/admin/clientes', methods=['GET','POST'])
def cliente():
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
        referencia = request.form['referencia']
        mapa=request.form['mapa']
        comentario = request.form['comentario']
        
        existing_nombre = clientes.find_one({'nombre':nombre})
        existing_telefono = clientes.find_one({'telefono':telefono})
        
        if existing_nombre:
            flash("Ya existe ese nombre")
            return render_template('admin/clientes.pug')
            
        elif existing_telefono:
            flash("Ya existe ese telefono")
            return render_template('admin/clientes.pug')

        else :
            client = Clientes(nombre, telefono, provincia,canton,direccion,referencia,mapa,comentario)
            clientes.insert_one(client.clientesDBCollection())
            flash("Se envio a la base de datos")
            return redirect(url_for('cliente'))#Este es para que se quede en la misma pagina
        
    else:
        # Aquí va tu código para manejar el GET
        return render_template('admin/clientes.pug')



# Este es para editar los clientes

@cliente.route('/edit_cl/<string:client_name>', methods=['GET', 'POST'])#Para editar debes colocar edit_cl en la misma ruta
def edit_c(client_name):
    cliente = db['clientes']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    provincia = request.form['provincia']
    canton = request.form['canton']
    direccion = request.form['direccion']
    referencia = request.form['referencia']
    mapa = request.form['mapa']
    comentario = request.form['comentario']
    

    if nombre and telefono and provincia and canton and referencia and mapa and comentario and direccion: 
        cliente.update_one({'nombre' : client_name}, {'$set' : {'nombre' : nombre, 'telefono' : telefono, 'provincia' : provincia ,'canton':canton,'referencia':referencia,'mapa':mapa,'comentario':comentario,'direccion':direccion}})
        response = jsonify({'message' : 'Clientes ' + client_name + ' actualizado correctamente'})
        return redirect(url_for('editarclient'))
    else:
        return render_template('admin/editarclientes.pug', client_name=client_name)



# Metodo Eliminar CLientes
@cliente.route('/delete_cl/<string:client_name>')
def delete_client(client_name):#Pasa la funcion al form osea al boton
    cliente = db['clientes']
    cliente.delete_one({'nombre' : client_name})
    return redirect(url_for('editarclient'))

# Este es para visualizar a todos los clientes de mi base de datos 
@cliente.route('/admin/v_client')
def editarclient():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    cliente = db['clientes'].find()
    return render_template('admin/v_client.html', clientes=cliente)


