from db import conexionMySQL

def obtener_items_carrito(user_id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query = "SELECT * FROM cart_items WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return result

def agregar_item_carrito(product_id, quantity, user_id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query = """
            INSERT INTO cart_items (product_id, quantity, user_id)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE quantity = quantity + %s
        """
        cursor.execute(query, (product_id, quantity, user_id, quantity))
        result = cursor
    conexion.commit()
    conexion.close()
    return result

def actualizar_cantidad_item(product_id, quantity, user_id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query = "UPDATE cart_items SET quantity = %s WHERE product_id = %s AND user_id = %s"
        cursor.execute(query, (quantity, product_id, user_id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result

def eliminar_item_carrito(product_id, user_id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query = "DELETE FROM cart_items WHERE product_id = %s AND user_id = %s"
        cursor.execute(query, (product_id, user_id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result
