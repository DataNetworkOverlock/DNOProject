import tkinter as tk
import os

def create_menu_window(root, app):
    menu_window = tk.Toplevel(root)
    MenuWindow(menu_window, app)

class MenuWindow:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        root.title("menu") #Titulo de la ventana
        root.geometry("1200x720") #Tamaño de la ventana
        root.configure(bg="#1B1A20")# Cambiar el color de fondo a un color hexadecimal
        root.resizable(False, False)# Impedir que la ventana sea redimensionada
        # Centrar la ventana
        root.update_idletasks()
        ancho = root.winfo_width()
        alto = root.winfo_height()
        x = (root.winfo_screenwidth() - ancho) // 2
        y = (root.winfo_screenheight() - alto) // 2
        root.geometry(f"{ancho}x{alto}+{x}+{y}")

        # Inicializar los widgets
        self.ListBoxReportes = None
        self.contenido = {}
        self.text_area = None
        self.lblNombreReporte = None

        self.create_widgets()

    def create_widgets(self):

        #Frame (Visualizacion de contenido)
        #Creacion y especificacion decolor
        cuadroV = tk.Frame(self.root, bg="#1E1F24")
        #Ubicacion del frame
        cuadroV.place(relx=0.65, rely=0.0, relwidth=0.7, relheight=1.0, anchor="n")

        #Label (Subtitulo)
        #Texto del Label
        self.lblNombreReporte = tk.Label(cuadroV, text="Nombre de reporte")
        #Configuracion de Label
        self.lblNombreReporte.config(fg = "#72737A", bg= "#1E1F24", font=("Arial", 15))
        #Ubicacion
        self.lblNombreReporte.pack(anchor=("w"), padx=25, pady=(100,10))
        self.lblNombreReporte.pack()

        # Creacion de text area
        self.text_area = tk.Text(cuadroV, wrap=tk.WORD)
        self.text_area.pack()
        # Configuracion del textArea
        self.text_area.config(width=95, height=27, bg="#1B1A20", fg="white", relief="solid", borderwidth=0)
        self.text_area.pack(anchor=("w"), padx=25, pady=10)

        #Frame (Listados de reportes)
        #Creacion y especificacion decolor
        cuadroL = tk.Frame(self.root, bg="#1B1A20")
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
        btnSearch = tk.Button(cuadroLI, text="Buscar", relief="flat", bg="#1B1A20", fg="#B4BADE", font=("Arial", 10))
        #ubicacion de boton
        btnSearch.place(relx=0.85, rely=0.025, anchor="n")

        # Crear un ListBox
        self.ListBoxReportes = tk.Listbox(cuadroLI, selectmode=tk.SINGLE)
        self.ListBoxReportes.configure(bg="#25242D", fg = "#AEAEB0")
        self.ListBoxReportes.place(x=10, y=60, width=260, height=425)

        # Directorio que se explora
        directorio = "D:/trabajos/Tesis/Repositorio/DNOProject/Recursos/TXTs"

        # Obtener una lista de nombres de archivos en el directorio
        archivos = os.listdir(directorio)

        # Procesar y agregar los nombres de archivos al ListBox
        for archivo in archivos:
            # Verificar el nombre del archivo
            if archivo.endswith(".txt"):
                #Divide el archivo en dos partes (nombre/extension)
                nombre_sin_extension = os.path.splitext(archivo)[0]
                #Agrega el el nombre sin extension a la lista
                self.ListBoxReportes.insert(tk.END, nombre_sin_extension)

        # Crear un diccionario para almacenar el contenido de los archivos
        self.contenido = {}

        # Leer el contenido de los archivos y agregarlo al diccionario
        for archivo in archivos:
            if archivo.endswith(".txt"):
                nombre_sin_extension = os.path.splitext(archivo)[0]  # Obtener el nombre sin extensión
                with open(os.path.join(directorio, archivo), "r", encoding="utf-8") as file:
                    self.contenido[nombre_sin_extension] = file.read()

        # Configurar un evento de selección en el ListBox
        self.ListBoxReportes.bind("<<ListboxSelect>>", self.seleccionar_elemento)

        #boton (Exportar a PDF)
        #configuracion de boton
        btnSearch = tk.Button(cuadroV, text="Exportar a PDF", relief="flat", bg="#0E0D13", fg="#ADB2D6", font=("Arial", 14))
        #ubicacion de boton
        btnSearch.place(relx=0.85, rely=0.85, anchor="n")

        #boton (Regresar a consola)
        #configuracion de boton
        btnSearch = tk.Button(cuadroV, text="Volver a consola", relief="flat", bg="#0E0D13", fg="#ADB2D6", font=("Arial", 14), command=self.ir_a_panel)
        #ubicacion de boton
        btnSearch.place(relx=0.125, rely=0.85, anchor="n")

        #boton (Deslogueo)
        #configuracion de boton
        btnSearch = tk.Button(cuadroV, text="Salir de cuenta", relief="flat", bg="#0E0D13", fg="#ADB2D6", font=("Arial", 14), command=self.ir_a_inicio_sesion)
        #ubicacion de boton
        btnSearch.place(relx=0.85, rely=0.05, anchor="n")

    def ir_a_panel(self):
        # Lógica para ir a la ventana de registro
        self.root.withdraw()  # Oculta la ventana actual
        self.app.mostrar_panel()  # Muestra la ventana de registro en la ventana principal

    def ir_a_inicio_sesion(self):
        # Lógica para volver a la ventana de inicio de sesión
        self.root.withdraw()  # Oculta la ventana actual
        self.app.show()  # Muestra la ventana de inicio de sesión en la ventana principal
    
    def seleccionar_elemento(self, event):

        index = self.ListBoxReportes.curselection()
        if index:
            selected_item = self.ListBoxReportes.get(index[0])
            if selected_item in self.contenido:
                self.lblNombreReporte.config(text=f"{selected_item}")
                self.mostrar_contenido(selected_item)

    # Función para mostrar el contenido del archivo seleccionado en el Text
    def mostrar_contenido(self, selected_item):
        if selected_item in self.contenido:
            contenido_text = self.contenido[selected_item]  # Obtener el contenido del archivo seleccionado
            self.text_area.delete('1.0', tk.END)  # Borrar el contenido actual del Text
            self.text_area.insert(tk.END, contenido_text)

if __name__ == "__main__":
    ventana_registro = tk.Toplevel()
    ventana_registro.withdraw()
    ventana_registro.mainloop()

    