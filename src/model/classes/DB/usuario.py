from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.model.classes.DB.database import Base

class Usuario(Base):
    __tablename__ = "Usuarios"
    
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

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    
    contactos = relationship("Contacto", back_populates="usuario")

    def __repr__(self):
        """
        Devuelve una cadena representativa del usuario.

        Returns:
            str: formato "ID: {id} - Nombre: {nombre} - Email: {email}".
        """
        return f"ID: {self.id} - Nombre: {self.nombre} - Email: {self.email}"