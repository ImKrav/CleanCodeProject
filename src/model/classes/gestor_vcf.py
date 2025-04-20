import os
from src.model.classes.contacto import Contacto
from src.model.classes.usuario import Usuario
from src.model.errors import ErrorListaVaciaDeContactos, ErrorArchivoCorrupto, ErrorNoVCF, ErrorPermisosDeEscritura

class GestorVCF:
    """
    Gestiona la exportación e importación de contactos a/desde archivos .vcf.
    """
    def __init__(self, usuario: Usuario):
        """
        Inicializa el gestor con un usuario cuyas operaciones
        de importación añadirán contactos a `usuario.contactos`.

        Args:
            usuario (Usuario): instancia de Usuario.
        """
        self.usuario = usuario

    def exportar_contactos(self, contactos: list[Contacto], archivo: str) -> None:
        """
        Valida y escribe una lista de contactos en un archivo VCF.

        Args:
            contactos (list[Contacto]): contactos a exportar.
            archivo (str): ruta del archivo destino (debe terminar en .vcf).

        Raises:
            ErrorListaVaciaDeContactos: si `contactos` es vacío.
            ErrorNoVCF: si la ruta no termina en `.vcf`.
            ErrorPermisosDeEscritura: si no hay permisos de escritura.
            Exception: para errores imprevistos durante la escritura.
        """
        if not contactos:
            raise ErrorListaVaciaDeContactos("La lista de contactos está vacía.")
        if not archivo.endswith(".vcf"):
            raise ErrorNoVCF("El archivo debe tener la extensión .vcf.")
        if os.path.exists(archivo) and not os.access(archivo, os.W_OK):
            raise ErrorPermisosDeEscritura("No tienes permisos de escritura en el directorio de destino.")
        if not os.access(os.path.dirname(archivo) or ".", os.W_OK):
            raise ErrorPermisosDeEscritura("No tienes permisos de escritura en el directorio de destino.")

        try:
            with open(archivo, "w", encoding="utf-8") as file:
                for contacto in contactos:
                    file.write(self._formatear_contacto_vcf(contacto))
            print(f"Contactos exportados exitosamente a '{archivo}'.")
        except PermissionError:
            raise ErrorPermisosDeEscritura("No tienes permisos de escritura en el directorio de destino.")
        except Exception as e:
            raise Exception(f"Error inesperado al exportar contactos: {e}")

    def importar_contactos(self, archivo: str) -> list[Contacto]:
        """
        Lee un archivo VCF y convierte cada vCard en un Contacto,
        añadiéndolos a `usuario.contactos`.

        Args:
            archivo (str): ruta del archivo fuente (debe terminar en .vcf).

        Returns:
            list[Contacto]: lista de contactos importados.

        Raises:
            ErrorNoVCF: si la ruta no termina en `.vcf`.
            ErrorArchivoCorrupto: si el archivo no existe o no puede leerse.
            Exception: para errores imprevistos durante la lectura.
        """

        if not archivo.endswith(".vcf"):
            raise ErrorNoVCF("El archivo debe tener la extensión .vcf.")

        contactos_importados = []
        try:
            with open(archivo, "r", encoding="utf-8") as file:
                contenido = file.read()
                contactos_raw = contenido.split("END:VCARD")
                for contacto_raw in contactos_raw:
                    if contacto_raw.strip():
                        contacto = self._parsear_contacto_vcf(contacto_raw + "END:VCARD")
                        contactos_importados.append(contacto)
            
            # Agregar los contactos importados al usuario
            self.usuario.contactos.extend(contactos_importados)
            
            print(f"Contactos importados exitosamente desde '{archivo}'.")
            return contactos_importados
        except FileNotFoundError:
            raise ErrorArchivoCorrupto("El archivo no existe o está corrupto.")
        except Exception as e:
            raise Exception(f"Error inesperado al importar contactos: {e}")
        
    def _formatear_contacto_vcf(self, contacto: Contacto) -> str:
        """
        Convierte un Contacto a formato .VCF.

        Args:
            contacto (Contacto): contacto a serializar.

        Returns:
            str: cadena VCF completa para ese contacto.
        """
        return (
            "BEGIN:VCARD\n"
            "VERSION:3.0\n"
            f"FN:{contacto.nombre}\n"
            f"TEL:{contacto.telefono}\n"
            f"EMAIL:{contacto.email}\n"
            f"ADR:{contacto.direccion}\n"
            f"CATEGORY:{contacto.categoria}\n"
            "END:VCARD\n"
        )

    def _parsear_contacto_vcf(self, vcf_data: str) -> Contacto:
        """Convierte un bloque VCF en un objeto Contacto.
        Args:
            vcf_data (str): bloque de texto con los campos VCF.

        Returns:
            Contacto: instancia con los datos extraídos.
        """
        lines = vcf_data.split("\n")
        nombre = telefono = email = direccion = categoria = ""
        for line in lines:
            if line.startswith("FN:"):
                nombre = line[3:].strip()
            elif line.startswith("TEL:"):
                telefono = line[4:].strip()
            elif line.startswith("EMAIL:"):
                email = line[6:].strip()
            elif line.startswith("ADR:"):
                direccion = line[4:].strip()
            elif line.startswith("CATEGORY:"):
                categoria = line[9:].strip()

        id_contacto = len(self.usuario.contactos) + 1
        return Contacto(id_contacto, nombre, telefono, email, direccion, categoria)