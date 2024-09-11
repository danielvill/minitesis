from flask import Blueprint, render_template, request, flash, session, jsonify, redirect, url_for 
from controllers.database import Conexion as dbase
from modules.admin import Admin
from pymongo import MongoClient
db = dbase()
admin = Blueprint("admin",__name__)


