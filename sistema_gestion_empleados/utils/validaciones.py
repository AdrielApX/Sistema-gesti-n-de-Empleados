import re

def es_numero(valor):
    return valor.isdigit()

def es_texto(valor):
    return re.fullmatch(r'[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+', valor) is not None

def es_decimal(valor):
    return re.fullmatch(r'\d+(\.\d{1,2})?', valor) is not None


def registrar_empleado(servicio):
    while True:
        id_empleado = input("Ingrese el ID del empleado: ")
        if not es_numero(id_empleado):
            print("ID inválido. Solo se permiten números.")
            continue

        nombre = input("Ingrese el nombre del empleado: ")
        if not es_texto(nombre):
            print("Nombre inválido. Solo se permiten letras sin espacios ni caracteres especiales.")
            continue

        puesto = input("Ingrese el puesto del empleado: ")
        # Para simplificar, dejamos este sin validación estricta

        salario = input("Ingrese el salario del empleado: ")
        if not es_decimal(salario):
            print("Salario inválido. Solo se permiten números (puede incluir decimales).")
            continue

        # Si todo es válido, salimos del bucle
        break

    servicio.registrar_empleado(
        int(id_empleado),
        nombre,
        puesto,
        float(salario)
    )
    print("Empleado registrado exitosamente.")

