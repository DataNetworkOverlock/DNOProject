import tkinter as tk
from tkinter import *

#metodos/funciones
#Funcion para imprimir en consola
def miFuncion():
    print("Este mensaje es del boton")
#Funcion para centrar la ventana
def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() - ancho) // 2
    y = (ventana.winfo_screenheight() - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

#Ventana
#se crea el objeto ventana a partir de la clase TK, para hacer una ventana
ventana = Tk()
#Titulo de la ventana
ventana.title("Login")
#Tamaño de la ventana
ventana.geometry("1200x720")
# Cambiar el color de fondo a un color hexadecimal
ventana.configure(bg="#1B1A20")
# Impedir que la ventana sea redimensionada
ventana.resizable(False, False)

centrar_ventana(ventana)  # Llamada de la función para centrar la ventana

#Label (titulo)
#Texto del Label
lbl =Label(ventana,text="LOGIN")
#Color de la letra Label
lbl.config(fg = "#B7BBD0")
#Color del label (transparente)
lbl.config(bg= "#1B1A20")
#tipo de letra y tamaño de esta
lbl.config(font=("Arial", 40))
#Ubicacion del Label
lbl.place(relx=0.5, rely=0.05, anchor="n")


#Frame (cuadro)
#Creacion y especificacion decolor
cuadro = tk.Frame(ventana, bg="#26272B")
#Ubicacion del frame
cuadro.place(relx=0.5, rely=0.2, relwidth=0.6, relheight=0.6, anchor="n")

#Label (Nombre de usuario)
#Texto del Label
lblNU = tk.Label(cuadro, text="Nombre de usuario")
#Color de la letra Label
lblNU.config(fg = "#B4BDE2")
#Color del label (transparente)
lblNU.config(bg= "#26272B")
#tipo de letra y tamaño de esta
lblNU.config(font=("Arial", 15))
#Ubicacion
lblNU.pack(anchor=("w"), padx=50, pady=(100,10))
lblNU.pack()

# TextField (Nombre de usuario)
TextField_UserName = tk.Entry(cuadro)
#Configuracion de text fielg
TextField_UserName.config(bg="#0D4044", font=("Arial", 12), width=100, fg="white")
#Ubicacion
TextField_UserName.pack(anchor=("w"), padx=55, pady=5)
TextField_UserName.pack()

#Label (contraseña)
#Texto del Label
lblPass = tk.Label(cuadro, text="Contraseña")
#Color de la letra Label
lblPass.config(fg = "#B4BDE2")
#Color del label (transparente)
lblPass.config(bg= "#26272B")
#tipo de letra y tamaño de esta
lblPass.config(font=("Arial", 15))
#Ubicacion
lblPass.pack(anchor=("w"), padx=50, pady=(50,10))
lblPass.pack()

# TextField(Password)
TextField_Pass = tk.Entry(cuadro)
#Configuracion de text fielg
TextField_Pass.config(bg="#0D4044", font=("Arial", 12), width=100, fg="white")
#Ubicacion
TextField_Pass.pack(anchor=("w"), padx=55, pady=5)
TextField_Pass.pack()

# Botton
btn_acceder = tk.Button(cuadro, text="Acceder", relief="sunken", bg="#0E0D13", fg="#ADB2D6", font=("Arial", 14))
btn_acceder.pack(anchor=("e"), padx=55, pady=50)
btn_acceder.pack()

#boton (registrarse)
#configuracion de boton
btnR = Button(ventana, text="Registrarse", relief="flat", bg="#1B1A20", fg="#B4BADE", font=("Arial", 14), command = miFuncion)
#ubicacion de boton
btnR.place(relx=0.245, rely=0.825, anchor="n")

#Boton (recordar contraseña)
btnRP = Button(ventana, text="¿Olvidaste tu contraseña?", relief="flat", bg="#1B1A20", fg="#B4BADE", font=("Arial", 14), command = miFuncion)
#ubicacion de boton
btnRP.place(relx=0.4, rely=0.825, anchor="n")

ventana.mainloop()