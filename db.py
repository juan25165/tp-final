import pymysql

host = "localhost"
user = "root"
clave= ""
db="tiendaanimales"

def conexionMySQL():
    return pymysql.connect(host=host,user=user,password=clave,database=db)
