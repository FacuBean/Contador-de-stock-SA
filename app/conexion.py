import psycopg2
import datetime
host = "localhost"
db_name = "pintureria_sa-db"
user = "FacuB"
password = "Cadaques0"

dicc_paint_table = {
    "id" : int,
    "name": str,
    "color": str,
    "category": str,
    "category_color": str,
    "color_code": str,
    "description": str,
    "price": float,
    "stock": int,
    "upload_date": datetime,
    "update_item_date": datetime,
    "date_restock": datetime,
    "items_sold": int,
}

dicc_tables = {
    "product_paint_table" : dicc_paint_table
}





def connect():
    try:
        connection = psycopg2.connect(f"host={host} dbname={db_name} user={user} password={password} port = 5432")
        # print("+-----------Conectando-----------------+")
        # if connection.status == psycopg2.extensions.STATUS_READY:
        #     print ("+--------------------------------------+")
        #     print ("+-----------Conexion exitosa-----------+")
        #     print ("+--------------------------------------+")

    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: '{e}'")
        return None

    return connection
    
connect()
connect().close

''' 
FUNCION QUE ABRE CONEXION CON LA BASE DE DATOS Y LA DESCONECTA


# def connect():
#     try:
#         conexion = psycopg2.connect(f"host={host} dbname={db_name} user={user} password={password} port = 5432")

#         print ("┌--- Conexion exitosa            ---┐")

#         conexion.close()

#         print ("└--- Se a cerrado la conexion ---┘")


#     except psycopg2.Error as e:
#         print(f"Error al conectar a la base de datos: '{e}'")


'''

