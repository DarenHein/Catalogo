import tkinter as tk
from tkinter import messagebox

def ingreso():
    nombreR = "Luis"
    contraR = "1234" 
    nombre = campo_nombre.get()
    contra = campo_contraseña.get()
    
    if ("Luis" == nombre and "1234" == contra) : 
        print("entro")
        messagebox.showinfo("Mensaje" , "Hola Bienvenido")
    elif nombre != nombreR and contra == contraR : 
        messagebox.showinfo("Mensaje" , "El usuario esta mal")
    elif nombre == nombreR and contra != contraR : 
        messagebox.showinfo("Mensaje " , "Contraseña invalida")
    else : 
        messagebox.showinfo("Mensaje" , "Nombre y contraseña invalidos")

ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("700x500")
etiqueta_titulo =  tk.Label(ventana , text= "Bienvenido" , font=("arial" , 20 , "bold"))
etiqueta_titulo.place(x = 250 , y = 40)
etiqueta_sub = tk.Label(ventana , text="Ingresa los datos " , font=("arial" , 16, "bold") , fg= "gray")
etiqueta_sub.place( x = 30 , y = 100)
etiqueta_nombre = tk.Label(ventana,text="Nombre " , font=("arial" , 13 , "bold") , fg="gray")
etiqueta_nombre.place(x = 30 , y = 170)
campo_nombre = tk.Entry(ventana, width= 30  )
campo_nombre .place(x = 30 , y = 200)
etiqueta_contraseña = tk.Label(ventana , text="Contraseña " , fg= "gray" , font=("arial" , 13 , "bold") )
etiqueta_contraseña.place(x = 30 , y = 240)
campo_contraseña = tk.Entry(ventana, width= 30 , show="*")
campo_contraseña.place(x = 30 , y = 270)
boton_ingreso = tk.Button(ventana, text="Iniciar" , width= 10 , fg= "white", bg= "red" , command=ingreso )
boton_ingreso.place(x = 50 , y = 360 )





ventana.mainloop()