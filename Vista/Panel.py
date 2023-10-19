import tkinter as tk
from tkinter import *
import os

#funciones
#Funcion para centrar la ventana
def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() - ancho) // 2
    y = (ventana.winfo_screenheight() - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def seleccionar_elemento(event):
    seleccion = ListTools.get(ListTools.curselection())
    etiqueta.config(text=f"{seleccion}")

#Ventana
#se crea el objeto ventana a partir de la clase TK, para hacer una ventana
ventana = Tk()
#Titulo de la ventana
ventana.title("Panel")
#Tamaño de la ventana
ventana.geometry("1200x720+0+0")
# Cambiar el color de fondo a un color hexadecimal
ventana.configure(bg="#1B1A20")
# Impedir que la ventana sea redimensionada
ventana.resizable(False, False)

centrar_ventana(ventana)  # Llamada de la función para centrar la ventana

#Frame (Consola)
#Creacion y especificacion decolor
cuadroCmd = tk.Frame(ventana, bg="#1E1F24")
#Ubicacion del frame
cuadroCmd.place(relx=0.65, rely=0.0, relwidth=0.7, relheight=1.0, anchor="n")


#Frame (Herramientas)
#Creacion y especificacion decolor
cuadroTool = tk.Frame(ventana, bg="#1B1A20")
#Ubicacion del frame
cuadroTool.place(relx=0.14, rely=0.0, relwidth=0.25, relheight=1.0, anchor="n")

#Label (Principal)
#Texto del Label
lblOverlook =Label(cuadroCmd,text="OVERLOCK")
#Color de la letra Label
lblOverlook.config(fg = "#B7BBD0")
#Color del label (transparente)
lblOverlook.config(bg= "#1B1A20")
#tipo de letra y tamaño de esta
lblOverlook.config(font=("Arial", 40))
#Ubicacion del Label
lblOverlook.place(relx=0.5, rely=0.05, anchor="n")

#Label (titulo)
#Texto del Label
lblTools =Label(cuadroTool,text="Herramientas")
#Color de la letra Label
lblTools.config(fg = "#B7BBD0")
#Color del label (transparente)
lblTools.config(bg= "#1B1A20")
#tipo de letra y tamaño de esta
lblTools.config(font=("Arial", 25))
#Ubicacion del Label
lblTools.place(relx=0.5, rely=0.05, anchor="n")

# Crear un ListBox
ListTools = tk.Listbox(cuadroTool, selectmode=tk.SINGLE)
ListTools.configure(bg="#25242D", fg = "#AEAEB0", font=("Verdana", 20, "bold"))
ListTools.place(x=10, y=100, width=260, height=425)

# Agregar elementos al ListTools
elementos = ["kismet", "john the ripper", "sqlmap", "nmap", "nikto"]
for elemento in elementos:
    ListTools.insert(tk.END, elemento)

# Configurar un evento de selección en el ListTools
ListTools.bind("<<ListboxSelect>>", seleccionar_elemento)

# Crear una etiqueta para mostrar el elemento seleccionado
etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

ventana.mainloop()