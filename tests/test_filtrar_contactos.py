import pytest
from src.classes.Usuario import Usuario
from src.classes.GestorDeContactos import GestorDeContactos
from src.errors import ErrorNombreVacio, CategoriaNoExistente

# CASOS NORMALES
def test_filtrar_contactos_nombre_exacto():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contactos = gestor.filtrar_contacto(nombre="Juan Perez")
    
    for contacto in contactos:
        assert contacto.nombre == "Juan Perez"

def test_filtrar_contactos_categoria():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contactos = gestor.filtrar_contacto(categoria="Personal")
    
    for contacto in contactos:
        assert contacto.categoria == "Personal"

def test_filtrar_contactos_nombre_parcial():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contactos = gestor.filtrar_contacto(nombre="Juan")
    
    for contacto in contactos:
        assert "Juan" in contacto.nombre


# CASOS EXTREMOS
def test_filtrar_contactos_nombre_largo():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    nombre_largo = "N" * 50
    contactos = gestor.filtrar_contacto(nombre=nombre_largo)
    
    for contacto in contactos:
        assert contacto.nombre == nombre_largo

def test_filtrar_contactos_categoria_vacia():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contactos = gestor.filtrar_contacto(categoria="")
    
    for contacto in contactos:
        assert contacto.categoria == "Sin asignar"

def test_filtrar_contactos_nombre_caracteres_especiales():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    nombre_especial = "Juán Pérez #$%&/()"
    contactos = gestor.filtrar_contacto(nombre=nombre_especial)
    
    for contacto in contactos:
        assert contacto.nombre == nombre_especial


# CASOS DE ERROR
def test_filtrar_contactos_nombre_vacio():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    
    with pytest.raises(ErrorNombreVacio):
        gestor.filtrar_contacto(nombre="")

def test_filtrar_contactos_categoria_inexistente():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(CategoriaNoExistente):
        gestor.filtrar_contacto(categoria="Amigo")
    
def test_filtrar_contactos_tipo_dato_incorrecto():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(TypeError):
        gestor.filtrar_contacto(nombre=12345)