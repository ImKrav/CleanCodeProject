from src.classes.Contacto import Contacto

class Usuario:
    def __init__(self, id: int, nombre: str, email: str, password: str, contactos: list[Contacto]):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.contactos = contactos

    def ver_contactos() -> list[Contacto]:
        pass