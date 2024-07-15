from flask import Flask,render_template
from dataUser import *


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
    return render_template("contacto.html")

@app.route('/registro-exitoso')
def registro():
    return render_template("registro-exitoso.html")

