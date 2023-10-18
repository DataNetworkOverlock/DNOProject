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
ventana.title("Registro")
#Tamaño de la ventana
ventana.geometry("1200x720")
# Cambiar el color de fondo a un color hexadecimal
ventana.configure(bg="#1B1A20")
# Impedir que la ventana sea redimensionada
ventana.resizable(False, False)

centrar_ventana(ventana)  # Llamada de la función para centrar la ventana

#Label (titulo)
#Texto del Label
lbl =Label(ventana,text="REGISTRO")
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
cuadro.place(relx=0.5, rely=0.15, relwidth=0.6, relheight=0.7, anchor="n")

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
lblNU.pack(anchor=("w"), padx=50, pady=(15,5))
lblNU.pack()

# TextField (Nombre de usuario)
TextField_UserName = tk.Entry(cuadro)
#Configuracion de text fielg
TextField_UserName.config(bg="#26272B", font=("Arial", 12), width=100, fg="white")
#Ubicacion
TextField_UserName.pack(anchor=("w"), padx=55, pady=0)
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
lblPass.pack(anchor=("w"), padx=50, pady=(30,5))
lblPass.pack()

# TextField(Password)
TextField_Pass = tk.Entry(cuadro)
#Configuracion de text fielg
TextField_Pass.config(bg="#26272B", font=("Arial", 12), width=100, fg="white")
#Ubicacion
TextField_Pass.pack(anchor=("w"), padx=55, pady=0)
TextField_Pass.pack()

#Label (confirmar contraseña)
#Texto del Label
lblPass2 = tk.Label(cuadro, text="Confirmar Contraseña")
#Color de la letra Label
lblPass2.config(fg = "#B4BDE2")
#Color del label (transparente)
lblPass2.config(bg= "#26272B")
#tipo de letra y tamaño de esta
lblPass2.config(font=("Arial", 15))
#Ubicacion
lblPass2.pack(anchor=("w"), padx=50, pady=(30,5))
lblPass2.pack()

# TextField(confirmar Password)
TextField_Pass2 = tk.Entry(cuadro)
#Configuracion de text fielg
TextField_Pass2.config(bg="#26272B", font=("Arial", 12), width=100, fg="white")
#Ubicacion
TextField_Pass2.pack(anchor=("w"), padx=55, pady=0)
TextField_Pass2.pack()

#Label (Pregunta)
#Texto del Label
lblQ = tk.Label(cuadro, text="pregunta de seguridad")
#Color de la letra Label
lblQ.config(fg = "#B4BDE2")
#Color del label (transparente)
lblQ.config(bg= "#26272B")
#tipo de letra y tamaño de esta
lblQ.config(font=("Arial", 15))
#Ubicacion
lblQ.pack(anchor=("w"), padx=50, pady=(30,5))
lblQ.pack()

# TextField(Pregunta)
TextField_Pass2 = tk.Entry(cuadro)
#Configuracion de text fielg
TextField_Pass2.config(bg="#26272B", font=("Arial", 12), width=100, fg="white")
#Ubicacion
TextField_Pass2.pack(anchor=("w"), padx=55, pady=0)
TextField_Pass2.pack()

#Label (respuesta)
#Texto del Label
lblAnsw = tk.Label(cuadro, text="respuesta de pregunta de confirmacion")
#Color de la letra Label
lblAnsw.config(fg = "#B4BDE2")
#Color del label (transparente)
lblAnsw.config(bg= "#26272B")
#tipo de letra y tamaño de esta
lblAnsw.config(font=("Arial", 15))
#Ubicacion
lblAnsw.pack(anchor=("w"), padx=50, pady=(30,5))
lblAnsw.pack()

# TextField(respuesta)
TextField_Pass2 = tk.Entry(cuadro)
#Configuracion de text fielg
TextField_Pass2.config(bg="#26272B", font=("Arial", 12), width=100, fg="white")
#Ubicacion
TextField_Pass2.pack(anchor=("w"), padx=55, pady=0)
TextField_Pass2.pack()

# Botton
btn_acceder = tk.Button(cuadro, text="Registrar", relief="sunken", bg="#0E0D13", fg="#ADB2D6", font=("Arial", 14))
btn_acceder.pack(anchor=("e"), padx=55, pady=25)
btn_acceder.pack()

#boton (Cancelar)
#configuracion de boton
btnCancel = Button(ventana, text="Cancelar", relief="flat", bg="#1B1A20", fg="#B4BADE", font=("Arial", 14), command = miFuncion)
#ubicacion de boton
btnCancel.place(relx=0.24, rely=0.875, anchor="n")

ventana.mainloop()
