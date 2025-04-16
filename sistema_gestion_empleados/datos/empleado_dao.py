import json
import os
from modelo.empleado import Empleado

class EmpleadoDAO:
    # Ruta absoluta al archivo empleados.json en la raíz del proyecto
    ARCHIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'empleados.json')

    def __init__(self):
        self.empleados = self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        with open(self.ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump([emp.to_dict() for emp in self.empleados], archivo, indent=4)

    def cargar_desde_archivo(self):
        ruta = os.path.normpath(self.ARCHIVO)
        if not os.path.exists(ruta):
            return []
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return [Empleado.from_dict(emp) for emp in datos]

    def agregar(self, empleado):
        self.empleados.append(empleado)
        self.guardar_en_archivo()

    def listar(self):
        return sorted(self.empleados, key=lambda emp: int(emp.id))

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
