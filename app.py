from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
from routes.iniciarSesion import iniciarSesion_route
import os
load_dotenv()

app = Flask(__name__)
app.register_blueprint(iniciarSesion_route)


#@app.route('/')
#def inicio():
#   todas_las_recetas = list(recetas.find())
#    print("Recetas encontradas:", todas_las_recetas)  # 👈 agrega esto
#    return render_template("index.html", recetas=todas_las_recetas)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iniciar-sesion')
def iniciarSesion():
    return render_template('iniciarSesion.html')

@app.route('/recetas')
def verRecetas():
    return render_template('recetas.html')

@app.route('/FAQ')
def faq():
    return render_template('faq.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)