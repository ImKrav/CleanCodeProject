import pytest

from src.classes.Usuario import Usuario
from src.classes.GestorDeContactos import GestorDeContactos

from src.errors import ContactoNoExistente, ErrorTelefonoMuyLargo, ErrorCorreoInvalido, ErrorNombreVacio


# CASOS NORMALES
def test_editar_contacto_nombre():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(1, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal")
    contacto = gestor.editar_contacto(1, nombre='Pepito Pelaez')
    assert contacto.nombre == 'Pepito Pelaez'

def test_editar_contacto_email():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(2, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal")
    contacto = gestor.editar_contacto(2, email='pedritoanimal@hotmail.com')
    assert contacto.email == 'pedritoanimal@hotmail.com'

def test_editar_contacto_categoria():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(3, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal")
    contacto = gestor.editar_contacto(3, categoria='Profesional')
    assert contacto.categoria == 'Profesional'


# CASOS EXTREMOS
def test_editar_contacto_nombre_extremo():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(4, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal")
    nombre_extremo = 'P' * 200
    contacto = gestor.editar_contacto(4, nombre=nombre_extremo)
    assert contacto.nombre == nombre_extremo

def test_editar_contacto_email_extremo():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(5, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal")
    email_extremo = ("P" * 190) + "@gmail.com"
    contacto = gestor.editar_contacto(5, email=email_extremo)
    assert contacto.nombre == email_extremo

def test_editar_contacto_telefono_extremo():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(6, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal")
    telefono_extremo = "9" * 20
    with pytest.raises(ErrorTelefonoMuyLargo):
        gestor.editar_contacto(6, telefono=telefono_extremo)


# CASOS DE ERROR
def test_editar_contacto_inexistente():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ContactoNoExistente):
        gestor.editar_contacto(999, nombre="Juancho")

def test_editar_contacto_nombre_vacio():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(7, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal")
    with pytest.raises(ErrorNombreVacio):
        gestor.editar_contacto(7, nombre="")

def test_editar_contacto_email_invalido():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(8, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal")
    with pytest.raises(ErrorCorreoInvalido):
        gestor.editar_contacto(8, email="pedropelaezgmail.com")