from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
mongo_uri=os.getenv('MONGO_URI')
client=MongoClient(mongo_uri)
db=client.get_default_database()
usuarios = db['usuarios']
recetas = db['recetas']

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

if __name__ == '__main__':
    app.run(debug=True)