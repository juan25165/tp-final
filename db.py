import pymysql

host = "localhost"
user = "root"
clave= ""
db="tiendaanimales"

def conexionMySQL():
    return pymysql.connect(host=host,user=user,password=clave,database=db)

# host = "unicornio82.mysql.pythonanywhere-services.com"
# user = "unicornio82"
# clave= "Lobito460912"
# db="unicornio82$Tienda-de-Mascotas"