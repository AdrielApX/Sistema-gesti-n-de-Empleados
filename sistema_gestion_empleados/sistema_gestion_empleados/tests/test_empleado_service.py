import unittest
import os
from servicios.empleado_service import EmpleadoService

# Asegurarse de que siempre se use un archivo de prueba y no afecte al original
from datos.empleado_dao import EmpleadoDAO
EmpleadoDAO.ARCHIVO = "test_empleados.json"

class TestEmpleadoService(unittest.TestCase):
    def setUp(self):
        # Reiniciar DAO con archivo limpio antes de cada prueba
        if os.path.exists(EmpleadoDAO.ARCHIVO):
            os.remove(EmpleadoDAO.ARCHIVO)
        self.service = EmpleadoService()

    def test_crear_empleado_valido(self):
        self.service.crear_empleado("001", "Ana", "Ingeniera", 2500.0)
        empleados = self.service.listar_empleados()
        self.assertEqual(len(empleados), 1)
        self.assertEqual(empleados[0].id, "001")

    def test_id_duplicado(self):
        self.service.crear_empleado("002", "Luis", "Contador", 2000.0)
        with self.assertRaises(ValueError) as e:
            self.service.crear_empleado("002", "Maria", "Diseñadora", 2200.0)
        self.assertIn("ID", str(e.exception))

    def test_id_vacio(self):
        with self.assertRaises(ValueError) as e:
            self.service.crear_empleado("   ", "Jose", "Gerente", 3000.0)
        self.assertIn("ID", str(e.exception))

    def test_salario_negativo(self):
        with self.assertRaises(ValueError) as e:
            self.service.crear_empleado("003", "Rosa", "Asistente", -100.0)
        self.assertIn("salario", str(e.exception))

    def test_eliminar_empleado_existente(self):
        self.service.crear_empleado("004", "Pedro", "Técnico", 1800.0)
        self.service.eliminar_empleado("004")
        empleados = self.service.listar_empleados()
        self.assertEqual(len(empleados), 0)

if __name__ == '__main__':
    unittest.main()
