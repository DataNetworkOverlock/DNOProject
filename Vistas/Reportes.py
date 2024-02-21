import tkinter as tk
import os
from utils.tests import Tests


class MenuWindow:
    def __init__(self, root, app, credentials):
        self.root = root
        self.app = app
        self.credentials = credentials

        self.ventana = tk.Toplevel(self.root)
        self.ventana.title("Reportes")  # Titulo de la ventana
        self.ventana.geometry("1200x720")  # Tamaño de la ventana
        # Cambiar el color de fondo a un color hexadecimal
        self.ventana.configure(bg="#1B1A20")
        # Impedir que la ventana sea redimensionada
        self.ventana.resizable(False, False)
        # Centrar la ventana
        self.ventana.update_idletasks()
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() - ancho) // 2
        y = (self.ventana.winfo_screenheight() - alto) // 2
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.ventana.protocol("WM_DELETE_WINDOW", self.app.close)

        # Inicializar los widgets
        self.ListBoxReportes = None
        self.contenido = {}
        self.text_area = None
        self.lblNombreReporte = None
        self.TextField_Busqueda = None

        self.token = self.credentials["token"]
        self.username = self.credentials["username"]
        self.test = Tests(token=self.token)

        self.create_widgets()

    def create_widgets(self):

        # Frame (Visualizacion de contenido)
        # Creacion y especificacion decolor
        cuadroV = tk.Frame(self.ventana, bg="#1E1F24", border=0)
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
        cuadroL = tk.Frame(self.ventana, bg="#1B1A20", border=0)
        # Ubicacion del frame
        cuadroL.place(relx=0.155, rely=0.0, relwidth=0.3,
                      relheight=1.0, anchor="n")

        # Frame (cuadro)
        # Creacion y especificacion de color
        cuadroLI = tk.Frame(cuadroL, bg="#16151A", border=0)
        # Ubicacion del frame
        cuadroLI.place(relx=0.475, rely=0.1,
                       relwidth=0.8, relheight=0.85, anchor="n")

        # TextField (Busqueda)
        self.TextField_Busqueda = tk.Entry(cuadroLI)
        self.TextField_Busqueda.config(bg="#0D4044",
                                       font=("Poppins", 12), relief="solid",
                                       border=0, width=18)
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
        # Crear un diccionario para almacenar el contenido de los archivos
        self.contenido = {}

        reportes_usuario = self.test.get_tests_by_username(
            username=self.username)["response"]
        print(reportes_usuario)

        for reporte in reportes_usuario["tests"]:
            nombre_reporte = reporte["date"][:15]
            var = tk.IntVar()
            chk = tk.Checkbutton(cuadroLI, text=nombre_reporte,
                                 bg="#24B1BD", fg="black", variable=var, wraplength=300,
                                 onvalue=1, offvalue=0, font=("Poppins", 11),
                                 command=lambda nombre=nombre_reporte: self.mostrar_contenido_checkbox(nombre))
            chk.var = var
            chk.pack(anchor=tk.W, padx=10, pady=5)
            self.Checkboxes.append(chk)
            self.contenido[nombre_reporte] = reporte["report"]

        # boton (Exportar a PDF)
        # configuracion de boton
        btnPDF = tk.Button(cuadroV, text="PDF", relief="solid",
                           bg="#B7BBD0", fg="black", font=("Poppins", 12),
                           border=0, command=self.handle_checkboxes)
        # ubicacion de boton
        btnPDF.place(relx=0.91, rely=0.875, anchor="n")

        # boton (Regresar a consola)
        # configuracion de boton
        btnVolver = tk.Button(cuadroV, text="Volver a consola",
                              relief="solid", bg="#B7BBD0", fg="black",
                              font=("Poppins", 12), border=0,
                              command=self.ir_a_panel)
        # ubicacion de boton
        btnVolver.place(relx=0.115, rely=0.875, anchor="n")

    def ir_a_panel(self):
        # Lógica para ir a la ventana de registro
        self.ventana.destroy()  # Cierra la ventana actual
        self.app.abrir_panel()  # Muestra la ventana de registro en la ventana principal

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
                checkbox.pack(anchor=tk.W, padx=10, pady=5)
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
