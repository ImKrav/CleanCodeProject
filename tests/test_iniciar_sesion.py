import pytest
from src.classes.Autenticador import Autenticador
from src.classes.Usuario import Usuario
from src.errors import ErrorContrasenaMuyLarga, UsuarioNoExistente, ErrorContrasenaIncorrecta, LoginEspacioVacio

@pytest.fixture
def autenticador():
    return Autenticador()


# CASOS NORMALES
def test_iniciar_sesion_credenciales_correctas(autenticador):
    autenticador.registrar_usuario("Juan Perez", "juanperez@gmail.com", "password123")
    
    usuario = autenticador.iniciar_sesion("juanperez@gmail.com", "password123")
    assert isinstance(usuario, Usuario)

def test_iniciar_sesion_email_mayusculas(autenticador):
    autenticador.registrar_usuario("Maria Lopez", "maria@gmail.com", "password456")
    usuario = autenticador.iniciar_sesion("MARIA@GMAIL.COM", "password456")
    assert isinstance(usuario, Usuario)

def test_iniciar_sesion_despues_registrarse(autenticador):
    autenticador.registrar_usuario("Pedro Gomez", "pedro@gmail.com", "password789")
    
    usuario = autenticador.iniciar_sesion("pedro@gmail.com", "password789")
    assert isinstance(usuario, Usuario)


# CASOS EXTREMOS
def test_iniciar_sesion_contrasena_larga(autenticador):
    password_larga = "P" * 50
    with pytest.raises(ErrorContrasenaMuyLarga):
        autenticador.iniciar_sesion("extremo@gmail.com", password_larga)

def test_iniciar_sesion_muchos_usuarios(autenticador):
    for i in range(1000):
        autenticador.registrar_usuario(f"Usuario {i}", f"usuario{i}@gmail.com", f"password{i}")
    
    usuario = autenticador.iniciar_sesion("usuario999@gmail.com", "password999")
    assert isinstance(usuario, Usuario)

def test_iniciar_sesion_contrasena_caracteres_especiales(autenticador):
    password_especial = "P@$$w0rd!#%&*"
    autenticador.registrar_usuario("Ana Diaz", "ana@gmail.com", password_especial)
    usuario = autenticador.iniciar_sesion("ana@gmail.com", password_especial)
    assert isinstance(usuario, Usuario)


# CASOS DE ERROR
def test_iniciar_sesion_email_inexistente(autenticador):
    with pytest.raises(UsuarioNoExistente):
        autenticador.iniciar_sesion("noexiste@gmail.com", "cualquierpassword")

def test_iniciar_sesion_contrasena_incorrecta(autenticador):
    autenticador.registrar_usuario("Carlos Ruiz", "carlos@gmail.com", "password123")
    with pytest.raises(ErrorContrasenaIncorrecta):
        autenticador.iniciar_sesion("carlos@gmail.com", "passwordincorrecta")

def test_iniciar_sesion_email_vacio(autenticador):
    with pytest.raises(LoginEspacioVacio):
        autenticador.iniciar_sesion("", "password123")