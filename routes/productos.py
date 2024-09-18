from flask import Blueprint, render_template, request, flash, session, jsonify, redirect, url_for 
from controllers.database import Conexion as dbase
from modules.productos import Productos
from pymongo import MongoClient
import pandas as pd
db = dbase()
producto = Blueprint("producto",__name__)

# En este apartado tendre que agregar todo lo relacionado a Productos y si es posible que pueda convertir contraer 
# Un archivo de lo que es csv para que pueda llenar mi base de datos eso seria 

@producto.route("/admin/productos.html",methods=['GET', 'POST'])
def get_products():
    file = request.files['file']
    if not file:
        return "No file"

    # Leer el archivo CSV
    data = pd.read_csv(file)

    # Convertir el DataFrame a un diccionario
    data_dict = data.to_dict("records")

    # Insertar los datos en MongoDB
    db.insert_many(data_dict)

    return "Enviado a la base de datos "




@producto.route('/edit_pr/<string:prodcod>', methods=['GET', 'POST'])#Para editar debes colocar edit_cl en la misma ruta
def edit_pr(prodcod):
    producto = db['producto']
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    veinticinco = request.form['venticinco']
    treinta = request.form['treinta']
    treintaicinco = request.form['treintaicinco']
    

    if codigo and nombre and veinticinco and treinta and treintaicinco: 
        producto.update_one({'nombre' : prodcod}, {'$set' : {"codigo": codigo,"nombre":nombre, "veinticinco":veinticinco, "treinta":treinta, "treinticinco":treintaicinco}})
        response = jsonify({'message' : 'Productos ' + prodcod + ' actualizado correctamente'})
        return redirect(url_for('editarclient'))
    else:
        return render_template('admin/productos.pug', prodcod=prodcod)



# Metodo Eliminar CLientes
@producto.route('/delete_pr/<int:prodco>')
def delete_pr(prodco):#Pasa la funcion al form osea al boton
    producto = db['producto']
    producto.delete_one({'codigo' : prodco})
    return redirect(url_for('editpro'))

# Este es para visualizar a todos los productos de mi base de datos 
@producto.route('/admin/producto')
def editpro():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    producto = db['producto'].find()
    return render_template('admin/producto.pug', clientes=cliente)


