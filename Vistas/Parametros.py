import tkinter as tk
import datetime
from utils.execute_command import ExecCommand
from utils.tests import Tests


class Parametros:
    def __init__(self, root, datos):
        # Inicialización de la clase
        self.root = root
        self.token = datos["token"]
        self.user = datos["user"]
        self.script = datos["script"]
        self.nombre_script = datos["nombre_script"]
        self.parametros = datos["parametros"]
        self.descripcion_script = datos["descripcion_script"]
        self.ruta = datos["ruta"]
        self.cuadro = None
        self.param_fields = {}

        self.test = Tests(self.token)
        self.comando = ExecCommand()

        self.create_widgets()

    def create_widgets(self):
        # Configuración de la ventana de parámetros
        self.ventana = tk.Toplevel(self.root)
        self.ventana.title(f"Parámetros - {self.nombre_script}")
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
                             text=self.descripcion_script)
        lblDescrp.config(fg="#B4BDE2", bg="#26272B",
                         wraplength=200, font=("Poppins", 11))
        lblDescrp.pack(anchor="w", padx=10, pady=(0, 10))

        # Frame principal
        self.cuadro = tk.Frame(self.ventana, bg="#26272B")
        self.cuadro.place(relx=0.65, rely=0.2, relwidth=0.65,
                          relheight=0.65, anchor="n")

        for parametro in self.parametros:
            self.mostrar_campos(parametro=parametro)

        # Botón para ejecutar el script
        btn_ejecutar = tk.Button(self.ventana, text="Ejecutar Script", relief="solid",
                                 bg="#B7BBD0", fg="black", font=("Poppins", 12), border=0,
                                 command=lambda: self.ejecutar_script())
        btn_ejecutar.place(relx=0.9, rely=0.875, anchor="n")

    def centrar_ventana(self):
        # Función para centrar la ventana
        self.ventana.update_idletasks()
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() - ancho) // 2
        y = (self.ventana.winfo_screenheight() - alto) // 2
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def mostrar_campos(self, parametro):
        label_param = tk.Label(self.cuadro, text=parametro)
        label_param.config(fg="#B4BDE2", bg="#26272B",
                           font=("Poppins", 12))
        label_param.pack(anchor="w", padx=40, pady=(15, 5))

        field_param = tk.Entry(self.cuadro, bg="#0D4044",
                               font=("Poppins", 12), relief="solid",
                               border=0, width=150, fg="white")
        field_param.pack(anchor="w", padx=40)
        self.param_fields[parametro] = field_param

    def ejecutar_script(self):
        payload = {
            "token": self.token,
            "user": self.user,
            "script": self.script,
            "nombre_script": self.nombre_script,
            "source": self.ruta,
            "parameters": {}
        }

        tests = []

        for param, value in self.param_fields.items():
            payload["parameters"][param] = value.get()

        if not self.nombre_script in tests and len(tests) < 4:
            tests.append(self.nombre_script)
            test_result = self.comando.exec(payload.copy())
            print("\nResultado: \n", test_result)
            payload["report"] = test_result
            # payload["report"] = "este es el reporte"
            self.crear_test(data=payload)
        else:
            print("No tengo tiempo para poner un error")

        self.cerrar_ventana()

    def crear_test(self, data):
        payload = {
            "ip": list(data["parameters"].values())[0],
            "date": str(datetime.datetime.now()),
            "report": data["report"],
            "user": data["user"],
            "script": data["script"]
        }
        self.test.create_test(payload)

    def cerrar_ventana(self):
        self.ventana.destroy()
