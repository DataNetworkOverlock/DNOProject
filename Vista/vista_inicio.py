import tkinter as tk
from tkinter import *
from vista_inicio import VistaInicio

class VistaConfiguracion(tk.Frame):
    def centrar_ventana(self, ventana):
        ventana.update_idletasks()
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() - ancho) // 2
        y = (ventana.winfo_screenheight() - alto) // 2
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def __init__(self, root, inicio):
        super().__init__(root)
        self.inicio = inicio

        # Configurar la ventana principal
        self.root = root
        self.root.geometry("1200x720")
        # Impedir que la ventana sea redimensionada  --
        root.resizable(False, False)

        self.centrar_ventana(root)  # Llamada de la función para centrar la ventana

        # Crear un Frame principal para toda la vista
        frame_principal = tk.Frame(self.root, bg="#26272B")
        frame_principal.pack(expand=True, fill="both")

        # Definición de la interfaz gráfica de la vista principal (configuración)
        frame_configuracion = tk.Frame(frame_principal, bg="#26272B")
        frame_configuracion.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Frame (Visualización de contenido)
        cuadroV = tk.Frame(frame_configuracion, bg="#1E1F24")
        cuadroV.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Label (Subtitulo)
        lblNombreReporte = tk.Label(cuadroV, text="Configuración")
        lblNombreReporte.config(fg="#72737A", bg="#1E1F24", font=("Arial", 15))
        lblNombreReporte.place(relx=0.1, rely=0.1)

        # Creación de text area
        text_area = tk.Text(cuadroV, wrap=tk.WORD)
        text_area.config(width=95, height=27, bg="#1B1A20", fg="white", relief="solid", borderwidth=0)
        text_area.place(relx=0.1, rely=0.2)

        # Botón (Atrás)
        btnAtras = Button(cuadroV, text="Volver a inicio", relief="flat", bg="#0E0D13", fg="#ADB2D6", font=("Arial", 14), command=self.ir_a_inicio)
        btnAtras.place(relx=0.85, rely=0.05, anchor="n")

    def ir_a_inicio(self):
        # Cargar la vista de inicio y pasar la instancia de VistaConfiguracion
        inicio = VistaInicio(self.master)
        inicio.pack()
        self.pack_forget()  # Ocultar la vista de configuración

# Crear la ventana principal
if __name__ == "__main__":
    ventana = tk.Tk()
    app = VistaConfiguracion(ventana, None)
    app.pack()
    ventana.mainloop()
