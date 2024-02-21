import tkinter as tk
from tkinter import messagebox
from utils.usuarios import Usuarios


class SigninWindow:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        self.ventana = tk.Toplevel(self.root)
        self.ventana.title("Registro")  # Titulo de la ventana
        self.ventana.geometry("1200x720")  # Tamaño de la ventana
        # Cambiar el color de fondo a un color hexadecimal
        self.ventana.configure(bg="#1B1A20")
        # Impedir que la ventana sea redimensionada
        self.ventana.resizable(False, False)
        # Centrar la ventana
        self.ventana.update_idletasks()
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() - ancho) // 2
        y = (self.ventana.winfo_screenheight() - alto) // 2
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.ventana.protocol("WM_DELETE_WINDOW", self.app.close)

        self.usuarios = Usuarios()

        self.create_widgets()

    def create_widgets(self):
        # Label (titulo)
        # Texto del Label
        lbl = tk.Label(self.ventana, text="REGISTRO")
        # Color de la letra Label
        lbl.config(fg="#B7BBD0")
        # Color del label (transparente)
        lbl.config(bg="#1B1A20")
        # tipo de letra y tamaño de esta
        lbl.config(font=("Lucida Console", 40))
        # Ubicación del Label
        lbl.place(relx=0.5, rely=0.05, anchor="n")

        # Frame (cuadro)
        # Creacion y especificacion decolor
        cuadro = tk.Frame(self.ventana, bg="#26272B")
        # Ubicación del frame
        cuadro.place(relx=0.5, rely=0.15, relwidth=0.6,
                     relheight=0.7, anchor="n")

        # Label (Nombre completo)
        # Texto del Label
        lblNU = tk.Label(cuadro, text="Nombre completo")
        # Color de la letra Label
        lblNU.config(fg="#B4BDE2")
        # Color del label (transparente)
        lblNU.config(bg="#26272B")
        # tipo de letra y tamaño de esta
        lblNU.config(font=("Poppins", 14))
        # Ubicación
        lblNU.pack(anchor=("w"), padx=50, pady=(5, 2))
        lblNU.pack()

        # TextField (Nombre de usuario)
        self.TextField_User = tk.Entry(cuadro)
        # Configuracion de text fielg
        self.TextField_User.config(bg="#0D4044", font=(
            "Poppins", 12), relief="solid", border=0, width=100, fg="white")
        # Ubicación
        self.TextField_User.pack(anchor=("w"), padx=55, pady=0)
        self.TextField_User.pack()

        # Label (Nombre de usuario)
        # Texto del Label
        lblNU = tk.Label(cuadro, text="Nombre de usuario *")
        # Color de la letra Label
        lblNU.config(fg="#B4BDE2")
        # Color del label (transparente)
        lblNU.config(bg="#26272B")
        # tipo de letra y tamaño de esta
        lblNU.config(font=("Poppins", 14))
        # Ubicación
        lblNU.pack(anchor=("w"), padx=50, pady=(5, 2))
        lblNU.pack()

        # TextField (Nombre de usuario)
        self.TextField_UserName = tk.Entry(cuadro)
        # Configuracion de text fielg
        self.TextField_UserName.config(bg="#0D4044", font=(
            "Poppins", 12), relief="solid", border=0, width=100, fg="white")
        # Ubicación
        self.TextField_UserName.pack(anchor=("w"), padx=55, pady=0)
        self.TextField_UserName.pack()

        # Label (contraseña)
        # Texto del Label
        lblPass = tk.Label(cuadro, text="Contraseña *")
        # Color de la letra Label
        lblPass.config(fg="#B4BDE2")
        # Color del label (transparente)
        lblPass.config(bg="#26272B")
        # tipo de letra y tamaño de esta
        lblPass.config(font=("Poppins", 14))
        # Ubicación
        lblPass.pack(anchor=("w"), padx=50, pady=(5, 2))
        lblPass.pack()

        # TextField(Password)
        self.TextField_Pass = tk.Entry(cuadro)
        # Configuracion de text fielg
        self.TextField_Pass.config(bg="#0D4044", font=(
            "Poppins", 12), relief="solid", border=0, width=100, fg="white")
        # Ubicación
        self.TextField_Pass.pack(anchor=("w"), padx=55, pady=0)
        self.TextField_Pass.pack()

        # Label (confirmar contraseña)
        # Texto del Label
        lblPass2 = tk.Label(cuadro, text="Confirmar contraseña *")
        # Color de la letra Label
        lblPass2.config(fg="#B4BDE2")
        # Color del label (transparente)
        lblPass2.config(bg="#26272B")
        # tipo de letra y tamaño de esta
        lblPass2.config(font=("Poppins", 14))
        # Ubicación
        lblPass2.pack(anchor=("w"), padx=50, pady=(5, 2))
        lblPass2.pack()

        # TextField(confirmar Password)
        self.TextField_Pass2 = tk.Entry(cuadro)
        # Configuracion de text fielg
        self.TextField_Pass2.config(bg="#0D4044", font=(
            "Poppins", 12), relief="solid", border=0, width=100, fg="white")
        # Ubicación
        self.TextField_Pass2.pack(anchor=("w"), padx=55, pady=0)
        self.TextField_Pass2.pack()

        # Label (Pregunta)
        # Texto del Label
        lblQ = tk.Label(cuadro, text="Pregunta de seguridad *")
        # Color de la letra Label
        lblQ.config(fg="#B4BDE2")
        # Color del label (transparente)
        lblQ.config(bg="#26272B")
        # tipo de letra y tamaño de esta
        lblQ.config(font=("Poppins", 14))
        # Ubicación
        lblQ.pack(anchor=("w"), padx=50, pady=(5, 2))
        lblQ.pack()

        # TextField(Pregunta)
        self.TextField_Ask = tk.Entry(cuadro)
        # Configuracion de text fielg
        self.TextField_Ask.config(bg="#0D4044", font=(
            "Poppins", 12), relief="solid", border=0, width=100, fg="white")
        # Ubicación
        self.TextField_Ask.pack(anchor=("w"), padx=55, pady=0)
        self.TextField_Ask.pack()

        # Label (respuesta)
        # Texto del Label
        lblAnsw = tk.Label(
            cuadro, text="Respuesta de pregunta de seguridad *")
        # Color de la letra Label
        lblAnsw.config(fg="#B4BDE2")
        # Color del label (transparente)
        lblAnsw.config(bg="#26272B")
        # tipo de letra y tamaño de esta
        lblAnsw.config(font=("Poppins", 14))
        # Ubicación
        lblAnsw.pack(anchor=("w"), padx=50, pady=(5, 2))
        lblAnsw.pack()

        # TextField(respuesta)
        self.TextField_Answ = tk.Entry(cuadro)
        # Configuracion de text fielg
        self.TextField_Answ.config(bg="#0D4044", font=(
            "Poppins", 12), relief="solid", border=0, width=100, fg="white")
        # Ubicación
        self.TextField_Answ.pack(anchor=("w"), padx=55, pady=0)
        self.TextField_Answ.pack()

        # Botón (registrar)
        btn_acceder = tk.Button(self.ventana, text="Registrar", relief="solid", bg="#B7BBD0", fg="black", font=(
            "Poppins", 14), border=0, command=self.registrar_usuario)
        btn_acceder.place(relx=0.7575, rely=0.875, anchor="n")

        # botón (Cancelar)
        # configuracion de boton
        btnCancel = tk.Button(self.ventana, text="Cancelar", relief="flat", bg="#1B1A20", fg="#B4BADE", font=(
            "Poppins", 14, "italic"), command=self.volver_al_inicio)
        # Ubicación de botón
        btnCancel.place(relx=0.245, rely=0.875, anchor="n")

    def registrar_usuario(self):
        # Lógica de registro de usuario

        name = self.TextField_User.get()
        username = self.TextField_UserName.get()
        password = self.TextField_Pass.get()
        confirm_password = self.TextField_Pass2.get()
        question = self.TextField_Ask.get()
        answer = self.TextField_Answ.get()

        esValido = self.validar_campos(
            name, username, password, confirm_password, question, answer)

        if esValido:
            payload = {
                "name": name,
                "username": username,
                "password": password,
                "question": question,
                "answer": answer
            }

            usuario_creado = self.usuarios.create_user(payload)
            usuario_status = usuario_creado["status"]

            if usuario_status != 200:
                message = f"Error {usuario_status}. {
                    str(usuario_creado["response"]["message"])}"
                messagebox.showerror("Error", message)
            else:
                messagebox.showinfo("Registro exitoso",
                                    f"Muy bien, {username}. Serás redirigido al login")
                self.volver_al_inicio()
        else:
            messagebox.showerror("Error", "Falló el registro")

    def validar_campos(self, name, username, password, confirm_password, question, answer):
        contador_registro = 0

        if not username or not password or not confirm_password or not question or not answer:
            messagebox.showerror("Error", "Debe de llenar todos los campos.")
        else:
            # Condicion de seguridad de contraseña
            if len(password) <= 10:
                self.TextField_Pass.config(fg="red")
                messagebox.showerror("Error", "La contraseña no es segura.")
                contador_registro = 0
            else:
                contador_registro += 1

            # Condición de confirmacion de contraseñas
            if password != confirm_password:
                messagebox.showerror(
                    "Error", "Las contraseñas no son iguales.")
                self.TextField_Pass2.config(fg="red")
                self.TextField_Pass2.delete(0, tk.END)
                contador_registro = 0
            else:
                contador_registro += 1

            # condición de pregunta de seguridad
            if answer.lower() == "si" or answer.lower() == "no":
                messagebox.showerror(
                    "Error", "La pregunta no puede ser respondida con un 'Si' o 'No'.")
                self.TextField_Answ.config(fg="red")
                contador_registro = 0
            elif len(answer) <= 6:
                messagebox.showerror(
                    "Error", "La respuesta es demasiado corta.")
                self.TextField_Answ.config(fg="red")
                contador_registro = 0
            else:
                contador_registro += 1

        return contador_registro == 3

    def volver_al_inicio(self):
        self.ventana.destroy()
        self.app.show()
