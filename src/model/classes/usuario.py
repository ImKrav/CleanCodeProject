from dataclasses import dataclass, field
from src.model.classes.contacto import Contacto

@dataclass
class Usuario:
    
    """
    Representa un usuario de la aplicación.
    ---------------------------------------------------------
    Atributos:
        id (int): Identificador único.
        nombre (str): Nombre de usuario.
        email (str): Correo electrónico.
        password (str): Contraseña.
        contactos (list[Contacto]): lista de contactos del usuario.
    """

    id: int
    nombre: str
    email: str
    password: str
    contactos: list[Contacto] = field(default_factory=list)

    def __repr__(self):
        """
        Devuelve una cadena representativa del usuario.

        Returns:
            str: formato "ID: {id} - Nombre: {nombre} - Email: {email}".
        """
        return f"ID: {self.id} - Nombre: {self.nombre} - Email: {self.email}"