class Empleado:
    def __init__(self, id, nombre, puesto, salario):
        self.id = id
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Puesto: {self.puesto}, Salario: ${self.salario}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "puesto": self.puesto,
            "salario": self.salario
        }

    @staticmethod
    def from_dict(data):
        return Empleado(data["id"], data["nombre"], data["puesto"], data["salario"])
