from servicio.empleado_service import EmpleadoService
from utils.validaciones import es_numero, es_texto, es_decimal

class Interfaz:
    def __init__(self):
        self.servicio = EmpleadoService()

    def mostrar_menu(self):
        while True:
            print("\n1. Registrar empleado")
            print("2. Listar empleados")
            print("3. Eliminar empleado")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.registrar_empleado()
            elif opcion == '2':
                self.listar_empleados()
            elif opcion == '3':
                self.eliminar_empleado()
            elif opcion == '4':
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def registrar_empleado(self):
        id = input("Ingrese el ID del empleado: ")
        nombre = input("Ingrese el nombre del empleado: ")
        puesto = input("Ingrese el puesto del empleado: ")
        salario = input("Ingrese el salario del empleado: ")
        if self.servicio.crear_empleado(id, nombre, puesto, salario):
            print("Empleado registrado exitosamente.")
        else:
            print("Error: El ID ya existe.")

    def listar_empleados(self):
        empleados = self.servicio.listar_empleados()
        if empleados:
            for empleado in empleados:
                print(empleado)
        else:
            print("No hay empleados registrados.")

    def eliminar_empleado(self):
        id = input("Ingrese el ID del empleado a eliminar: ")
        if self.servicio.eliminar_empleado(id):
            print("Empleado eliminado exitosamente.")
        else:
            print("Error: El empleado no existe.")