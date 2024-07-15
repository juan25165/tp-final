import pymysql

host = "unicornio82.mysql.pythonanywhere-services.com"
user = "unicornio82"
clave= "Lobito460912"
db="unicornio82$Tienda-de-Mascotas"

def conexionMySQL():
    return pymysql.connect(host=host,user=user,password=clave,database=db)
