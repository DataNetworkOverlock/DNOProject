import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        root.title("Inicio de Sesión")
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self.root, text="¡Bienvenido!")
        label.pack(pady=10)

        boton_registro = tk.Button(self.root, text="Registrarse", command=self.mostrar_ventana_registro)
        boton_registro.pack(pady=5)

    def mostrar_ventana_registro(self):
        self.hide()
        from test2 import create_signin_window
        create_signin_window(self.root, self)

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.deiconify()

if __name__ == "__main__":
    ventana_login = tk.Tk()
    app = App(ventana_login)
    ventana_login.mainloop()
