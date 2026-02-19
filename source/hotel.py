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
    
    