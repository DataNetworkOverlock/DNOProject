import tkinter as tk

def create_signin_window(root, app):
    signin_window = tk.Toplevel(root)
    SigninWindow(signin_window, app)

class SigninWindow:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        root.title("Registro") #Titulo de la ventana
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
        self.create_widgets()

    def create_widgets(self):
        label_registro = tk.Label(self.root, text="Regístrate")
        label_registro.pack(pady=10)

        boton_registrar = tk.Button(self.root, text="Registrar", command=self.registrar_usuario)
        boton_registrar.pack(pady=5)

        boton_volver = tk.Button(self.root, text="Volver al inicio de sesión", command=self.volver_al_inicio)
        boton_volver.pack()

    def registrar_usuario(self):
        # Lógica de registro de usuario
        print("Usuario registrado")

    def volver_al_inicio(self):
        self.root.withdraw()
        self.app.show()

if __name__ == "__main__":
    ventana_registro = tk.Toplevel()
    ventana_registro.withdraw()
    ventana_registro.mainloop()
