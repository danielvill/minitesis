from flask import Blueprint, render_template, request, flash, session, jsonify, redirect, url_for 
from controllers.database import Conexion as dbase
from modules.comprobantes import Comprobantes
from pymongo import MongoClient
db = dbase()
comprobante = Blueprint("comprobante",__name__)


