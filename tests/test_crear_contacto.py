import pytest
from src.classes.Usuario import Usuario
from src.classes.GestorDeContactos import GestorDeContactos
from src.errors import ErrorNombreVacio, ErrorTelefonoNoNumerico, ErrorCorreoInvalido, ErrorTelefonoMuyLargo

# CASOS NORMALES
def test_crear_contacto_normal():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(1, "Juan Perez", "123456", "juanperez@gmail.com", "Calle 123", "Profesional")
    assert contacto in usuario.contactos

def test_crear_contacto_minimo():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(1, "Juan Perez", "123456")
    assert contacto in usuario.contactos

def test_crear_contacto_sin_categoria():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(1, "Juan Perez", "123456", "juanperez@gmail.com", "Calle 123")
    assert contacto in usuario.contactos


# CASOS EXTREMOS
def test_crear_contacto_nombre_largo():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(1, 'J' * 100, '123456', 'juanperez@gmail.com', 'Calle 123', 'Profesional')
    assert contacto in usuario.contactos

def test_crear_contacto_telefono_largo():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ErrorTelefonoMuyLargo):
        gestor.agregar_contacto(1, 'Juan Perez', '98172398172983712983', 'juanperez@gmail.com', 'Calle 123', 'Profesional')

def test_crear_contacto_email_largo():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(1, 'Juan Perez', '123456', 'j' * 200 + '@gmail.com', 'Calle 123', 'Profesional')
    assert contacto in usuario.contactos


# CASOS DE ERROR
def test_crear_contacto_sin_nombre():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ErrorNombreVacio):
        gestor.agregar_contacto(1, '', '123456', 'juanperez@gmail.com', 'Calle 123', 'Personal')
    
def test_crear_contacto_telefono_no_numerico():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ErrorTelefonoNoNumerico):
        gestor.agregar_contacto(1, 'Juan Perez', 'abc123', 'juanperez@gmail.com', 'Calle 123', 'Personal')

def test_crear_contacto_correo_invalido():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ErrorCorreoInvalido):
        gestor.agregar_contacto(1, 'Juan Perez', '123456', 'juanperezgmail.com', 'Calle 123', 'Personal')