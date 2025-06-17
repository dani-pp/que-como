from flask import Flask, render_template, request, Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

iniciarSesion_route = Blueprint('iniciarSesion_route', __name__)
mongo_uri=os.getenv('MONGO_URI')
client=MongoClient(mongo_uri)
db=client.get_default_database()
usuario = db['usuarios']



@iniciarSesion_route.route('/validar-usuario', methods=['POST'])
def validarUsuario():
    correo = request.form.get('inputEmail')
    contrasena = request.form.get('inputPass')

    usuario_encontrado = usuario.find_one({
        "correo": correo,
        "contrasena": contrasena
    })

    if usuario_encontrado:
        nombre = nombre.usuario(usuario_encontrado)
        return render_template('prueba1.html')
    else:
        return render_template('prueba2.html')