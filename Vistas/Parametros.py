import tkinter as tk

class Parametros:
    def __init__(self, root, nombre_script, parametros_scripts):
        # Inicialización de la clase
        self.root = root
        self.nombre_script = nombre_script
        self.parametros_scripts = parametros_scripts
        self.create_widgets()

    def create_widgets(self):
        # Configuración de la ventana de parámetros
        self.ventana = tk.Toplevel(self.root)
        self.ventana.title(f"Parámetros - {self.nombre_script}")
        self.ventana.geometry("1050x550")
        self.ventana.configure(bg="#1B1A20")
        self.ventana.resizable(False, False)
        self.centrar_ventana()

        # Título de la ventana
        lbl = tk.Label(self.ventana, text="Parametros")
        lbl.config(fg="#B7BBD0", bg="#1B1A20", font=("Lucida Console", 40))
        lbl.place(relx=0.5, rely=0.05, anchor="n")

        # Frame Descripcion
        cuadro_Descripcion = tk.Frame(self.ventana, bg="#26272B")
        cuadro_Descripcion.place(relx=0.15, rely=0.2, relwidth=0.25, relheight=0.65, anchor="n")

        # Etiqueta y entrada para el titulo de descripcion
        lblDescrp = tk.Label(cuadro_Descripcion, text="Descripcion")
        lblDescrp.config(fg="#B4BDE2", bg="#26272B", font=("Poppins", 10))
        lblDescrp.pack(anchor="w", padx=25, pady=(5, 10))

        # Etiqueta y entrada para el Contenido de la descripcion
        lblDescrp = tk.Label(cuadro_Descripcion, text=f"Descripcion: {self.parametros_scripts}")
        lblDescrp.config(fg="#B4BDE2", bg="#26272B", font=("Poppins", 14))
        lblDescrp.pack(anchor="w", padx=25, pady=(5, 10))

        # Frame principal
        cuadro = tk.Frame(self.ventana, bg="#26272B")
        cuadro.place(relx=0.61, rely=0.2, relwidth=0.6, relheight=0.65, anchor="n")

        # Etiqueta y entrada para el primer parámetro
        lblP1 = tk.Label(cuadro, text="Primer parametro")
        lblP1.config(fg="#B4BDE2", bg="#26272B", font=("Poppins", 14))
        lblP1.pack(anchor="w", padx=40, pady=(25, 10))

        TextField_P1 = tk.Entry(cuadro, bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=150, fg="white")
        TextField_P1.pack(anchor="w", padx=40, pady=3)

        # Etiqueta y entrada para el segundo parámetro
        lblP2 = tk.Label(cuadro, text="Segundo parametro")
        lblP2.config(fg="#B4BDE2", bg="#26272B", font=("Poppins", 14))
        lblP2.pack(anchor="w", padx=40, pady=(10))

        TextField_P2 = tk.Entry(cuadro, bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=150, fg="white")
        TextField_P2.pack(anchor="w", padx=40, pady=3)

        # Etiqueta y entrada para el tercer parámetro
        lblP3 = tk.Label(cuadro, text="Tercer parametro")
        lblP3.config(fg="#B4BDE2", bg="#26272B", font=("Poppins", 14))
        lblP3.pack(anchor="w", padx=40, pady=(10))

        TextField_P3 = tk.Entry(cuadro, bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=150, fg="white")
        TextField_P3.pack(anchor="w", padx=40, pady=3)

        bloqueo = int(self.parametros_scripts)

        if bloqueo == 1:
            TextField_P2.config(state='readonly', bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=150, fg="white")
            TextField_P3.config(state='readonly', bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=150, fg="white")

        if bloqueo == 2:
            TextField_P3.config(state='readonly', bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=150, fg="white")

        # Botón para ejecutar el script
        btn_acceder = tk.Button(self.ventana, text="Ejecutar Script", relief="solid", bg="#B7BBD0", fg="black", font=("Poppins", 14), border=0)
        btn_acceder.place(relx=0.83, rely=0.875, anchor="n")

    def centrar_ventana(self):
        # Función para centrar la ventana
        self.ventana.update_idletasks()
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() - ancho) // 2
        y = (self.ventana.winfo_screenheight() - alto) // 2
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Para probar el módulo por separado
if __name__ == "__main__":
    ventana_parametros = tk.Tk()
    parametros = Parametros(ventana_parametros, "Script1")  # Debes proporcionar el nombre del script
    ventana_parametros.mainloop()
