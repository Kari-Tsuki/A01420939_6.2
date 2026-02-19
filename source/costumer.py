"""
customer.py

Este programa gestiona la clase customer. Incluye funciones de
creación, eliminación, muestreo y modificacion.
"""

import json
import os

class Customer:
    """Clase para la administración de los clientes"""

    def __init__(self, customer_id, name, email):
        """Se crea un nuevo objeto 'customer'"""
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convierte el objeto 'Customer' en un diccionario"""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
        }

    @staticmethod
    def save_to_file(customers, filename="customers.json"):
        """Guardar la lista de customers en un archivo JSON"""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump([c.to_dict() for c in customers], f, indent=4)
        except IOError as e:
            print(f"Error, no se pudo guardar el archivo: {e}.")

    @staticmethod
    def load_from_file(filename="customers.json"):
        """Cargar la lista de clientes de un archivo JSON"""
        if not os.path.exists(filename):
            return []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Customer(**c) for c in data]
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            print(f"Error, no se pudo leer el archivo {filename}: {e}.")
            return []

    @staticmethod
    def create_customer(customers, customer_id, name, email):
        """Creación e incorporación de un nuevo cliente"""
        if any(c.customer_id == customer_id for c in customers):
            print(f"Error, el ID del cliente {customer_id} ya existe.")
            return False
        new_customer = Customer(customer_id, name, email)
        customers.append(new_customer)
        return True

    @staticmethod
    def delete_customer(customers, customer_id):
        """Eliminación de un cliente del listado de clientes"""
        initial_length = len(customers)
        customers[:] = [c for c in customers if c.customer_id != customer_id]
        if len(customers) < initial_length:
            return True
        print(f"Error, no se encontro el cliente con el ID {customer_id}.")
        return False

    def display_info(self):
        """Muestra la información de la instancia actual"""
        print(f"ID: {self.customer_id} | Cliente: {self.name} | "
              f"Email: {self.email}")

    @staticmethod
    def display_customer(customers, customer_id):
        """Muestra la información de un cliente"""
        for customer in customers:
            if customer.customer_id == customer_id:
                customer.display_info()
                return True
        print(f"Error, no se encontro un cliente con el ID: {customer_id}.")
        return False

    def modify_customer(self, name=None, email=None):
        """Modifica los datos de un cliente"""
        if name:
            self.name = name
        if email:
            self.email = email
