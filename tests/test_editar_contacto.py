import pytest

from src.classes.Contacto import Contacto
from src.classes.Usuario import Usuario
from src.classes.Autenticador import Autenticador
from src.classes.GestorDeContactos import GestorDeContactos
from src.classes.GestorVCF import GestorVCF

usuario = Usuario(1, "user", "user@email.com", "anotherpass")

def test_editar_contacto_nombre():
    gestor = GestorDeContactos(usuario)
    contacto = gestor.editar_contacto(1, nombre='Pepito Pelaez')
    assert contacto.nombre == 'Pepito Pelaez'

def test_editar_contacto_email():
    gestor = GestorDeContactos(usuario)
    contacto = gestor.editar_contacto(2, email='nuevo_email@example.com')
    assert contacto.email == 'nuevo_email@example.com'

def test_editar_contacto_categoria():
    gestor = GestorDeContactos(usuario)
    contacto = gestor.editar_contacto(3, categoria='Personal')
    assert contacto.categoria == 'Personal'


def test_editar_contacto_nombre_extremo():
    gestor = GestorDeContactos(usuario)
    nombre_extremo = "N" * 100
    contacto = gestor.editar_contacto(4, nombre=nombre_extremo)
    assert len(contacto.nombre) == 100

def test_editar_contacto_email_extremo():
    gestor = GestorDeContactos(usuario)
    email_extremo = ("e" * 190) + "@gmail.com"
    contacto = gestor.editar_contacto(5, email=email_extremo)
    assert len(contacto.email) >= 200

def test_editar_contacto_telefono_extremo():
    gestor = GestorDeContactos(usuario)
    telefono_extremo = "9" * 20
    contacto = gestor.editar_contacto(6, telefono=telefono_extremo)
    assert len(contacto.telefono) == 20

def test_editar_contacto_inexistente():
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ValueError):
        gestor.editar_contacto(999, nombre="Contacto Inexistente")

def test_editar_contacto_nombre_vacio():
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ValueError):
        gestor.editar_contacto(7, nombre="")

def test_editar_contacto_email_invalido():
    gestor = GestorDeContactos(usuario)
    with pytest.raises(ValueError):
        gestor.editar_contacto(8, email="correo-invalido")