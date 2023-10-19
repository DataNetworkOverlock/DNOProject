import tkinter as tk
import subprocess
import threading

def ejecutar_comando(event):
    comando = entrada_terminal.get("insert linestart", "insert lineend")
    entrada_terminal.insert(tk.END, f"\n> {comando}\n")
    entrada_terminal.mark_set(tk.INSERT, "insert + 1l linestart")
    entrada_terminal.see(tk.END)

    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    for linea in proceso.stdout:
        entrada_terminal.insert(tk.END, linea)
        entrada_terminal.mark_set(tk.INSERT, "insert + 1l linestart")
        entrada_terminal.see(tk.END)
        entrada_terminal.update()

app = tk.Tk()
app.title("Terminal GUI")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10, fill="both", expand=True)

entrada_terminal = tk.Text(frame, wrap="none", height=10)
entrada_terminal.pack(fill=tk.BOTH, expand=True)

entrada_terminal.bind("<Return>", ejecutar_comando)

app.mainloop()

