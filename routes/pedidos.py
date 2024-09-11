from flask import Blueprint, render_template, request, flash, session, jsonify, redirect, url_for 
from controllers.database import Conexion as dbase
from modules.pedidos import Pedidos
from pymongo import MongoClient
db = dbase()
pedido = Blueprint("pedido",__name__)


