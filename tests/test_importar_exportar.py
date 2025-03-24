import pytest
import os
from src.classes.Usuario import Usuario
from src.classes.Contacto import Contacto
from src.classes.GestorVCF import GestorVCF
from src.errors import ErrorListaVaciaDeContactos, ErrorArchivoCorrupto, ErrorNoVCF, ErrorPermisosDeEscritura

# CASOS NORMALES
def test_exportar_lista_con_5_contactos():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    usuario.contactos = [Contacto(i, f"Contacto {i}", "123456789", "contacto@email.com", "Calle Falsa 123", "Trabajo") for i in range(5)]
    gestor.exportar_contactos(usuario.contactos, "contactos.vcf")
    assert os.path.exists("contactos.vcf")

def test_importar_archivo_vcf_valido_con_3_contactos():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    gestor.importar_contactos("3_contactos.vcf")
    assert len(usuario.contactos) == 3

def test_exportar_contactos_con_caracteres_especiales():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    usuario.contactos = [
        Contacto(1, "José", "123456789", "jose@email.com", "Calle A", "Trabajo"),
        Contacto(2, "María", "987654321", "maria@email.com", "Calle B", "Amigos"),
        Contacto(3, "El Triple #$%&", "555123456", "triple@email.com", "Calle C", "Personal"),
    ]
    gestor.exportar_contactos(usuario.contactos, "contactos_especiales.vcf")
    assert os.path.exists("contactos_especiales.vcf")


# CASOS EXTREMOS
def test_exportar_lista_con_1000_contactos():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    usuario.contactos = [Contacto(i, f"Contacto {i}", "123456789", "contacto@email.com", "Calle Falsa 123", "Trabajo") for i in range(1000)]
    gestor.exportar_contactos(usuario.contactos, "contactos_1000.vcf")
    assert os.path.exists("contactos_1000.vcf")

def test_importar_archivo_vcf_con_500_contactos():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    gestor.importar_contactos("500_contactos.vcf")
    assert len(usuario.contactos) == 500

def test_exportar_lista_vacia_de_contactos():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    usuario.contactos = []
    with pytest.raises(ErrorListaVaciaDeContactos):
        gestor.exportar_contactos(usuario.contactos, "contactos_vacios.vcf")


# CASOS DE ERROR
def test_importar_archivo_vcf_corrupto():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    with pytest.raises(ErrorArchivoCorrupto):
        gestor.importar_contactos("corrupto.vcf")

def test_importar_archivo_no_vcf():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    with pytest.raises(ErrorNoVCF):
        gestor.importar_contactos("archivo.txt")

def test_exportar_contactos_sin_permisos_de_escritura():
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    usuario.contactos = [Contacto(1, "José", "123456789", "jose@email.com", "Calle A", "Trabajo")]
    with pytest.raises(ErrorPermisosDeEscritura):
        gestor.exportar_contactos(usuario.contactos, "/ruta/sin/permisos/contactos.vcf")