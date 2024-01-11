import tkinter as tk
import subprocess
from Vistas.Parametros import Parametros

def create_panel_window(root, app, credentials):
    panel_window = tk.Toplevel(root)
    PanelWindow(panel_window, app, credentials)

class PanelWindow:

    def __init__(self, root, app, credentials):
        self.root = root
        self.app = app
        self.credentials = credentials
        root.title("Inicio de Sesión") #Titulo de la ventana
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

        self.TextField_Busqueda = None
        self.cuadroCmdInterno = None
        self.frame_interior = None
        self.selected_options = []  # Inicializar la lista aquí

        self.create_widgets() # Llamado de funcion para crear los widgets

    def create_widgets(self):
        #Frame (Consola)
        #Creacion y especificacion decolor
        cuadroCmd = tk.Frame(self.root, bg="#1E1F24")
        #Ubicacion del frame
        cuadroCmd.place(relx=0.65, rely=0.0, relwidth=0.7, relheight=1.0, anchor="n")

        #Label (Principal)
        #Texto del Label
        lblOverlook = tk.Label(cuadroCmd,text="OVERLOCK")
        #Color de la letra Label
        lblOverlook.config(fg = "#B4BDE2")
        #Color del label (transparente)
        lblOverlook.config(bg= "#1E1F24")
        #tipo de letra y tamaño de esta
        lblOverlook.config(font=("Lucida Console", 40))
        #Ubicacion del Label
        lblOverlook.place(relx=0.5, rely=0.05, anchor="n")

        cuadroCmd2 = tk.Frame(cuadroCmd, bg='#191A1E')
        cuadroCmd2.place(relx=0.5, rely=0.2, relwidth=0.85, relheight=0.7, anchor="n")

        scrollbar = tk.Scrollbar(cuadroCmd2, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.cuadroCmdInterno = tk.Canvas(cuadroCmd2, bg="#191A1E", yscrollcommand=scrollbar.set)
        self.cuadroCmdInterno.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.cuadroCmdInterno.yview)

        self.frame_interior = tk.Frame(self.cuadroCmdInterno, bg='#191A1E')  # Frame interno al Canvas
        self.cuadroCmdInterno.create_window((0, 0), window=self.frame_interior, anchor='nw')

        nombres_scripts = ["Script " + str(i) for i in range(1, 21)]  # Ejemplo con 20 scripts
        etiquetas_scripts = ["John The Ripper","John The Ripper","John The Ripper","John The Ripper","John The Ripper", 
                             "Nikto","Nikto","Nikto","Nikto","Nikto", "Nmap", "Nmap","Nmap","Nmap","Nmap", "SQLMap"
                             ,"SQLMap","SQLMap","SQLMap","SQLMap"] # Ejemplo con 20 scripts
        parametros_scripts = ["1","1","2","1","3","1","1","2","1","3","1","1","2","1","3","1","1","2","1","3"]  # Ejemplo con 20 parámetros
        #descripcion_Scripts = ["A1","B1","C2","D1","E3","F1","G1","H2","I1","J3","K1","L1","M2","N1","O3","P1","Q1","R2","S1","T3"]  # Ejemplo con 20 parámetros
        # Combinar los tres arreglos en una matriz
        scripts_info = [{"nombre": nombre, "etiqueta": etiqueta, "parametro": parametro} for nombre, etiqueta, parametro in zip(nombres_scripts, etiquetas_scripts * (len(nombres_scripts) // len(etiquetas_scripts)), parametros_scripts)]

        # Agregamos una variable para almacenar los scripts originales sin filtrar
        self.scripts_info_original = scripts_info.copy()

        grupos = [scripts_info[i:i + 3] for i in range(0, len(scripts_info), 3)]

        for grupo in grupos:
            marco_grupo = tk.Frame(self.frame_interior, bg='#191A1E')
            marco_grupo.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

            for script_info in grupo:
                nombre = script_info["nombre"]
                etiqueta = script_info["etiqueta"]
                parametro = script_info["parametro"]

                nuevo_frame = tk.Frame(marco_grupo, bg='#26272B')
                nuevo_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

                label_nombre = tk.Label(nuevo_frame, text=f"                  {nombre}                  ", font=("Poppins", 12), bg='#26272B', fg="white")
                label_nombre.pack()

                label_etiqueta = tk.Label(nuevo_frame, text=f"                  {etiqueta}                  ", font=("Poppins", 10), bg='#26272B', fg="#B4BDE2")
                label_etiqueta.pack()

                label_parametro = tk.Label(nuevo_frame, text=f"                  Parametros: {parametro}                  ", font=("Poppins", 10), bg='#26272B', fg="#B4BDE2")
                label_parametro.pack()

                button = tk.Button(nuevo_frame, text=f"Ejecutar {nombre}", relief="solid", bg="#B7BBD0", fg="black", font=("Poppins", 10), border=0, command=lambda n=nombre, p=parametro: self.abrir_parametros(n, p))
                button.pack()
        
        # Actualizar el área desplazable del Canvas después de agregar los elementos
        self.cuadroCmdInterno.update_idletasks()
        self.cuadroCmdInterno.configure(scrollregion=self.cuadroCmdInterno.bbox("all"))

        #Frame (Scripts)
        #Creacion y especificacion decolor
        cuadroTool = tk.Frame(self.root, bg="#1B1A20")
        #Ubicacion del frame
        cuadroTool.place(relx=0.14, rely=0.0, relwidth=0.35, relheight=1.0, anchor="n")

        #Label (titulo)
        #Texto del Label
        lblTools = tk.Label(cuadroTool,text="Scripts")
        #Color de la letra Label
        lblTools.config(fg = "#B7BBD0")
        #Color del label (transparente)
        lblTools.config(bg= "#1B1A20")
        #tipo de letra y tamaño de esta
        lblTools.config(font=("Lucida Console", 25))
        #Ubicacion del Label
        lblTools.place(relx=0.5, rely=0.05, anchor="n")

        #Frame (Consola)
        #Creacion y especificacion decolor
        cuadroEtiquetas = tk.Frame(cuadroTool, bg="#1E1F24")
        #Ubicacion del frame
        cuadroEtiquetas.place(relx=0.55, rely=0.15, relwidth=0.8, relheight=0.7, anchor="n")

        # TextField (Busqueda)
        self.TextField_Busqueda = tk.Entry(cuadroEtiquetas)
        self.TextField_Busqueda.config(bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=23)
        self.TextField_Busqueda.insert(0, 'Filtro')
        self.TextField_Busqueda.bind('<FocusIn>', self.on_entry_click)
        self.TextField_Busqueda.bind('<FocusOut>', self.on_focus_out)
        self.TextField_Busqueda.config(fg='grey')
        self.TextField_Busqueda.pack(anchor=("w"), padx=10, pady=17)
        self.TextField_Busqueda.pack()

        #boton (Buscar)
        #configuracion de boton
        btnSearch = tk.Button(cuadroEtiquetas, text="Buscar", relief="solid", bg="#B7BBD0", fg="black", font=("Poppins", 10),border=0, command=self.buscar_scripts_por_nombre)
        #ubicacion de boton
        btnSearch.place(relx=0.85, rely=0.025, anchor="n")

        # Lista para los checkboxes
        etiquetas = ["John The Ripper", "Nikto", "Nmap", "SQLMap"]

        for i, etiqueta in enumerate(etiquetas):
            var = tk.IntVar()
            chk = tk.Checkbutton(cuadroEtiquetas, text=etiqueta, bg="#24B1BD", fg="black", variable=var, onvalue=1, offvalue=0, font=("Poppins", 12), command=lambda v=var: self.update_options(v))
            chk.pack(anchor=tk.W, padx = 10, pady=5)
            self.selected_options.append((etiqueta, var))  # Agregar a la lista

        #boton (Ver Reportes)
        #configuracion de boton
        btnR = tk.Button(cuadroTool, text="Ver reportes", relief="solid", bg="#B7BBD0", fg="black", font=("Poppins", 12),border=0, command=self.ir_a_reportes)
        #ubicacion de boton
        btnR.place(relx=0.275, rely=0.875, anchor="n")

        #Boton (Abrir CLI)
        btnCLI = tk.Button(cuadroTool, text="Filtrar por etiqueta", relief="solid", bg="#B7BBD0", fg="black", font=("Poppins", 12),border=0, command=self.buscar_scripts)
        #ubicacion de boton
        btnCLI.place(relx=0.625, rely=0.875, anchor="n")

        #Boton (Volver a Login)
        btnRP = tk.Button(cuadroTool, text="Salir", relief="solid", bg="#B7BBD0", fg="black", font=("Poppins", 12),border=0, command=self.ir_a_inicio_sesion)
        #ubicacion de boton
        btnRP.place(relx=0.89, rely=0.875, anchor="n")

    def buscar_scripts(self):
        etiquetas_seleccionadas = [etiqueta for etiqueta, var in self.selected_options if var.get() == 1]
        scripts_filtrados = [script for script in self.scripts_info_original if script["etiqueta"] in etiquetas_seleccionadas]
        self.actualizar_scrollbar(scripts_filtrados)
    
    def buscar_scripts_por_nombre(self):
        nombre_a_buscar = self.TextField_Busqueda.get()
        scripts_filtrados = [script for script in self.scripts_info_original if nombre_a_buscar.lower() in script["nombre"].lower()]
        self.actualizar_scrollbar(scripts_filtrados)

    def actualizar_scrollbar(self, scripts_filtrados):
        for widget in self.frame_interior.winfo_children():
            widget.destroy()

        grupos_filtrados = [scripts_filtrados[i:i + 3] for i in range(0, len(scripts_filtrados), 3)]

        for grupo in grupos_filtrados:
            marco_grupo = tk.Frame(self.frame_interior, bg='#191A1E')
            marco_grupo.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

            for script_info in grupo:
                nombre = script_info["nombre"]
                etiqueta = script_info["etiqueta"]
                parametro = script_info["parametro"]

                nuevo_frame = tk.Frame(marco_grupo, bg='#26272B')
                nuevo_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

                label_nombre = tk.Label(nuevo_frame, text=f"                  {nombre}                  ", font=("Poppins", 12), bg='#26272B', fg="white")
                label_nombre.pack()

                label_etiqueta = tk.Label(nuevo_frame, text=f"                  {etiqueta}                  ", font=("Poppins", 10), bg='#26272B', fg="#B4BDE2")
                label_etiqueta.pack()

                label_parametro = tk.Label(nuevo_frame, text=f"                  Parametros: {parametro}                  ", font=("Poppins", 10), bg='#26272B', fg="#B4BDE2")
                label_parametro.pack()

                button = tk.Button(nuevo_frame, text=f"Ejecutar {nombre}", relief="solid", bg="#B7BBD0", fg="black", font=("Poppins", 10), border=0, command=lambda n=nombre, p=parametro: self.abrir_parametros(n, p))
                button.pack()

        self.cuadroCmdInterno.update_idletasks()
        self.cuadroCmdInterno.configure(scrollregion=self.cuadroCmdInterno.bbox("all"))
        
    # ...
    def abrir_parametros(self, nombre_script, parametros_scripts):
        # Crea una instancia de la clase Parametros y pasa el nombre del script
        parametros_window = Parametros(self.root, nombre_script, parametros_scripts)
        # Mostrar la ventana de parámetros
        parametros_window.ventana.deiconify()

    def ir_a_reportes(self):
        # Lógica para ir a la ventana de registro
        self.root.withdraw()  # Oculta la ventana actual
        self.app.mostrar_menu()  # Muestra la ventana de registro en la ventana principal

    def ir_a_inicio_sesion(self):
        # Lógica para volver a la ventana de inicio de sesión
        self.root.withdraw()  # Oculta la ventana actual
        self.app.show()  # Muestra la ventana de inicio de sesión en la ventana principal

    #Metodo para hacer desaparecer el subtexto del Entry de busqueda
    def on_entry_click(self, event):
        if self.TextField_Busqueda.get() == 'Filtro':
            self.TextField_Busqueda.delete(0, "end")
            self.TextField_Busqueda.config(fg='white')

    #Metodo para que aparezca la etiqueta de filtro en el Entry de busqueda
    def on_focus_out(self, event):
        if self.TextField_Busqueda.get() == '':
            self.TextField_Busqueda.insert(0, 'Filtro')
            self.TextField_Busqueda.config(fg='grey')
    
    def update_options(self, var):
        for option in self.selected_options:
            label, state = option  # Corregir desempaquetado
            if state == var.get():  # Revisar si el estado es igual al valor de la variable
                print(f"Opción seleccionada: {label if state == 1 else None}")

if __name__ == "__main__":
    ventana_registro = tk.Toplevel()
    ventana_registro.withdraw()
    ventana_registro.mainloop()
