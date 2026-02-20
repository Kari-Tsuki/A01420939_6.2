"""
Pruebas unitarias para el módulo hotel.py.
Verifica la creación, eliminación, modificación y persistencia de hoteles.
"""
import unittest
import os
from source.hotel import Hotel


class TestHotel(unittest.TestCase):
    """Casos de prueba para la clase Hotel."""

    def setUp(self):
        """Configuración inicial antes de cada prueba."""
        self.hotels = []
        self.test_file = "test_hotels.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        """Limpieza después de cada prueba."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_hotel(self):
        """Prueba la creación de un hotel de forma exitosa."""
        result = Hotel.create_hotel(self.hotels, 1, "Hotel Test", "CDMX", 10)
        self.assertTrue(result)
        self.assertEqual(len(self.hotels), 1)

    def test_create_duplicate_hotel(self):
        """Prueba que no se pueda crear un hotel con un ID ya existente."""
        Hotel.create_hotel(self.hotels, 1, "Hotel Test", "CDMX", 10)
        result = Hotel.create_hotel(self.hotels, 1, "Hotel Duplicado",
                                    "MTY", 5)
        self.assertFalse(result)
        self.assertEqual(len(self.hotels), 1)

    def test_delete_hotel(self):
        """Prueba la eliminación de un hotel existente."""
        Hotel.create_hotel(self.hotels, 1, "Hotel Test", "CDMX", 10)
        result = Hotel.delete_hotel(self.hotels, 1)
        self.assertTrue(result)
        self.assertEqual(len(self.hotels), 0)

    def test_delete_nonexistent_hotel(self):
        """Prueba intentar eliminar un hotel que no existe."""
        result = Hotel.delete_hotel(self.hotels, 99)
        self.assertFalse(result)

    def test_modify_hotel(self):
        """Prueba la modificación de atributos de un hotel."""
        hotel = Hotel(1, "Hotel Viejo", "CDMX", 10)
        hotel.modify_hotel(name="Hotel Nuevo", rooms=20)
        self.assertEqual(hotel.name, "Hotel Nuevo")
        self.assertEqual(hotel.rooms, 20)
        self.assertEqual(hotel.location, "CDMX")

    def test_reserve_and_cancel_room(self):
        """Prueba la reserva y cancelación de habitaciones."""
        hotel = Hotel(1, "Hotel Test", "CDMX", 1)

        self.assertTrue(hotel.reserve_room())
        self.assertEqual(hotel.rooms, 0)

        self.assertFalse(hotel.reserve_room())

        hotel.cancel_reservation()
        self.assertEqual(hotel.rooms, 1)

    def test_save_and_load_file(self):
        """Prueba guardar los datos en un JSON y cargarlos de vuelta."""
        Hotel.create_hotel(self.hotels, 1, "Hotel JSON", "Cancún", 50)

        Hotel.save_to_file(self.hotels, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

        loaded_hotels = Hotel.load_from_file(self.test_file)
        self.assertEqual(len(loaded_hotels), 1)
        self.assertEqual(loaded_hotels[0].name, "Hotel JSON")
        self.assertEqual(loaded_hotels[0].rooms, 50)


if __name__ == "__main__":
    unittest.main()
