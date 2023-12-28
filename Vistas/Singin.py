import tkinter as tk
from tkinter import messagebox

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
        #Label (titulo)
        #Texto del Label
        lbl = tk.Label(self.root,text="REGISTRO")
        #Color de la letra Label
        lbl.config(fg = "#B7BBD0")
        #Color del label (transparente)
        lbl.config(bg= "#1B1A20")
        #tipo de letra y tamaño de esta
        lbl.config(font=("Lucida Console", 40))
        #Ubicacion del Label
        lbl.place(relx=0.5, rely=0.05, anchor="n")

        #Frame (cuadro)
        #Creacion y especificacion decolor
        cuadro = tk.Frame(self.root, bg="#26272B")
        #Ubicacion del frame
        cuadro.place(relx=0.5, rely=0.15, relwidth=0.6, relheight=0.7, anchor="n")

        #Label (Nombre completo)
        #Texto del Label
        lblNU = tk.Label(cuadro, text="Nombre completo")
        #Color de la letra Label
        lblNU.config(fg = "#B4BDE2")
        #Color del label (transparente)
        lblNU.config(bg= "#26272B")
        #tipo de letra y tamaño de esta
        lblNU.config(font=("Poppins", 14))
        #Ubicacion
        lblNU.pack(anchor=("w"), padx=50, pady=(5,2))
        lblNU.pack()

        # TextField (Nombre de usuario)
        TextField_User = tk.Entry(cuadro)
        #Configuracion de text fielg
        TextField_User.config(bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=100, fg="white")
        #Ubicacion
        TextField_User.pack(anchor=("w"), padx=55, pady=0)
        TextField_User.pack()

        #Label (Nombre de usuario)
        #Texto del Label
        lblNU = tk.Label(cuadro, text="Nombre de usuario *")
        #Color de la letra Label
        lblNU.config(fg = "#B4BDE2")
        #Color del label (transparente)
        lblNU.config(bg= "#26272B")
        #tipo de letra y tamaño de esta
        lblNU.config(font=("Poppins", 14))
        #Ubicacion
        lblNU.pack(anchor=("w"), padx=50, pady=(5,2))
        lblNU.pack()

        # TextField (Nombre de usuario)
        self.TextField_UserName = tk.Entry(cuadro)
        #Configuracion de text fielg
        self.TextField_UserName.config(bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=100, fg="white")
        #Ubicacion
        self.TextField_UserName.pack(anchor=("w"), padx=55, pady=0)
        self.TextField_UserName.pack()

        #Label (contraseña)
        #Texto del Label
        lblPass = tk.Label(cuadro, text="Contraseña *")
        #Color de la letra Label
        lblPass.config(fg = "#B4BDE2")
        #Color del label (transparente)
        lblPass.config(bg= "#26272B")
        #tipo de letra y tamaño de esta
        lblPass.config(font=("Poppins", 14))
        #Ubicacion
        lblPass.pack(anchor=("w"), padx=50, pady=(5,2))
        lblPass.pack()

        # TextField(Password)
        self.TextField_Pass = tk.Entry(cuadro)
        #Configuracion de text fielg
        self.TextField_Pass.config(bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=100, fg="white")
        #Ubicacion
        self.TextField_Pass.pack(anchor=("w"), padx=55, pady=0)
        self.TextField_Pass.pack()

        #Label (confirmar contraseña)
        #Texto del Label
        lblPass2 = tk.Label(cuadro, text="Confirmar Contraseña *")
        #Color de la letra Label
        lblPass2.config(fg = "#B4BDE2")
        #Color del label (transparente)
        lblPass2.config(bg= "#26272B")
        #tipo de letra y tamaño de esta
        lblPass2.config(font=("Poppins", 14))
        #Ubicacion
        lblPass2.pack(anchor=("w"), padx=50, pady=(5,2))
        lblPass2.pack()

        # TextField(confirmar Password)
        self.TextField_Pass2 = tk.Entry(cuadro)
        #Configuracion de text fielg
        self.TextField_Pass2.config(bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=100, fg="white")
        #Ubicacion
        self.TextField_Pass2.pack(anchor=("w"), padx=55, pady=0)
        self.TextField_Pass2.pack()

        #Label (Pregunta)
        #Texto del Label
        lblQ = tk.Label(cuadro, text="pregunta de seguridad *")
        #Color de la letra Label
        lblQ.config(fg = "#B4BDE2")
        #Color del label (transparente)
        lblQ.config(bg= "#26272B")
        #tipo de letra y tamaño de esta
        lblQ.config(font=("Poppins", 14))
        #Ubicacion
        lblQ.pack(anchor=("w"), padx=50, pady=(5,2))
        lblQ.pack()

        # TextField(Pregunta)
        self.TextField_Ask = tk.Entry(cuadro)
        #Configuracion de text fielg
        self.TextField_Ask.config(bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=100, fg="white")
        #Ubicacion
        self.TextField_Ask.pack(anchor=("w"), padx=55, pady=0)
        self.TextField_Ask.pack()

        #Label (respuesta)
        #Texto del Label
        lblAnsw = tk.Label(cuadro, text="respuesta de pregunta de confirmacion *")
        #Color de la letra Label
        lblAnsw.config(fg = "#B4BDE2")
        #Color del label (transparente)
        lblAnsw.config(bg= "#26272B")
        #tipo de letra y tamaño de esta
        lblAnsw.config(font=("Poppins", 14))
        #Ubicacion
        lblAnsw.pack(anchor=("w"), padx=50, pady=(5,2))
        lblAnsw.pack()

        # TextField(respuesta)
        self.TextField_Answ = tk.Entry(cuadro)
        #Configuracion de text fielg
        self.TextField_Answ.config(bg="#0D4044", font=("Poppins", 12), relief="solid", border=0, width=100, fg="white")
        #Ubicacion
        self.TextField_Answ.pack(anchor=("w"), padx=55, pady=0)
        self.TextField_Answ.pack()

        # Botton (registrar)
        btn_acceder = tk.Button(self.root, text="Registrar", relief="solid", bg="#B7BBD0", fg="black", font=("Poppins", 14),border=0, command=self.registrar_usuario)
        btn_acceder.place(relx=0.7575, rely=0.875, anchor="n")

        #boton (Cancelar)
        #configuracion de boton
        btnCancel = tk.Button(self.root, text="Cancelar", relief="flat", bg="#1B1A20", fg="#B4BADE", font=("Poppins", 14, "italic"), command=self.volver_al_inicio)
        #ubicacion de boton
        btnCancel.place(relx=0.245, rely=0.875, anchor="n")

    def registrar_usuario(self):
        # Lógica de registro de usuario
        contador_registro = 0

        if not self.TextField_UserName.get() or not self.TextField_Pass.get() or not self.TextField_Pass2.get() or not self.TextField_Ask.get(): # Verifica si los campos estan vacío
             messagebox.showinfo("Error", "Debe de llenar todos los campos")
        else:

            #Condicion de nombre de usuario
            Usuarios_Existentes = ["u1", "u2", "u3", "u4"]
            if self.TextField_UserName.get() in [usuario.lower() for usuario in Usuarios_Existentes]:
                self.TextField_UserName.config(fg="red")
                messagebox.showinfo("Error", "El nombre de usuario ya existe en la base de datos, elija uno diferente")
                contador_registro = 0
            else:
                self.TextField_UserName.config(fg="green")
                contador_registro += 1

            #Condicion de seguridad de contraseña
            if len(self.TextField_Pass.get()) <= 10:
                self.TextField_Pass.config(fg="red")
                messagebox.showinfo("Error", "Contraseña insegura")
                contador_registro = 0
            else:
                self.TextField_Pass.config(fg="green")
                contador_registro += 1

            #Condicion de confirmacion de contraseñas
            if self.TextField_Pass.get() == self.TextField_Pass2.get():
                self.TextField_Pass2.config(fg="green")
                contador_registro += 1
            else:
                messagebox.showinfo("Error", "La confirmacion de contraseña fallo")
                self.TextField_Pass2.config(fg="red")
                self.TextField_Pass2.delete(0, tk.END)
                contador_registro = 0

            #condicion de pregunta de seguridad
            if not self.TextField_Answ.get(): # Verifica si el campo de respuesta está vacío
                messagebox.showinfo("Error", "El campo de respuesta está vacío.")
            else:
                if self.TextField_Answ.get().lower() == "si" or self.TextField_Answ.get().lower() == "no":
                    messagebox.showinfo("Error", "La pregunta no puede ser respondida con un 'Si' o 'No'.")
                    self.TextField_Answ.config(fg="red")
                    contador_registro = 0
                else:
                    if len(self.TextField_Answ.get()) <= 6:
                        messagebox.showinfo("Error", "La respuesta es demaciado corta.")
                        self.TextField_Answ.config(fg="red")
                        contador_registro = 0
                    else:
                        self.TextField_Answ.config(fg="green")
                        contador_registro += 1
        
        if contador_registro <= 3:
            messagebox.showinfo("Error", "Fallo en el registro")
        else:
            messagebox.showinfo("Exitoso", "Registro exitoso\n" + f"usuario: {self.TextField_UserName.get()}" + " sera redirigido al login")
            self.TextField_UserName.delete(0, tk.END)
            self.TextField_Pass.delete(0, tk.END)
            self.TextField_Pass2.delete(0, tk.END)
            self.TextField_Ask.delete(0, tk.END)
            self.TextField_Answ.delete(0, tk.END)
            self.volver_al_inicio()
    def volver_al_inicio(self):
        self.root.withdraw()
        self.app.show()

if __name__ == "__main__":
    ventana_registro = tk.Toplevel()
    ventana_registro.withdraw()
    ventana_registro.mainloop()
