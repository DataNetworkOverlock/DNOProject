import tkinter as tk

def create_menu_window(root, app):
    menu_window = tk.Toplevel(root)
    MenuWindow(menu_window, app)

class MenuWindow:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        root.title("menu") #Titulo de la ventana
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
        label_menu = tk.Label(self.root, text="Menu")
        label_menu.pack(pady=10)

        boton_ir_registro = tk.Button(self.root, text="Registrarme", command=self.ir_a_registro)
        boton_ir_registro.pack(pady=5)

        boton_ir_Login = tk.Button(self.root, text="Volver al inicio de sesión",  command=self.ir_a_inicio_sesion)
        boton_ir_Login.pack()
    
    def ir_a_registro(self):
        # Lógica para ir a la ventana de registro
        self.root.withdraw()  # Oculta la ventana actual
        self.app.mostrar_ventana_registro()  # Muestra la ventana de registro en la ventana principal

    def ir_a_inicio_sesion(self):
        # Lógica para volver a la ventana de inicio de sesión
        self.root.withdraw()  # Oculta la ventana actual
        self.app.show()  # Muestra la ventana de inicio de sesión en la ventana principal

if __name__ == "__main__":
    ventana_registro = tk.Toplevel()
    ventana_registro.withdraw()
    ventana_registro.mainloop()

    