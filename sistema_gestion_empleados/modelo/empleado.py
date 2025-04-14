class Empleado:
    def __init__(self, id, nombre, puesto, salario):
        self.id = id
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Puesto: {self.puesto}, Salario: {self.salario}"