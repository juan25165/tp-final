from flask import Flask, render_template, request, redirect, url_for, session
from dataUser import *
from controller_db import conexionMySQL, obtener_items_carrito, agregar_item_carrito, actualizar_cantidad_item, eliminar_item_carrito

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Home route
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

# Shopping cart routes
@app.route('/cart')
def view_cart():
    user_id = session.get('user_id', 1)  # Default to user 1 for this example
    items = obtener_items_carrito(user_id)
    return render_template("cart.html", items=items)

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    user_id = session.get('user_id', 1)
    product_id = request.form['product_id']
    quantity = int(request.form['quantity'])
    agregar_item_carrito(product_id, quantity, user_id)
    return redirect(url_for('view_cart'))

@app.route('/cart/update', methods=['POST'])
def update_cart():
    user_id = session.get('user_id', 1)
    product_id = request.form['product_id']
    quantity = int(request.form['quantity'])
    actualizar_cantidad_item(product_id, quantity, user_id)
    return redirect(url_for('view_cart'))

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    user_id = session.get('user_id', 1)
    product_id = request.form['product_id']
    eliminar_item_carrito(product_id, user_id)
    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug=True)
