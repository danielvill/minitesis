from flask import Blueprint, render_template, request, flash, session, jsonify, redirect, url_for 
from controllers.database import Conexion as dbase
from modules.comprobantes import Comprobantes
from pymongo import MongoClient
db = dbase()
comprobante = Blueprint("comprobante",__name__)


@comprobante.route('/admin/in_comprobante', methods=['GET','POST'])
def comprobante():
    # Verifica si el usuario está en la sesión
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    
    if request.method == 'POST':
        comprobante = db["comprobante"]
        codigo_deposito = request.form["codigo_deposito"]
        valor = request.form["valor"]
        fecha = request.form["fecha"]
        descripciones = request.form["descripciones"]

        compro = Comprobantes(codigo_deposito, valor, fecha,descripciones)
        comprobante.insert_one(compro.comprobanteDBCollection())
        flash("Comprobante agregado correctamente")
        return redirect(url_for('comprobante.comprobante'))
    
    else:
        return render_template('admin/in_comprobante.pug')




