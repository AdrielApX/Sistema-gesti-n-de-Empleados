from datos.empleado_dao import EmpleadoDAO
from modelo.empleado import Empleado

class EmpleadoService:
    def __init__(self):
        self.dao = EmpleadoDAO()

    def crear_empleado(self, id, nombre, puesto, salario):
        if not isinstance(id, str) or not id.strip():
            raise ValueError("El ID debe ser un texto no vacío.")

        if self.dao.buscar_por_id(id):
            raise ValueError("Ya existe un empleado con ese ID.")

        if not isinstance(salario, (int, float)) or salario <= 0:
            raise ValueError("El salario debe ser un número positivo.")

        nuevo_empleado = Empleado(id.strip(), nombre.strip(), puesto.strip(), salario)
        self.dao.agregar(nuevo_empleado)

    def listar_empleados(self):
        return self.dao.listar()

    def eliminar_empleado(self, id):
        if not self.dao.eliminar(id):
            raise ValueError("No se encontró el empleado con ese ID.")
