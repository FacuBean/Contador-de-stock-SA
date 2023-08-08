from conexion import connect

from product_class import *

Product = NewProductPaint()

menu_terminal_option=0
menu_terminal_option= 1 #int(input("Elija la opcion '1' para comenzar:  "))

connection = connect()
cursor = connection.cursor()

sql_Insert_Paint = "INSERT INTO product (nombre, legajo, materias_aprobadas) VALUES (?, ?, ?)"

show_product_table_sql = "select * from products p "



if menu_terminal_option == 1:

     #creo producto con la funcion 'NewProductPaint' 
     Product1 = NewProductPaint()

     # IMPRESION DEL OBJETO PRODUCT1

     print(f"Product1")

     #
     upload_paint_sql = ""
     cursor.execute(show_product_table_sql)
     results = cursor.fetchall()
     for i in results:
          print(i)


else:
     print("No se ejecuto ninguna opcion")
     option_request = False


cursor.close()
connection.close()
print ("+--------------------------------------+")
print ("+-----------Se a cerrado la conexion---+")
print ("+--------------------------------------+")

#print("ERROR AL CERRAR CONEXION CON LA BASE DE DATOS: ")