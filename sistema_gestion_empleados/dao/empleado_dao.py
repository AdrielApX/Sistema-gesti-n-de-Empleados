class EmpleadoDAO:
    def __init__(self):
        self.empleados = []

    def agregar(self, empleado):
        self.empleados.append(empleado)

    def listar(self):
        return self.empleados

    def buscar_por_id(self, id):
        for empleado in self.empleados:
            if empleado.id == id:
                return empleado
        return None

    def eliminar(self, id):
        empleado = self.buscar_por_id(id)
        if empleado:
            self.empleados.remove(empleado)
            return True
        return False