import tkinter as tk
from tkinter import messagebox
from utils.usuarios import Usuarios
from Vistas.Panel import create_panel_window
from Vistas.Reportes import create_menu_window
from Vistas.Singin import create_signin_window


class App:
    def __init__(self, root):
        self.root = root
        root.title("Inicio de Sesión")  # Titulo de la ventana
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

        self.TextField_UserName = None
        self.TextField_Pass = None

        self.users = Usuarios()

        self.create_widgets()  # Llamado de funcion para crear los widgets

    def create_widgets(self):
        # Label (titulo)
        # Texto del Label
        lbl = tk.Label(self.root, text="LOGIN")
        # Color de la letra Label
        lbl.config(fg="#B7BBD0")
        # Color del label (transparente)
        lbl.config(bg="#1B1A20")
        # tipo de letra y tamaño de esta
        lbl.config(font=("Lucida Console", 40))
        # Ubicacion del Label
        lbl.place(relx=0.5, rely=0.05, anchor="n")

        # Frame (cuadro)
        # Creacion y especificacion decolor
        cuadro = tk.Frame(self.root, bg="#26272B")
        # Ubicacion del frame
        cuadro.place(relx=0.5, rely=0.2, relwidth=0.6,
                     relheight=0.6, anchor="n")

        # Label (Nombre de usuario)
        # Texto del Label
        lblNU = tk.Label(cuadro, text="Nombre de usuario")
        # Color de la letra Label
        lblNU.config(fg="#B4BDE2")
        # Color del label (transparente)
        lblNU.config(bg="#26272B")
        # tipo de letra y tamaño de esta
        lblNU.config(font=("Poppins", 14))
        # Ubicacion
        lblNU.pack(anchor=("w"), padx=50, pady=(60, 10))
        lblNU.pack()

        # TextField (Nombre de usuario)
        self.TextField_UserName = tk.Entry(cuadro)
        # Configuracion de text fielg
        self.TextField_UserName.config(bg="#0D4044", font=(
            "Poppins", 12), relief="solid", border=0, width=100, fg="white")
        # Ubicacion
        self.TextField_UserName.pack(anchor=("w"), padx=55, pady=5)
        self.TextField_UserName.pack()

        # Label (contraseña)
        # Texto del Label
        lblPass = tk.Label(cuadro, text="Contraseña")
        # Color de la letra Label
        lblPass.config(fg="#B4BDE2")
        # Color del label (transparente)
        lblPass.config(bg="#26272B")
        # tipo de letra y tamaño de esta
        lblPass.config(font=("Poppins", 14))
        # Ubicacion
        lblPass.pack(anchor=("w"), padx=50, pady=(50, 10))
        lblPass.pack()

        # TextField(Password)
        self.TextField_Pass = tk.Entry(cuadro)
        # Configuracion de text fielg
        self.TextField_Pass.config(bg="#0D4044", font=(
            "Poppins", 12), relief="solid", border=0, width=100, fg="white")
        # Ubicacion
        self.TextField_Pass.pack(anchor=("w"), padx=55, pady=5)
        self.TextField_Pass.pack()

        # Botton acceder a panel
        btn_acceder = tk.Button(cuadro, text="Iniciar sesión", relief="solid", bg="#B7BBD0", fg="black", font=(
            "Poppins", 14), border=0, command=self.mostrar_panel)
        btn_acceder.pack(anchor=("e"), padx=55, pady=50)
        btn_acceder.pack()

        # boton (registrarse)
        # configuracion de boton
        btnR = tk.Button(self.root, text="Registrarse", relief="flat", bg="#1B1A20", fg="#B4BADE", font=(
            "Poppins", 14, "italic"), command=self.mostrar_ventana_registro)
        # ubicacion de boton
        btnR.place(relx=0.245, rely=0.825, anchor="n")

        # Boton (recordar contraseña)
        btnRP = tk.Button(self.root, text="¿Olvidaste tu contraseña?", relief="flat",
                          bg="#1B1A20", fg="#B4BADE", font=("Poppins", 14, "italic"))
        # ubicacion de boton
        btnRP.place(relx=0.425, rely=0.825, anchor="n")

    # Funcion para abrir ventana Singin.py
    def mostrar_ventana_registro(self):
        self.hide()
        create_signin_window(self.root, self)

    # Funcion para abrir ventana Panel.py
    def mostrar_panel(self):

        # Verificar si los valores ingresados coinciden con los correctos
        username = self.TextField_UserName.get()
        password = self.TextField_Pass.get()

        if not username or not password:
            messagebox.showinfo("Error", "Debe llenar todos los campos")

        payload = {
            "username": username,
            "password": password
        }

        login = self.users.login(payload)
        login_status = login["status"]

        if login_status != 200:
            message = f"Error {login_status}. {
                str(login["response"]["message"])}"
            messagebox.showinfo("Error", message)
        else:
            self.credentials = login["response"]
            self.hide()
            create_panel_window(self.root, self, self.credentials)

        # Limpiar los campos después de intentar iniciar sesión
        self.TextField_UserName.delete(0, tk.END)
        self.TextField_Pass.delete(0, tk.END)

    def mostrar_panel2(self):
        self.hide()
        create_panel_window(self.root, self, self.credentials)

    # Función para abrir ventana Reportes.py
    def mostrar_menu(self):
        self.hide()
        create_menu_window(self.root, self, self.credentials)

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.deiconify()
