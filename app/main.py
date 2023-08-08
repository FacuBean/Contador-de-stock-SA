from conexion import connect

from product_class import *

Product = NewProductPaint()

menu_terminal_option=0
menu_terminal_option= 1 #int(input("Elija la opcion '1' para comenzar:  "))

connection = connect()

print("+-----------Conectando-----------------+")
if connection.status == psycopg2.extensions.STATUS_READY:
    print ("+--------------------------------------+")
    print ("+-----------Conexion exitosa-----------+")
    print ("+--------------------------------------+")

cursor = connection.cursor()

show_product_table_sql = "select * from products"



if menu_terminal_option == 1:

     #creo producto con la funcion 'NewProductPaint' 
     Product1 = NewProductPaint()

     # IMPRESION DEL OBJETO PRODUCT1

     print(f"+Producto 1: - - - - - - - - - - - - - + \n{Product1}")

     # = 
     #cursor.execute(sql_Insert_Paint)
     cursor.execute(show_product_table_sql)
     print (cursor.fetchall())
     

else:
     print("No se ejecuto ninguna opcion")
     option_request = False


cursor.close()
connection.close()
print ("+--------------------------------------+")
print ("+-----------Se a cerrado la conexion---+")
print ("+--------------------------------------+")

#print("ERROR AL CERRAR CONEXION CON LA BASE DE DATOS: ")