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
# Función para manejar la selección de elementos en el ListBox
def seleccionar_elemento(event):
    # Obtener el índice del elemento seleccionado
    index = ListBox.curselection()
    
    # Obtener el elemento seleccionado
    selected_item = ListBox.get(index)

    # Actualizar una etiqueta para mostrar el elemento seleccionado
    lblNombreReporte.config(text=f"{selected_item}")

    # Actualizar el contenido del Text
    mostrar_contenido(selected_item)

# Función para actualizar el contenido del Text
def mostrar_contenido(selected_item):
    contenido_text = contenido.get(selected_item, '')  # Obtener el contenido del elemento seleccionado
    text_area.delete('1.0', tk.END)  # Borrar el contenido actual del Text
    text_area.insert(tk.END, contenido_text)

# Función para manejar la selección en el Listbox
def seleccionar_archivo(event):
    # Obtener el elemento seleccionado
    seleccion = Listbox.get(Listbox.curselection())
    print(f"Seleccionaste: {seleccion}")

#Ventana
#se crea el objeto ventana a partir de la clase TK, para hacer una ventana
ventana = Tk()
#Titulo de la ventana
ventana.title("Login")
#Tamaño de la ventana
ventana.geometry("1200x720+0+0")
# Cambiar el color de fondo a un color hexadecimal
ventana.configure(bg="#1B1A20")
# Impedir que la ventana sea redimensionada
ventana.resizable(False, False)

centrar_ventana(ventana)  # Llamada de la función para centrar la ventana

#Frame (Visualizacion de contenido)
#Creacion y especificacion decolor
cuadroV = tk.Frame(ventana, bg="#1E1F24")
#Ubicacion del frame
cuadroV.place(relx=0.65, rely=0.0, relwidth=0.7, relheight=1.0, anchor="n")

#Label (Subtitulo)
#Texto del Label
lblNombreReporte = tk.Label(cuadroV, text="Nombre de reporte")
#Configuracion de Label
lblNombreReporte.config(fg = "#72737A", bg= "#1E1F24", font=("Arial", 15))
#Ubicacion
lblNombreReporte.pack(anchor=("w"), padx=25, pady=(100,10))
lblNombreReporte.pack()

# Creacion de text area
text_area = tk.Text(cuadroV, wrap=tk.WORD)
text_area.pack()

# Puedes establecer un ancho y alto inicial
text_area.config(width=95, height=27, bg="#1B1A20", fg="white", relief="solid", borderwidth=0)
text_area.pack(anchor=("w"), padx=25, pady=10)

#Frame (Listados de reportes)
#Creacion y especificacion decolor
cuadroL = tk.Frame(ventana, bg="#1B1A20")
#Ubicacion del frame
cuadroL.place(relx=0.155, rely=0.0, relwidth=0.3, relheight=1.0, anchor="n")

#Label (Subtitulo)
#Texto del Label
lblNU = tk.Label(cuadroL, text="Reportes existentes")
#Configuracion de Label
lblNU.config(fg = "#72737A", bg= "#1B1A20", font=("Arial", 15))
#Ubicacion
lblNU.pack(anchor=("w"), padx=25, pady=(100,10))
lblNU.pack()

#Frame (cuadro)
#Creacion y especificacion de color
cuadroLI = tk.Frame(cuadroL, bg="#16151A", relief="solid", borderwidth=0)
#Ubicacion del frame
cuadroLI.place(relx=0.475, rely=0.2, relwidth=0.8, relheight=0.7, anchor="n")

# TextField (Busqueda)
TextField_Busqueda = tk.Entry(cuadroLI)
#Configuracion de text fielg
TextField_Busqueda.config(bg="#0F0E12", font=("Arial", 12), width=22, fg="white", relief="solid")
#Ubicacion
TextField_Busqueda.pack(anchor=("w"), padx=10, pady=15)
TextField_Busqueda.pack()

#boton (Buscar)
#configuracion de boton
btnSearch = Button(cuadroLI, text="Buscar", relief="flat", bg="#1B1A20", fg="#B4BADE", font=("Arial", 10))
#ubicacion de boton
btnSearch.place(relx=0.85, rely=0.025, anchor="n")

# Crear un ListBox
ListBox = tk.Listbox(cuadroLI, selectmode=tk.SINGLE)
ListBox.configure(bg="#25242D", fg = "#AEAEB0")
ListBox.place(x=10, y=60, width=260, height=425)

# Directorio que se explora
directorio = "D:/trabajos/Tesis/Repositorio/DNOProject/Recursos/TXTs"

# Obtener una lista de nombres de archivos en el directorio
archivos = os.listdir(directorio)

# Agregar los nombres de archivos al Listbox
for archivo in archivos:
    ListBox.insert(tk.END, archivo)

# Crear un diccionario con contenido asociado
contenido = {
    "Manzana.txt": "Este es el contenido de la manzana.",
    "Banana": "Este es el contenido de la banana.",
    "Cereza": "Este es el contenido de la cereza.",
    "Naranja": "Este es el contenido de la naranja.",
    "Frambuesa": "Este es el contenido de la frambuesa.",
    "Uva": "Este es el contenido de la uva."
}

# Configurar un evento de selección en el ListBox
ListBox.bind("<<ListboxSelect>>", seleccionar_elemento)

ventana.mainloop()