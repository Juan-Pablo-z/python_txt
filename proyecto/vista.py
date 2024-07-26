import tkinter as tk
from tkinter import messagebox, simpledialog

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.root = tk.Tk()
        self.root.title("Gestión de Archivos")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.texto_label = tk.Label(self.frame, text="Escriba el texto a guardar:")
        self.texto_label.pack()

        self.texto_entry = tk.Entry(self.frame, width=50)
        self.texto_entry.pack()

        self.nombre_archivo_label = tk.Label(self.frame, text="Escriba el nombre del archivo:")
        self.nombre_archivo_label.pack()

        self.nombre_archivo_entry = tk.Entry(self.frame, width=50)
        self.nombre_archivo_entry.pack()

        self.crear_btn = tk.Button(self.frame, text="Crear Archivo", command=self.crear_archivo)
        self.crear_btn.pack(pady=5)

        self.leer_btn = tk.Button(self.frame, text="Leer Archivo", command=self.leer_archivo)
        self.leer_btn.pack(pady=5)

    def crear_archivo(self):
        texto = self.texto_entry.get()
        nombre_archivo = self.nombre_archivo_entry.get()
        if texto and nombre_archivo:
            mensaje = self.controlador.crear_archivo(texto, nombre_archivo)
            messagebox.showinfo("Información", mensaje)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def leer_archivo(self):
        nombre_archivo = simpledialog.askstring("Entrada", "Escriba el nombre del archivo a leer (sin .txt):")
        if nombre_archivo:
            datos = self.controlador.leer_archivo(nombre_archivo)
            if datos:
                messagebox.showinfo("Contenido del Archivo", datos["contenido"])
            else:
                messagebox.showwarning("Advertencia", "El archivo no existe.")
    
    def iniciar(self):
        self.root.mainloop()
