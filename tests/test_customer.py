"""
Pruebas unitarias para el módulo customer.py.
Verifica la creación, eliminación, modificación y persistencia de hoteles.
"""

import unittest
import os
from source.customer import Customer


class TestCustomer(unittest.TestCase):
    """Casos de prueba para la clase Customer."""

    def setUp(self):
        """Configuración inicial antes de cada prueba."""
        self.customers = []
        self.test_file = "test_customers.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        """Limpieza después de cada prueba."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_customer(self):
        """Prueba la creación de un cliente exitosa."""
        result = Customer.create_customer(
            self.customers, 1, "Juan Perez", "juan@test.com"
        )
        self.assertTrue(result)
        self.assertEqual(len(self.customers), 1)

    def test_create_duplicate_customer(self):
        """Prueba que no se pueda crear un cliente con ID duplicado."""
        Customer.create_customer(
            self.customers, 1, "Juan Perez", "juan@test.com"
        )
        # Intentamos crear otro con el mismo ID
        result = Customer.create_customer(
            self.customers, 1, "Ana Gomez", "ana@test.com"
        )
        self.assertFalse(result)
        self.assertEqual(len(self.customers), 1)

    def test_delete_customer(self):
        """Prueba la eliminación de un cliente existente."""
        Customer.create_customer(
            self.customers, 1, "Juan Perez", "juan@test.com"
        )
        result = Customer.delete_customer(self.customers, 1)
        self.assertTrue(result)
        self.assertEqual(len(self.customers), 0)

    def test_delete_nonexistent_customer(self):
        """Prueba intentar eliminar un cliente que no existe."""
        result = Customer.delete_customer(self.customers, 99)
        self.assertFalse(result)

    def test_modify_customer(self):
        """Prueba la modificación de atributos de un cliente."""
        customer = Customer(1, "Viejo Nombre", "viejo@test.com")
        customer.modify_customer(name="Nuevo Nombre", email="nuevo@test.com")
        self.assertEqual(customer.name, "Nuevo Nombre")
        self.assertEqual(customer.email, "nuevo@test.com")

    def test_save_and_load_file(self):
        """Prueba guardar los datos en JSON y cargarlos de vuelta."""
        Customer.create_customer(
            self.customers, 1, "Cliente JSON", "json@test.com"
        )

        Customer.save_to_file(self.customers, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

        loaded_customers = Customer.load_from_file(self.test_file)
        self.assertEqual(len(loaded_customers), 1)
        self.assertEqual(loaded_customers[0].name, "Cliente JSON")


if __name__ == "__main__":
    unittest.main()
