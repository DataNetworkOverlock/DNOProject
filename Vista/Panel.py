import tkinter as tk
import subprocess

def create_panel_window(root, app):
    panel_window = tk.Toplevel(root)
    PanelWindow(panel_window, app)

class PanelWindow:
    def __init__(self, root, app):
        self.root = root
        self.app = app
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

        self.ListTools = None
        self.entrada_terminal = None
        self.etiqueta = None

        self.create_widgets() # Llamado de funcion para crear los widgets

    def create_widgets(self):
        #Frame (Consola)
        #Creacion y especificacion decolor
        cuadroCmd = tk.Frame(self.root, bg="#1E1F24")
        #Ubicacion del frame
        cuadroCmd.place(relx=0.65, rely=0.0, relwidth=0.7, relheight=1.0, anchor="n")

        #Label (Principal)
        #Texto del Label
        lblOverlook = tk.Label(cuadroCmd,text="OVERLOCK")
        #Color de la letra Label
        lblOverlook.config(fg = "#B7BBD0")
        #Color del label (transparente)
        lblOverlook.config(bg= "#1E1F24")
        #tipo de letra y tamaño de esta
        lblOverlook.config(font=("Arial", 40))
        #Ubicacion del Label
        lblOverlook.place(relx=0.5, rely=0.05, anchor="n")

        #Creacion del textArea que muestra resultados de cmd
        self.entrada_terminal = tk.Text(cuadroCmd)
        self.entrada_terminal.config(width=95, height=26, bg="black", fg="white", relief="solid", borderwidth=0, font=("Consolas", 12))
        self.entrada_terminal.pack(anchor="w", padx=25, pady=110)
        self.entrada_terminal.bind("<Return>", self.ejecutar_comando)

        #Frame (Herramientas)
        #Creacion y especificacion decolor
        cuadroTool = tk.Frame(self.root, bg="#1B1A20")
        #Ubicacion del frame
        cuadroTool.place(relx=0.14, rely=0.0, relwidth=0.25, relheight=1.0, anchor="n")

        #Label (titulo)
        #Texto del Label
        lblTools = tk.Label(cuadroTool,text="Herramientas")
        #Color de la letra Label
        lblTools.config(fg = "#B7BBD0")
        #Color del label (transparente)
        lblTools.config(bg= "#1B1A20")
        #tipo de letra y tamaño de esta
        lblTools.config(font=("Arial", 25))
        #Ubicacion del Label
        lblTools.place(relx=0.5, rely=0.05, anchor="n")

        # Crear un ListBox
        self.ListTools = tk.Listbox(cuadroTool, selectmode=tk.SINGLE)
        self.ListTools.configure(bg="#25242D", fg = "#AEAEB0", font=("Verdana", 20, "bold"))
        self.ListTools.place(x=40, y=100, width=260, height=425)

        # Agregar elementos al ListTools
        elementos = ["kismet", "john the ripper", "sqlmap", "nmap", "nikto"]
        for elemento in elementos:
            self.ListTools.insert(tk.END, elemento)

        # Configurar un evento de selección en el ListTools
        self.ListTools.bind("<<ListboxSelect>>", self.seleccionar_elemento)

        #boton (registrarse)
        #configuracion de boton
        btnR = tk.Button(cuadroTool, text="Ver reportes", relief="sunken", bg="#0E0D13", fg="#ADB2D6", font=("Arial", 14),command=self.ir_a_reportes)
        #ubicacion de boton
        btnR.place(relx=0.33, rely=0.765, anchor="n")

        #Boton (recordar contraseña)
        btnRP = tk.Button(cuadroTool, text="Salir", relief="sunken", bg="#0E0D13", fg="#ADB2D6", font=("Arial", 14), command=self.ir_a_inicio_sesion)
        #ubicacion de boton
        btnRP.place(relx=0.91, rely=0.765, anchor="n")

        # Crear una label para mostrar el elemento seleccionado
        self.etiqueta = tk.Label(cuadroTool, text="")
        self.etiqueta.pack()

    def ir_a_reportes(self):
        # Lógica para ir a la ventana de registro
        self.root.withdraw()  # Oculta la ventana actual
        self.app.mostrar_menu()  # Muestra la ventana de registro en la ventana principal

    def ir_a_inicio_sesion(self):
        # Lógica para volver a la ventana de inicio de sesión
        self.root.withdraw()  # Oculta la ventana actual
        self.app.show()  # Muestra la ventana de inicio de sesión en la ventana principal
    
    def seleccionar_elemento(self, event):
        seleccion = self.ListTools.get(self.ListTools.curselection())
        self.etiqueta.config(text=f"{seleccion}")

    def ejecutar_comando(self, event):
        comando = self.entrada_terminal.get("insert linestart", "insert lineend")
        self.entrada_terminal.insert(tk.END, f"\n> {comando}\n")
        self.entrada_terminal.mark_set(tk.INSERT, "insert + 1l linestart")
        self.entrada_terminal.see(tk.END)

        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        for linea in proceso.stdout:
            self.entrada_terminal.insert(tk.END, linea)
            self.entrada_terminal.mark_set(tk.INSERT, "insert + 1l linestart")
            self.entrada_terminal.see(tk.END)
            self.entrada_terminal.update()

if __name__ == "__main__":
    ventana_registro = tk.Toplevel()
    ventana_registro.withdraw()
    ventana_registro.mainloop()
