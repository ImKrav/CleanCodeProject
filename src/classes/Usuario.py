from src.classes.Contacto import Contacto

class Usuario:
    def __init__(self, id: int, nombre: str, email: str, password: str):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.contactos : list[Contacto] = []

    def __repr__(self):
        return f"ID: {self.id} - Nombre: {self.nombre} - Email: {self.email}"