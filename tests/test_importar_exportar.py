import pytest
import os
from src.classes.usuario import Usuario
from src.classes.contacto import Contacto
from src.classes.gestor_vcf import GestorVCF
from src.errors import ErrorListaVaciaDeContactos, ErrorArchivoCorrupto, ErrorNoVCF, ErrorPermisosDeEscritura


# CASOS NORMALES
def test_exportar_lista_con_5_contactos():
    """
    Caso Normal 1:
    Exportar una lista con 5 contactos.
    Resultado: Contactos exportados correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    usuario.contactos = [Contacto(i, f"Contacto {i}", "123456789", "contacto@email.com", "Calle Falsa 123", "Trabajo") for i in range(5)]
    gestor.exportar_contactos(usuario.contactos, "VCF/export/contactos.vcf")
    assert os.path.exists("VCF/export/contactos.vcf")

def test_importar_archivo_vcf_valido_con_3_contactos():
    """
    Caso Normal 2:
    Importar un archivo `.vcf` válido con 3 contactos.
    Resultado: Contactos importados correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    gestor.importar_contactos("VCF/import/3_contactos.vcf")
    assert len(usuario.contactos) == 3

def test_exportar_contactos_con_caracteres_especiales():
    """
    Caso Normal 3:
    Exportar contactos con nombres que contienen caracteres especiales.
    Resultado: Contactos exportados correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    usuario.contactos = [
        Contacto(1, "José", "123456789", "jose@email.com", "Calle A", "Trabajo"),
        Contacto(2, "María", "987654321", "maria@email.com", "Calle B", "Amigos"),
        Contacto(3, "El Triple #$%&", "555123456", "triple@email.com", "Calle C", "Personal"),
    ]
    gestor.exportar_contactos(usuario.contactos, "VCF/export/contactos_especiales.vcf")
    assert os.path.exists("VCF/export/contactos_especiales.vcf")


# CASOS EXTREMOS
def test_exportar_lista_con_1000_contactos():
    """
    Caso Extremo 1:
    Exportar una lista con 1000 contactos.
    Resultado: Contactos exportados correctamente.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    usuario.contactos = [Contacto(i, f"Contacto {i}", "123456789", "contacto@email.com", "Calle Falsa 123", "Trabajo") for i in range(1000)]
    gestor.exportar_contactos(usuario.contactos, "VCF/export/contactos_1000.vcf")
    assert os.path.exists("VCF/export/contactos_1000.vcf")

def test_importar_archivo_vcf_con_500_contactos():
    """
    Caso Extremo 2:
    Importar un `.vcf` con 500 contactos.
    Resultado: Contactos importados correctamente.
    """
    usuario = Usuario(2, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    gestor.importar_contactos("VCF/import/500_contactos.vcf")
    assert len(usuario.contactos) == 500

def test_exportar_lista_vacia_de_contactos():
    """
    Caso Extremo 3:
    Exportar una lista vacía de contactos.
    Resultado: Error: La lista de contactos está vacía.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    usuario.contactos = []
    with pytest.raises(ErrorListaVaciaDeContactos):
        gestor.exportar_contactos(usuario.contactos, "contactos_vacios.vcf")


# CASOS DE ERROR
def test_importar_archivo_vcf_corrupto():
    """
    Caso de Error 1:
    Importar un archivo `.vcf` corrupto.
    Resultado: Error: El archivo está corrupto o no se puede cargar.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    with pytest.raises(ErrorArchivoCorrupto):
        gestor.importar_contactos("corrupto.vcf")

def test_importar_archivo_no_vcf():
    """
    Caso de Error 2:
    Importar un archivo que no es `.vcf`.
    Resultado: Error: El archivo no es un archivo de extensión .vcf.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    with pytest.raises(ErrorNoVCF):
        gestor.importar_contactos("archivo.txt")

def test_exportar_contactos_sin_permisos_de_escritura():
    """
    Caso de Error 3:
    Exportar contactos sin permisos de escritura en la carpeta destino.
    Resultado: Error: No tienes permisos de escritura en el directorio de destino.
    """
    usuario = Usuario(1, "user", "user@email.com", "anotherpass")
    gestor = GestorVCF(usuario)
    usuario.contactos = [Contacto(1, "José", "123456789", "jose@email.com", "Calle A", "Trabajo")]
    with pytest.raises(ErrorPermisosDeEscritura):
        gestor.exportar_contactos(usuario.contactos, "/ruta/sin/permisos/contactos.vcf")