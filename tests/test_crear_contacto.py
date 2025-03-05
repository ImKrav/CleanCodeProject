import pytest

from src.classes.Usuario import Usuario
from src.classes.GestorDeContactos import GestorDeContactos
from src.errors import ErrorNombreVacio, ErrorTelefonoNoNumerico, ErrorCorreoInvalido

usuario = Usuario(1, "user", "user@email.com", "anotherpass")

# CASOS NORMALES
def test_crear_contacto_normal():
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(1, "Juan Perez", "123456", "juanperez@gmail.com", "Calle 123", "Amigo")
    assert contacto.nombre == "Juan Perez"
    assert contacto.telefono == "123456"
    assert contacto.email == "juanperez@gmail.com"
    assert contacto.direccion == "Calle 123"
    assert contacto.categoria == "Amigo"

def test_crear_contacto_minimo():
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(1, "Juan Perez", "123456", "", "", "")
    assert contacto.nombre == "Juan Perez"
    assert contacto.telefono == "123456"
    assert contacto.email == ""
    assert contacto.direccion == ""
    assert contacto.categoria == ""

def test_crear_contacto_sin_categoria():
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(1, "Juan Perez", "123456", "juanperez@gmail.com", "Calle 123", "")
    assert contacto.nombre == "Juan Perez"
    assert contacto.telefono == "123456"
    assert contacto.email == "juanperez@gmail.com"
    assert contacto.direccion == "Calle 123"
    assert contacto.categoria == ""

# CASOS EXTREMOS
def test_crear_contacto_nombre_largo():
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(1, 'J' * 100, '123456', 'juanperez@gmail.com', 'Calle 123', 'Amigo')
    assert len(contacto.nombre) == 100

def test_crear_contacto_telefono_largo():
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(1, 'Juan Perez', '55555555555555555555', 'juanperez@gmail.com', 'Calle 123', 'Amigo')
    assert len(contacto.telefono) == 20

def test_crear_contacto_email_largo():
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(1, 'Juan Perez', '123456', 'j' * 200 + '@gmail.com', 'Calle 123', 'Amigo')
    assert len(contacto.email) == 210

# CASOS DE ERROR
def test_crear_contacto_sin_nombre():
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ErrorNombreVacio):
        gestor.agregar_contacto(1, '', '123456', 'juanperez@gmail.com', 'Calle 123', 'Amigo')
    
def test_crear_contacto_telefono_no_numerico():
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ErrorTelefonoNoNumerico):
        gestor.agregar_contacto(1, 'Juan Perez', 'abc123', 'juanperez@gmail.com', 'Calle 123', 'Amigo')

def test_crear_contacto_correo_invalido():
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ErrorCorreoInvalido):
        gestor.agregar_contacto(1, 'Juan Perez', '123456', 'juanperezgmail.com', 'Calle 123', 'Amigo')