import tkinter as tk
from tkinter import messagebox
from servicios.empleado_service import EmpleadoService

class VentanaPrincipal:
    def __init__(self, root):
        self.servicio = EmpleadoService()
        self.root = root
        self.root.title("Gestión de Empleados")

        # Campos de entrada
        tk.Label(root, text="ID:").grid(row=0, column=0)
        self.entry_id = tk.Entry(root)
        self.entry_id.grid(row=0, column=1)

        tk.Label(root, text="Nombre:").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(root, text="Puesto:").grid(row=2, column=0)
        self.entry_puesto = tk.Entry(root)
        self.entry_puesto.grid(row=2, column=1)

        tk.Label(root, text="Salario:").grid(row=3, column=0)
        self.entry_salario = tk.Entry(root)
        self.entry_salario.grid(row=3, column=1)

        # Botones
        tk.Button(root, text="Registrar", command=self.registrar).grid(row=4, column=0, pady=10)
        tk.Button(root, text="Eliminar por ID", command=self.eliminar).grid(row=4, column=1)
        tk.Button(root, text="Listar empleados", command=self.listar).grid(row=5, column=0, columnspan=2)

        # Área de resultados
        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.grid(row=6, column=0, columnspan=2)

    def registrar(self):
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        puesto = self.entry_puesto.get()
        try:
            salario = float(self.entry_salario.get())
            self.servicio.crear_empleado(id, nombre, puesto, salario)
            messagebox.showinfo("Éxito", "Empleado registrado correctamente.")
            self.limpiar_entradas()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar(self):
        id = self.entry_id.get()
        try:
            self.servicio.eliminar_empleado(id)
            messagebox.showinfo("Éxito", "Empleado eliminado.")
            self.limpiar_entradas()
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

    def limpiar_entradas(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_puesto.delete(0, tk.END)
        self.entry_salario.delete(0, tk.END)
