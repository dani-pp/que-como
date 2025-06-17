from flask import Flask, render_template, request, Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

iniciarSesion_route = Blueprint('iniciarSesion_route', __name__)

@iniciarSesion_route.route('/validar-usuario')
def validarUsuario():
  correo = request.form.get('inputEmail')
  password = request.form.get('inputPass')