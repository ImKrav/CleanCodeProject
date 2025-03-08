import pytest

from src.classes.Autenticador import Autenticador
from src.classes.Usuario import Usuario

from src.errors import ErrorCorreoInvalido, ErrorContrasenaVacia, EmailYaExistente, ErrorContrasenaMuyLarga


@pytest.fixture
def autenticador():
    return Autenticador()


# CASOS NORMALES
def test_crear_usuario_normal(autenticador):
    usuario = autenticador.registrar_usuario("Juan Perez", "juanperez@gmail.com", "password123")
    assert isinstance(usuario, Usuario)

def test_crear_usuario_email_corto(autenticador):
    usuario = autenticador.registrar_usuario("Ana Gomez", "a@b.c", "password123")
    assert isinstance(usuario, Usuario)

def test_crear_usuario_password_8_caracteres(autenticador):
    usuario = autenticador.registrar_usuario("Pedro Lopez", "pedro@mail.com", "12345678")
    assert isinstance(usuario, Usuario)


# CASOS EXTREMOS
def test_crear_usuario_nombre_50_caracteres(autenticador):
    nombre_largo = "N" * 50
    usuario = autenticador.registrar_usuario(nombre_largo, "largo@mail.com", "password123")
    assert isinstance(usuario, Usuario)

def test_crear_usuario_password_100_caracteres(autenticador):
    password_larga = "P" * 100
    with pytest.raises(ErrorContrasenaMuyLarga):
        autenticador.registrar_usuario("Maria Sanchez", "maria@mail.com", password_larga)

def test_crear_usuario_email_extremadamente_largo(autenticador):
    prefijo = "e" * 200
    email_largo = f"{prefijo}@example.com"
    usuario = autenticador.registrar_usuario("Carlos Rodriguez", email_largo, "password123")
    assert isinstance(usuario, Usuario)


# CASOS DE ERROR
def test_crear_usuario_email_invalido(autenticador):
    with pytest.raises(ErrorCorreoInvalido):
        autenticador.registrar_usuario("Roberto Diaz", "robertogmail.com", "password123")

def test_crear_usuario_password_vacia(autenticador):
    with pytest.raises(ErrorContrasenaVacia):
        autenticador.registrar_usuario("Laura Martinez", "laura@mail.com", "")

def test_crear_usuario_email_ya_registrado(autenticador):
    autenticador.registrar_usuario("Jose Fernandez", "jose@mail.com", "password123")
    with pytest.raises(EmailYaExistente):
        autenticador.registrar_usuario("Otro Jose", "jose@mail.com", "otraclave123")