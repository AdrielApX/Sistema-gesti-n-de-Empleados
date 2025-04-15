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

    def registrar_empleado(servicio):
        while True:
            id_empleado = input("Ingrese el ID del empleado (solo números): ")
            if not es_numero(id_empleado):
                print("ID inválido. Solo se permiten números enteros.")
                continue

            nombre = input("Ingrese el nombre del empleado (solo letras y espacios): ")
            if not es_texto(nombre):
                print("Nombre inválido. Solo se permiten letras y espacios.")
                continue

            puesto = input("Ingrese el puesto del empleado (solo letras y espacios): ")
            if not es_texto(puesto):
                print("Puesto inválido. Solo se permiten letras y espacios.")
                continue

            salario = input("Ingrese el salario del empleado (solo números, puede incluir decimales): ")
            if not es_decimal(salario):
                print("Salario inválido. Debe ser un número válido (ej: 3000 o 2500.50).")
                continue

            break
        servicio.registrar_empleado(
        int(id_empleado),
        nombre,
        puesto,
        float(salario)
        )
        print("Empleado registrado exitosamente.")