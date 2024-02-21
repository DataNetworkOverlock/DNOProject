import tkinter as tk
import subprocess
from utils.scripts import Scripts
from Vistas.Parametros import Parametros


class PanelWindow:

    def __init__(self, root, app, credentials):
        self.root = root
        self.app = app
        self.credentials = credentials

        self.ventana = tk.Toplevel(self.root)
        self.ventana.title("Data Network Overlock")  # Titulo de la ventana
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

        self.entry_busqueda = None
        self.cuadroCmdInterno = None
        self.frame_interior = None
        self.selected_options = []  # Inicializar la lista aquí

        self.token = self.credentials["token"]
        self.scripts = Scripts(token=self.token)

        self.create_widgets()  # Llamado de funcion para crear los widgets

    def create_widgets(self):
        # Frame (Consola)
        # Creacion y especificacion decolor
        cuadroCmd = tk.Frame(self.ventana, bg="#1E1F24")
        # Ubicacion del frame
        cuadroCmd.place(relx=0.65, rely=0.0, relwidth=0.7,
                        relheight=1.0, anchor="n")

        # Label (Principal)
        # Texto del Label
        lblOverlock = tk.Label(cuadroCmd, text="OVERLOCK")
        # Color de la letra Label
        lblOverlock.config(fg="#B4BDE2")
        # Color del label (transparente)
        lblOverlock.config(bg="#1E1F24")
        # tipo de letra y tamaño de esta
        lblOverlock.config(font=("Lucida Console", 40))
        # Ubicacion del Label
        lblOverlock.place(relx=0.5, rely=0.05, anchor="n")

        cuadroCmd2 = tk.Frame(cuadroCmd, bg='#191A1E')
        cuadroCmd2.place(relx=0.5, rely=0.2, relwidth=0.85,
                         relheight=0.7, anchor="n")

        scrollbar = tk.Scrollbar(cuadroCmd2, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.cuadroCmdInterno = tk.Canvas(cuadroCmd2,
                                          bg="#191A1E", background="#191A1E",
                                          yscrollcommand=scrollbar.set, highlightthickness=0)
        self.cuadroCmdInterno.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.cuadroCmdInterno.yview)

        self.frame_interior = tk.Frame(
            self.cuadroCmdInterno, bg='#191A1E')  # Frame interno al Canvas
        self.cuadroCmdInterno.create_window(
            (0, 0), window=self.frame_interior, anchor='nw')

        scripts = self.scripts.get_scripts()
        scripts_info = scripts["response"]
        scripts_status = scripts["status"]

        if scripts_status != 200:
            print(
                f"Error {scripts_status}. No se pudieron obtener los scripts. {
                    scripts_info}"
            )
            self.ir_a_inicio_sesion()

        # Agregamos una variable para almacenar los scripts originales sin filtrar
        self.scripts_info_original = scripts_info.copy()

        self.crear_componente_scripts(scripts_info)

        # Frame (Scripts)
        # Creacion y especificacion decolor
        contenedor_opciones = tk.Frame(self.ventana, bg="#1B1A20")
        # Ubicacion del frame
        contenedor_opciones.place(relx=0.14, rely=0.0, relwidth=0.3,
                         relheight=1.0, anchor="n")

        # Label (titulo)
        lblTools = tk.Label(contenedor_opciones, text="Scripts")
        lblTools.config(fg="#B7BBD0", bg="#1B1A20",
                        font=("Lucida Console", 25))
        lblTools.place(relx=0.5, rely=0.05, anchor="n")

        # Frame (Consola)
        # Creacion y especificacion decolor
        contenedor_filtros = tk.Frame(contenedor_opciones, bg="#1E1F24")
        # Ubicacion del frame
        contenedor_filtros.place(relx=0.55, rely=0.15,
                                 relwidth=0.8, relheight=0.7, anchor="n")

        contenedor_busqueda = tk.Frame(
            contenedor_filtros, bg="#1E1F24", padx=10, pady=10)
        contenedor_busqueda.place(
            relx=0.5, relwidth=1, relheight=0.15, anchor="n")

        contenedor_etiquetas = tk.Frame(contenedor_filtros, bg="#1E1F24")
        contenedor_etiquetas.place(
            relx=0, rely=0.15, relwidth=1, relheight=0.9)

        # TextField (Busqueda)
        self.entry_busqueda = tk.Entry(contenedor_busqueda)
        self.entry_busqueda.config(bg="#0D4044", relief="solid",
                                   font=("Poppins", 12), border=0)
        self.entry_busqueda.insert(0, 'Filtro')
        self.entry_busqueda.bind('<FocusIn>', self.on_entry_click)
        self.entry_busqueda.bind('<FocusOut>', self.on_focus_out)
        self.entry_busqueda.config(fg='grey')
        self.entry_busqueda.pack(side=tk.LEFT)

        # boton (Buscar)
        # configuracion de boton
        btnSearch = tk.Button(contenedor_busqueda, text="Buscar",
                              relief="solid", bg="#B7BBD0", fg="black",  border=0,
                              font=("Poppins", 10), command=self.buscar_scripts_por_nombre)
        # ubicacion de boton
        btnSearch.pack(side=tk.RIGHT)

        # Lista para los checkboxes
        etiquetas = ["John",
                     "Contraseñas",
                     "Nikto",
                     "Host",
                     "Discreción",
                     "Avanzado",
                     "Nmap",
                     "Puertos",
                     "SO",
                     "Servicios",
                     "Hosts",
                     "HTTP",
                     "SQLMap",
                     "BBDD",
                     "SQLInjection"]

        counter = 0
        for i, etiqueta in enumerate(etiquetas):
            var = tk.IntVar()
            checkbox = tk.Checkbutton(contenedor_etiquetas, text=etiqueta,
                                      bg="#24B1BD", fg="black", font=("Poppins", 11),
                                      variable=var, onvalue=1, offvalue=0, anchor="w",
                                      command=lambda v=var: self.update_options(v))
            if (i < round(len(etiquetas) / 2)):
                checkbox.grid(row=i, column=0, padx=10, pady=5)
            else:
                checkbox.grid(row=counter, column=1, padx=10, pady=5)
                counter += 1
            self.selected_options.append((etiqueta, var))  # Agregar a la lista

        # boton (Ver Reportes)
        # configuracion de boton
        btnR = tk.Button(contenedor_opciones, text="Ver reportes",
                         relief="solid", bg="#B7BBD0", fg="black",
                         font=("Poppins", 11), border=0, command=self.ir_a_reportes)
        # ubicacion de boton
        btnR.place(relx=0.275, rely=0.875, anchor="n")

        # Boton (Abrir CLI)
        btnCLI = tk.Button(contenedor_opciones, text="Buscar etiquetas",
                           relief="solid", bg="#B7BBD0", fg="black",
                           font=("Poppins", 11), border=0, command=self.buscar_scripts)
        # ubicacion de boton
        btnCLI.place(relx=0.625, rely=0.875, anchor="n")

        # Boton (Volver a Login)
        btnRP = tk.Button(contenedor_opciones, text="Salir",
                          relief="solid", bg="#B7BBD0", fg="black",
                          font=("Poppins", 11), border=0, command=self.ir_a_inicio_sesion)
        # ubicacion de boton
        btnRP.place(relx=0.89, rely=0.875, anchor="n")

    def buscar_scripts(self):
        etiquetas_seleccionadas = [etiqueta for etiqueta,
                                   var in self.selected_options if var.get() == 1]
        scripts_filtrados = [
            script for script in self.scripts_info_original if set(script["tags"]).intersection(etiquetas_seleccionadas)
        ]
        self.crear_componente_scripts(scripts_filtrados)

    def buscar_scripts_por_nombre(self):
        nombre_a_buscar = self.entry_busqueda.get()
        scripts_filtrados = [
            script for script in self.scripts_info_original if nombre_a_buscar.lower() in script["name"].lower()
        ]
        self.crear_componente_scripts(scripts_filtrados)

    def crear_componente_scripts(self, scripts):
        for widget in self.frame_interior.winfo_children():
            widget.destroy()

        grupos = [scripts[i:i + 3]
                  for i in range(0, len(scripts), 3)]

        for grupo in grupos:
            marco_grupo = tk.Frame(self.frame_interior, bg='#191A1E')
            marco_grupo.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

            for script_info in grupo:
                nombre = script_info["name"]
                etiqueta = script_info["tags"]
                parametros = script_info["parameters"]
                n_parametros = len(parametros)
                descripcion = script_info["description"]

                datos = {
                    "token": self.token,
                    "user": self.credentials["uuid"],
                    "script": script_info["uuid"],
                    "nombre_script": nombre,
                    "parametros": parametros,
                    "descripcion_script": descripcion,
                    "ruta": script_info["source"]
                }

                nuevo_frame = tk.Frame(marco_grupo, bg='#26272B')
                nuevo_frame.pack(side=tk.LEFT, padx=5, pady=5,
                                 fill=tk.BOTH, expand=True)

                label_nombre = tk.Label(nuevo_frame,
                                        text=f"{nombre}",
                                        font=("Poppins", 12), bg='#26272B', fg="white",
                                        wraplength=150, width=20)
                label_nombre.pack(pady=(5, 0))

                label_etiqueta = tk.Label(nuevo_frame,
                                          text=f"| {" | ".join(etiqueta)} |",
                                          font=("Poppins", 10), bg='#26272B', fg="#B4BDE2",
                                          wraplength=150)
                label_etiqueta.pack()

                label_parametro = tk.Label(nuevo_frame,
                                           text=f"Parametros: {n_parametros}",
                                           font=("Poppins", 10), bg='#26272B', fg="#B4BDE2")
                label_parametro.pack()

                button = tk.Button(nuevo_frame, text=f"Ejecutar",
                                   relief="solid", bg="#B7BBD0", fg="black", font=("Poppins", 10), border=0,
                                   command=lambda datos=datos: self.abrir_parametros(datos=datos))
                button.pack(pady=(0, 10))

        self.cuadroCmdInterno.update_idletasks()
        self.cuadroCmdInterno.configure(
            scrollregion=self.cuadroCmdInterno.bbox("all"))

    # ...
    def abrir_parametros(self, datos):
        # Inicia la interfaz de Parametros y pasa el nombre del script
        parametros_window = Parametros(root=self.ventana, datos=datos)

    def ir_a_reportes(self):
        # Lógica para ir a la ventana de registro
        self.ventana.destroy()  # Cierra la ventana actual
        self.app.mostrar_menu()  # Muestra la ventana de registro en la ventana principal

    def ir_a_inicio_sesion(self):
        # Lógica para volver a la ventana de inicio de sesión
        self.ventana.destroy()  # Cierra la ventana actual
        self.app.show()  # Muestra la ventana de inicio de sesión en la ventana principal

    # Metodo para hacer desaparecer el subtexto del Entry de busqueda
    def on_entry_click(self, event):
        if self.entry_busqueda.get() == 'Filtro':
            self.entry_busqueda.delete(0, "end")
            self.entry_busqueda.config(fg='white')

    # Metodo para que aparezca la etiqueta de filtro en el Entry de busqueda
    def on_focus_out(self, event):
        if self.entry_busqueda.get() == '':
            self.entry_busqueda.insert(0, 'Filtro')
            self.entry_busqueda.config(fg='grey')

    def update_options(self, var):
        for option in self.selected_options:
            label, state = option  # Corregir desempaquetado
            if state == var.get():  # Revisar si el estado es igual al valor de la variable
                print(f"Opción seleccionada: {label if state == 1 else None}")
