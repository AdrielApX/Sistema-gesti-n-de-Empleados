from dao.empleado_dao import EmpleadoDAO
from modelo.empleado import Empleado

class EmpleadoService:
    def __init__(self):
        self.dao = EmpleadoDAO()

    def crear_empleado(self, id, nombre, puesto, salario):
        if self.dao.buscar_por_id(id) is None:
            empleado = Empleado(id, nombre, puesto, salario)
            self.dao.agregar(empleado)
            return True
        return False

    def listar_empleados(self):
        return self.dao.listar()

    def eliminar_empleado(self, id):
        return self.dao.eliminar(id)
