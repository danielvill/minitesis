from flask import flash, Flask, json, send_file,session, render_template, request,Response ,jsonify, redirect, url_for
from bson import json_util
from controllers.database import Conexion as dbase
from datetime import datetime,timedelta #* Importacion de manejo de tiempo
from flask import jsonify
from reportlab.pdfgen import canvas # *pip install reportlab este es para imprimir reportes
from reportlab.lib.pagesizes import letter #* pip install reportlab 
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer ,Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet ,ParagraphStyle
# todo: pip install pypugjs   instala este paquete
 


db = dbase()

app = Flask(__name__)
app.secret_key = 'daniel123' # Es necesario tener una clave secreta para esto y el manejo de errores


# ---- Rutas ----- 
@app.route('/',methods=['GET','POST'])
def index():
    pagetitle = "Login" 
    youAreUsingPugJs = True
    return render_template('index.pug',pagetitle=pagetitle,youAreUsingPugJs=youAreUsingPugJs)


@app.route('/logout')
def logout():
    # Elimina el usuario de la sesión si está presente
    session.pop('username', None)
    return redirect(url_for('index'))





# *  Este es para manejo de errores
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    return render_template('404.pug', message=message), 404


if __name__ == '__main__':
    app.run(debug=True, port=3000)
