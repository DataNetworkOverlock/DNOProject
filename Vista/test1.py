import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
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

        self.create_widgets() # Llamado de funcion para crear los widgets

    def create_widgets(self):
        label = tk.Label(self.root, text="¡Bienvenido!")
        label.pack(pady=10)

        boton_registro = tk.Button(self.root, text="Registrarse", command=self.mostrar_ventana_registro)
        boton_registro.pack(pady=5)

        boton_menu = tk.Button(self.root, text="Abrir Menú", command=self.mostrar_menu)
        boton_menu.pack(pady=5)

    def mostrar_ventana_registro(self):
        self.hide()
        from test2 import create_signin_window
        create_signin_window(self.root, self)

    def mostrar_menu(self):
        self.hide()
        from test3 import create_menu_window
        create_menu_window(self.root, self)

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.deiconify()

if __name__ == "__main__":
    ventana_login = tk.Tk()
    app = App(ventana_login)
    ventana_login.mainloop()
