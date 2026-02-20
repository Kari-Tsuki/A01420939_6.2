"""
Pruebas unitarias para el módulo reservation.py.
Verifica la creación, cancelación y persistencia de reservaciones.
"""
import unittest
import os
from source.reservation import Reservation


class TestReservation(unittest.TestCase):
    """Casos de prueba para la clase Reservation."""

    def setUp(self):
        """Configuración inicial antes de cada prueba."""
        self.reservations = []
        self.test_file = "test_reservations.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        """Limpieza después de cada prueba."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_reservation(self):
        """Prueba la creación de una reservación exitosa."""
        result = Reservation.create_reservation(
            self.reservations, 1, 100, 200
        )
        self.assertTrue(result)
        self.assertEqual(len(self.reservations), 1)

    def test_create_duplicate_reservation(self):
        """Prueba que no se pueda crear una reservación duplicada."""
        Reservation.create_reservation(self.reservations, 1, 100, 200)
        result = Reservation.create_reservation(
            self.reservations, 1, 101, 201
        )
        self.assertFalse(result)
        self.assertEqual(len(self.reservations), 1)

    def test_cancel_reservation(self):
        """Prueba la cancelación (eliminación) de una reservación."""
        Reservation.create_reservation(self.reservations, 1, 100, 200)
        result = Reservation.cancel_reservation(self.reservations, 1)
        self.assertTrue(result)
        self.assertEqual(len(self.reservations), 0)

    def test_cancel_nonexistent_reservation(self):
        """Prueba intentar cancelar una reservación que no existe."""
        result = Reservation.cancel_reservation(self.reservations, 99)
        self.assertFalse(result)

    def test_save_and_load_file(self):
        """Prueba guardar y cargar reservaciones en JSON."""
        Reservation.create_reservation(self.reservations, 1, 100, 200)

        Reservation.save_to_file(self.reservations, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

        loaded_res = Reservation.load_from_file(self.test_file)
        self.assertEqual(len(loaded_res), 1)
        self.assertEqual(loaded_res[0].customer_id, 100)


if __name__ == "__main__":
    unittest.main()
