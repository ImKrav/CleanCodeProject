import pytest
from src.model.classes.autenticador import Autenticador
from src.model.classes.usuario import Usuario
from src.model.errors import ErrorCorreoInvalido, ErrorContrasenaVacia, EmailYaExistente, ErrorContrasenaMuyLarga

@pytest.fixture
def autenticador():
    """Proporciona una instancia limpia de Autenticador para cada test."""
    return Autenticador()


# CASOS NORMALES
def test_crear_usuario_normal(autenticador):
    """
    Caso Normal 1:
    Crear usuario con nombre, email y contraseña válidos.
    Resultado: Usuario creado correctamente.
    """
    usuario = Usuario(len(autenticador.usuarios) + 1, "Juan Perez", "juanperez@gmail.com", "password123")
    autenticador.registrar_usuario(usuario)
    assert usuario in autenticador.usuarios

def test_crear_usuario_email_corto(autenticador):
    """
    Caso Normal 2:
    Crear usuario con un email corto pero válido (p.ej. a@b.c).
    Resultado: Usuario creado correctamente.
    """
    usuario = Usuario(len(autenticador.usuarios) + 1, "Ana Gomez", "a@b.c", "password123")
    autenticador.registrar_usuario(usuario)
    assert usuario in autenticador.usuarios

def test_crear_usuario_password_8_caracteres(autenticador):
    """
    Caso Normal 3:
    Crear usuario con una contraseña de 8 caracteres.
    Resultado: Usuario creado correctamente.
    """
    usuario = Usuario(len(autenticador.usuarios) + 1, "Pedro Lopez", "pedro@mail.com", "12345678")
    autenticador.registrar_usuario(usuario)
    assert usuario in autenticador.usuarios


# CASOS EXTREMOS
def test_crear_usuario_nombre_50_caracteres(autenticador):
    """
    Caso Extremo 1:
    Crear usuario con un nombre de 50 caracteres.
    Resultado: Usuario creado correctamente.
    """
    nombre_largo = "N" * 50
    usuario = Usuario(len(autenticador.usuarios) + 1, nombre_largo, "largo@mail.com", "password123")
    autenticador.registrar_usuario(usuario)
    assert usuario in autenticador.usuarios

def test_crear_usuario_password_100_caracteres(autenticador):
    """
    Caso Extremo 2:
    Crear usuario con una contraseña de 100 caracteres.
    Resultado: Error: La contraseña es muy larga, debe tener como máximo 15 caracteres.
    """
    password_larga = "P" * 100
    with pytest.raises(ErrorContrasenaMuyLarga):
        usuario = Usuario(len(autenticador.usuarios) + 1, "Maria Sanchez", "maria@mail.com", password_larga)
        autenticador.registrar_usuario(usuario)

def test_crear_usuario_email_extremadamente_largo(autenticador):
    """
    Caso Extremo 3:
    Crear usuario con un email extremadamente largo (>200 caracteres).
    Resultado: Usuario creado correctamente.
    """
    prefijo = "e" * 200
    email_largo = f"{prefijo}@example.com"
    usuario = Usuario(len(autenticador.usuarios) + 1, "Carlos Rodriguez", email_largo, "password123")
    autenticador.registrar_usuario(usuario)
    assert usuario in autenticador.usuarios


# CASOS DE ERROR
def test_crear_usuario_email_invalido(autenticador):
    """
    Caso de Error 1:
    Crear usuario con email inválido (sin '@').
    Resultado: Error: El email no tiene un formato válido.
    """
    usuario = Usuario(len(autenticador.usuarios) + 1, "Roberto Diaz", "robertogmail.com", "password123")
    with pytest.raises(ErrorCorreoInvalido):
        autenticador.registrar_usuario(usuario)

def test_crear_usuario_password_vacia(autenticador):
    """
    Caso de Error 2:
    Crear usuario con contraseña vacía.
    Resultado: Error: La contraseña no puede estar vacía.
    """
    usuario = Usuario(len(autenticador.usuarios) + 1, "Laura Martinez", "laura@mail.com", "")
    with pytest.raises(ErrorContrasenaVacia):
        autenticador.registrar_usuario(usuario)

def test_crear_usuario_email_ya_registrado(autenticador):
    """
    Caso de Error 3:
    Crear usuario con un email ya registrado.
    Resultado: Error: El email ya está registrado.
    """
    usuario1 = Usuario(len(autenticador.usuarios) + 1, "Jose Fernandez", "jose@mail.com", "password123")
    usuario2 = Usuario(len(autenticador.usuarios) + 1, "Otro Jose", "jose@mail.com", "otraclave123")
    with pytest.raises(EmailYaExistente):
        autenticador.registrar_usuario(usuario1)
        autenticador.registrar_usuario(usuario2)