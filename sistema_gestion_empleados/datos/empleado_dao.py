import json
import os
from modelo.empleado import Empleado

class EmpleadoDAO:
    ARCHIVO = "empleados.json"

    def __init__(self):
        self.empleados = self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        with open(self.ARCHIVO, "w") as archivo:
            json.dump([emp.to_dict() for emp in self.empleados], archivo, indent=4)

    def cargar_desde_archivo(self):
        if not os.path.exists(self.ARCHIVO):
            return []
        with open(self.ARCHIVO, "r") as archivo:
            datos = json.load(archivo)
            return [Empleado.from_dict(emp) for emp in datos]

    def agregar(self, empleado):
        self.empleados.append(empleado)
        self.guardar_en_archivo()

    def listar(self):
        return self.empleados

    def buscar_por_id(self, id):
        for emp in self.empleados:
            if emp.id == id:
                return emp
        return None

    def eliminar(self, id):
        emp = self.buscar_por_id(id)
        if emp:
            self.empleados.remove(emp)
            self.guardar_en_archivo()
            return True
        return False
