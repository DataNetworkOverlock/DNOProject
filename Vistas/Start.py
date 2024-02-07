import tkinter as tk
from tkinter import *

# funciones
# Funcion para centrar la ventana


def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() - ancho) // 2
    y = (ventana.winfo_screenheight() - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


# Ventana
# se crea el objeto ventana a partir de la clase TK, para hacer una ventana
ventana = Tk()
# Titulo de la ventana
ventana.title("Starting...")
# Tamaño de la ventana
ventana.geometry("1200x720")
# Cambiar el color de fondo a un color hexadecimal
ventana.configure(bg="#1B1A20")
# Impedir que la ventana sea redimensionada
ventana.resizable(False, False)

centrar_ventana(ventana)  # Llamada de la función para centrar la ventana

# Crear el Canvas para dibujar la figura
canvas = tk.Canvas(ventana, width=1200, height=720, bg="#1B1A20")
canvas.pack()

# Coordenadas de los puntos de la figura
x1, y1 = 0, 650  # SI
x2, y2 = 1200, 400  # SD
x3, y3 = 1200, 720  # ID
x4, y4 = 0, 720  # II

# Dibuja la figura con las coordenadas especificadas
canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4,
                      fill="#2C2D32", outline="#ADAEB3")

# Label (titulo)
# Texto del Label
lbl = Label(ventana, text="Data Network Overlock")
# Configuracion del label
lbl.config(fg="#F6A00C", bg="#1B1A20", font=("Arial", 40))
# Ubicacion del Label
lbl.place(relx=0.5, rely=0.45, anchor="e")

# Label (version)
# Texto del Label
lbl = Label(ventana, text="Data Network Overlock 2.0")
# Configuracion del label
lbl.config(fg="#C0C6E3", bg="#2C2D32", font=("Arial", 15))
# Ubicacion del Label
lbl.place(relx=0.75, rely=0.9, anchor="w")

ventana.mainloop()
