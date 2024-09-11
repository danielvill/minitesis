from flask import Blueprint, render_template, request, flash, session, jsonify, redirect, url_for 
from controllers.database import Conexion as dbase
from modules.productos import Productos
from pymongo import MongoClient
db = dbase()
producto = Blueprint("producto",__name__)

# En este apartado tendre que agregar todo lo relacionado a Productos y si es posible que pueda convertir contraer 
# Un archivo de lo que es csv para que pueda llenar mi base de datos eso seria 

