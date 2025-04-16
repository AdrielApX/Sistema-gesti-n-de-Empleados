from servicios.empleado_service import EmpleadoService

class Interfaz:
    def __init__(self):
        self.servicio = EmpleadoService()

    def mostrar_menu(self):
        while True:
            print("\n----- Sistema de Gestión de Empleados -----")
            print("1. Registrar empleado")
            print("2. Listar empleados")
            print("3. Eliminar empleado")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_empleado()
            elif opcion == "2":
                self.listar_empleados()
            elif opcion == "3":
                self.eliminar_empleado()
            elif opcion == "4":
                self.editar_empleado()
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def registrar_empleado(self):
        id = input("Ingrese ID: ")
        nombre = input("Ingrese nombre: ")
        puesto = input("Ingrese puesto: ")
        try:
            salario = float(input("Ingrese salario: "))
            self.servicio.crear_empleado(id, nombre, puesto, salario)
            print("Empleado registrado exitosamente.")
        except ValueError as e:
            print(f"Error: {e}")

    def listar_empleados(self):
        empleados = self.servicio.listar_empleados()
        if not empleados:
            print("No hay empleados registrados.")
        else:
            for emp in empleados:
                print(emp)

    def eliminar_empleado(self):
        id = input("Ingrese ID del empleado a eliminar: ")
        try:
            self.servicio.eliminar_empleado(id)
            print("Empleado eliminado exitosamente.")
        except ValueError as e:
            print(f"Error: {e}")

    def editar_empleado(self):
        print("\n--- Editar Empleado ---")
        id = input("ID del empleado a editar: ")
        nombre = input("Nuevo nombre: ")
        puesto = input("Nuevo puesto: ")
        salario = input("Nuevo salario: ")
        try:
            self.servicio.editar_empleado(id, nombre, puesto, float(salario))
            print("Empleado actualizado correctamente.")
        except Exception as e:
            print("Error:", e)

