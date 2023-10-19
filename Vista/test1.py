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
        '''
        label = tk.Label(self.root, text="¡Bienvenido!")
        label.pack(pady=10)

        boton_registro = tk.Button(self.root, text="Registrarse", command=self.mostrar_ventana_registro)
        boton_registro.pack(pady=5)

        boton_menu = tk.Button(self.root, text="Abrir Menú", command=self.mostrar_menu)
        boton_menu.pack(pady=5)
        '''
        #----

        #Label (titulo)
        #Texto del Label
        lbl =tk.Label(self.root,text="LOGIN")
        #Color de la letra Label
        lbl.config(fg = "#B7BBD0")
        #Color del label (transparente)
        lbl.config(bg= "#1B1A20")
        #tipo de letra y tamaño de esta
        lbl.config(font=("Arial", 40))
        #Ubicacion del Label
        lbl.place(relx=0.5, rely=0.05, anchor="n")


        #Frame (cuadro)
        #Creacion y especificacion decolor
        cuadro = tk.Frame(self.root, bg="#26272B")
        #Ubicacion del frame
        cuadro.place(relx=0.5, rely=0.2, relwidth=0.6, relheight=0.6, anchor="n")

        #Label (Nombre de usuario)
        #Texto del Label
        lblNU = tk.Label(cuadro, text="Nombre de usuario")
        #Color de la letra Label
        lblNU.config(fg = "#B4BDE2")
        #Color del label (transparente)
        lblNU.config(bg= "#26272B")
        #tipo de letra y tamaño de esta
        lblNU.config(font=("Arial", 15))
        #Ubicacion
        lblNU.pack(anchor=("w"), padx=50, pady=(100,10))
        lblNU.pack()

        # TextField (Nombre de usuario)
        TextField_UserName = tk.Entry(cuadro)
        #Configuracion de text fielg
        TextField_UserName.config(bg="#0D4044", font=("Arial", 12), width=100, fg="white")
        #Ubicacion
        TextField_UserName.pack(anchor=("w"), padx=55, pady=5)
        TextField_UserName.pack()

        #Label (contraseña)
        #Texto del Label
        lblPass = tk.Label(cuadro, text="Contraseña")
        #Color de la letra Label
        lblPass.config(fg = "#B4BDE2")
        #Color del label (transparente)
        lblPass.config(bg= "#26272B")
        #tipo de letra y tamaño de esta
        lblPass.config(font=("Arial", 15))
        #Ubicacion
        lblPass.pack(anchor=("w"), padx=50, pady=(50,10))
        lblPass.pack()

        # TextField(Password)
        TextField_Pass = tk.Entry(cuadro)
        #Configuracion de text fielg
        TextField_Pass.config(bg="#0D4044", font=("Arial", 12), width=100, fg="white")
        #Ubicacion
        TextField_Pass.pack(anchor=("w"), padx=55, pady=5)
        TextField_Pass.pack()

        # Botton acceder a panel
        btn_acceder = tk.Button(cuadro, text="Acceder", relief="sunken", bg="#0E0D13", fg="#ADB2D6", font=("Arial", 14), command=self.mostrar_menu)
        btn_acceder.pack(anchor=("e"), padx=55, pady=50)
        btn_acceder.pack()

        #boton (registrarse)
        #configuracion de boton
        btnR = tk.Button(self.root, text="Registrarse", relief="flat", bg="#1B1A20", fg="#B4BADE", font=("Arial", 14), command = self.mostrar_ventana_registro)
        #ubicacion de boton
        btnR.place(relx=0.245, rely=0.825, anchor="n")

        #Boton (recordar contraseña)
        btnRP = tk.Button(self.root, text="¿Olvidaste tu contraseña?", relief="flat", bg="#1B1A20", fg="#B4BADE", font=("Arial", 14))
        #ubicacion de boton
        btnRP.place(relx=0.4, rely=0.825, anchor="n")

        #----

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
