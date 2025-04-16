import tkinter as tk
from tkinter import messagebox
from servicios.empleado_service import EmpleadoService

class VentanaPrincipal:
    def __init__(self, root):
        self.servicio = EmpleadoService()
        self.root = root
        self.root.title("Gestión de Empleados")
        self.root.configure(bg="#dcdcdc")  # Fondo gris claro
        self.root.geometry("800x400")
        self.root.minsize(600, 300)

        # Variables de entrada
        self.id_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.puesto_var = tk.StringVar()
        self.salario_var = tk.StringVar()

        # Crear contenedor centrado
        self.frame = tk.Frame(self.root, bg="#dcdcdc")
        self.frame.pack(pady=20)

        # Etiquetas y entradas
        self._crear_label_entry("ID:", self.id_var, 0)
        self._crear_label_entry("Nombre:", self.nombre_var, 1)
        self._crear_label_entry("Puesto:", self.puesto_var, 2)
        self._crear_label_entry("Salario:", self.salario_var, 3)

        # Botones
        boton_frame = tk.Frame(self.frame, bg="#dcdcdc")
        boton_frame.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(boton_frame, text="Registrar", command=self.registrar, font=("Segoe UI", 10)).grid(row=0, column=0, padx=5)
        tk.Button(boton_frame, text="Eliminar por ID", command=self.eliminar, font=("Segoe UI", 10)).grid(row=0, column=1, padx=5)
        tk.Button(self.frame, text="Listar empleados", command=self.listar, font=("Segoe UI", 10)).grid(row=5, column=0, columnspan=2, pady=10)

        # Área de texto para mostrar resultados
        self.text_area = tk.Text(self.root, height=10, font=("Consolas", 11))
        self.text_area.pack(expand=True, fill="both", padx=20, pady=10)

    def _crear_label_entry(self, texto, variable, fila):
        tk.Label(self.frame, text=texto, font=("Segoe UI", 11), bg="#dcdcdc").grid(row=fila, column=0, sticky="e", padx=5, pady=3)
        tk.Entry(self.frame, textvariable=variable, font=("Segoe UI", 11), width=30).grid(row=fila, column=1, padx=5, pady=3)

    def registrar(self):
        id = self.id_var.get()
        nombre = self.nombre_var.get()
        puesto = self.puesto_var.get()
        salario = self.salario_var.get()
        try:
            salario_float = float(salario)
            self.servicio.crear_empleado(id, nombre, puesto, salario_float)
            messagebox.showinfo("Éxito", "Empleado registrado correctamente.")
            self._limpiar()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar(self):
        id = self.id_var.get()
        try:
            self.servicio.eliminar_empleado(id)
            messagebox.showinfo("Éxito", "Empleado eliminado.")
            self._limpiar()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def listar(self):
        empleados = self.servicio.listar_empleados()
        self.text_area.delete("1.0", tk.END)
        if empleados:
            for emp in empleados:
                self.text_area.insert(tk.END, str(emp) + "\n")
        else:
            self.text_area.insert(tk.END, "No hay empleados registrados.")

    def _limpiar(self):
        self.id_var.set("")
        self.nombre_var.set("")
        self.puesto_var.set("")
        self.salario_var.set("")
