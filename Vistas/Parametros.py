import tkinter as tk


class Parametros:
    def __init__(self, root, nombre, n_parametros, descripcion):
        # Inicialización de la clase
        self.root = root
        self.nombre = nombre
        self.n_parametros = n_parametros
        self.descripcion = descripcion
        self.cuadro = None
        self.create_widgets()

    def create_widgets(self):
        # Configuración de la ventana de parámetros
        self.ventana = tk.Toplevel(self.root)
        self.ventana.title(f"Parámetros - {self.nombre}")
        self.ventana.geometry("800x550")
        self.ventana.configure(bg="#1B1A20")
        self.ventana.resizable(False, False)
        self.centrar_ventana()

        # Título de la ventana
        lbl = tk.Label(self.ventana, text="Parámetros")
        lbl.config(fg="#B7BBD0", bg="#1B1A20", font=("Lucida Console", 40))
        lbl.place(relx=0.5, rely=0.05, anchor="n")

        # Frame Descripcion
        cuadro_descripcion = tk.Frame(self.ventana, bg="#26272B")
        cuadro_descripcion.place(
            relx=0.15, rely=0.2, relwidth=0.26, relheight=0.65, anchor="n")

        # Etiqueta y entrada para el titulo de descripcion
        lblDescrp = tk.Label(cuadro_descripcion, text="Descripción")
        lblDescrp.config(fg="#B4BDE2", bg="#26272B", font=("Poppins", 18))
        lblDescrp.pack(anchor="n", pady=10)

        # Etiqueta y entrada para el Contenido de la descripcion
        lblDescrp = tk.Label(cuadro_descripcion,
                             text=self.descripcion)
        lblDescrp.config(fg="#B4BDE2", bg="#26272B",
                         wraplength=200, font=("Poppins", 11))
        lblDescrp.pack(anchor="w", padx=15, pady=(0, 10))

        # Frame principal
        self.cuadro = tk.Frame(self.ventana, bg="#26272B")
        self.cuadro.place(relx=0.65, rely=0.2, relwidth=0.65,
                     relheight=0.65, anchor="n")

        for i in range(1, self.n_parametros + 1):
            self.mostrar_campos(numero=i)
        
        # Botón para ejecutar el script
        btn_acceder = tk.Button(self.ventana, text="Ejecutar Script", relief="solid",
                                bg="#B7BBD0", fg="black", font=("Poppins", 12), border=0)
        btn_acceder.place(relx=0.9, rely=0.875, anchor="n")

    def centrar_ventana(self):
        # Función para centrar la ventana
        self.ventana.update_idletasks()
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() - ancho) // 2
        y = (self.ventana.winfo_screenheight() - alto) // 2
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    
    def mostrar_campos(self, numero):
        label_param = tk.Label(self.cuadro, text=f"Parámetro número {numero}")
        label_param.config(fg="#B4BDE2", bg="#26272B",
                     font=("Poppins", 12))
        label_param.pack(anchor="w", padx=40, pady=(15, 5))

        field_param = tk.Entry(self.cuadro, bg="#0D4044",
                                font=("Poppins", 12), relief="solid",
                                border=0, width=150, fg="white")
        field_param.pack(anchor="w", padx=40)
