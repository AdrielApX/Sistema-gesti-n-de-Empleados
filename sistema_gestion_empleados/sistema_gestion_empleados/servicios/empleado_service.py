from datos.empleado_dao import EmpleadoDAO
from modelo.empleado import Empleado
from utils.validaciones import Validaciones

class EmpleadoService:
    def __init__(self, dao):
        self.dao = dao
        self.validaciones = Validaciones()

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
        
    def editar_empleado(self, id, nombre, puesto, salario):
        if not self.validaciones.validar_campos(id, nombre, puesto, salario):
            raise ValueError("Todos los campos son obligatorios.")
        if not self.validaciones.salario_valido(salario):
            raise ValueError("El salario debe ser numérico y mayor a cero.")
        if not self.dao.buscar_por_id(id):
            raise ValueError(f"No existe un empleado con ID {id}")
        self.dao.actualizar(id, nombre, puesto, salario)

    def buscar_empleado(self, id):
        return self.dao.buscar_por_id(id)