import pytest

from src.classes.Contacto import Contacto
from src.classes.Usuario import Usuario
from src.classes.Autenticador import Autenticador
from src.classes.GestorDeContactos import GestorDeContactos
from src.classes.GestorVCF import GestorVCF
from src.errors import ErrorNombreVacio

usuario = Usuario(1, "user", "user@email.com", "anotherpass")

def test_filtrar_contactos_nombre_exacto():
    gestor = GestorDeContactos(usuario)
    contactos = gestor.filtrar_contacto(nombre="Juan Perez")
    
    for contacto in contactos:
        assert contacto.nombre == "Juan Perez"

def test_filtrar_contactos_categoria():
    gestor = GestorDeContactos(usuario)
    contactos = gestor.filtrar_contacto(categoria="Amigo")
    
    for contacto in contactos:
        assert contacto.categoria == "Amigo"

def test_filtrar_contactos_nombre_parcial():
    gestor = GestorDeContactos(usuario)
    contactos = gestor.filtrar_contacto(nombre_parcial="Juan")
    
    for contacto in contactos:
        assert "Juan" in contacto.nombre


def test_filtrar_contactos_nombre_largo():
    gestor = GestorDeContactos(usuario)
    nombre_largo = "N" * 50
    contactos = gestor.filtrar_contacto(nombre=nombre_largo)
    
    for contacto in contactos:
        assert contacto.nombre == nombre_largo
        assert len(contacto.nombre) == 50

def test_filtrar_contactos_categoria_inexistente():
    gestor = GestorDeContactos(usuario)
    contactos = gestor.filtrar_contacto(categoria="CategoriaQueNoExiste")
    
    assert len(contactos) == 0

def test_filtrar_contactos_nombre_caracteres_especiales():
    gestor = GestorDeContactos(usuario)
    nombre_especial = "Juán Pérez #$%&/()"
    contactos = gestor.filtrar_contacto(nombre=nombre_especial)
    
    for contacto in contactos:
        assert contacto.nombre == nombre_especial

def test_filtrar_contactos_nombre_vacio():
    gestor = GestorDeContactos(usuario)
    
    with pytest.raises(ErrorNombreVacio):
        gestor.filtrar_contacto(nombre="")

def test_filtrar_contactos_categoria_vacia():
    gestor = GestorDeContactos(usuario)
    
    contactos = gestor.filtrar_contacto(categoria="")
    
    assert isinstance(contactos, list)

def test_filtrar_contactos_tipo_dato_incorrecto():
    pass