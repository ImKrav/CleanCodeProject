import pytest
from src.model.classes.autenticador import Autenticador
from src.model.classes.usuario import Usuario
from src.model.errors import ErrorContrasenaMuyLarga, UsuarioNoExistente, ErrorContrasenaIncorrecta, LoginEspacioVacio


@pytest.fixture
def autenticador():
    return Autenticador()


# CASOS NORMALES
def test_iniciar_sesion_credenciales_correctas(autenticador):
    """
    Caso Normal 1:
    Iniciar sesión con credenciales correctas.
    Resultado: Sesión iniciada correctamente.
    """
    autenticador.usuarios.append(
        Usuario(len(autenticador.usuarios) + 1, "Juan Perez", "juanperez@gmail.com", "password123")
    )
    usuario = autenticador.iniciar_sesion("juanperez@gmail.com", "password123")
    assert usuario is True

def test_iniciar_sesion_email_mayusculas(autenticador):
    """
    Caso Normal 2:
    Iniciar sesión con email en mayúsculas.
    Resultado: Sesión iniciada correctamente.
    """
    autenticador.usuarios.append(
        Usuario(len(autenticador.usuarios) + 1, "Maria Lopez", "maria@gmail.com", "password456")
    )
    usuario = autenticador.iniciar_sesion("MARIA@GMAIL.COM", "password456")
    assert usuario is True

def test_iniciar_sesion_despues_registrarse(autenticador):
    """
    Caso Normal 3:
    Iniciar sesión inmediatamente después de registrarse.
    Resultado: Sesión iniciada correctamente.
    """
    usuario = Usuario(
        len(autenticador.usuarios) + 1, "Pedro Gomez", "pedro@gmail.com", "password789"
    )
    autenticador.registrar_usuario(usuario)
    resultado = autenticador.iniciar_sesion("pedro@gmail.com", "password789")
    assert resultado is True


# CASOS EXTREMOS
def test_iniciar_sesion_contrasena_larga(autenticador):
    """
    Caso Extremo 1:
    Iniciar sesión con una contraseña de 50 caracteres.
    Resultado: Error: La contraseña es muy larga, debe tener como máximo 20 caracteres.
    """
    password_larga = "P" * 50
    autenticador.usuarios.append(
        Usuario(len(autenticador.usuarios) + 1, "Laura Torres", "laurat@gmail.com", password_larga)
    )
    with pytest.raises(ErrorContrasenaMuyLarga):
        autenticador.iniciar_sesion("extremo@gmail.com", password_larga)

def test_iniciar_sesion_muchos_usuarios(autenticador):
    """
    Caso Extremo 2:
    Iniciar sesión después de haber creado 1000 usuarios.
    Resultado: Sesión iniciada correctamente.
    """
    for i in range(1000):
        u = Usuario(
            len(autenticador.usuarios) + 1,
            f"Usuario {i}",
            f"usuario{i}@gmail.com",
            f"password{i}"
        )
        autenticador.registrar_usuario(u)
    assert autenticador.iniciar_sesion("usuario999@gmail.com", "password999") is True

def test_iniciar_sesion_contrasena_caracteres_especiales(autenticador):
    """
    Caso Extremo 3:
    Iniciar sesión con una contraseña con caracteres especiales.
    Resultado: Sesión iniciada correctamente.
    """
    password_especial = "P@$$w0rd!#%&*"
    usuario = Usuario(
        len(autenticador.usuarios) + 1, "Ana Diaz", "ana@gmail.com", password_especial
    )
    autenticador.registrar_usuario(usuario)
    assert autenticador.iniciar_sesion("ana@gmail.com", password_especial) is True


# CASOS DE ERROR
def test_iniciar_sesion_email_inexistente(autenticador):
    """
    Caso de Error 1:
    Iniciar sesión con email inexistente.
    Resultado: Error: El usuario no existe.
    """
    with pytest.raises(UsuarioNoExistente):
        autenticador.iniciar_sesion("noexiste@gmail.com", "password")

def test_iniciar_sesion_contrasena_incorrecta(autenticador):
    """
    Caso de Error 2:
    Iniciar sesión con contraseña incorrecta.
    Resultado: Error: La contraseña es incorrecta.
    """
    usuario = Usuario(
        len(autenticador.usuarios) + 1, "Carlos Ruiz", "carlos@gmail.com", "password123"
    )
    autenticador.registrar_usuario(usuario)
    with pytest.raises(ErrorContrasenaIncorrecta):
        autenticador.iniciar_sesion("carlos@gmail.com", "password")

def test_iniciar_sesion_email_vacio(autenticador):
    """
    Caso de Error 3:
    Iniciar sesión con email vacío.
    Resultado: Error: Faltan campos obligatorios por llenar.
    """
    usuario = Usuario(
        len(autenticador.usuarios) + 1, "Sofia Perez", "sofiperez@gmail.com", "password123"
    )
    autenticador.registrar_usuario(usuario)
    with pytest.raises(LoginEspacioVacio):
        autenticador.iniciar_sesion("", "password123")