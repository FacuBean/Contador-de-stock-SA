import psycopg2
from datetime import datetime
from conexion import connect


'''
 Clase de los productos, los atributos son:

    ID: Identificador de la base
    P_Name: Nombre del producto
    P_Color: Color del producto
    P_ColorCode: Codigo Hexadecimal de color de la pintura | Sirve para visualizar el color de la pintura
    CategoryColor: Categoria del color, puede ser "Verde, azul, rojo, etc"
    Date: Fecha en la que se cargo el producto

'''

ProductListOfDict_ForEachID = []

# --- Clases ---

class Product:
    def __init__(self, P_Name ,P_Color, P_Description, P_Date, Price, Stock = 0, DateRestock = None, Selled = 0, Id = "None"):

        self.Id  = Id
        self.P_Name = P_Name
        self.P_Color = P_Color
        self.P_Description = P_Description
        self.Price = Price
        self.Stock = Stock
        self.P_Date = P_Date
        self.DateRestock = DateRestock
        self.Selled = Selled

    def __str__(self):
        return f"Nombre: {self.P_Name} | Color: {self.P_Color} | Descripcion: {self.P_Description} | Fecha: {self.P_Date} | Precio: {self.Price} | Stock: {self.Stock} | Vendidos: {self.Selled} "


# Clase hija "ProductPaint" de padre "Product"

class Product_Paint(Product):
    def __init__(self, P_Name, P_Color, ColorCode, CategoryColor, P_Description, P_Date, P_Time, Price, Stock=0, Selled=0, Id="None"):
        super().__init__(P_Name, P_Description, P_Color, P_Date, P_Time, Price, Stock, Selled, Id)
        self.ColorCode = ColorCode
        self.CategoryColor = CategoryColor

    def __str__(self):
        return f"+{'-'*50}+\n Nombre: {self.P_Name} |\n Color: {self.P_Color} |\n Codigo color Hexadecimal: {self.ColorCode} |\n Categoria de color: {self.CategoryColor}|\n Descripcion: {self.P_Description} |\n Fecha: {self.P_Date} |\n Precio: {self.Price} |\n Stock: {self.Stock} |\n Vendidos: {self.Selled}\n+{'-'*50}+"


#   Clase para crear un USUARIO | - - - - COMING SOON - - - - |
class User:
    def __init__(self, U_FirstName, U_LastName, Email, Num_Phone, Direction):
        self.U_FirstName = U_FirstName
        self.U_LastName = U_LastName
        self.Email = Email
        self.Num_Phone = Num_Phone
        self.Direction = Direction


#Clase para crear un TICKET | - - - - COMING SOON - - - - |
class Ticket:
    def __init__(self, T_Price, T_Iva, T_Date, T_Time, T_Tipe, T_PayMethod, T_AmountPaid, T_UserID):
        self.T_Price = T_Price
        self.T_Iva = T_Iva
        self.T_Date = T_Date
        self.T_Time = T_Time
        self.T_Tipe = T_Tipe
        self.T_PayMethod = T_PayMethod
        self.T_AmountPaid = T_AmountPaid
        self.T_UserID = T_UserID


# --- Funciones ---

#Funcion para crear el objeto product_paint con parametros fijos [] | Se genera id distinta al igual que el tiempo en la db | 
def NewProductPaint():

    #Productos definidos para Test:

    P_Name = "Rojo Vino"
    P_Color = "Vino"
    ColorCode = "#83072D"
    CategoryColor = "Rojo"
    P_Description = "Pintura color Rojo vino para interiores"
    P_Date = datetime.today().date() # Seleccionar Solo Fecha del daterime.today()
    P_Time = datetime.today().time() #Remplazar porla hora de [datetime.today()]
    Price = 34.95
    Stock = Stock = 0
    Selled= Selled = 0

    new_product = Product_Paint(P_Name, P_Color, ColorCode, CategoryColor, P_Description, P_Date, P_Time, Price, Stock, Selled)

    #Devuelve un objeto "new_product" con el constructor de la clase Product_Paint con los parametros definidos
    return new_product

    ''' Inputs por definir - commit
        

        while True:
            try:
                P_Name = str(input("Nombre: "))}
                if P_Name:
                    break
                else:
                    True
                        
            except Error as e:
                print(f"Error al ingresado. DATO INVALIDO :'{e}'")


        P_Color = str(input("Color: "))
        ColorCode = str(input("Codigo hexadecimal del color: "))
        CategoryColor = str(input("Categoria del color: "))
        P_Description = str(input("Descripcion: "))
        P_Date = str(input("Fecha: "))
        P_Time = str(input("Hora: "))
        Price = float(input("Precio: "))
        Stock = int(input("Stock: "))
        Selled= int(input("Selled: "))
    '''

#Creo el objeto porduct1 con los parametros de la clase hija 'Class Product_Paint(Product):' con product como clase padre

select_option = 1
option_request = True



#cursor = connect().cursor


# if select_option == 1:

#     #creo producto con la funcion 'NewProductPaint' 
#     Product1 = NewProductPaint()

#     # IMPRESION DEL OBJETO PRODUCT1
#     print(Product1)

#     #
# else:
#     print("No se ejecuto ninguna opcion")
#     option_request = False


#connect().close