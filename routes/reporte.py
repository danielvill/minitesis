from flask import Blueprint, render_template, request, flash, session, jsonify, redirect, url_for 
from controllers.database import Conexion as dbase
from modules.reporte import Reporte
from pymongo import MongoClient
db = dbase()
reporte = Blueprint("reporte",__name__)



