"""
hotel.py

Este programa gestiona la clase Hotel. Incluye funciones de
creación, eliminación, muestreo, modificacion, reserva y
cancelación de reserva.
"""

import json
import os


class Hotel:
    """Clase para la administración de los hoteles"""

    def __init__(self, hotel_id, name, location, rooms):
        "Se crea un nuevo objeto 'Hotel'"
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms
    
    def to_dict(self):
        """Convierte el objeto 'Hotel' en un diccionario"""
        return{
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms
        }
    
    @staticmethod
    def save_to_file(hotels, filename="hotels.json"):
        """Guardar la lista de hoteles en un archivo JSON"""
        try:
            with open(filename, "w", encoding="uft8") as f:
                json.dump([h.to_dict() for h in hotels], f, indent=4)
        except IOError as e:
            print(f"Error, no se pudo guardar el archivo: {e}")
    
    @staticmethod
    def load_from_file(filename="hotels.json"):
        """Cargar la lista de hoteles de un archivo JSON"""
        if not os.path.exists(filename):
            return []
        try:
            with open(filename, "r", encoding="uft8") as f:
                data = json.load(f)
                return [Hotel(**h) for h in data]
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            print(f"Error, no se pudo leer el archivo {filename}: {e}")
            return []
    
    @staticmethod
    def create_hotel(hotels, hotel_id, name, location, rooms):
        """Creación e incorporación de un nuevo hotel"""
        if any(h.hotel_id == hotel_id for h in hotels):
            print(f"Error, el ID del hotel {hotel_id} ya existe")
            return False
        new_hotel = Hotel(hotel_id, name, location, rooms)
        hotels.append(new_hotel)
        return True
