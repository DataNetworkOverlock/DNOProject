import tkinter as tk
import os


def create_menu_window(root, app, credentials):
    menu_window = tk.Toplevel(root)
    MenuWindow(menu_window, app, credentials)


class MenuWindow:
    def __init__(self, root, app, credentials):
        self.root = root
        self.app = app
        self.credentials = credentials
        root.title("Reportes")  # Titulo de la ventana
        root.geometry("1200x720")  # Tamaño de la ventana
        # Cambiar el color de fondo a un color hexadecimal
        root.configure(bg="#1B1A20")
        # Impedir que la ventana sea redimensionada
        root.resizable(False, False)
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
        self.TextField_Busqueda = None

        self.create_widgets()

    def create_widgets(self):

        # Frame (Visualizacion de contenido)
        # Creacion y especificacion decolor
        cuadroV = tk.Frame(self.root, bg="#1E1F24", border=0)
        # Ubicacion del frame
        cuadroV.place(relx=0.65, rely=0.0, relwidth=0.7,
                      relheight=1.0, anchor="n")

        # Label (Subtitulo)
        # Texto del Label
        self.lblNombreReporte = tk.Label(cuadroV, text="REPORTES")
        # Configuracion de Label
        self.lblNombreReporte.config(
            fg="#B7BBD0", bg="#1E1F24", font=("Lucida Console", 40))
        # Ubicacion
        self.lblNombreReporte.pack(anchor=("w"), padx=25, pady=(100, 10))
        self.lblNombreReporte.pack()

        # Creacion de text area
        self.text_area = tk.Text(cuadroV, wrap=tk.WORD)
        self.text_area.pack()
        # Configuracion del textArea
        self.text_area.config(width=95, height=27, bg="#1B1A20",
                              fg="white", relief="solid", borderwidth=0)
        self.text_area.pack(anchor=("w"), padx=25, pady=10)

        # Frame (Listados de reportes)
        # Creacion y especificacion de color
        cuadroL = tk.Frame(self.root, bg="#1B1A20", border=0)
        # Ubicacion del frame
        cuadroL.place(relx=0.155, rely=0.0, relwidth=0.3,
                      relheight=1.0, anchor="n")

        # Frame (cuadro)
        # Creacion y especificacion de color
        cuadroLI = tk.Frame(cuadroL, bg="#16151A", border=0)
        # Ubicacion del frame
        cuadroLI.place(relx=0.475, rely=0.1, relwidth=0.8,
                       relheight=0.85, anchor="n")

        # TextField (Busqueda)
        self.TextField_Busqueda = tk.Entry(cuadroLI)
        self.TextField_Busqueda.config(bg="#0D4044", font=(
            "Poppins", 12), relief="solid", border=0, width=20)
        self.TextField_Busqueda.insert(0, 'Filtro')
        self.TextField_Busqueda.bind('<FocusIn>', self.on_entry_click)
        self.TextField_Busqueda.bind('<FocusOut>', self.on_focus_out)
        self.TextField_Busqueda.config(fg='grey')
        self.TextField_Busqueda.pack(anchor=("w"), padx=10, pady=17)

        # boton (Buscar)
        # configuracion de boton
        btnSearch = tk.Button(cuadroLI, text="Buscar",
                              relief="solid", bg="#B7BBD0", fg="black",
                              font=("Poppins", 10), border=0,
                              command=self.actualizar_checkboxes)
        # ubicacion de boton
        btnSearch.place(relx=0.85, rely=0.025, anchor="n")

        # Crear una lista para almacenar los checkboxes
        self.Checkboxes = []

        # Directorio que se explora
        directorio = "Recursos/TXTs"

        # Obtener una lista de nombres de archivos en el directorio
        archivos = os.listdir(directorio)

        # Procesar y agregar los nombres de archivos como checkboxes
        for archivo in archivos:
            # Verificar el nombre del archivo
            if archivo.endswith(".txt"):
                # Divide el archivo en dos partes (nombre/extension)
                nombre_sin_extension = os.path.splitext(archivo)[0]
                # Crear un IntVar para el checkbox
                var = tk.IntVar()
                # Crear el checkbox y agregarlo a la lista
                chk = tk.Checkbutton(cuadroLI, text=nombre_sin_extension, bg="#24B1BD", fg="black", variable=var,
                                     onvalue=1, offvalue=0, font=("Poppins", 12), command=lambda nombre=nombre_sin_extension: self.mostrar_contenido_checkbox(nombre))
                chk.var = var  # Guardar la variable de control como un atributo del Checkbutton
                chk.pack(anchor=tk.W)  # Ajustar la posición
                self.Checkboxes.append(chk)

        # Crear un diccionario para almacenar el contenido de los archivos
        self.contenido = {}

        # Leer el contenido de los archivos y agregarlo al diccionario
        for archivo in archivos:
            if archivo.endswith(".txt"):
                nombre_sin_extension = os.path.splitext(
                    archivo)[0]  # Obtener el nombre sin extensión
                with open(os.path.join(directorio, archivo), "r", encoding="utf-8") as file:
                    self.contenido[nombre_sin_extension] = file.read()

        # boton (Exportar a PDF)
        # configuracion de boton
        btnPDF = tk.Button(cuadroV, text="PDF", relief="solid",
                           bg="#B7BBD0", fg="black", font=("Poppins", 12), border=0, command=self.handle_checkboxes)
        # ubicacion de boton
        btnPDF.place(relx=0.91, rely=0.875, anchor="n")

        # boton (Regresar a consola)
        # configuracion de boton
        btnVolver = tk.Button(cuadroV, text="Volver a consola", relief="solid", bg="#B7BBD0",
                              fg="black", font=("Poppins", 12), border=0, command=self.ir_a_panel)
        # ubicacion de boton
        btnVolver.place(relx=0.115, rely=0.875, anchor="n")

        # boton (Deslogueo)
        # configuracion de boton
        btnSalir = tk.Button(cuadroV, text="Salir de cuenta", relief="solid", bg="#B7BBD0", fg="black", font=(
            "Poppins", 14), border=0, command=self.ir_a_inicio_sesion)
        # ubicacion de boton
        btnSalir.place(relx=0.851, rely=0.05, anchor="n")

    def ir_a_panel(self):
        # Lógica para ir a la ventana de registro
        self.root.withdraw()  # Oculta la ventana actual
        self.app.mostrar_panel2()  # Muestra la ventana de registro en la ventana principal

    def ir_a_inicio_sesion(self):
        # Lógica para volver a la ventana de inicio de sesión
        self.root.withdraw()  # Oculta la ventana actual
        self.app.show()  # Muestra la ventana de inicio de sesión en la ventana principal

    def seleccionar_elemento(self, event):
        index = self.ListBoxReportes.curselection()
        if index:
            selected_item = self.ListBoxReportes.get(index[0])
            if selected_item in self.contenido:
                self.mostrar_contenido(selected_item)

    def on_entry_click(self, event):
        if self.TextField_Busqueda.get() == 'Filtro':
            self.TextField_Busqueda.delete(0, "end")
            self.TextField_Busqueda.config(fg='white')

    def on_focus_out(self, event):
        if self.TextField_Busqueda.get() == '':
            self.TextField_Busqueda.insert(0, 'Filtro')
            self.TextField_Busqueda.config(fg='grey')

    def actualizar_checkboxes(self):
        filtro = self.TextField_Busqueda.get().lower()  # Obtener el filtro
        # Recorrer todos los checkboxes
        for checkbox in self.Checkboxes:
            # Verificar si el nombre del checkbox coincide con el filtro
            if filtro in checkbox.cget("text").lower():
                # Mostrar el checkbox y alinear a la izquierda
                checkbox.pack(anchor=tk.W)
            else:
                # Ocultar el checkbox
                checkbox.pack_forget()

    # Función para manejar los checkboxes seleccionados
    def handle_checkboxes(self):
        for checkbox in self.Checkboxes:
            if checkbox.var.get() == 1:
                # Checkbox seleccionado, hacer algo con él
                print(f"{checkbox.cget('text')} seleccionado")

    # Función para mostrar el contenido del archivo seleccionado en el Text
    def mostrar_contenido(self, selected_item):
        if selected_item in self.contenido:
            # Obtener el contenido del archivo seleccionado
            contenido_text = self.contenido[selected_item]
            # Borrar el contenido actual del Text
            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, contenido_text)

    # Función para mostrar el contenido del archivo asociado al checkbox seleccionado
    def mostrar_contenido_checkbox(self, nombre_checkbox):
        if nombre_checkbox in self.contenido:
            # Obtener el contenido del archivo asociado al checkbox
            contenido_text = self.contenido[nombre_checkbox]
            # Borrar el contenido actual del Text
            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, contenido_text)
