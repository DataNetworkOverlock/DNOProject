import tkinter as tk

root = tk.Tk()
root.geometry("1200x1500")
root.configure(bg='#191A1E')

cuadroCmd2 = tk.Frame(root, bg='#191A1E')
cuadroCmd2.place(relx=0.5, rely=0.2, relwidth=0.85, relheight=0.7, anchor="n")

scrollbar = tk.Scrollbar(cuadroCmd2, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

cuadroCmdInterno = tk.Canvas(cuadroCmd2, bg="#191A1E", yscrollcommand=scrollbar.set)
cuadroCmdInterno.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=cuadroCmdInterno.yview)

frame_interior = tk.Frame(cuadroCmdInterno, bg='#191A1E')  # Frame interno al Canvas
cuadroCmdInterno.create_window((0, 0), window=frame_interior, anchor='nw')

nombres_scripts = ["Script" + str(i) for i in range(1, 19)]  # Ejemplo con 18 scripts

grupos = [nombres_scripts[i:i + 3] for i in range(0, len(nombres_scripts), 3)]

for grupo in grupos:
    marco_grupo = tk.Frame(frame_interior, bg='#191A1E')
    marco_grupo.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    for nombre in grupo:
        nuevo_frame = tk.Frame(marco_grupo, bg='#26272B')
        nuevo_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
        label = tk.Label(nuevo_frame, text="                             "+nombre+"                             ", font=("Arial", 12), bg='#26272B', fg="white")
        label.pack()
        button = tk.Button(nuevo_frame, text=f"Botón de {nombre}")
        button.pack()

# Actualizar el área desplazable del Canvas después de agregar los elementos
cuadroCmdInterno.update_idletasks()
cuadroCmdInterno.configure(scrollregion=cuadroCmdInterno.bbox("all"))

root.mainloop()
