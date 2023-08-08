from tkinter import *

window_conection = Tk()

window_conection.title("CONECTION INFO")
window_conection.geometry("360x120")

Label_1 = Label(window_conection, text = "¡Hola mundo!", font=("Arial Bold",30))
Label_1.grid(column=0,row=0)


window_conection.mainloop()