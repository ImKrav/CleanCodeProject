import pytest
from src.classes.Autenticador import Autenticador
from src.classes.Usuario import Usuario
from src.errors import ErrorContrasenaMuyLarga, UsuarioNoExistente, ErrorContrasenaIncorrecta, LoginEspacioVacio


@pytest.fixture
def autenticador():
    return Autenticador()


# CASOS NORMALES
def test_iniciar_sesion_credenciales_correctas(autenticador):
    autenticador.usuarios.append(Usuario(len(autenticador.usuarios) + 1, "Juan Perez", "juanperez@gmail.com", "password123"))
    usuario = autenticador.iniciar_sesion("juanperez@gmail.com", "password123")
    assert usuario == True

def test_iniciar_sesion_email_mayusculas(autenticador):
    autenticador.usuarios.append(Usuario(len(autenticador.usuarios) + 1, "Maria Lopez", "maria@gmail.com", "password456"))
    usuario = autenticador.iniciar_sesion("MARIA@GMAIL.COM", "password456")
    assert usuario == True

def test_iniciar_sesion_despues_registrarse(autenticador):
    usuario = Usuario(len(autenticador.usuarios) + 1, "Pedro Gomez", "pedro@gmail.com", "password789")
    autenticador.registrar_usuario(usuario)
    usuario = autenticador.iniciar_sesion("pedro@gmail.com", "password789")
    assert usuario == True


# CASOS EXTREMOS
def test_iniciar_sesion_contrasena_larga(autenticador):
    password_larga = "P" * 50
    autenticador.usuarios.append(Usuario(len(autenticador.usuarios) + 1, "Laura Torres", "laurat@gmail.com", password_larga))
    with pytest.raises(ErrorContrasenaMuyLarga):
        autenticador.iniciar_sesion("extremo@gmail.com", password_larga)

def test_iniciar_sesion_muchos_usuarios(autenticador):
    for i in range(1000):
        usuario = Usuario(len(autenticador.usuarios) + 1, f"Usuario {i}", f"usuario{i}@gmail.com", f"password{i}")
        autenticador.registrar_usuario(usuario)
    
    usuario = autenticador.iniciar_sesion("usuario999@gmail.com", "password999")
    assert usuario is True

def test_iniciar_sesion_contrasena_caracteres_especiales(autenticador):
    password_especial = "P@$$w0rd!#%&*"
    usuario = Usuario(len(autenticador.usuarios) + 1, "Ana Diaz", "ana@gmail.com", password_especial)
    autenticador.registrar_usuario(usuario)
    usuario = autenticador.iniciar_sesion("ana@gmail.com", password_especial)
    assert usuario is True


# CASOS DE ERROR
def test_iniciar_sesion_email_inexistente(autenticador):
    with pytest.raises(UsuarioNoExistente):
        autenticador.iniciar_sesion("noexiste@gmail.com", "password")

def test_iniciar_sesion_contrasena_incorrecta(autenticador):
    usuario = Usuario(len(autenticador.usuarios) + 1, "Carlos Ruiz", "carlos@gmail.com", "password123")
    autenticador.registrar_usuario(usuario)
    with pytest.raises(ErrorContrasenaIncorrecta):
        autenticador.iniciar_sesion("carlos@gmail.com", "password")

def test_iniciar_sesion_email_vacio(autenticador):
    usuario = Usuario(len(autenticador.usuarios) + 1, "Sofia Perez", "sofiperez@gmail.com", "password123")
    autenticador.registrar_usuario(usuario)
    with pytest.raises(LoginEspacioVacio):
        autenticador.iniciar_sesion("", "password123")