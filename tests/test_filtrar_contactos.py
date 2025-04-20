import pytest
from src.classes.usuario import Usuario
from src.classes.gestor_de_contactos import GestorDeContactos
from src.errors import ErrorNombreVacio, CategoriaNoExistente


# CASOS NORMALES
def test_filtrar_contactos_nombre_exacto():
    """
    Caso Normal 1:
    Filtrar contactos por nombre exacto.
    Resultado: Contactos filtrados correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contactos = gestor.filtrar_contacto(nombre="Juan Perez")
    
    for contacto in contactos:
        assert contacto.nombre == "Juan Perez"

def test_filtrar_contactos_categoria():
    """
    Caso Normal 2:
    Filtrar contactos por una categoría específica.
    Resultado: Contactos filtrados correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contactos = gestor.filtrar_contacto(categoria="Personal")
    
    for contacto in contactos:
        assert contacto.categoria == "Personal"

def test_filtrar_contactos_nombre_y_categoria():
    """
    Caso Normal 3:
    Filtrar contactos por nombre parcial y categoría.
    Resultado: Contactos filtrados correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contactos = gestor.filtrar_contacto(nombre="Juan", categoria="Personal")
    
    for contacto in contactos:
        assert "Juan" in contacto.nombre


# CASOS EXTREMOS
def test_filtrar_contactos_nombre_largo():
    """
    Caso Extremo 1:
    Filtrar contactos con un nombre de 50 caracteres.
    Resultado: Contactos filtrados correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    nombre_largo = "N" * 50
    contactos = gestor.filtrar_contacto(nombre=nombre_largo)
    
    for contacto in contactos:
        assert contacto.nombre == nombre_largo

def test_filtrar_contactos_categoria_vacia():
    """
    Caso Extremo 2:
    Filtrar contactos con categoría vacía (solo nombre).
    Resultado: Contactos filtrados correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contactos = gestor.filtrar_contacto(nombre="Antonio")
    
    for contacto in contactos:
        assert contacto.nombre == "Antonio"

def test_filtrar_contactos_nombre_caracteres_especiales():
    """
    Caso Extremo 3:
    Filtrar contactos con un nombre con caracteres especiales.
    Resultado: Contactos filtrados correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    nombre_especial = "Juán Pérez #$%&/()"
    contactos = gestor.filtrar_contacto(nombre=nombre_especial)
    
    for contacto in contactos:
        assert contacto.nombre == nombre_especial


# CASOS DE ERROR
def test_filtrar_contactos_sin_datos():
    """
    Caso de Error 1:
    Filtrar sin nombre ni categoría.
    Resultado: Error ValueError, se debe proporcionar nombre o categoría.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    
    with pytest.raises(ValueError):
        gestor.filtrar_contacto(nombre="", categoria="")

def test_filtrar_contactos_categoria_inexistente():
    """
    Caso de Error 2:
    Filtrar con una categoría inexistente.
    Resultado: Error CategoriaNoExistente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(CategoriaNoExistente):
        gestor.filtrar_contacto(categoria="Amigo")
    
def test_filtrar_contactos_tipo_dato_incorrecto():
    """
    Caso de Error 3:
    Filtrar con tipo de dato incorrecto para nombre.
    Resultado: Error TypeError.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(TypeError):
        gestor.filtrar_contacto(nombre=12345)