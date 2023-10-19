import tkinter as tk

def create_signin_window(root, app):
    signin_window = tk.Toplevel(root)
    SigninWindow(signin_window, app)

class SigninWindow:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.title("Registro")
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
