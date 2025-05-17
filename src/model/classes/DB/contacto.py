from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.model.classes.DB.database import Base

class Contacto(Base):
    __tablename__ = "Contactos"
    
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

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String)
    direccion = Column(String)
    categoria = Column(String, default='Sin asignar')
    usuario_id = Column(Integer, ForeignKey("Usuarios.id"))
    
    usuario = relationship("Usuario", back_populates="contactos")

    def __repr__(self):
        return f"ID: {self.id} - Nombre: {self.nombre} - Teléfono: {self.telefono} - Email: {self.email} - Dirección: {self.direccion} - Categoría: {self.categoria}"