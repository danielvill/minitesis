from flask import Blueprint, render_template, request, flash, session, jsonify, redirect, url_for 
from controllers.database import Conexion as dbase
from modules.deudas import Deudas
from pymongo import MongoClient
db = dbase()
deuda = Blueprint("deuda",__name__)


