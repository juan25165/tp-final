from flask import Flask,render_template
from dataUser import *
from controller_db import conexionMySQL


app = Flask(__name__)

# home
@app.route("/")
def dataHome():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template("nosotros.html")

@app.route('/productos')
def productos():
    return render_template("productos.html")


@app.route('/servicios')
def servicios():
    return render_template("servicios.html")

@app.route('/contacto')
def contacto():
    conexion = conexionMySQL()
    return render_template("contacto.html", conexion=conexion)

@app.route('/registroexitoso')
def registro():
    return render_template("registroexitoso.html")

