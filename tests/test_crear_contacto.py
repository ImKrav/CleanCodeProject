import pytest
from src.model.classes.contacto import Contacto
from src.model.classes.usuario import Usuario
from src.model.classes.gestor_de_contactos import GestorDeContactos
from src.model.errors import (
    ErrorNombreVacio,
    ErrorTelefonoNoNumerico,
    ErrorCorreoInvalido,
    ErrorTelefonoMuyLargo,
)

# CASOS NORMALES
def test_crear_contacto_normal():
    """
    Caso Normal 1:
    Crear contacto con nombre, teléfono, email, dirección y categoría válidos.
    Resultado: Contacto creado correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    
    contacto = gestor.agregar_contacto(Contacto(1, "Juan Perez", "123456", "juanperez@gmail.com", "Calle 123", "Trabajo"))
    assert contacto in usuario.contactos

def test_crear_contacto_minimo():
    """
    Caso Normal 2:
    Crear contacto mínimo (solo con nombre y teléfono).
    Resultado: Contacto creado correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(Contacto(1, "Juan Perez", "123456"))
    assert contacto in usuario.contactos

def test_crear_contacto_sin_categoria():
    """
    Caso Normal 3:
    Crear contacto con categoría vacía.
    Resultado: Contacto creado correctamente (asignado automáticamente a "Sin asignar").
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(Contacto(1, "Juan Perez", "123456", "juanperez@gmail.com", "Calle 123"))
    assert contacto in usuario.contactos


# CASOS EXTREMOS
def test_crear_contacto_nombre_largo():
    """
    Caso Extremo 1:
    Crear contacto con un nombre de 100 caracteres.
    Resultado: Contacto creado correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(Contacto(1, 'J' * 100, '123456', 'juanperez@gmail.com', 'Calle 123', 'Trabajo'))
    assert contacto in usuario.contactos

def test_crear_contacto_telefono_largo():
    """
    Caso Extremo 2:
    Crear contacto con un número de teléfono de 20 dígitos.
    Resultado: Error: El número de teléfono es muy largo (máximo 15 dígitos).
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ErrorTelefonoMuyLargo):
        gestor.agregar_contacto(Contacto(1, 'Juan Perez', '98172398172983712983', 'juanperez@gmail.com', 'Calle 123', 'Trabajo'))

def test_crear_contacto_email_largo():
    """
    Caso Extremo 3:
    Crear contacto con un email extremadamente largo (>200 caracteres).
    Resultado: Contacto creado correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(Contacto(1, 'Juan Perez', '123456', 'j' * 200 + '@gmail.com', 'Calle 123', 'Trabajo'))
    assert contacto in usuario.contactos


# CASOS DE ERROR
def test_crear_contacto_sin_nombre():
    """
    Caso de Error 1:
    Crear contacto sin nombre.
    Resultado: Error: El nombre no puede estar vacío.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ErrorNombreVacio):
        gestor.agregar_contacto(Contacto(1, '', '123456', 'juanperez@gmail.com', 'Calle 123', 'Personal'))
    
def test_crear_contacto_telefono_no_numerico():
    """
    Caso de Error 2:
    Crear contacto con un teléfono no numérico ("abc123").
    Resultado: Error: El teléfono debe ser un valor numérico.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ErrorTelefonoNoNumerico):
        gestor.agregar_contacto(Contacto(1, 'Juan Perez', 'abc123', 'juanperez@gmail.com', 'Calle 123', 'Personal'))

def test_crear_contacto_correo_invalido():
    """
    Caso de Error 3:
    Crear contacto con un email sin "@" o con formato inválido.
    Resultado: Error: El email no tiene un formato válido.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ErrorCorreoInvalido):
        gestor.agregar_contacto(Contacto(1, 'Juan Perez', '123456', 'juanperezgmail.com', 'Calle 123', 'Personal'))