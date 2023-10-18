import tkinter as tk
from tkinter import *

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
    etiqueta.config(text=f"Elemento seleccionado: {selected_item}")

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
#Creacion y especificacion decolor
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
ListBox.place(x=10, y=60, width=260, height=425)

# Agregar elementos al ListBox
elementos = ["Manzana", "Banana", "Cereza", "Dátil", "Frambuesa", "Uva"]
for elemento in elementos:
    ListBox.insert(tk.END, elemento)

# Configurar un evento de selección en el ListBox
ListBox.bind("<<ListboxSelect>>", seleccionar_elemento)

# Crear una etiqueta para mostrar el elemento seleccionado
etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

ventana.mainloop()

