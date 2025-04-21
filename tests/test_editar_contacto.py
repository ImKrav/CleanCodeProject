import pytest
from src.model.classes.contacto import Contacto
from src.model.classes.usuario import Usuario
from src.model.classes.gestor_de_contactos import GestorDeContactos
from src.model.errors import ErrorTelefonoNoNumerico, IDNoEncontrado, ErrorTelefonoMuyLargo, ErrorCorreoInvalido, ErrorNombreVacio


# CASOS NORMALES
def test_editar_contacto_nombre():
    """
    Caso Normal 1:
    Editar el nombre de un contacto existente.
    Resultado: Contacto editado correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(Contacto(1, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal"))
    contacto = gestor.editar_contacto(Contacto(1, "Pepito Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal"))
    assert contacto.nombre == 'Pepito Pelaez'

def test_editar_contacto_email():
    """
    Caso Normal 2:
    Editar el email de un contacto existente.
    Resultado: Contacto editado correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(Contacto(2, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal"))
    contacto = gestor.editar_contacto(Contacto(2, "Pedro Pelaez", "123456", "pedritoanimal@hotmail.com", "Calle 321", "Personal"))
    assert contacto.email == 'pedritoanimal@hotmail.com'

def test_editar_contacto_categoria():
    """
    Caso Normal 3:
    Editar la categoría de un contacto sin cambiar otros datos.
    Resultado: Contacto editado correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    contacto = gestor.agregar_contacto(Contacto(3, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal"))
    contacto = gestor.editar_contacto(Contacto(3, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Trabajo"))
    assert contacto.categoria == 'Trabajo'


# CASOS EXTREMOS
def test_editar_contacto_nombre_extremo():
    """
    Caso Extremo 1:
    Editar el nombre con 200 caracteres.
    Resultado: Contacto editado correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    nombre_extremo = 'P' * 200
    contacto = gestor.agregar_contacto(Contacto(4, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal"))
    contacto = gestor.editar_contacto(Contacto(4, nombre_extremo, "123456", "pedropelaez@gmail.com", "Calle 321", "Personal"))
    assert contacto.nombre == nombre_extremo

def test_editar_contacto_email_extremo():
    """
    Caso Extremo 2:
    Editar el email con más de 190 caracteres.
    Resultado: Contacto editado correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    email_extremo = ("P" * 190) + "@gmail.com"
    contacto = gestor.agregar_contacto(Contacto(5, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal"))
    contacto = gestor.editar_contacto(Contacto(5, "Pedro Pelaez", "123456", email_extremo, "Calle 321", "Personal"))
    assert contacto.email == email_extremo

def test_editar_contacto_telefono_extremo():
    """
    Caso Extremo 3:
    Editar el teléfono con 20 dígitos.
    Resultado: Error: El número de teléfono es muy largo (máximo 15 dígitos).
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    telefono_extremo = "9" * 20
    gestor.agregar_contacto(Contacto(6, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal"))
    with pytest.raises(ErrorTelefonoMuyLargo):
        gestor.editar_contacto(Contacto(6, "Pedro Pelaez", telefono_extremo, "pedropelaez@gmail.com", "Calle 321", "Personal"))


# CASOS DE ERROR
def test_editar_contacto_inexistente():
    """
    Caso de Error 1:
    Editar un contacto que no existe.
    Resultado: Error: El contacto no existe.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    with pytest.raises(IDNoEncontrado):
        gestor.editar_contacto(Contacto(999, "Juanchito", "123456", "juanchito@gmail.com", "Calle 123", "Personal"))

def test_editar_contacto_telefono_no_numerico():
    """
    Caso de Error 2:
    Editar un contacto con un teléfono que contiene caracteres no numéricos.
    Resultado: Error: El teléfono debe contener solo dígitos.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    gestor.agregar_contacto(Contacto(9, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal"))
    with pytest.raises(ErrorTelefonoNoNumerico):
        gestor.editar_contacto(Contacto(9, "Pedro Pelaez", "123ABC456", "pedropelaez@gmail.com", "Calle 321", "Personal"))

def test_editar_contacto_email_invalido():
    """
    Caso de Error 3:
    Editar un contacto con un email inválido.
    Resultado: Error: El email no tiene un formato válido.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorDeContactos(usuario)
    gestor.agregar_contacto(Contacto(8, "Pedro Pelaez", "123456", "pedropelaez@gmail.com", "Calle 321", "Personal"))
    with pytest.raises(ErrorCorreoInvalido):
        gestor.editar_contacto(Contacto(8, "Pedro Pelaez", "123456", "pedropelaezgmail.com", "Calle 321", "Personal"))