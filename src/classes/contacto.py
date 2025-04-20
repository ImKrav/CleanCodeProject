from dataclasses import dataclass
from typing import Optional

@dataclass
class Contacto:
    
    """
    Representa un contacto con los campos necesarios para su gestión.
    ---------------------------------------------------------
    Atributos:
        id (int): Identificador único del contacto.
        nombre (str): Nombre del contacto.
        telefono (str): Número de teléfono del contacto.
        email (str): Correo electrónico del contacto.
        direccion (str): Dirección del contacto.
        categoria (str): Categoría del contacto.
    """

    id: int
    nombre: str
    telefono: str
    email: Optional[str] = None
    direccion: Optional[str] = None
    categoria: Optional[str] = 'Sin asignar'

    def __repr__(self):
        return f"ID: {self.id} - Nombre: {self.nombre} - Teléfono: {self.telefono} - Email: {self.email} - Dirección: {self.direccion} - Categoría: {self.categoria}"