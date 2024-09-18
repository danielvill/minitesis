from flask import Blueprint, render_template, request, flash, session, jsonify, redirect, url_for 
from controllers.database import Conexion as dbase
from modules.deudas import Deudas
from pymongo import MongoClient
db = dbase()
deuda = Blueprint("deuda",__name__)

@deuda.route("/admin/deudas", methods=["GET"])
def deudas():
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('index'))  # Redirige al usuario al inicio si no está en la sesión
    
    if request.method == 'POST':
        deuda = db["deudas"]
        codigo = request.form["codigo"]
        valor_deuda = request.form["valor_deuda"]
        deuda = request.form["deuda"]
        fecha_limite = request.form["fecha_limite"]

        deud = Deudas(codigo, valor_deuda, deuda, fecha_limite)
        deuda.insert_one(deud.deudaDBCollection())
        flash("Se envio a la base de datos")
        return redirect(url_for('deudas'))#Este es para que se quede en la misma pagina
    
    else:
        # Aquí va tu código para manejar el GET
        return render_template('admin/deudas.pug')






