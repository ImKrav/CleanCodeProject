import pytest
from src.classes.Autenticador import Autenticador
from src.classes.Usuario import Usuario
from src.errors import ErrorCorreoInvalido, ErrorContrasenaVacia, EmailYaExistente, ErrorContrasenaMuyLarga


@pytest.fixture
def autenticador():
    return Autenticador()


# CASOS NORMALES
def test_crear_usuario_normal(autenticador):
    usuario = Usuario(len(autenticador.usuarios) + 1, "Juan Perez", "juanperez@gmail.com", "password123")
    autenticador.registrar_usuario(usuario)
    assert usuario in autenticador.usuarios

def test_crear_usuario_email_corto(autenticador):
    usuario = Usuario(len(autenticador.usuarios) + 1, "Ana Gomez", "a@b.c", "password123")
    autenticador.registrar_usuario(usuario)
    assert usuario in autenticador.usuarios

def test_crear_usuario_password_8_caracteres(autenticador):
    usuario = Usuario(len(autenticador.usuarios) + 1, "Pedro Lopez", "pedro@mail.com", "12345678")
    autenticador.registrar_usuario(usuario)
    assert usuario in autenticador.usuarios


# CASOS EXTREMOS
def test_crear_usuario_nombre_50_caracteres(autenticador):
    nombre_largo = "N" * 50
    usuario = Usuario(len(autenticador.usuarios) + 1, nombre_largo, "largo@mail.com", "password123")
    autenticador.registrar_usuario(usuario)
    assert usuario in autenticador.usuarios

def test_crear_usuario_password_100_caracteres(autenticador):
    password_larga = "P" * 100
    with pytest.raises(ErrorContrasenaMuyLarga):
        usuario = Usuario(len(autenticador.usuarios) + 1, "Maria Sanchez", "maria@mail.com", password_larga)
        autenticador.registrar_usuario(usuario)

def test_crear_usuario_email_extremadamente_largo(autenticador):
    prefijo = "e" * 200
    email_largo = f"{prefijo}@example.com"
    usuario = Usuario(len(autenticador.usuarios) + 1, "Carlos Rodriguez", email_largo, "password123")
    autenticador.registrar_usuario(usuario)
    assert usuario in autenticador.usuarios


# CASOS DE ERROR
def test_crear_usuario_email_invalido(autenticador):
    usuario = Usuario(len(autenticador.usuarios) + 1, "Roberto Diaz", "robertogmail.com", "password123")
    with pytest.raises(ErrorCorreoInvalido):
        autenticador.registrar_usuario(usuario)

def test_crear_usuario_password_vacia(autenticador):
    usuario = Usuario(len(autenticador.usuarios) + 1, "Laura Martinez", "laura@mail.com", "")
    with pytest.raises(ErrorContrasenaVacia):
        autenticador.registrar_usuario(usuario)

def test_crear_usuario_email_ya_registrado(autenticador):
    usuario1 = Usuario(len(autenticador.usuarios) + 1, "Jose Fernandez", "jose@mail.com", "password123")
    usuario2 = Usuario(len(autenticador.usuarios) + 1, "Otro Jose", "jose@mail.com", "otraclave123")
    with pytest.raises(EmailYaExistente):
        autenticador.registrar_usuario(usuario1)
        autenticador.registrar_usuario(usuario2)