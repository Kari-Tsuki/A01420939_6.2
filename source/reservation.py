"""
reservation.py

Este programa gestiona la clase reservation. Incluye funciones de
creación y eliminación.
"""

import json
import os


class Reservation:
    """Clase para la administración de las reservaciones"""
    def __init__(self, reservation_id, customer_id, hotel_id):
        """Se crea un nuevo objeto 'Reservation"""
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Convierte el objeto 'Reservation' en un diccionario"""
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
        }

    @staticmethod
    def save_to_file(reservations, filename="reservation.json"):
        """Guardar la lista de reservaciones en un archivo JSON"""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump([r.to_dict() for r in reservations], f, indent=4)
        except IOError as e:
            print(f"Error, no se pudo guardar el archivo: {e}.")

    @staticmethod
    def load_from_file(filename="reservation.json"):
        """Cargar la lista de reservaciones de un archivo JSON"""
        if not os.path.exists(filename):
            return []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Reservation(**r) for r in data]
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            print(f"Error, no se pudo leer el archivo {filename}: {e}.")
            return []

    @staticmethod
    def create_reservation(reservations, res_id, cust_id, hot_id):
        """Crea e incorpora una nueva reservación en la lista 
        de reservaciones"""
        if any(r.reservation_id == res_id for r in reservations):
            print(f"Error: el ID de la reservación {res_id} ya existe.")
            return False
        new_res = Reservation(res_id, cust_id, hot_id)
        reservations.append(new_res)
        return True

    @staticmethod
    def cancel_reservation(reservations, res_id):
        """Eliminación de una reservación del listado de reservaciones"""
        initial_length = len(reservations)
        reservations[:] = [r for r in reservations if r.reservation_id != res_id]
        if len(reservations) < initial_length:
            return True
        print(f"Error: No se encontro la reservación con ID: {res_id}.")
        return False
